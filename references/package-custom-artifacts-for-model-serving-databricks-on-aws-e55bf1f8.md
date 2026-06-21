---
title: Package custom artifacts for Model Serving | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/model-serving/model-serving-custom-artifacts
ingestedAt: "2026-06-18T08:12:06.999Z"
---

This article describes how to ensure your model's file and artifact dependencies are available on your [Deploy models using Model Serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/) endpoint.

## Requirements[​](#requirements "Direct link to Requirements")

MLflow 1.29 and above

## Package artifacts with models[​](#package-artifacts-with-models "Direct link to Package artifacts with models")

When your model requires files or artifacts during inference, you can package them into the model artifact when you log the model.

If you are working with Databricks notebooks, a common practice is to have these files reside in [Unity Catalog volumes](https://docs.databricks.com/aws/en/files/#volumes). Models are also sometimes configured to download artifacts from the internet (such as HuggingFace Tokenizers). Real-time workloads at scale perform best when all required dependencies are statically captured at deployment time. For this reason, Model Serving requires that Unity Catalog volumes artifacts are packaged into the model artifact itself using MLflow interfaces. Network artifacts loaded with the model should be packaged with the model whenever possible.

With the MLflow command [log\_model()](https://mlflow.org/docs/latest/python_api/mlflow.pyfunc.html#mlflow.pyfunc.log_model) you can log a model and its dependent artifacts with the `artifacts` parameter.

Python

    mlflow.pyfunc.log_model(    ...    artifacts={'model-weights': "/Volumes/catalog/schema/volume/path/to/file", "tokenizer_cache": "./tokenizer_cache"},    ...)

In PyFunc models, these artifacts' paths are accessible from the `context` object under `context.artifacts`, and they can be loaded in the standard way for that file type.

For example, in a custom MLflow model:

Python

    class ModelPyfunc(mlflow.pyfunc.PythonModel):    def load_context(self, context):        self.model = torch.load(context.artifacts["model-weights"])        self.tokenizer = transformers.BertweetTokenizer.from_pretrained("model-base", local_files_only=True, cache_dir=context.artifacts["tokenizer_cache"])    ...

After your files and artifacts are packaged within your model artifact, you can serve your model to a [Model Serving endpoint](https://docs.databricks.com/aws/en/machine-learning/model-serving/create-manage-serving-endpoints).
