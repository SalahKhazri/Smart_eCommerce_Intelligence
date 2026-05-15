import pandas as pd
import argparse

def clean_data(df):
    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    df["price"] = df["price"].fillna(df["price"].median())

    df["availability"] = df["availability"].astype(int)

    df = df.dropna(subset=["title", "vendor"])
    return df

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input")
    parser.add_argument("--output")

    args = parser.parse_args()

    df = pd.read_csv(args.input)
    df = clean_data(df)

    df.to_csv(args.output, index=False)