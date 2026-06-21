---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: edee5e85e20a112c18a640b8cd83d17039ca0520952c6a548857adb823fd15c4
  pageDirectory: concepts
  sources:
    - debugging-guide-for-model-serving-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - flash-attention-model-logging-for-serving
    - FMLFS
  citations:
    - file: debugging-guide-for-model-serving-databricks-on-aws.md
title: Flash-Attention Model Logging for Serving
description: Best practices for logging MLflow models that require flash-attn, including custom wheel versions and compatible CUDA/pytorch dependency specification.
tags:
  - model-serving
  - mlflow
  - gpu
  - deep-learning
timestamp: "2026-06-19T18:17:58.916Z"
---

# Flash-Attention Model Logging for Serving

**Flash-Attention Model Logging for Serving** refers to the specific considerations and best practices when logging models that require the `flash-attn` library for deployment to [Model Serving](/concepts/model-serving.md) endpoints on Databricks. This guidance applies when models depend on the [Flash Attention](/concepts/flash-attention.md) optimization technique for efficient transformer inference.

## Overview

When logging a model that requires `flash-attn` for [Model Serving](/concepts/model-serving.md), Databricks recommends using a custom wheel version of `flash-attn` rather than relying on default package installation. Failure to use a custom wheel can result in build errors such as `ModuleNotFoundError: No module named 'torch'` during the container build process. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

## Best Practice: Custom Wheel Version

To properly log a model with flash-attention support, you must specify all pip requirements as a list and pass them as parameters to your `mlflow.transformers.log_model` function. This approach ensures compatibility between the flash-attention wheel and the required PyTorch ecosystem versions. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

### Required Dependencies

When using a custom wheel, you must also specify:

- The **pytorch**, **torch**, and **torchvision** versions that are compatible with the CUDA version specified in your `flash-attn` wheel
- All other model dependencies as explicit pip requirements

^[debugging-guide-for-model-serving-databricks-on-aws.md]

### Example for CUDA 11.8

Databricks recommends the following versions and wheels for CUDA 11.8:

- PyTorch: `https://download.pytorch.org/whl/cu118`
- Torch: `2.0.1+cu118`
- Torchvision: `0.15.2+cu118`
- Flash-Attn: `flash_attn-2.5.8+cu118torch2.0cxx11abiFALSE-cp311-cp311-linux_x86_64.whl`

^[debugging-guide-for-model-serving-databricks-on-aws.md]

### Python Example

```python
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

^[debugging-guide-for-model-serving-databricks-on-aws.md]

## Common Build Errors

If `flash-attn` is not properly configured, the following errors can occur:

- **`ModuleNotFoundError: No module named 'torch'`**: This occurs when the flash-attention wheel is incompatible with the installed torch version, or when torch is not explicitly listed in the pip requirements. ^[debugging-guide-for-model-serving-databricks-on-aws.md]
- **`OSError: [Errno 28] No space left on device`**: Can occur when too many large artifacts are logged alongside the model. Check in [MLflow](/concepts/mlflow.md) that extraneous artifacts are not logged and redeploy the slimmed-down package. ^[debugging-guide-for-model-serving-databricks-on-aws.md]
- **Build failure due to GPU unavailability**: GPU builds may fail due to supply constraints. Contact your Databricks account team for resolution. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

## Related Concepts

- [Model Serving](/concepts/model-serving.md) - Deployment platform for MLflow models
- Debugging guide for Model Serving - General debugging procedures
- Container Build Debugging - Troubleshooting build failures
- [MLflow transformers](/concepts/mlflow-transformers-flavor.md) - Logging transformers models
- [Flash Attention](/concepts/flash-attention.md) - Efficient attention mechanism
- CUDA Compatibility - Ensuring GPU library alignment

## Sources

- debugging-guide-for-model-serving-databricks-on-aws.md

# Citations

1. [debugging-guide-for-model-serving-databricks-on-aws.md](/references/debugging-guide-for-model-serving-databricks-on-aws-67072c6a.md)
