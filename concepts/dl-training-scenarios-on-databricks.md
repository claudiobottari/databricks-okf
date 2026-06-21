---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f4b85249adfa1f0c473acc29b240e87ec9238dbfed7a0a832c70264133c9fd1e
  pageDirectory: concepts
  sources:
    - load-data-using-petastorm-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - dl-training-scenarios-on-databricks
    - DTSOD
  citations:
    - file: load-data-using-petastorm-databricks-on-aws.md
    - file: fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md
    - file: get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md
title: DL Training Scenarios on Databricks
description: "The three supported deep learning training scenarios on Databricks: single-node training, distributed hyperparameter tuning, and distributed training."
tags:
  - deep-learning
  - training
  - databricks
  - distributed-computing
timestamp: "2026-06-19T19:14:54.349Z"
---

# DL Training Scenarios on Databricks

**Deep learning (DL) training on Databricks** is categorized into three main scenarios: single‑node training, distributed hyperparameter tuning, and distributed training. Each scenario addresses different model sizes, hardware topologies, and optimization requirements. Databricks provides infrastructure and libraries such as Petastorm (deprecated, with Mosaic Streaming recommended), Fully Sharded Data Parallel (FSDP), and serverless GPU compute to support these workloads. ^[load-data-using-petastorm-databricks-on-aws.md] ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md] ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

## Single‑Node Training

Single‑node training uses the memory and compute of a single machine, which may contain one or several GPUs. For models that fit entirely within a single GPU, standard [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) is a straightforward choice. When a single node contains multiple GPUs (e.g., an 8×H100 configuration), the `@distributed` decorator from the `serverless_gpu` library can coordinate work across those GPUs on the same node. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md] ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

Data for single‑node training can be loaded from Apache Spark DataFrames or directly from Parquet files using the Petastorm library, which converts the data into a `tf.data.Dataset` or `torch.utils.data.DataLoader`. The recommended workflow is to use Spark for preprocessing, materialize the DataFrame in Parquet format via Petastorm’s Spark converter, and then feed the data into a DL framework. ^[load-data-using-petastorm-databricks-on-aws.md]

## Distributed Hyperparameter Tuning

Distributed hyperparameter tuning runs multiple training trials in parallel, each on a separate set of resources. Databricks supports this scenario by leveraging cluster parallelism and frameworks like [Hyperopt](/concepts/hyperopt.md) or built-in tuning utilities. Petastorm can be used to convert and cache data so that each trial reads from the same Parquet cache, avoiding redundant data loading. ^[load-data-using-petastorm-databricks-on-aws.md]

## Distributed Training

Distributed training scales model training across multiple nodes and GPUs. For models in the 20 billion to 120 billion+ parameter range, [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) is the recommended approach. FSDP shards model parameters, gradients, and optimizer states across GPUs, substantially reducing per‑GPU memory usage compared to DDP. For workloads requiring even more advanced memory optimization, [DeepSpeed](/concepts/deepspeed.md) can be considered as an alternative. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

Distributed training on Databricks can use serverless GPU compute with multi‑node configurations. Each 8×H100 node provides eight H100 80 GB GPUs; multiple such nodes can be coordinated for larger models. Petastorm also supports distributed training environments by enabling single‑node or distributed reading of Parquet datasets. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md] ^[load-data-using-petastorm-databricks-on-aws.md]

## Data Loading Options

| Approach | Description | Status |
|----------|-------------|--------|
| Petastorm Spark Converter | Converts Spark DataFrames to TensorFlow or PyTorch formats via Parquet cache. | Deprecated |
| Mosaic Streaming | Recommended replacement for Petastorm; streams large datasets from cloud storage. | Active |
| Direct Parquet with Petastorm | Loads Parquet files via DBFS mount without the Spark converter. | Deprecated |

The Petastorm Spark converter caches the input DataFrame in a user‑specified directory (e.g., `file:///dbfs/tmp/`). The cache can be explicitly deleted or managed through object‑storage lifecycle rules. ^[load-data-using-petastorm-databricks-on-aws.md]

## Related Concepts

- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md)
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md)
- [DeepSpeed](/concepts/deepspeed.md)
- [Mosaic Streaming](/concepts/mosaic-streaming.md)
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md)
- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md)
- [20B to 120B+ Parameter Model Training](/concepts/20b-to-120b-parameter-model-training.md)
- [Petastorm](/concepts/petastorm.md)
- [Hyperopt](/concepts/hyperopt.md)

## Sources

- load-data-using-petastorm-databricks-on-aws.md
- fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md
- get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md

# Citations

1. [load-data-using-petastorm-databricks-on-aws.md](/references/load-data-using-petastorm-databricks-on-aws-328aca7b.md)
2. [fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md](/references/fully-sharded-data-parallel-fsdp-training-databricks-on-aws-50fc8f20.md)
3. [get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md](/references/get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws-047f70e1.md)
