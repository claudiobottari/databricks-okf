---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b73dfce0e2822fd204e7c04739d6eef682caa30c337bbf41d04d1319d67da262
  pageDirectory: concepts
  sources:
    - debugging-guide-for-model-serving-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - flash-attn-dependency-management-in-model-serving
    - FDMIMS
  citations:
    - file: debugging-guide-for-model-serving-databricks-on-aws.md
title: flash-attn Dependency Management in Model Serving
description: Best practices for logging models requiring flash-attn, including using custom wheel versions, specifying compatible PyTorch/CUDA versions, and listing all pip requirements explicitly in mlflow.transformers.log_model.
tags:
  - model-serving
  - dependencies
  - mlflow
  - gpu
timestamp: "2026-06-18T11:44:36.629Z"
---

#flash-attn Dependency Management in Model Serving

**flash-attn** (Flash Attention) is an optimized attention implementation commonly used with large transformer models. When serving such models on [Databricks Model Serving](/concepts/databricks-model-serving.md), special care is required to manage the `flash-attn` dependency, particularly if the model was logged with MLflow. Without proper handling, the container build can fail with errors such as `ModuleNotFoundError: No module named 'torch'`. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

## The Problem

If you log a model that requires `flash-attn` and do not explicitly specify compatible versions for PyTorch, Torch, TorchVision, and CUDA, the container build may fail. The error typically surfaces as `ModuleNotFoundError: No module named 'torch'` because `flash-attn` is compiled against a specific CUDA and PyTorch version, and the default build environment may not satisfy those constraints. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

## The Solution: Use a Custom Wheel

Databricks recommends using a **custom wheel version** of `flash-attn` rather than relying on PyPI’s standard distribution. This ensures that the compiled binary matches the CUDA and PyTorch versions present in the serving container. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

To do this, specify all pip requirements as a list and pass it as the `pip_requirements` parameter to `mlflow.transformers.log_model`. The list must include:

- An extra-index URL pointing to the PyTorch wheel repository for the correct CUDA version.
- Exact versions of `torch`, `torchvision`, and any other critical libraries.
- The full URL of the `flash-attn` wheel from the [flash-attention releases](https://github.com/Dao-AILab/flash-attention/releases).

## Recommended Versions for CUDA 11.8

For CUDA 11.8, Databricks recommends the following versions and wheel URLs: ^[debugging-guide-for-model-serving-databricks-on-aws.md]

| Dependency | Recommended Version/URL |
|------------|-------------------------|
| PyTorch index | `https://download.pytorch.org/whl/cu118` |
| `torch` | `2.0.1+cu118` |
| `torchvision` | `0.15.2+cu118` |
| `flash-attn` wheel | `https://github.com/Dao-AILab/flash-attention/releases/download/v2.5.8/flash_attn-2.5.8+cu118torch2.0cxx11abiFALSE-cp311-cp311-linux_x86_64.whl` |

Use these in `pip_requirements` to ensure compatibility.

## Example Code

The following example shows how to log a transformer model with `flash-attn` as a dependency using the recommended wheel: ^[debugging-guide-for-model-serving-databricks-on-aws.md]

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

Key points in the example:

- The `--extra-index-url` points to the PyTorch CUDA 11.8 wheel index.
- `torch`, `torchvision`, and `flash-attn` versions are pinned to match the CUDA build.
- The `flash-attn` wheel is provided as a full HTTPS URL, which pip will download and install.

## When to Use This Approach

Use the custom wheel approach whenever your model logged with MLflow requires `flash-attn` and is intended to be deployed on Model Serving. This avoids build failures and ensures the serving container has a consistent, working environment. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

If you are using a different CUDA version, adjust the PyTorch index URL, torch/torchvision versions, and the flash-attn wheel accordingly. Databricks recommends using the publicly available wheels from the flash-attention releases page that match your CUDA and PyTorch combination.

## Related Concepts

- [Model Serving](/concepts/model-serving.md)
- [MLflow](/concepts/mlflow.md)
- Dependency management in serving
- CUDA compatibility
- Container build debugging
- [Pre-deployment Validation for Model Serving](/concepts/pre-deployment-validation-for-model-serving.md)

## Sources

- debugging-guide-for-model-serving-databricks-on-aws.md

# Citations

1. [debugging-guide-for-model-serving-databricks-on-aws.md](/references/debugging-guide-for-model-serving-databricks-on-aws-67072c6a.md)
