from kfp import dsl
from kfp.dsl import component
from typing import NamedTuple


# =========================
# COMPONENT 1 : LOAD DATA
# =========================

@component(
    base_image="python:3.11",
    packages_to_install=["pandas"]
)
def load_data() -> str:
    import pandas as pd

    df = pd.read_csv("data/raw/products.csv")

    print("✔ Dataset loaded :", df.shape)

    return df.to_json()


# =========================
# COMPONENT 2 : PREPROCESS
# =========================

@component(
    base_image="ecommerce-preprocessing:latest",
    packages_to_install=["pandas"]
)
def preprocess_data(data_json: str) -> str:
    import pandas as pd

    df = pd.read_json(data_json)

    # Supprimer les valeurs nulles
    df = df.dropna()

    # Nettoyage simple
    df["price"] = df["price"].astype(float)

    print("✔ Preprocessing done")

    return df.to_json()


# =========================
# COMPONENT 3 : SCORING
# =========================

@component(
    base_image="ecommerce-scoring:latest",
    packages_to_install=["pandas"]
)
def score_products(data_json: str) -> str:
    import pandas as pd

    df = pd.read_json(data_json)

    # Exemple de score
    df["score"] = (
        df["rating"] * 0.5 +
        df["sales"] * 0.3 -
        df["price"] * 0.2
    )

    print("✔ Scoring completed")

    return df.to_json()


# =========================
# COMPONENT 4 : TOP-K
# =========================

@component(
    base_image="ecommerce-topk:latest",
    packages_to_install=["pandas"]
)
def select_top_k(data_json: str, k: int = 5) -> str:
    import pandas as pd

    df = pd.read_json(data_json)

    top_k = df.sort_values(by="score", ascending=False).head(k)

    print("✔ Top-K selected")

    return top_k.to_json()


# =========================
# COMPONENT 5 : SAVE
# =========================

@component(
    base_image="ecommerce-training:latest",
    packages_to_install=["pandas"]
)
def save_results(data_json: str):
    import pandas as pd
    import os

    df = pd.read_json(data_json)

    os.makedirs("reports", exist_ok=True)

    df.to_csv("reports/top_products.csv", index=False)

    print("✔ Results saved")


# =========================
# PIPELINE
# =========================

@dsl.pipeline(
    name="smart-ecommerce-pipeline"
)
def ecommerce_pipeline():

    load_task = load_data()

    preprocess_task = preprocess_data(
        data_json=load_task.output
    )

    scoring_task = score_products(
        data_json=preprocess_task.output
    )

    topk_task = select_top_k(
        data_json=scoring_task.output,
        k=10
    )

    save_results(
        data_json=topk_task.output
    )