def map_flexibility_row(row: dict) -> dict:
    return {
        "timestamp": row["timestamp"],
        "price": row["price_eur_mwh"],
        "consumption": row["consumption_kw"],
    }