---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a73adb89d7db73224080e6e8af33ce4734467a17eb4b96bd2e14fb6f06c02a2a
  pageDirectory: concepts
  sources:
    - debugging-guide-for-model-serving-databricks-on-aws.md
  confidence: 0.93
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - gpu-build-failures-and-flash-attention-dependencies
    - Flash-Attention Dependencies and GPU Build Failures
    - GBFAFD
  citations:
    - file: debugging-guide-for-model-serving-databricks-on-aws.md
title: GPU Build Failures and Flash-Attention Dependencies
description: Handling GPU-specific container build failures in model serving, including flash-attn dependency management with custom wheels and CUDA version compatibility.
tags:
  - model-serving
  - gpu
  - dependencies
  - flash-attn
timestamp: "2026-06-18T15:11:44.257Z"
---

# GPU Build Failures and Flash-Attention Dependencies

**GPU Build Failures** in [Model Serving](/concepts/model-serving.md) on Databricks occur when the container image for a GPU-serving endpoint fails to build. Common causes include GPU resource shortages and improperly configured dependencies for models that require the `flash-attn` library. Understanding these failure modes helps you diagnose and resolve build errors efficiently.

## GPU Availability Failures

A GPU build may fail with the following error: `Build could not start due to an internal error - please contact your Databricks representative.`. This typically indicates that GPU resources are unavailable in the current region due to supply constraints. To resolve this, contact your Databricks account team, who can provision additional GPU capacity depending on regional availability. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

## Flash-Attention Dependency Failures

Models that depend on `flash-attn` (such as many large language models) often cause build errors if the dependency is installed via a standard `pip install flash-attn`. A common symptom is `ModuleNotFoundError: No module named 'torch'` because the `flash-attn` package attempts to compile native code before the PyTorch dependencies are fully resolved in the build environment. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

### Recommended Workaround: Use a Custom Wheel

To avoid build failures, Databricks recommends using a pre-built wheel version of `flash-attn` rather than relying on `pip` to compile it from source. When logging the model with `mlflow.transformers.log_model`, pass all pip requirements as a list via the `pip_requirements` parameter. This list must include:

- A compatible version of PyTorch and torchvision that matches the CUDA version your wheel is built for.
- The explicit wheel URL for `flash-attn`.
- Any other required packages, such as `transformers`, `accelerate`, and supporting libraries.

For example, for CUDA 11.8 the following versions are recommended:  
`torch==2.0.1+cu118`, `torchvision==0.15.2+cu118`, and the flash-attn wheel `flash_attn-2.5.8+cu118torch2.0cxx11abiFALSE-cp311-cp311-linux_x86_64.whl`. The full `pip_requirements` list should include the appropriate `--extra-index-url` for PyTorch and all required packages. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

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
        "torchvision==0.15.2+cu118",
        "transformers==4.41.2",
        "https://github.com/Dao-AILab/flash-attention/releases/download/v2.5.8/flash_attn-2.5.8+cu118torch2.0cxx11abiFALSE-cp311-cp311-linux_x86_64.whl",
        # ... other required packages
    ],
    input_example=input_example,
    registered_model_name=registered_model_name,
)
```

## Preventative Measures

- **Define all important libraries as model dependencies** to ensure consistent and reproducible builds across environments. ^[debugging-guide-for-model-serving-databricks-on-aws.md]
- **Check the build logs** (available in the Events tab of the endpoint UI) to verify that the correct package versions are installed. ^[debugging-guide-for-model-serving-databricks-on-aws.md]
- For GPU builds, Databricks Model Serving automatically installs the recommended versions of CUDA and cuDNN according to public PyTorch and TensorFlow documentation; you do not need to specify these manually unless you require a custom version. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

## Related Concepts

- Model Serving Container Build
- [FlashAttention](/concepts/flash-attention.md)
- CUDA Compatibility
- [MLflow Transformers Integration](/concepts/mlflow-transformers-flavor.md)
- Debugging Model Serving Endpoints
- GPU Scheduling on Databricks

## Sources

- debugging-guide-for-model-serving-databricks-on-aws.md

# Citations

1. [debugging-guide-for-model-serving-databricks-on-aws.md](/references/debugging-guide-for-model-serving-databricks-on-aws-67072c6a.md)
