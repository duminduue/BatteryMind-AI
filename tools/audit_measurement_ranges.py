#!/usr/bin/env python3
"""Exploratory measurement-range audit for NASA randomized battery packs.

This tool reports threshold counts and example rows. Threshold hits are review
candidates only; they are not automatically classified as outliers or errors.
"""
from __future__ import annotations

import argparse
from io import BytesIO
from pathlib import Path
from zipfile import ZipFile

import pandas as pd


def find_pack_csv(archive: ZipFile, pack: str) -> str:
    suffix = f"/regular_alt_batteries/battery{pack.replace('.', '')}.csv"
    matches = [n for n in archive.namelist() if n.endswith(suffix)]
    if not matches:
        raise FileNotFoundError(f"Could not find regular pack {pack} in archive")
    if len(matches) > 1:
        raise RuntimeError(f"Multiple matching CSVs found for pack {pack}: {matches}")
    return matches[0]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archive", type=Path, help="Path to battery_alt_dataset.zip")
    parser.add_argument("--pack", default="0.0", help="Regular pack ID (default: 0.0)")
    parser.add_argument("--current-below", type=float, default=15.0)
    parser.add_argument("--voltage-le", type=float, default=0.0)
    parser.add_argument("--temperature-ge", type=float, default=90.0)
    parser.add_argument("--examples", type=int, default=5)
    parser.add_argument("--output-dir", type=Path, default=Path("outputs"))
    args = parser.parse_args()

    with ZipFile(args.archive) as archive:
        member = find_pack_csv(archive, args.pack)
        with archive.open(member) as raw:
            data = pd.read_csv(raw)

    required = {"time", "mode", "mission_type", "current_load", "voltage_load", "temperature_battery"}
    missing = required.difference(data.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    discharge = data.loc[
        (data["mode"] == -1) & (data["mission_type"] == 1)
    ].copy()
    fields = ["start_time", "time", "current_load", "voltage_load", "temperature_battery"]

    print(f"Pack: {args.pack}")
    print(f"Archive member: {member}")
    print(f"Discharge mission rows: {len(discharge):,}")
    for col in ["current_load", "voltage_load", "temperature_battery"]:
        print(f"\n{col} descriptive statistics:")
        print(discharge[col].describe(percentiles=[.01, .05, .5, .95, .99]).round(3).to_string())

    checks = {
        "current_below_threshold": discharge["current_load"] < args.current_below,
        "voltage_at_or_below_threshold": discharge["voltage_load"] <= args.voltage_le,
        "battery_temperature_at_or_above_threshold": discharge["temperature_battery"] >= args.temperature_ge,
    }

    args.output_dir.mkdir(parents=True, exist_ok=True)
    summary_rows = []
    example_frames = []
    for name, mask in checks.items():
        selected = discharge.loc[mask, fields].copy()
        print(f"\n{name}: {len(selected):,} records")
        if not selected.empty:
            print(selected.head(args.examples).to_string(index=False))
            selected.insert(0, "check", name)
            example_frames.append(selected.head(args.examples))
        summary_rows.append({
            "pack": args.pack,
            "check": name,
            "threshold": {
                "current_below_threshold": args.current_below,
                "voltage_at_or_below_threshold": args.voltage_le,
                "battery_temperature_at_or_above_threshold": args.temperature_ge,
            }[name],
            "record_count": int(mask.sum()),
            "discharge_rows": len(discharge),
        })

    summary_path = args.output_dir / f"pack_{args.pack.replace('.', '_')}_measurement_range_summary.csv"
    examples_path = args.output_dir / f"pack_{args.pack.replace('.', '_')}_measurement_range_examples.csv"
    pd.DataFrame(summary_rows).to_csv(summary_path, index=False)
    if example_frames:
        pd.concat(example_frames, ignore_index=True).to_csv(examples_path, index=False)
    else:
        pd.DataFrame(columns=["check", *fields]).to_csv(examples_path, index=False)

    print(f"\nWrote: {summary_path}")
    print(f"Wrote: {examples_path}")
    print("Interpretation: threshold hits are candidates for contextual review, not confirmed anomalies.")


if __name__ == "__main__":
    main()
