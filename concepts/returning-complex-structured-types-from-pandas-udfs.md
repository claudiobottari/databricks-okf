---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2d0449ed3317b6648397e0adef5f8ea605995712b06962a3b52ea0e950c9f76f
  pageDirectory: concepts
  sources:
    - model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - returning-complex-structured-types-from-pandas-udfs
    - RCSTFPU
  citations:
    - file: model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md
title: Returning Complex Structured Types from Pandas UDFs
description: Using array<struct<...>> return type annotations in Pandas UDFs to represent complex NLP pipeline outputs like entity recognition results
tags:
  - spark
  - pandas-udf
  - type-system
timestamp: "2026-06-19T19:43:00.450Z"
---

# Returning Complex Structured Types from Pandas UDFs

**Returning Complex Structured Types from Pandas UDFs** refers to the technique of using Pandas User-Defined Functions (UDFs) in Apache Spark to return structured, nested outputs — such as arrays of structs — from model inference or other complex computations. This approach is particularly useful when working with Hugging Face Transformers pipelines that produce rich, multi-field results like named-entity recognition (NER) outputs. ^[model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md]

## Motivation

Many NLP pipelines return outputs that are more complex than a single scalar value. For example, named-entity recognition pipelines return a list of dictionaries, each containing the entity text, its type, a confidence score, and character offsets. To preserve this structured information when processing data at scale across a Spark cluster, the UDF's return type must represent the nested schema. ^[model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md]

## Defining the Return Type

When a Pandas UDF returns complex output, you specify the return type as a Spark SQL type string in the `@pandas_udf` annotation. The return type should match the structure of the dictionaries returned by the pipeline. ^[model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md]

### Example: Named-Entity Recognition

Consider a Hugging Face NER pipeline that produces results like:

```python
[
  {'entity_group': 'ORG', 'score': 0.99933606, 'word': 'Hugging Face', 'start': 0, 'end': 12},
  {'entity_group': 'LOC', 'score': 0.99967843, 'word': 'New York City', 'start': 42, 'end': 55}
]
```

To represent this as a return type, use an `array` of `struct` fields, listing each dictionary entry as a field in the struct: ^[model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md]

```python
import pandas as pd
from pyspark.sql.functions import pandas_udf

@pandas_udf('array<struct<word string, entity_group string, score float, start integer, end integer>>')
def ner_udf(texts: pd.Series) -> pd.Series:
    return pd.Series(ner_pipeline(texts.to_list(), batch_size=1))
```

The `@pandas_udf` annotation specifies the complex return type. The UDF function accepts a Pandas Series of input texts and returns a Pandas Series where each element is a list of structs. ^[model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md]

## Usage in a Query

Once defined, the UDF can be called in a Spark `select` statement to apply the pipeline across the entire DataFrame: ^[model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md]

```python
display(df.select(df.texts, ner_udf(df.texts).alias('entities')))
```

This produces a DataFrame with a column `entities` containing structured annotations for each input text.

## Related Concepts

- Pandas User-Defined Functions (UDFs) — General mechanism for distributing pandas operations on Spark
- Hugging Face Transformers — Library providing pretrained NLP models and pipelines
- [Named-Entity Recognition (NER)](/concepts/named-entity-recognition-with-spark-nlp-and-mlflow.md) — An NLP task that commonly produces complex structured output
- Spark DataFrame API — The primary interface for working with structured data in Spark
- Model inference using Hugging Face Transformers for NLP — Broader guide on using Transformers with Pandas UDFs

## Sources

- model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md

# Citations

1. [model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws.md](/references/model-inference-using-hugging-face-transformers-for-nlp-databricks-on-aws-b5ae44ca.md)
