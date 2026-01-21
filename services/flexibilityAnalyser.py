def get_flexibility(df):
    mean_price = df['price_eur_mwh'].mean()
    price_volatility = df['price_eur_mwh'].std()
    mean_consumption = df['consumption_kw'].mean()

    mask = ((df['price_eur_mwh'] > mean_price + price_volatility)
             & (df['consumption_kw'] > mean_consumption))
    return df[mask]