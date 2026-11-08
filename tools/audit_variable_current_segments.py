#!/usr/bin/env python3
"""Audit approximate constant-current plateaus in NASA randomized battery CSVs.

This is an exploratory segmentation tool, not a validated reconstruction of
the experiment's commanded load schedule. It detects adjacent discharge
samples whose measured current remains within a configurable tolerance.
"""
from __future__ import annotations

import argparse
import csv
import io
import math
import statistics
import zipfile
from collections import Counter
from pathlib import Path

DEFAULT_PACKS = ("4.0", "4.1", "5.0", "5.1")


def normalise_pack(value: str) -> str:
    return value.strip()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Summarise approximate current plateaus in variable-load packs."
    )
    parser.add_argument("archive", help="Path to battery_alt_dataset.zip")
    parser.add_argument(
        "--packs", nargs="+", default=list(DEFAULT_PACKS),
        help="Pack IDs to inspect (default: 4.0 4.1 5.0 5.1)",
    )
    parser.add_argument(
        "--tolerance", type=float, default=0.30,
        help="Maximum deviation in amperes from the plateau's first sample (default: 0.30)",
    )
    parser.add_argument(
        "--max-gap-s", type=float, default=2.0,
        help="Split a candidate plateau when adjacent sample times differ by more than this many seconds (default: 2.0)",
    )
    parser.add_argument(
        "--output-dir", default="segment_audit",
        help="Directory for segment-level and pack-summary CSV outputs",
    )
    return parser.parse_args()


def get_mode(value: str) -> bool:
    try:
        return float(value.strip()) == -1.0
    except (ValueError, AttributeError):
        return False


def get_mission(value: str) -> bool:
    try:
        return float(value.strip()) == 1.0
    except (ValueError, AttributeError):
        return False


def get_time(value: str) -> float | None:
    try:
        return float(value.strip())
    except (ValueError, AttributeError):
        return None


def flush_segment(pack: str, day: str, samples: list[tuple[float, float]], output: list[dict], boundary_after: str) -> None:
    if not samples:
        return
    currents = [item[1] for item in samples]
    start_t, end_t = samples[0][0], samples[-1][0]
    # Duration is based on elapsed-time span; add one sample interval when
    # estimating sample coverage, while retaining the raw span separately.
    intervals = [samples[i][0] - samples[i - 1][0] for i in range(1, len(samples))]
    typical_step = statistics.median(intervals) if intervals else 0.0
    span = end_t - start_t
    estimated_duration = span + typical_step if len(samples) > 1 else typical_step
    output.append({
        "pack": pack,
        "date": day,
        "start_time_s": round(start_t, 3),
        "end_time_s": round(end_t, 3),
        "sample_count": len(samples),
        "duration_estimate_s": round(estimated_duration, 3),
        "current_median_A": round(statistics.median(currents), 4),
        "current_min_A": round(min(currents), 4),
        "current_max_A": round(max(currents), 4),
        "current_range_A": round(max(currents) - min(currents), 4),
        "max_deviation_from_first_A": round(max(abs(value - currents[0]) for value in currents), 4),
        "boundary_after": boundary_after,
    })


