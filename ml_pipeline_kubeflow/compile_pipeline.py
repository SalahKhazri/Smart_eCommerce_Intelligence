from kfp import compiler
from ecommerce_pipeline import ecommerce_pipeline

if __name__ == "__main__":
    compiler.Compiler().compile(
        pipeline_func=ecommerce_pipeline,
        package_path="pipeline.yaml"
    )

    print("✔ pipeline.yaml generated successfully")