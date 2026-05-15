import pandas as pd

def create_features(df):

    # ======================
    # SAFE NUMERIC CHECK
    # ======================
    df["price"] = pd.to_numeric(df["price"], errors="coerce")

    # fill missing BEFORE binning
    df["price"] = df["price"].fillna(df["price"].median())

    # ======================
    # FEATURES
    # ======================
    df["is_available"] = df["availability"].astype(int)

    # safe binning
    df["price_level"] = pd.cut(
        df["price"],
        bins=[0, 25, 60, df["price"].max() + 1],
        labels=[0, 1, 2],
        include_lowest=True
    )

    # IMPORTANT: handle NaN before astype
    df["price_level"] = df["price_level"].fillna(0).astype(int)

    # title length safe
    df["title_length"] = df["title"].fillna("").astype(str).apply(len)

    return df