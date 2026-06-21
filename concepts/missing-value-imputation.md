---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 470323f0bd063bada569a68eeefff7149674f5669a6734649e7f036074a67ddd
  pageDirectory: concepts
  sources:
    - data-preparation-for-classification-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - missing-value-imputation
    - MVI
    - Imputation
    - imputation
  citations:
    - file: data-preparation-for-classification-databricks-on-aws.md
    - file: data-preparation-for-classification-databricks-on-aws.md
      start: 17
      end: 20
    - file: data-preparation-for-classification-databricks-on-aws.md
      start: 20
      end: 21
    - file: data-preparation-for-classification-databricks-on-aws.md
      start: 23
      end: 25
title: Missing Value Imputation
description: Configurable strategies for imputing null values in AutoML, including default auto-detection and user-specified methods via UI or API.
tags:
  - imputation
  - missing-values
  - automl
  - databricks
timestamp: "2026-06-19T14:41:27.004Z"
---

---
title: Missing Value Imputation
summary: Configurable handling of null values in AutoML, with default auto-selection based on column type and content, or user-specified methods via UI dropdown or API `imputers` parameter.
sources:
  - data-preparation-for-classification-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T14:59:57.141Z"
updatedAt: "2026-06-18T14:59:57.141Z"
tags:
  - automl
  - data-preparation
  - missing-data
aliases:
  - missing-value-imputation
  - MVI
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Missing Value Imputation

**Missing Value Imputation** in the context of AutoML on Databricks refers to the process of filling null values in a dataset before training a classification (or regression) model. AutoML provides configurable imputation methods that can be set either through the UI or via the API. ^[data-preparation-for-classification-databricks-on-aws.md]

## Supported Configuration

Beginning with Databricks Runtime 10.4 LTS ML, users can specify how null values are imputed. In the AutoML experiment UI, this is controlled by selecting a method from the **Impute with** drop-down in the table schema. In the AutoML Python API, the `imputers` parameter is used to configure imputation. For more details, see the [AutoML Python API reference](/concepts/automl-python-api.md). ^[data-preparation-for-classification-databricks-on-aws.md:17-20]

## Default Behavior

By default, AutoML automatically selects an imputation method based on the column’s data type and content. The selection is designed to be suitable for typical classification and regression workflows without requiring manual intervention. ^[data-preparation-for-classification-databricks-on-aws.md:20-21]

## Interaction with Semantic Type Detection

A key interaction is that if a non-default imputation method is specified, AutoML **does not perform semantic type detection** on the affected columns. Semantic type detection is the process by which AutoML identifies columns that should be treated as a different type (e.g., treating a string column as a timestamp or numeric). Custom imputation overrides this automatic detection. ^[data-preparation-for-classification-databricks-on-aws.md:23-25]

## Related Concepts

- [Semantic Type Detection](/concepts/semantic-type-detection.md) – AutoML’s ability to reinterpret column types based on content.
- [Data preparation for classification](/concepts/automl-data-preparation-for-classification.md) – Broader context for this imputation feature.
- Data preparation for regression – Similar settings for regression problems.
- [AutoML experiment setup](/concepts/automl-classification-experiment-setup.md) – How to configure imputation and other data settings.
- [Feature types supported by AutoML](/concepts/supported-feature-types-in-automl.md) – The column types that can be imputed.
- Imputation methods (UI/API) – The specific methods available in the drop-down or `imputers` parameter.

## Sources

- data-preparation-for-classification-databricks-on-aws.md

# Citations

1. [data-preparation-for-classification-databricks-on-aws.md](/references/data-preparation-for-classification-databricks-on-aws-23ffa2ac.md)
2. [data-preparation-for-classification-databricks-on-aws.md:17-20](/references/data-preparation-for-classification-databricks-on-aws-23ffa2ac.md)
3. [data-preparation-for-classification-databricks-on-aws.md:20-21](/references/data-preparation-for-classification-databricks-on-aws-23ffa2ac.md)
4. [data-preparation-for-classification-databricks-on-aws.md:23-25](/references/data-preparation-for-classification-databricks-on-aws-23ffa2ac.md)
