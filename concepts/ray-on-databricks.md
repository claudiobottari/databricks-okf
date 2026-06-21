---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bc9c59f326781589b64b43c347708e24348e24f19b8b5b68a12a40fdae9b2bdd
  pageDirectory: concepts
  sources:
    - distributed-training-databricks-on-aws.md
    - start-a-ray-cluster-on-databricks-databricks-on-aws.md
    - what-is-ray-on-databricks-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - ray-on-databricks
    - ROD
    - RayTune on Databricks
    - What is Ray on Databricks?
  citations:
    - file: what-is-ray-on-databricks-databricks-on-aws.md
    - file: start-a-ray-cluster-on-databricks-databricks-on-aws.md
    - file: distributed-training-databricks-on-aws.md
title: Ray on Databricks
description: An open-source framework for parallel compute processing that scales ML workflows and AI applications within the Databricks environment.
tags:
  - distributed-computing
  - ray
  - ai
timestamp: "2026-06-19T18:35:12.977Z"
---

# Ray on Databricks

**Ray on Databricks** allows you to run [Ray](https://docs.ray.io/en/latest/index.html) applications — an open-source framework for scaling Python and AI workloads — directly on Databricks clusters. With Databricks Runtime ML 12.2 LTS and above, you can create Ray clusters inside an Apache Spark cluster and benefit from Databricks' platform features. ^[what-is-ray-on-databricks-databricks-on-aws.md, start-a-ray-cluster-on-databricks-databricks-on-aws.md]

Ray and Apache Spark are complementary frameworks. Spark excels at data parallelism for tasks like ETL and data analytics, while Ray handles dynamic, compute-intensive workloads such as machine learning training, hyperparameter tuning, and reinforcement learning. Running them together on a single platform simplifies infrastructure and enables seamless data transfer. ^[what-is-ray-on-databricks-databricks-on-aws.md]

## Benefits of Running Ray on Databricks

- **Unified platform** – Run Ray and Apache Spark in the same compute environment, enabling seamless ETL and parallel computation. ^[what-is-ray-on-databricks-databricks-on-aws.md]
- **Governance** – Lineage tracking, data versioning, and access control via [Unity Catalog](/concepts/unity-catalog.md). ^[what-is-ray-on-databricks-databricks-on-aws.md]
- **Infrastructure management** – Use Databricks Terraform Provider and Databricks Asset Bundles to manage clusters and jobs. ^[what-is-ray-on-databricks-databricks-on-aws.md]
- **Managed Ray clusters** – Ray runs in the same execution environment as the Spark cluster, ensuring scalability without complex setup. ^[what-is-ray-on-databricks-databricks-on-aws.md]
- **Model Serving** – Models trained with Ray Train can be deployed to [Databricks Model Serving](/concepts/databricks-model-serving.md) for low-latency inference. ^[what-is-ray-on-databricks-databricks-on-aws.md]
- **MLflow integration** – Track experiments and manage model development using the fully managed [MLflow on Databricks](/concepts/mlflow-on-databricks.md). ^[what-is-ray-on-databricks-databricks-on-aws.md]
- **Automated workflows** – Use [Lakeflow Jobs](/concepts/lakeflow-jobs.md) to build production-ready pipelines. ^[what-is-ray-on-databricks-databricks-on-aws.md]
- **Code management** – Integrate with Databricks Git folders for version control. ^[what-is-ray-on-databricks-databricks-on-aws.md]
- **Delta Lake** – Connect Ray to [Delta Lake](/concepts/delta-lake.md) for efficient data access. ^[what-is-ray-on-databricks-databricks-on-aws.md]

## Use Cases

### Machine Learning and Deep Learning

- **Hyperparameter tuning** – Use [Ray Tune](/concepts/ray-tune.md) for scalable hyperparameter search. ^[what-is-ray-on-databricks-databricks-on-aws.md]
- **Distributed training** – Scale PyTorch, TensorFlow, HuggingFace, and Keras models across multiple nodes. ^[what-is-ray-on-databricks-databricks-on-aws.md]
- **Traditional ML** – Distribute training, evaluation, and batch inference for models built with scikit-learn or XGBoost. ^[what-is-ray-on-databricks-databricks-on-aws.md]

### High-Performance Computing (HPC)

- **Mathematical computations** – Parallelize complex calculations in physics, genomics, or finance using Ray Core. ^[what-is-ray-on-databricks-databricks-on-aws.md]
- **Time series forecasting** – Run concurrent forecasting models with Prophet or ARIMA. ^[what-is-ray-on-databricks-databricks-on-aws.md]

### Data Processing and Feature Engineering

- **Computed features** – Distribute compute-intensive feature engineering tasks. ^[what-is-ray-on-databricks-databricks-on-aws.md]
- **Multimedia processing** – Accelerate audio, image, and video processing for speech recognition, classification, and analysis. ^[what-is-ray-on-databricks-databricks-on-aws.md]

## Limitations

- Ray on Apache Spark is supported for **dedicated access mode** and **no isolation shared access mode**; it cannot be initiated on serverless compute clusters. ^[what-is-ray-on-databricks-databricks-on-aws.md]
- Avoid running `%pip` after the Ray cluster is started — it will shut down the cluster. Install libraries before initializing Ray. ^[what-is-ray-on-databricks-databricks-on-aws.md]
- Overriding configuration from `ray.util.spark.setup_ray_cluster` can destabilize the cluster. Avoid over-subscribing Ray cluster resources. ^[what-is-ray-on-databricks-databricks-on-aws.md]
- For GPU multi-node training, set `NCCL_SOCKET_IFNAME` to `eth0` to avoid `ncclInternalError`. ^[what-is-ray-on-databricks-databricks-on-aws.md]

## Starting a Ray Cluster

Databricks simplifies starting a Ray cluster by handling cluster and job configuration the same way as any Apache Spark job. The Ray cluster runs on top of the managed Spark cluster. ^[start-a-ray-cluster-on-databricks-databricks-on-aws.md]

```python
from ray.util.spark import setup_ray_cluster
import ray

# Example: cluster with four workers, 8 CPUs each
setup_ray_cluster(num_worker_nodes=4, num_cpus_per_worker=8)

# Pass custom configuration to ray.init
ray.init(ignore_reinit_error=True)
```

This approach works at any cluster scale, from a few to hundreds of nodes, and supports autoscaling. ^[start-a-ray-cluster-on-databricks-databricks-on-aws.md]

After creating the Ray cluster, you can run any Ray application code in a Databricks notebook. ^[start-a-ray-cluster-on-databricks-databricks-on-aws.md]

### Example Application

```python
import ray
import random
import time
from fractions import Fraction

ray.init()

@ray.remote
def pi4_sample(sample_count):
    in_count = 0
    for i in range(sample_count):
        x = random.random()
        y = random.random()
        if x*x + y*y <= 1:
            in_count += 1
    return Fraction(in_count, sample_count)

SAMPLE_COUNT = 1000 * 1000
start = time.time()
future = pi4_sample.remote(sample_count=SAMPLE_COUNT)
pi4 = ray.get(future)
end = time.time()
print(f'Running {SAMPLE_COUNT} tests took {end - start} seconds')
print(f'Pi estimate: {float(pi4 * 4)}')
```

^[start-a-ray-cluster-on-databricks-databricks-on-aws.md]

### Shutting Down a Ray Cluster

Ray clusters automatically shut down when:
- You detach your interactive notebook from the Databricks cluster
- Your Databricks job completes
- Your Databricks cluster is restarted or terminated
- There's no activity for the specified idle time

To shut down manually, call `shutdown_ray_cluster` and `ray.shutdown()`. ^[start-a-ray-cluster-on-databricks-databricks-on-aws.md]

```python
from ray.utils.spark import shutdown_ray_cluster
import ray

shutdown_ray_cluster()
ray.shutdown()
```

^[start-a-ray-cluster-on-databricks-databricks-on-aws.md]

## Installation Notes

Databricks recommends installing necessary libraries with `%pip install <your-library>` before starting the Ray cluster. Specifying dependencies in the Ray init function call installs them in a location inaccessible to Spark worker nodes, causing version incompatibilities and import errors. ^[start-a-ray-cluster-on-databricks-databricks-on-aws.md]

## Best Practices

- Install all dependencies with `%pip` before initializing the Ray cluster. ^[start-a-ray-cluster-on-databricks-databricks-on-aws.md]
- For large-scale distributed training, Databricks recommends considering [DeepSpeed](/concepts/deepspeed.md) or [TorchDistributor](/concepts/torchdistributor.md) as alternatives to Ray depending on the workload. ^[distributed-training-databricks-on-aws.md]

## Related Concepts

- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) – Overview of distributed training options on Databricks
- [DeepSpeed](/concepts/deepspeed.md) – Memory-efficient training with Microsoft's DeepSpeed library
- [TorchDistributor](/concepts/torchdistributor.md) – Distributed PyTorch training on Spark
- [MLflow on Databricks](/concepts/mlflow-on-databricks.md) – Experiment tracking and model registry
- [Delta Lake](/concepts/delta-lake.md) – Storage layer for reliable data lakes
- [Unity Catalog](/concepts/unity-catalog.md) – Governance and data lineage
- [Databricks Model Serving](/concepts/databricks-model-serving.md) – Low-latency model deployment
- [Lakeflow Jobs](/concepts/lakeflow-jobs.md) – Production job orchestration
- Databricks Asset Bundles – Infrastructure as code

## Sources

- what-is-ray-on-databricks-databricks-on-aws.md
- start-a-ray-cluster-on-databricks-databricks-on-aws.md
- distributed-training-databricks-on-aws.md

# Citations

1. [what-is-ray-on-databricks-databricks-on-aws.md](/references/what-is-ray-on-databricks-databricks-on-aws-4f0da5d5.md)
2. [start-a-ray-cluster-on-databricks-databricks-on-aws.md](/references/start-a-ray-cluster-on-databricks-databricks-on-aws-abb1b2de.md)
3. [distributed-training-databricks-on-aws.md](/references/distributed-training-databricks-on-aws-826bf389.md)
