#!/usr/bin/env python3
"""Inventory NASA battery dataset archives without modifying the source files.

Usage:
    python tools/audit_nasa_archives.py /path/to/archive.zip
    python tools/audit_nasa_archives.py /path/to/folder --output datasets/audit/archive_inventory.csv

This first-stage audit records archive members and nested ZIP contents. It does not
claim to validate battery measurements or infer independent-cell counts.
"""
from __future__ import annotations

import argparse
import csv
import io
import zipfile
from pathlib import Path
from typing import Iterable

FIELDS = [
    "archive", "member_path", "file_type", "uncompressed_bytes",
    "compressed_bytes", "nested_archive_depth",
]


def walk_zip(data: bytes, archive_name: str, depth: int = 0) -> Iterable[dict[str, object]]:
    try:
        with zipfile.ZipFile(io.BytesIO(data)) as zf:
            for info in zf.infolist():
                if info.is_dir():
                    continue
                suffix = Path(info.filename).suffix.lower()
                kind = suffix.lstrip(".") or "no_extension"
                yield {
                    "archive": archive_name,
                    "member_path": info.filename,
                    "file_type": kind,
                    "uncompressed_bytes": info.file_size,
                    "compressed_bytes": info.compress_size,
                    "nested_archive_depth": depth,
                }
                if suffix == ".zip" and depth < 5:
                    try:
                        nested = zf.read(info)
                    except (RuntimeError, zipfile.BadZipFile, OSError) as exc:
                        yield {
                            "archive": archive_name,
                            "member_path": f"{info.filename} [READ ERROR: {exc}]",
                            "file_type": "error",
                            "uncompressed_bytes": info.file_size,
                            "compressed_bytes": info.compress_size,
                            "nested_archive_depth": depth + 1,
                        }
                        continue
                    yield from walk_zip(
                        nested, f"{archive_name}::{info.filename}", depth + 1
                    )
    except zipfile.BadZipFile as exc:
        raise ValueError(f"Not a readable ZIP archive: {archive_name}: {exc}") from exc


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="ZIP archive or folder containing ZIPs")
    parser.add_argument(
        "--output", type=Path, default=Path("datasets/audit/archive_inventory.csv")
    )
    args = parser.parse_args()

    sources = [args.source] if args.source.is_file() else sorted(args.source.rglob("*.zip"))
    if not sources:
        parser.error("No ZIP archives found.")

    rows: list[dict[str, object]] = []
    for source in sources:
        if source.suffix.lower() != ".zip":
            continue
        rows.extend(walk_zip(source.read_bytes(), str(source)))

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)

    mat_files = sum(row["file_type"] == "mat" for row in rows)
    print(f"Archives inspected: {len(sources)}")
    print(f"Files indexed (including nested ZIPs): {len(rows)}")
    print(f"MATLAB .mat files found: {mat_files}")
    print(f"Inventory written to: {args.output}")
    print("Note: this is archive inventory only; measurement-level audit is still required.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
