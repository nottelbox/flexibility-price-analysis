from fastapi import FastAPI
from data.provider import get_energy_data
from services.flexibilityAnalyser import get_flexibility
from services.mapper import map_flexibility_row

app = FastAPI()


@app.get("/prices/summary")
def read_summary():
    df = get_energy_data()
    return {
        "average_price": df["price_eur_mwh"].mean(),
        "min_price": df["price_eur_mwh"].min(),
        "max_price": df["price_eur_mwh"].max(),
        "price_volatility": df["price_eur_mwh"].std(),
    }


@app.get("/flexibility/windows")
def read_flexibility():
    df = get_energy_data()
    flex = get_flexibility(df)
    flex_rows = flex.to_dict(orient="records")

    return [map_flexibility_row(row) for row in flex_rows]