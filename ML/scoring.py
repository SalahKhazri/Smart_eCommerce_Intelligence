
def compute_score(df):

    df["score"] = (
        (1 / (df["price"] + 1)) * 0.4 +
        df["is_available"] * 0.3 +
        df["price_level"] * 0.2 +
        df["title_length"] * 0.1
    )

    return df