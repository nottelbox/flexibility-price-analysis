from typing import Union

from fastapi import FastAPI
from data.provider import get_energy_data

app = FastAPI()


@app.get("/prices/summary")
def read_summary():
    df = get_energy_data()
    return {
        "average_price": df["price_eur_mwh"].mean(),
        "min_price": df["price_eur_mwh"].min(),
        "max_price": df["price_eur_mwh"].max(),
    }


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}