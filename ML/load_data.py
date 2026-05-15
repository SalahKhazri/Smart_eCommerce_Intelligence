import pandas as pd

def load_data(path="Scrapping/data/products.csv"):
    return pd.read_csv(path)