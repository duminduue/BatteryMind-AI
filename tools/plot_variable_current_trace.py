#!/usr/bin/env python3
"""Plot a raw discharge current trace around a detected plateau.

Example:
  py tools/plot_variable_current_trace.py ../battery_alt_dataset.zip --pack 5.0 --start 7671.360 --end 7752.344
"""
from __future__ import annotations

import argparse
import csv
import io
import zipfile
from pathlib import Path

import matplotlib.pyplot as plt


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archive", help="Path to battery_alt_dataset.zip")
    parser.add_argument("--pack", default="5.0", help="Pack ID, e.g. 5.0")
    parser.add_argument("--start", type=float, default=7671.360, help="Detected plateau start time in seconds")
    parser.add_argument("--end", type=float, default=7752.344, help="Detected plateau end time in seconds")
    parser.add_argument("--window", type=float, default=30.0, help="Seconds shown before and after the plateau")
    parser.add_argument("--output", default="segment_audit/pack_5_0_trace.png", help="Output plot path")
    args = parser.parse_args()

    if args.end <= args.start or args.window <= 0:
        raise SystemExit("--end must be greater than --start and --window must be positive")

    member = f"battery_alt_dataset/regular_alt_batteries/battery{args.pack.replace('.', '')}.csv"
    lower, upper = args.start - args.window, args.end + args.window
    times: list[float] = []
    currents: list[float] = []

    with zipfile.ZipFile(args.archive) as archive:
        with archive.open(member) as raw:
            reader = csv.DictReader(io.TextIOWrapper(raw, encoding="utf-8-sig", newline=""))
            for row in reader:
                try:
                    if float(row["mode"].strip()) != -1.0:
                        continue
                    if float(row["mission_type"].strip()) != 1.0:
                        continue
                    t = float(row["time"].strip())
                    value = (row.get("current_load") or "").strip()
                    if lower <= t <= upper and value:
                        times.append(t)
                        currents.append(float(value))
                except (ValueError, AttributeError, KeyError):
                    continue

    if not times:
        raise SystemExit("No discharge-current samples found in the requested time window.")

    order = sorted(zip(times, currents))
    times, currents = map(list, zip(*order))

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(12, 5))
    plt.plot(times, currents, linewidth=0.8, marker=".", markersize=2, label="Measured discharge current")
    plt.axvline(args.start, linestyle="--", label="Detected plateau start")
    plt.axvline(args.end, linestyle="--", label="Detected plateau end")
    plt.axvspan(args.start, args.end, alpha=0.12, label="Detected plateau interval")
    plt.xlabel("Elapsed time from beginning of pack test (s)")
    plt.ylabel("Discharge current (A)")
    plt.title(f"Pack {args.pack}: raw current trace around detected plateau")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig(output, dpi=180)
    print(f"Pack: {args.pack}")
    print(f"Samples plotted: {len(times)}")
    print(f"Time window: {lower:.3f} to {upper:.3f} s")
    print(f"Detected interval: {args.start:.3f} to {args.end:.3f} s")
    print(f"Plot saved: {output}")


if __name__ == "__main__":
    main()
