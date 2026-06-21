---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fc0e97bc24074055f32b7af96bf3b0564e93e12a9bef1c4d5a57b2e4b7108bcb
  pageDirectory: concepts
  sources:
    - model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - stage-level-scheduling-for-gpu-parallelism
    - SSFGP
    - Stage-Level Scheduling
  citations:
    - file: model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md
title: Stage-Level Scheduling for GPU Parallelism
description: Using Spark's ResourceProfile and stage-level scheduling to control the number of tasks running per GPU for increased parallelism
tags:
  - spark
  - gpu
  - scheduling
timestamp: "2026-06-19T19:43:16.256Z"
---

# Stage-Level Scheduling for GPU Parallelism

**Stage-Level Scheduling for GPU Parallelism** is a Spark feature that allows you to control how many tasks run per GPU within a single stage. By default, Spark schedules one task per GPU on each machine. Stage-level scheduling lets you override that default to increase parallelism by specifying fractional GPU resource requests. ^[model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md]

## How It Works

Stage-level scheduling uses Spark’s ResourceProfile and TaskResourceRequests APIs to define the GPU resource requirement per task. When you set a fractional request — for example, `0.5` of a GPU — Spark schedules two tasks per physical GPU (since each task requires half a GPU). This increases the number of concurrent tasks executing on the same GPU, potentially improving throughput for models that do not fully saturate the GPU when run singly. ^[model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md]

The resource profile is built with ResourceProfileBuilder and applied to an RDD via the `.withResources()` method. The profile takes effect for the stage in which the RDD is computed. ^[model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md]

## Usage Example

The following code creates a resource profile that requests 0.5 GPU per task, applies it to a DataFrame’s RDD, and runs a model prediction stage with higher parallelism:

```python
from pyspark.resource import TaskResourceRequests, ResourceProfileBuilder

task_requests = TaskResourceRequests().resource("gpu", 0.5)
builder = ResourceProfileBuilder()
resource_profile = builder.require(task_requests).build

rdd = df.withColumn(
    'predictions', loaded_model(struct(*map(col, df.columns)))
).rdd.withResources(resource_profile)
```

^[model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md]

In this example:

- `TaskResourceRequests().resource("gpu", 0.5)` declares that each task uses half of one GPU.
- `ResourceProfileBuilder()` assembles the profile.
- `.withResources(resource_profile)` attaches the profile to the RDD, instructing the scheduler to allocate tasks according to the profile when executing that stage.

## When to Use

Stage-level scheduling is most beneficial when a single inference task does not fully utilise a GPU. By packing multiple tasks onto the same GPU, you can increase cluster throughput and reduce overall job run time. It is a tuning technique used in conjunction with batch-size tuning and DataFrame Repartitioning to maximise hardware utilisation. ^[model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md]

## Related Concepts

- ResourceProfile – Defines the resource requirements (CPU, GPU, memory) for a task set.
- TaskResourceRequests – Specifies the amount of a resource (e.g., GPU) per task.
- GPU Scheduling on Spark – Overview of how Spark allocates GPU resources to executors and tasks.
- Batch Inference with Pandas UDFs – Alternative approach for distributing model inference; stage-level scheduling can be combined with UDFs to increase task concurrency per GPU.
- Tune Performance for Hugging Face Inference – Broader guidance on optimising GPU inference on Databricks.

## Sources

- model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md

# Citations

1. [model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md](/references/model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws-b5ae44ca.md)
