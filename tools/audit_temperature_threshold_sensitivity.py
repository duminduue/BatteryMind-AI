#!/usr/bin/env python3
"""Sensitivity analysis for Pack 0.0 high-temperature episode thresholds.

Reads the NASA randomized dataset CSV directly from its ZIP archive.
Episodes are formed from regular-discharge mission rows at/above each
temperature threshold; a new episode starts when the time gap exceeds
the configured gap threshold.
"""
from __future__ import annotations

import argparse
import csv
import io
import statistics
import zipfile
from collections import defaultdict
from pathlib import Path


def rank(values):
    """Return average ranks for ties (small dependency-free Spearman support)."""
    order = sorted(range(len(values)), key=values.__getitem__)
    ranks = [0.0] * len(values)
    i = 0
    while i < len(order):
        j = i + 1
        while j < len(order) and values[order[j]] == values[order[i]]:
            j += 1
        avg = (i + 1 + j) / 2
        for k in range(i, j):
            ranks[order[k]] = avg
        i = j
    return ranks


def spearman(x, y):
    if len(x) < 2:
        return float("nan")
    rx, ry = rank(x), rank(y)
    mx, my = statistics.mean(rx), statistics.mean(ry)
    numerator = sum((a - mx) * (b - my) for a, b in zip(rx, ry))
    denom = (sum((a - mx) ** 2 for a in rx) * sum((b - my) ** 2 for b in ry)) ** 0.5
    return numerator / denom if denom else float("nan")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("archive", help="Path to battery_alt_dataset.zip")
    ap.add_argument("--gap-seconds", type=float, default=2.5)
    ap.add_argument("--member", default="battery_alt_dataset/regular_alt_batteries/battery00.csv",
                    help="CSV member path inside the ZIP archive")
    ap.add_argument("--pack-label", default="Pack 0.0")
    ap.add_argument("--output", default="outputs/pack_0_0_temperature_threshold_sensitivity.csv")
    ap.add_argument("--episode-output", default=None,
                    help="Optional CSV path for individual threshold episodes")
    args = ap.parse_args()

    member = args.member
    with zipfile.ZipFile(args.archive) as zf:
        with zf.open(member) as raw:
            reader = csv.DictReader(io.TextIOWrapper(raw, encoding="utf-8-sig"))
            rows = []
            for row in reader:
                if row["mode"] not in ("-1", "-1.0") or row["mission_type"] not in ("1", "1.0"):
                    continue
                temp = row["temperature_battery"].strip()
                current = row["current_load"].strip()
                voltage = row["voltage_load"].strip()
                if not temp or not row["time"].strip():
                    continue
                rows.append((
                    float(row["time"]), float(temp),
                    float(current) if current else None,
                    float(voltage) if voltage else None,
                ))

    rows.sort(key=lambda r: r[0])
    print(f"{args.pack_label} qualifying regular-discharge rows: {len(rows):,}")
    print(f"Episode gap rule: > {args.gap_seconds:g} seconds")
    print()
    print("Threshold | Records | Episodes | Mean duration(s) | Median max temp(C) | Spearman(max temp, duration)")
    output = []
    episode_output = []

    for threshold in (85.0, 90.0, 95.0):
        selected = [r for r in rows if r[1] >= threshold]
        episodes = []
        current_episode = []
        previous_time = None

        for row in selected:
            if previous_time is not None and row[0] - previous_time > args.gap_seconds:
                if current_episode:
                    episodes.append(current_episode)
                current_episode = []
            current_episode.append(row)
            previous_time = row[0]
        if current_episode:
            episodes.append(current_episode)

        durations, maxima = [], []
        for episode_id, ep in enumerate(episodes, start=1):
            duration = ep[-1][0] - ep[0][0]
            maximum = max(r[1] for r in ep)
            durations.append(duration)
            maxima.append(maximum)
            currents = [r[2] for r in ep if r[2] is not None]
            voltages = [r[3] for r in ep if r[3] is not None]
            episode_output.append({
                "pack_label": args.pack_label,
                "threshold_C": threshold,
                "episode_id": episode_id,
                "start_time_s": ep[0][0],
                "end_time_s": ep[-1][0],
                "sample_count": len(ep),
                "duration_s": duration,
                "mean_temperature_C": statistics.mean(r[1] for r in ep),
                "max_temperature_C": maximum,
                "mean_current_A": statistics.mean(currents) if currents else float("nan"),
                "minimum_voltage_V": min(voltages) if voltages else float("nan"),
                "gap_rule_s": args.gap_seconds,
            })

        mean_duration = statistics.mean(durations) if durations else float("nan")
        median_max = statistics.median(maxima) if maxima else float("nan")
        rho = spearman(maxima, durations)
        print(f"{threshold:>8.0f} | {len(selected):>7,} | {len(episodes):>8,} | "
              f"{mean_duration:>16.2f} | {median_max:>18.2f} | {rho:>29.3f}")

        output.append({
            "threshold_C": threshold,
            "qualifying_records": len(selected),
            "episode_count": len(episodes),
            "mean_duration_s": mean_duration,
            "median_duration_s": statistics.median(durations) if durations else float("nan"),
            "median_episode_max_temp_C": median_max,
            "spearman_max_temp_vs_duration": rho,
            "gap_rule_s": args.gap_seconds,
        })

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(output[0]))
        writer.writeheader()
        writer.writerows(output)
    print(f"\nSaved summary: {out}")

    if args.episode_output:
        episode_path = Path(args.episode_output)
        episode_path.parent.mkdir(parents=True, exist_ok=True)
        fields = list(episode_output[0]) if episode_output else [
            "pack_label", "threshold_C", "episode_id", "start_time_s",
            "end_time_s", "sample_count", "duration_s",
            "mean_temperature_C", "max_temperature_C", "mean_current_A",
            "minimum_voltage_V", "gap_rule_s",
        ]
        with episode_path.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fields)
            writer.writeheader()
            writer.writerows(episode_output)
        print(f"Saved episode details: {episode_path} ({len(episode_output):,} rows)")


if __name__ == "__main__":
    main()
