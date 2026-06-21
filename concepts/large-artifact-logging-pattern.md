---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 96207f23e4bee8a7cf7c83d48ff8bcf5b0cccf26b741bd54abd136165b374a1b
  pageDirectory: concepts
  sources:
    - integrate-mlflow-and-ray-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - large-artifact-logging-pattern
    - LALP
  citations:
    - file: integrate-mlflow-and-ray-databricks-on-aws.md
title: Large Artifact Logging Pattern
description: Best practice for handling large artifacts in distributed Ray workloads by persisting them as files and logging with MLflow via file path references.
tags:
  - mlflow
  - ray
  - artifacts
timestamp: "2026-06-19T19:11:15.958Z"
---

# Large Artifact Logging Pattern

The **Large Artifact Logging Pattern** is a best practice for handling memory-intensive objects — such as large Pandas tables, images, plots, or serialized models — when integrating Ray Core with [MLflow](/concepts/mlflow.md) in a distributed environment. Instead of returning large objects from remote tasks to the driver node (which can cause memory pressure), the pattern recommends persisting the artifact as a file on a distributed filesystem like DBFS and then logging it using MLflow’s file-based API. ^[integrate-mlflow-and-ray-databricks-on-aws.md]

## Rationale

When using Ray Core to distribute work across multiple nodes, it is generally best to log MLflow models and metrics from the driver process rather than from worker nodes. Metrics and metadata are small enough to transfer back to the driver without issue, but large artifacts can overwhelm the driver’s memory if returned directly. The Large Artifact Logging Pattern avoids this bottleneck by offloading the storage and transfer of heavy objects to the filesystem. ^[integrate-mlflow-and-ray-databricks-on-aws.md]

## Steps to Apply the Pattern

1. **Persist the artifact to a file** inside the remote Ray task. Use a shared filesystem such as DBFS (`/dbfs/...`) so the driver can later access it.
2. **Return any lightweight metadata** (e.g., a metric value or a status code) from the remote task back to the driver.
3. **On the driver side**, after collecting results, call `mlflow.log_artifact()` with the path to the saved file. Optionally, reload the artifact into memory if further processing is needed before logging.

The following code snippet demonstrates the pattern:

```python
import mlflow

@ray.remote
def example_logging_task(x):
    # ... create a large object that needs to be stored
    with open("/dbfs/myLargeFilePath.txt", "w") as f:
        f.write(myLargeObject)
    return x

with mlflow.start_run() as run:
    results = ray.get([example_logging_task.remote(x) for x in range(10)])
    for x in results:
        mlflow.log_metric("x", x)
        # Directly log the saved file by specifying the path
        mlflow.log_artifact("/dbfs/myLargeFilePath.txt")
```

^[integrate-mlflow-and-ray-databricks-on-aws.md]

## When to Use

Use this pattern whenever a Ray task generates an object that is too large to fit comfortably in the driver’s memory after aggregation. Examples include:

- Large Pandas DataFrames or NumPy arrays
- High‑resolution images or plots
- Serialized model checkpoints (`.pkl`, `.pt`, `.h5`)
- Any binary artifact that would cause memory contention if transferred as a Python object

In contrast, small metrics, scalars, and configuration parameters should still be returned from tasks and logged with `mlflow.log_metric()` or similar light‑weight methods. ^[integrate-mlflow-and-ray-databricks-on-aws.md]

## Alternatives and Considerations

For models produced by [Ray Train](/concepts/ray-train-resource-allocation.md), the recommended approach is to save the training checkpoint to disk using Ray’s checkpointing mechanism, reload it in the native deep‑learning framework on the driver, and then log it with the appropriate MLflow flavor (e.g., `mlflow.pytorch.log_model()`). This is similar in spirit to the Large Artifact Logging Pattern but uses Ray Train’s built‑in checkpoint facilities instead of a custom file. ^[integrate-mlflow-and-ray-databricks-on-aws.md]

When applying the pattern, ensure that the filesystem path is accessible from the driver (e.g., DBFS on Databricks). The artifact is logged in the current [MLflow Run](/concepts/mlflow-run.md), which can then be viewed in the [MLflow experiment UI](/concepts/mlflow-experiment.md) or retrieved programmatically.

## Related Concepts

- [MLflow Tracking](/concepts/mlflow-tracking.md) – The foundation for logging artifacts, metrics, and parameters.
- Ray Core – The distributed execution framework that requires this pattern for large objects.
- [Ray Train](/concepts/ray-train-resource-allocation.md) – Distributed model training; its checkpointing approach can be used instead of manual file persistence.
- mlflow.log_artifact – The API used to log a local file as an MLflow artifact.
- DBFS – The Databricks File System commonly used for shared artifact storage.

## Sources

- integrate-mlflow-and-ray-databricks-on-aws.md

# Citations

1. [integrate-mlflow-and-ray-databricks-on-aws.md](/references/integrate-mlflow-and-ray-databricks-on-aws-05a679fb.md)
