def shop_ranking(df):
    return df.groupby("vendor")["score"].mean().sort_values(ascending=False)