import pandas as pd
import argparse

def create_features(df):
    df["title_length"] = df["title"].fillna("").astype(str).apply(len)
    df["is_available"] = df["availability"].astype(int)

    df["price_level"] = pd.cut(
        df["price"],
        bins=[0, 25, 60, df["price"].max() + 1],
        labels=[0, 1, 2]
    ).astype(int)

    return df

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input")
    parser.add_argument("--output")

    args = parser.parse_args()

    df = pd.read_csv(args.input)
    df = create_features(df)

    df.to_csv(args.output, index=False)