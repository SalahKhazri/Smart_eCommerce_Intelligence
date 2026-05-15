import pandas as pd
import argparse

def get_top_k(df, k=20):
    return df.sort_values("score", ascending=False).head(k)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input")
    parser.add_argument("--output")
    parser.add_argument("--k", type=int, default=20)

    args = parser.parse_args()

    df = pd.read_csv(args.input)
    topk = get_top_k(df, args.k)

    topk.to_csv(args.output, index=False)