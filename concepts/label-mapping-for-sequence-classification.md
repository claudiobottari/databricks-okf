---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 191bb558d99e390e1f2230770bdd209f6c1077074255cb2fdac324a28ab635af
  pageDirectory: concepts
  sources:
    - prepare-data-for-fine-tuning-hugging-face-models-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - label-mapping-for-sequence-classification
    - LMFSC
  citations:
    - file: prepare-data-for-fine-tuning-hugging-face-models-databricks-on-aws.md
title: Label Mapping for Sequence Classification
description: Mapping string labels to integer IDs and creating id2label/label2id dictionaries for Hugging Face AutoModelForSequenceClassification
tags:
  - hugging-face
  - classification
  - data-preprocessing
  - nlp
timestamp: "2026-06-19T19:57:44.302Z"
---

#Label Mapping for Sequence Classification

**Label Mapping for Sequence Classification** refers to the process of converting string-format class labels into integer IDs when preparing data for fine-tuning a Hugging Face Transformers model with [`AutoModelForSequenceClassification`](https://huggingface.co/docs/transformers/model_doc/auto#transformers.AutoModelForSequenceClassification). Because the `AutoModelForSequenceClassification` loader expects integer IDs as category labels, any dataset containing string labels must first be transformed to meet that requirement. ^[prepare-data-for-fine-tuning-hugging-face-models-databricks-on-aws.md]

## Overview

When you prepare your own training and evaluation data for text classification fine-tuning, the data is typically formatted as a Spark DataFrame with two columns: a text column and a column of labels. If the label column contains strings, you need to create two mapping dictionaries (`id2label` and `label2id`) that associate each unique string label with a unique integer ID. The integer IDs are then generated in a new label column using a Pandas UDF that applies the `label2id` lookup. ^[prepare-data-for-fine-tuning-hugging-face-models-databricks-on-aws.md]

## Creating Label Mappings

The first step is to collect the distinct string labels from the DataFrame and assign each an index. The following code snippet shows how to create the dictionary mappings: ^[prepare-data-for-fine-tuning-hugging-face-models-databricks-on-aws.md]

```python
labels = df.select(df.label).groupBy(df.label).count().collect()
id2label = {index: row.label for (index, row) in enumerate(labels)}
label2id = {row.label: index for (index, row) in enumerate(labels)}
```

- `id2label` maps integer positions back to the original string labels.
- `label2id` maps the original string labels to their corresponding integer positions.

## Applying the Mapping

With the mappings defined, you can use a Pandas UDF to convert the string label column into an integer ID column: ^[prepare-data-for-fine-tuning-hugging-face-models-databricks-on-aws.md]

```python
from pyspark.sql.functions import pandas_udf
import pandas as pd

@pandas_udf('integer')
def replace_labels_with_ids(labels: pd.Series) -> pd.Series:
    return labels.apply(lambda x: label2id[x])

df_id_labels = df.select(replace_labels_with_ids(df.label).alias('label'), df.text)
```

The resulting DataFrame `df_id_labels` has an integer `label` column that `AutoModelForSequenceClassification` can accept. This DataFrame can then be loaded into a Hugging Face `Dataset` using `Dataset.from_spark()` for training. ^[prepare-data-for-fine-tuning-hugging-face-models-databricks-on-aws.md]

## Related Concepts

- [AutoModelForSequenceClassification](/concepts/automodelforsequenceclassification.md) – The Hugging Face model loader that requires integer label IDs.
- Hugging Face Transformers – The library providing the model and configuration classes.
- Pandas UDF – Used to apply the label mapping efficiently over a Spark DataFrame.
- [Unity Catalog](/concepts/unity-catalog.md) – The recommended location for caching datasets during fine-tuning.
- Fine-tuning – The broader process of adapting a pretrained model to a specific task.

## Sources

- prepare-data-for-fine-tuning-hugging-face-models-databricks-on-aws.md

# Citations

1. [prepare-data-for-fine-tuning-hugging-face-models-databricks-on-aws.md](/references/prepare-data-for-fine-tuning-hugging-face-models-databricks-on-aws-b70184e4.md)
