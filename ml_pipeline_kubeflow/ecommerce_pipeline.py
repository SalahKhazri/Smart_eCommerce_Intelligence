from kfp import dsl
from kfp.dsl import component, OutputPath, Output, Dataset


# =========================
# LOAD
# =========================
@component
def load_op(output_path: str):
    import pandas as pd

    df = pd.read_csv("data/raw/products.csv")

    df.to_json(output_path)


# =========================
# CLEAN
# =========================
@component
def clean_op(input_path: str, output_path: OutputPath(str)):
    import pandas as pd

    df = pd.read_json(input_path)

    df["price"] = pd.to_numeric(df["price"], errors="coerce").fillna(0)

    df.to_json(output_path)
    print("✔ Clean done")


# =========================
# SCORE
# =========================
@component
def score_op(input_path: str, output_data: Output[Dataset]):
    import pandas as pd

    df = pd.read_json(input_path)

    df["score"] = df["price"].rank(pct=True)

    df.to_json(output_data.path, orient="records")

    print("✔ Score done")


# =========================
# PIPELINE
# =========================
@dsl.pipeline(
    name="ecommerce-ml-pipeline"
)
def ecommerce_pipeline():

    load_task = load_op(output_path="data/processed/raw.json")

    clean_task = clean_op(input_data=load_task.outputs["output"])

    score_task = score_op(clean_task.output)