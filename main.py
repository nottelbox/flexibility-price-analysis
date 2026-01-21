from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("prices/summary")
def summary():
    return {
        "average_price": 70,
        "min_price": 50,
        "max_price": 100,
        "price_volatility": 5,
    }


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}