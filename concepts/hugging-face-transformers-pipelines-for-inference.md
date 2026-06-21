---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: dbd3ed967d9ed9f5b65d7cc7e61abbf8baab2f66e14f4072553c2cb4a30c4e31
  pageDirectory: concepts
  sources:
    - model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - hugging-face-transformers-pipelines-for-inference
    - HFTPFI
  citations:
    - file: model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md
title: Hugging Face Transformers Pipelines for Inference
description: Using the Hugging Face pipelines class to run pre-trained NLP models for tasks like translation and named-entity recognition on Databricks
tags:
  - nlp
  - hugging-face
  - inference
timestamp: "2026-06-19T19:42:55.223Z"
---

# Hugging Face Transformers Pipelines for Inference

**Hugging Face Transformers Pipelines for Inference** refers to the use of the `pipeline` class from the `transformers` library to run pre-trained models for natural language processing (NLP) tasks in a production or batch‑inference setting. On Databricks, these pipelines can be combined with Spark and Pandas UDFs to distribute inference across a cluster of CPU or GPU workers. ^[model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md]

## Overview

The Hugging Face `transformers` library provides the `pipeline` class, which abstracts away model loading, tokenization, and inference logic for a wide variety of NLP tasks — including text classification, translation, named‑entity recognition (NER), summarization, and question answering. ^[model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md]

On Databricks, you can use these pipelines for batch inference by wrapping them in [Pandas UDFs](/concepts/scalar-iterator-pandas-udfs.md), which distribute the model execution to each worker node in a Spark cluster. This approach works on both CPU and GPU clusters; many popular NLP models perform best on GPU hardware. ^[model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md]

> **Note:** This documentation has been retired. Databricks now recommends using `ai_query` for batch inference instead. See [Enrich data using AI Functions](https://docs.databricks.com/aws/en/large-language-models/ai-functions). ^[model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md]

## Requirements

- **MLflow 2.3** or later. ^[model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md]
- A cluster with the `transformers` library installed. The library is pre‑installed on Databricks Runtime 10.4 LTS ML and above. ^[model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md]
- For best performance, use a GPU cluster. CPU‑optimized models also work on CPU clusters. ^[model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md]

## Use Pandas UDFs to Distribute Model Computation

To perform inference on a Spark DataFrame, you can wrap a Hugging Face pipeline in a Pandas UDF. The following example creates a translation pipeline (English → French) and applies it to a text column:

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

The `device` parameter ensures GPUs are used if available. Spark automatically reassigns GPUs on worker nodes when using multi‑GPU instances. ^[model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md]

Call the UDF in a `select` statement:

```python
texts = ["Hugging Face is a French company based in New York City.",
         "Databricks is based in San Francisco."]
df = spark.createDataFrame(pd.DataFrame(texts, columns=["texts"]))
display(df.select(df.texts, translation_udf(df.texts).alias('translation')))
```

^[model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md]

## Return Complex Result Types

For tasks like named‑entity recognition, pipelines return a list of dictionaries (e.g., `entity_group`, `score`, `word`, `start`, `end`). You can define the UDF return type as an array of structs:

```python
@pandas_udf('array<struct<word string, entity_group string, score float, start integer, end integer>>')
def ner_udf(texts: pd.Series) -> pd.Series:
    return pd.Series(ner_pipeline(texts.to_list(), batch_size=1))
```

Use the UDF similarly:

```python
display(df.select(df.texts, ner_udf(df.texts).alias('entities')))
```

^[model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md]

## Tune Performance

Several knobs can improve inference throughput:

### Choose a Batch Size

Start with `batch_size=1`, then increase it until GPU utilisation is high but no `CUDA out of memory` errors occur. Monitor GPU metrics like `gpu0-util` and `gpu0_mem_util` in the cluster metrics. ^[model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md]

### Tune Parallelism with Stage‑Level Scheduling

By default, Spark schedules one task per GPU. To run multiple tasks per GPU, use `TaskResourceRequests`:

```python
from pyspark.resource import TaskResourceRequests, ResourceProfileBuilder

task_requests = TaskResourceRequests().resource("gpu", 0.5)
builder = ResourceProfileBuilder()
resource_profile = builder.require(task_requests).build
rdd = df.withColumn('predictions', loaded_model(struct(*map(col, df.columns)))).rdd.withResources(resource_profile)
```

^[model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md]

### Repartition Data to Use All Hardware

Check the number of partitions with `df.rdd.getNumPartitions()`. Repartition to a small multiple of the number of GPUs (or CPU cores) to fully utilise the cluster:

```python
repartitioned_df = df.repartition(desired_partition_count)
```

^[model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md]

### Cache the Model in DBFS or on Mount Points

To reduce model loading time and ingress costs across clusters, set the `TRANSFORMERS_CACHE` environment variable to a DBFS path before loading the pipeline:

```python
import os
os.environ['TRANSFORMERS_CACHE'] = '/dbfs/hugging_face_transformers_cache/'
```

Alternatively, log the model to [MLflow](/concepts/mlflow.md) using the MLflow `transformers` flavor. ^[model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md]

## Additional Resources

- [Fine‑tune Hugging Face models on Databricks](https://docs.databricks.com/aws/en/machine-learning/train-model/huggingface/fine-tune-model)
- [Prepare data for fine‑tuning Hugging Face models](https://docs.databricks.com/aws/en/machine-learning/train-model/huggingface/load-data)
- [What are Hugging Face Transformers?](https://docs.databricks.com/aws/en/machine-learning/train-model/huggingface/)

## Sources

- model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md

# Citations

1. [model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md](/references/model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws-b5ae44ca.md)
