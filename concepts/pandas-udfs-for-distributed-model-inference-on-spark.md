---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9cd61d6ff3341adb804f640a03cdb8f92ef303846a2992d04129e0800cda8440
  pageDirectory: concepts
  sources:
    - model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - pandas-udfs-for-distributed-model-inference-on-spark
    - PUFDMIOS
    - Pandas UDFs for Model Inference
    - Pandas UDFs for model inference
  citations:
    - file: model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md
title: Pandas UDFs for Distributed Model Inference on Spark
description: Wrapping Hugging Face models in Pandas UDFs to distribute batch inference across worker nodes in a Spark cluster
tags:
  - spark
  - pandas-udf
  - distributed-computing
timestamp: "2026-06-19T19:42:34.339Z"
---

# Pandas UDFs for Distributed Model Inference on Spark

**Pandas UDFs for Distributed Model Inference on Spark** describes how to use [Pandas UDFs](https://docs.databricks.com/aws/en/udf/pandas) (user-defined functions) to wrap a Hugging Face Transformers pipeline and distribute model inference across the worker nodes of a Spark cluster. This approach is suitable for batch inference on large datasets using pre-trained NLP models. ^[model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md]

## Requirements

- MLflow 2.3
- A cluster with the Hugging Face `transformers` library installed. The library is preinstalled on Databricks Runtime 10.4 LTS ML and above.
- GPU hardware is recommended for best performance, though some models optimized for CPUs can also be used. ^[model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md]

## Using Pandas UDFs for Model Inference

A Pandas UDF can wrap a Hugging Face Transformers pipeline and run it on each worker node. The `device` parameter controls GPU usage: set `device=0` when a GPU is available, or `device=-1` for CPU. Spark automatically handles GPU assignment on workers when using GPU clusters. ^[model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md]

### Example: Machine Translation

The following code creates a translation pipeline and a corresponding Pandas UDF:

```python
import pandas as pd
from transformers import pipeline
import torch
from pyspark.sql.functions import pandas_udf

device = 0 if torch.cuda.is_available() else -1
translation_pipeline = pipeline(task="translation_en_to_fr", model="t5-base", device=device)

@pandas_udf('string')
def translation_udf(texts: pd.Series) -> pd.Series:
    translations = [result['translation_text'] for result in translation_pipeline(texts.to_list(), batch_size=1)]
    return pd.Series(translations)
```

The UDF can then be applied in a `select` statement:

```python
texts = ["Hugging Face is a French company based in New York City.", "Databricks is based in San Francisco."]
df = spark.createDataFrame(pd.DataFrame(texts, columns=["texts"]))
display(df.select(df.texts, translation_udf(df.texts).alias('translation')))
```

^[model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md]

## Returning Complex Result Types

For tasks such as named-entity recognition (NER), pipelines return a list of dictionaries with fields like `entity_group`, `score`, `word`, `start`, and `end`. To return this structured output, annotate the UDF with a Spark `array<struct<...>>` type matching the pipeline’s output schema. ^[model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md]

### Example: Named-Entity Recognition

```python
import pandas as pd
from pyspark.sql.functions import pandas_udf

@pandas_udf('array<struct<word string, entity_group string, score float, start integer, end integer>>')
def ner_udf(texts: pd.Series) -> pd.Series:
    return pd.Series(ner_pipeline(texts.to_list(), batch_size=1))

display(df.select(df.texts, ner_udf(df.texts).alias('entities')))
```

^[model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md]

## Performance Tuning

Several techniques can improve inference throughput on a Spark cluster.

### Choose an Optimal Batch Size

The pipeline’s `batch_size` parameter controls how many samples are sent to the GPU at once. Start with a small batch (e.g., 1) and increase it until the GPU is fully utilized but not exceeding memory (avoiding `CUDA out of memory` errors). Monitor GPU utilization and memory via cluster metrics. ^[model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md]

### Increase Parallelism with Stage‑Level Scheduling

By default, Spark schedules one task per GPU. To run multiple tasks per GPU, use [Stage-Level Scheduling](/concepts/stage-level-scheduling-for-gpu-parallelism.md) with a `ResourceProfile` that requests a fractional GPU resource (e.g., 0.5 per task, yielding 2 tasks per GPU). ^[model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md]

### Repartition Data to Use All Resources

The input DataFrame should have enough partitions to cover the cluster’s parallelism. Check the partition count with `df.rdd.getNumPartitions()` and repartition to a small multiple of the number of GPUs (for GPU clusters) or cores (for CPU clusters). ^[model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md]

### Cache the Model in DBFS or Mount Points

Set the `TRANSFORMERS_CACHE` environment variable to a DBFS path or mount point before loading the pipeline. This caches the model files, reducing ingress costs and load times across cluster restarts. ^[model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md]

```python
import os
os.environ['TRANSFORMERS_CACHE'] = '/dbfs/hugging_face_transformers_cache/'
```

Alternatively, log the model to MLflow using the [MLflow Transformers Flavor](/concepts/mlflow-transformers-flavor.md) to achieve a similar effect. ^[model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md]

## Additional Resources

- [Prepare data for fine-tuning Hugging Face models](https://docs.databricks.com/aws/en/machine-learning/train-model/huggingface/load-data)
- [Fine-tune Hugging Face models for a single GPU](https://docs.databricks.com/aws/en/machine-learning/train-model/huggingface/fine-tune-model)
- [What are Hugging Face Transformers?](https://docs.databricks.com/aws/en/machine-learning/train-model/huggingface/)

^[model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md]

## Related Concepts

- Pandas UDF
- Hugging Face Transformers
- [MLflow](/concepts/mlflow.md)
- [Stage-Level Scheduling](/concepts/stage-level-scheduling-for-gpu-parallelism.md)
- DBFS
- GPU Utilization
- Batch Inference
- Spark DataFrame Partitioning

## Sources

- model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md

# Citations

1. [model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md](/references/model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws-b5ae44ca.md)
