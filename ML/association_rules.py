import pandas as pd

def generate_association_rules(df):

    # alias safety
    if "shop" not in df.columns:
        df["shop"] = df["vendor"]

    if "name" not in df.columns:
        df["name"] = df["title"]

    # create basket-style matrix (no sales needed)
    basket = (
        df.groupby(["shop", "name"])["score"]
        .mean()
        .unstack()
        .fillna(0)
    )

    return basket