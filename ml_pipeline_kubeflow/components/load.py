import pandas as pd
import argparse

def load_data(path):
    df = pd.read_csv(path)
    return df

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, required=True)
    parser.add_argument("--output", type=str, required=True)

    args = parser.parse_args()

    df = load_data(args.input)
    df.to_csv(args.output, index=False)