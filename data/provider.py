import pandas as pd
import numpy as np

def get_energy_data() -> pd.DataFrame:
    np.random.seed(42)

    start = pd.Timestamp("2024-01-01 00:00")
    periods = 7 * 24 * 4
    timestamps = pd.date_range(start=start, periods=periods, freq="15T")

    df = pd.DataFrame({"timestamp": timestamps})

    hour = df["timestamp"].dt.hour + df["timestamp"].dt.minute / 60

    df["price_eur_mwh"] = (
            70
            + 15 * np.sin((hour - 8) / 24 * 2 * np.pi)
            + np.random.normal(0, 5, len(df))
    )

    df["consumption_kw"] = (
            100
            + 30 * np.clip(np.sin((hour - 6) / 24 * 2 * np.pi), 0, None)
            + np.random.normal(0, 8, len(df))
    )

    return df
