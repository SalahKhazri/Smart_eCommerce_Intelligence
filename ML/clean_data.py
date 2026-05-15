import pandas as pd

def clean_data(df):

    # ======================
    # NORMALIZE COL NAMES
    # ======================
    df.columns = df.columns.str.lower()

    # ======================
    # CONVERT NUMERIC FIELDS
    # ======================
    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    df["availability"] = df["availability"].map({True: 1, False: 0})

    if "variants_count" in df.columns:
        df["variants_count"] = pd.to_numeric(df["variants_count"], errors="coerce")

    # ======================
    # FILL MISSING VALUES
    # ======================
    df["price"] = df["price"].fillna(df["price"].median())
    df["availability"] = df["availability"].fillna(0)

    if "variants_count" in df.columns:
        df["variants_count"] = df["variants_count"].fillna(1)

    df = df.drop_duplicates()

    return df