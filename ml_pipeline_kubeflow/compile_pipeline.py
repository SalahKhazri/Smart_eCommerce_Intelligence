from kfp import compiler
from ecommerce_pipeline import ecommerce_pipeline

if __name__ == "__main__":
    compiler.Compiler().compile(
        pipeline_func=ecommerce_pipeline,
        package_path="ml_pipeline_kubeflow/ecommerce_pipeline.yaml"
    )

    print("✔ pipeline.yaml generated successfully")