import pandas as pd
import argparse
from sklearn.ensemble import RandomForestRegressor

FEATURES = ["price", "is_available", "price_level", "title_length"]

def train(df):
    X = df[FEATURES]
    y = df["score"]

    model = RandomForestRegressor(n_estimators=100)
    model.fit(X, y)

    df["rf_prediction"] = model.predict(X)

    return df

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input")
    parser.add_argument("--output")

    args = parser.parse_args()

    df = pd.read_csv(args.input)
    df = train(df)

    df.to_csv(args.output, index=False)