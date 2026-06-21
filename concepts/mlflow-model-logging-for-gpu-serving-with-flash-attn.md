---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 91e7e324808daac4ae972f778193edf0fab7a6fc368c7f163b443d30d06e99f3
  pageDirectory: concepts
  sources:
    - debugging-guide-for-model-serving-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-model-logging-for-gpu-serving-with-flash-attn
    - MMLFGSWF
  citations:
    - file: debugging-guide-for-model-serving-databricks-on-aws.md
title: MLflow Model Logging for GPU Serving with flash-attn
description: Best practices for logging transformer models that require flash-attn, including specifying compatible CUDA, PyTorch, Torchvision versions and using custom wheel references in pip_requirements for mlflow.transformers.log_model.
tags:
  - mlflow
  - gpu
  - transformers
  - model-serving
timestamp: "2026-06-19T14:56:25.265Z"
---

# MLflow Model Logging for GPU Serving with flash-attn

**MLflow Model Logging for GPU Serving with flash-attn** refers to the best practices for logging models that depend on the `flash-attn` library when they are intended to be served on GPU endpoints in Databricks Model Serving. Because `flash-attn` is a compiled CUDA extension, special care is needed during model logging to ensure the container build succeeds and the model loads correctly at serving time. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

## Prerequisites

When a model requires `flash-attn`, Databricks recommends using a **custom wheel version** of `flash-attn` rather than relying on a pip-install from PyPI. Using a standard pip install can result in build errors such as `ModuleNotFoundError: No module named 'torch'` because the pre-built wheel is not compatible with the torch version present in the container. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

## Best Practices

1. **Specify all pip requirements as a list** and pass it as the `pip_requirements` parameter to `mlflow.transformers.log_model()`.
2. **Include explicit versions** for PyTorch, torch, and torchvision that are **compatible with the CUDA version** used in the `flash-attn` wheel.
3. **Pin MLflow version** (e.g., `mlflow==2.13.1`) to avoid unexpected runtime changes.
4. **Add an `--extra-index-url`** pointing to the PyTorch wheel repository for the target CUDA version (e.g., `https://download.pytorch.org/whl/cu118` for CUDA 11.8). ^[debugging-guide-for-model-serving-databricks-on-aws.md]

## Example

The following example logs a Hugging Face `transformers` pipeline with `flash-attn` support for CUDA 11.8 and Python 3.11:

```python
import mlflow

logged_model = mlflow.transformers.log_model(
    transformers_model=test_pipeline,
    artifact_path="artifact_path",
    pip_requirements=[
        "--extra-index-url https://download.pytorch.org/whl/cu118",
        "mlflow==2.13.1",
        "setuptools<70.0.0",
        "torch==2.0.1+cu118",
        "accelerate==0.31.0",
        "astunparse==1.6.3",
        "bcrypt==3.2.0",
        "boto3==1.34.39",
        "configparser==5.2.0",
        "defusedxml==0.7.1",
        "dill==0.3.6",
        "google-cloud-storage==2.10.0",
        "ipython==8.15.0",
        "lz4==4.3.2",
        "nvidia-ml-py==12.555.43",
        "optree==0.12.1",
        "pandas==1.5.3",
        "pyopenssl==23.2.0",
        "pytesseract==0.3.10",
        "scikit-learn==1.3.0",
        "sentencepiece==0.1.99",
        "torchvision==0.15.2+cu118",
        "transformers==4.41.2",
        "https://github.com/Dao-AILab/flash-attention/releases/download/v2.5.8/flash_attn-2.5.8+cu118torch2.0cxx11abiFALSE-cp311-cp311-linux_x86_64.whl"
    ],
    input_example=input_example,
    registered_model_name=registered_model_name
)
```

After logging, the model can be deployed to a GPU Serving endpoint. The container build will install the exact versions specified, avoiding dependency conflicts. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

## Troubleshooting

If a build fails with `ModuleNotFoundError: No module named 'torch'`, verify that:

- The `flash-attn` wheel is built for your Python version and CUDA version (e.g., `cp311` for Python 3.11, `cu118` for CUDA 11.8).
- The `torch` and `torchvision` versions in `pip_requirements` match the CUDA version used by `flash-attn` (e.g., `torch==2.0.1+cu118`).
- An `--extra-index-url` for the correct CUDA version is included before the torch pin.

For general debugging of container builds, see the Model Serving Debugging Guide. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

## Related Concepts

- [MLflow](/concepts/mlflow.md) – Model logging and experiment tracking framework.
- GPU Serving – Serving models on GPU endpoints in Databricks.
- [Model Serving](/concepts/model-serving.md) – General endpoint deployment.
- [Model Container Build](/concepts/model-serving-container-build-debugging.md) – The process that assembles the serving container.
- transformers library – Hugging Face library frequently used with flash-attn.
- CUDA version compatibility – Ensuring GPU libraries match in the container.

## Sources

- debugging-guide-for-model-serving-databricks-on-aws.md

# Citations

1. [debugging-guide-for-model-serving-databricks-on-aws.md](/references/debugging-guide-for-model-serving-databricks-on-aws-67072c6a.md)
