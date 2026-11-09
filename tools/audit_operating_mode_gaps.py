#!/usr/bin/env python3
"""Compare full-record timestamp gaps with discharge-only gaps in NASA randomized packs.

This is an exploratory data-quality audit. It does not label any interval as
missing data automatically: gaps in a filtered operating mode may contain
valid records from other modes.
"""
from __future__ import annotations

import argparse
import csv
import io
import statistics
import zipfile
from collections import Counter
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Audit timestamp gaps across all records and discharge-only records."
    )
    parser.add_argument("archive", help="Path to battery_alt_dataset.zip")
    parser.add_argument("--pack", default="0.0", help="Pack ID, e.g. 0.0 (default: 0.0)")
    parser.add_argument("--max-gap-s", type=float, default=2.0,
                        help="Report intervals longer than this threshold (default: 2 seconds)")
    parser.add_argument("--output", default="outputs/pack_gap_audit.csv",
                        help="CSV path for detected gaps")
    return parser.parse_args()


def pack_member(pack: str) -> str:
    digits = pack.replace(".", "")
    # Randomized dataset stores regular, recommissioned and second-life packs
    # in separate folders. This first version targets the regular group.
    return f"battery_alt_dataset/regular_alt_batteries/battery{digits}.csv"


def mode_label(value: str) -> str:
    try:
        number = float(value)
    except (TypeError, ValueError):
        return "unknown"
    return {-1.0: "discharge", 0.0: "rest", 1.0: "charge"}.get(number, "other")


def main() -> None:
    args = parse_args()
    if args.max_gap_s <= 0:
        raise SystemExit("--max-gap-s must be greater than zero")

    member = pack_member(args.pack)
    gaps: list[dict[str, object]] = []
    mode_counts: Counter[str] = Counter()
    total = 0
    previous_all: tuple[float, str] | None = None
    previous_discharge: float | None = None
    discharge_gap_count = 0
    full_gap_count = 0
    full_gap_seconds: list[float] = []

    with zipfile.ZipFile(args.archive) as archive:
        try:
            stream = archive.open(member)
        except KeyError as exc:
            raise SystemExit(f"Pack not found in archive: {member}") from exc

        with stream:
            reader = csv.DictReader(io.TextIOWrapper(stream, encoding="utf-8-sig", newline=""))
            required = {"time", "mode", "mission_type", "current_load"}
            if not required.issubset(reader.fieldnames or []):
                raise SystemExit(f"Required columns missing. Found: {reader.fieldnames}")

            for row in reader:
                try:
                    elapsed = float(row["time"])
                except (TypeError, ValueError):
                    continue

                mode = mode_label(row.get("mode", ""))
                mode_counts[mode] += 1
                total += 1

                if previous_all is not None:
                    gap = elapsed - previous_all[0]
                    if gap > args.max_gap_s:
                        full_gap_count += 1
                        full_gap_seconds.append(gap)
                        gaps.append({
                            "pack": args.pack,
                            "gap_type": "all_records",
                            "start_time_s": round(previous_all[0], 3),
                            "end_time_s": round(elapsed, 3),
                            "gap_s": round(gap, 3),
                            "mode_before": previous_all[1],
                            "mode_after": mode,
                            "mission_type_after": row.get("mission_type", ""),
                            "current_load_after_A": row.get("current_load", ""),
                            "interpretation": "candidate_full_record_gap_review_required",
                        })
                previous_all = (elapsed, mode)

                is_discharge_mission = mode == "discharge"
                try:
                    is_discharge_mission = (
                        is_discharge_mission
                        and float(row.get("mission_type", "")) == 1.0
                        and bool((row.get("current_load") or "").strip())
                    )
                except (TypeError, ValueError):
                    is_discharge_mission = False

                if is_discharge_mission:
                    if previous_discharge is not None:
                        gap = elapsed - previous_discharge
                        if gap > args.max_gap_s:
                            discharge_gap_count += 1
                            gaps.append({
                                "pack": args.pack,
                                "gap_type": "discharge_only",
                                "start_time_s": round(previous_discharge, 3),
                                "end_time_s": round(elapsed, 3),
                                "gap_s": round(gap, 3),
                                "mode_before": "discharge",
                                "mode_after": "discharge",
                                "mission_type_after": row.get("mission_type", ""),
                                "current_load_after_A": row.get("current_load", ""),
                                "interpretation": "filtered_gap_check_full_records_before_calling_missing",
                            })
                    previous_discharge = elapsed

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "pack", "gap_type", "start_time_s", "end_time_s", "gap_s",
        "mode_before", "mode_after", "mission_type_after",
        "current_load_after_A", "interpretation",
    ]
    with output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(gaps)

    print(f"Pack: {args.pack}")
    print(f"Records inspected: {total:,}")
    print("Operating-mode counts:")
    for label, count in sorted(mode_counts.items()):
        print(f"  {label}: {count:,}")
    print(f"Full-record gaps > {args.max_gap_s:g}s: {full_gap_count}")
    if full_gap_seconds:
        print(
            "  Gap duration (s): "
            f"min={min(full_gap_seconds):.3f}, "
            f"median={statistics.median(full_gap_seconds):.3f}, "
            f"max={max(full_gap_seconds):.3f}"
        )
    print(f"Discharge-only gaps > {args.max_gap_s:g}s: {discharge_gap_count}")
    print(f"Gap records written: {output}")
    print("Caution: a filtered discharge-only gap may contain valid charge/rest records.")
    print("Full-record gaps are candidates for review, not automatic proof of missing data.")


if __name__ == "__main__":
    main()
