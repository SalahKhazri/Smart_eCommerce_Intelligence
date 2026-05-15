from kfp.client import Client

def run_pipeline():
    client = Client()

    run = client.create_run_from_pipeline_package(
        pipeline_file="pipeline.yaml",
        arguments={}
    )

    print("🚀 Pipeline submitted to Kubeflow")
    print(run)


if __name__ == "__main__":
    run_pipeline()