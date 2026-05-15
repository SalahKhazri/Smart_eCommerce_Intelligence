import pandas as pd
import argparse

def compute_score(df):
    df["score"] = (
        (100 - df["price"]) * 0.3 +
        df["is_available"] * 20 +
        df["title_length"] * 0.2
    )
    return df

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input")
    parser.add_argument("--output")

    args = parser.parse_args()

    df = pd.read_csv(args.input)
    df = compute_score(df)

    df.to_csv(args.output, index=False)