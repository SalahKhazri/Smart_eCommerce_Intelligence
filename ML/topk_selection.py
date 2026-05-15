def get_top_k(df, k=20):
    return df.sort_values(by="score", ascending=False).head(k)