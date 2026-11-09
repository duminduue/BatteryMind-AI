"""Daily descriptive features for the NASA randomized battery dataset.

This module creates exploratory, day-level summaries. It does not derive SOH,
capacity, EOL, or RUL labels. Rows are grouped by pack-day and discharge
mission type so reference and regular missions are not silently mixed.
"""
from __future__ import annotations

import pandas as pd


REQUIRED_COLUMNS = {
    "start_time",
    "time",
    "mode",
    "voltage_load",
    "current_load",
    "temperature_battery",
    "temperature_mosfet",
    "temperature_resistor",
    "mission_type",
}


def build_daily_features(data: pd.DataFrame) -> pd.DataFrame:
    """Aggregate discharge measurements by calendar day and mission type.

    The source documentation states that load-board measurements are present
    only during discharge missions. Missing load-board values outside those
    missions are therefore not imputed here.

    Returns one row per observed (start_time date, mission_type) combination.
    These rows are descriptive features, not independent battery samples.
    """
    missing = REQUIRED_COLUMNS.difference(data.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    frame = data.copy()
    frame["time"] = pd.to_numeric(frame["time"], errors="coerce")
    numeric_columns = [
        "voltage_load",
        "current_load",
        "temperature_battery",
        "temperature_mosfet",
        "temperature_resistor",
        "mission_type",
        "mode",
    ]
    for column in numeric_columns:
        frame[column] = pd.to_numeric(frame[column], errors="coerce")

    # Use the date portion of the provider's start_time field.
    frame["date"] = frame["start_time"].astype("string").str.slice(0, 10)

    discharge = frame.loc[
        (frame["mode"] == -1)
        & frame["mission_type"].notna()
        & frame["current_load"].notna()
    ].copy()

    if discharge.empty:
        return pd.DataFrame(
            columns=[
                "date",
                "mission_type",
                "discharge_samples",
                "elapsed_span_s",
                "current_mean_A",
                "current_median_A",
                "current_std_A",
                "current_min_A",
                "current_max_A",
                "voltage_load_mean_V",
                "voltage_load_min_V",
                "temperature_battery_mean_C",
                "temperature_battery_max_C",
                "temperature_mosfet_mean_C",
                "temperature_resistor_mean_C",
            ]
        )

    grouped = discharge.groupby(["date", "mission_type"], dropna=True)

    features = grouped.agg(
        discharge_samples=("time", "count"),
        first_elapsed_time_s=("time", "min"),
        last_elapsed_time_s=("time", "max"),
        current_mean_A=("current_load", "mean"),
        current_median_A=("current_load", "median"),
        current_std_A=("current_load", "std"),
        current_min_A=("current_load", "min"),
        current_max_A=("current_load", "max"),
        voltage_load_mean_V=("voltage_load", "mean"),
        voltage_load_min_V=("voltage_load", "min"),
        temperature_battery_mean_C=("temperature_battery", "mean"),
        temperature_battery_max_C=("temperature_battery", "max"),
        temperature_mosfet_mean_C=("temperature_mosfet", "mean"),
        temperature_resistor_mean_C=("temperature_resistor", "mean"),
    ).reset_index()

    features["elapsed_span_s"] = (
        features["last_elapsed_time_s"] - features["first_elapsed_time_s"]
    )
    features = features.drop(
        columns=["first_elapsed_time_s", "last_elapsed_time_s"]
    )

    return features.sort_values(
        ["date", "mission_type"], kind="stable"
    ).reset_index(drop=True)