def audit_pack(archive: zipfile.ZipFile, pack: str, tolerance: float, max_gap_s: float) -> list[dict]:
    path = f"battery_alt_dataset/regular_alt_batteries/battery{pack.replace('.', '')}.csv"
    try:
        stream = archive.open(path)
    except KeyError:
        print(f"[SKIP] Pack {pack}: archive member not found: {path}")
        return []

    segments: list[dict] = []
    current_segment: list[tuple[float, float]] = []
    segment_day = ""
    anchor_current: float | None = None
    previous_time: float | None = None
    previous_day = ""
    pending_boundary = "start_of_filtered_discharge"

    with stream:
        reader = csv.DictReader(io.TextIOWrapper(stream, encoding="utf-8-sig", newline=""))
        required = {"start_time", "time", "mode", "current_load", "mission_type"}
        if not required.issubset(reader.fieldnames or []):
            print(f"[SKIP] Pack {pack}: required columns missing")
            return []

        for row in reader:
            if not (get_mode(row.get("mode", "")) and get_mission(row.get("mission_type", ""))):
                if current_segment:
                    flush_segment(pack, segment_day, current_segment, segments, "mission_or_mode_change")
                    current_segment = []
                anchor_current = None
                previous_time = None
                previous_day = ""
                continue

            raw_current = (row.get("current_load") or "").strip()
            elapsed = get_time(row.get("time", ""))
            if not raw_current or elapsed is None:
                if current_segment:
                    flush_segment(pack, segment_day, current_segment, segments, "missing_current_or_time")
                    current_segment = []
                anchor_current = None
                previous_time = None
                previous_day = ""
                continue

            try:
                current = float(raw_current)
            except ValueError:
                current = float("nan")

            # Treat malformed and non-finite measurements as a real data gap.
            # Do not allow a detected plateau to bridge across an invalid row.
            if not math.isfinite(current):
                if current_segment:
                    flush_segment(pack, segment_day, current_segment, segments, "non_finite_current")
                    current_segment = []
                anchor_current = None
                previous_time = None
                previous_day = ""
                continue

            day = (row.get("start_time") or "").split()[0]
            discontinuity = (
                previous_time is not None
                and (elapsed <= previous_time or elapsed - previous_time > max_gap_s)
            )
            new_day = bool(previous_day and day != previous_day)
            changed_level = anchor_current is not None and abs(current - anchor_current) > tolerance

            if current_segment and (discontinuity or new_day or changed_level):
                if discontinuity:
                    reason = "time_reversal_or_non_increasing_time" if elapsed <= previous_time else "time_gap"
                elif new_day:
                    reason = "date_change"
                else:
                    reason = "current_change_beyond_tolerance"
                flush_segment(pack, segment_day, current_segment, segments, reason)
                current_segment = []
                anchor_current = None

            if not current_segment:
                segment_day = day
                anchor_current = current

            current_segment.append((elapsed, current))
            previous_time = elapsed
            previous_day = day

    if current_segment:
        flush_segment(pack, segment_day, current_segment, segments, "end_of_file")

    return segments


def main() -> None:
    args = parse_args()
    if args.tolerance <= 0:
        raise SystemExit("--tolerance must be greater than zero")
    if args.max_gap_s <= 0:
        raise SystemExit("--max-gap-s must be greater than zero")

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    all_segments: list[dict] = []

    with zipfile.ZipFile(args.archive) as archive:
        for pack in map(normalise_pack, args.packs):
            segments = audit_pack(archive, pack, args.tolerance, args.max_gap_s)
            all_segments.extend(segments)
            durations = [s["duration_estimate_s"] for s in segments]
            print(f"Pack {pack}: {len(segments):,} approximate plateaus")
            if durations:
                print(
                    f"  Estimated duration range: {min(durations):.2f}–"
                    f"{max(durations):.2f} s; median: {statistics.median(durations):.2f} s"
                )
                bins = Counter(
                    min((40, 60, 80), key=lambda target: abs(target - duration))
                    for duration in durations
                    if min(abs(target - duration) for target in (40, 60, 80)) <= 5
                )
                print(f"  Counts within ±5 s of 40/60/80 s: {dict(sorted(bins.items()))}")
            else:
                print("  No qualifying segments detected.")

    segment_path = output_dir / "variable_current_segments.csv"
    fields = [
        "pack", "date", "start_time_s", "end_time_s", "sample_count",
        "duration_estimate_s", "current_median_A", "current_min_A",
        "current_max_A", "current_range_A", "max_deviation_from_first_A",
        "boundary_after",
    ]
    with segment_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(all_segments)

    summary_path = output_dir / "variable_current_pack_summary.csv"
    summary_fields = [
        "pack", "segment_count", "duration_median_s", "duration_min_s",
        "duration_max_s", "median_current_A",
    ]
    with summary_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=summary_fields)
        writer.writeheader()
        for pack in map(normalise_pack, args.packs):
            rows = [s for s in all_segments if s["pack"] == pack]
            durations = [s["duration_estimate_s"] for s in rows]
            currents = [s["current_median_A"] for s in rows]
            writer.writerow({
                "pack": pack,
                "segment_count": len(rows),
                "duration_median_s": round(statistics.median(durations), 3) if rows else "",
                "duration_min_s": round(min(durations), 3) if rows else "",
                "duration_max_s": round(max(durations), 3) if rows else "",
                "median_current_A": round(statistics.median(currents), 4) if rows else "",
            })

    print(f"\nWrote: {segment_path}")
    print(f"Wrote: {summary_path}")
    print(f"\nSegmentation settings: current tolerance={args.tolerance:.3f} A; maximum time gap={args.max_gap_s:.3f} s")
    print("Boundary reasons are recorded per segment; all detected candidates are retained.")
    print("Caution: detected plateaus depend on the settings and are not confirmed commanded-load segments.")


if __name__ == "__main__":
    main()
