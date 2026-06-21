---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f460fcf66751645a5738f062fb7b4a91f412e123ea6dfa7fb2c67fdc34157301
  pageDirectory: concepts
  sources:
    - evaluation-dataset-reference-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - dataset-record-tagging
    - DRT
  citations:
    - file: evaluation-dataset-reference-databricks-on-aws.md
title: Dataset Record Tagging
description: The ability to add and edit metadata tags on individual evaluation dataset records through the MLflow UI for organization and filtering.
tags:
  - mlflow
  - metadata
  - tagging
  - organization
timestamp: "2026-06-18T12:13:32.729Z"
---

---
title: Dataset Record Tagging
summary: The practice of adding metadata tags to individual records in an MLflow evaluation dataset to categorize, organize, or annotate evaluation data for GenAI applications.
sources:
  - evaluation-dataset-reference-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T12:00:00.000Z"
updatedAt: "2026-06-18T12:00:00.000Z"
tags:
  - mlflow
  - genai
  - evaluation
  - datasets
aliases:
  - dataset-record-tagging
  - DRT
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 1
---

# Dataset Record Tagging

**Dataset Record Tagging** is a feature in MLflow evaluation datasets that allows you to attach metadata tags to individual records within a dataset. Tags are key-value pairs that help categorize, organize, or annotate evaluation data, making it easier to filter and manage records during [GenAI application development](/concepts/genai-application-evaluation-lifecycle.md) and testing. ^[evaluation-dataset-reference-databricks-on-aws.md]

## Overview

Each record in an MLflow [Evaluation Dataset](/concepts/evaluation-dataset.md) supports lineage fields, including `source` and `tags`. Tags are part of the record's metadata and can be used for custom classification, such as marking records by scenario, priority, or data origin. The MLflow UI provides direct controls for adding, editing, and deleting tags on a per-record basis. ^[evaluation-dataset-reference-databricks-on-aws.md]

## Adding and Managing Tags in the UI

The **Datasets** tab of an MLflow experiment page displays the records of a selected dataset in a table. The **Tags** column shows the existing tags for each record. ^[evaluation-dataset-reference-databricks-on-aws.md]

### Add a Tag

To add a tag to a record:

1. In the **Tags** column, click **Add tags**.
2. Enter the tag key and value in the prompt that appears.

After saving, the tag appears in the **Tags** column for that record. ^[evaluation-dataset-reference-databricks-on-aws.md]

### Edit a Tag

To edit an existing tag:

Click on the tag in the **Tags** column and modify the key or value as needed. ^[evaluation-dataset-reference-databricks-on-aws.md]

### Delete a Tag

Tags can be removed by editing the record and clearing the tag, or by using the delete functionality in the tag editor. ^[evaluation-dataset-reference-databricks-on-aws.md]

### Saving Changes

After making any tag modifications (or editing other record fields), click **Save changes** at the upper right of the table to persist the updates to the dataset. ^[evaluation-dataset-reference-databricks-on-aws.md]

## Tagging via SDK

While the source documentation focuses on UI-based management, tags can also be included when programmatically creating or updating dataset records using the [Evaluation Dataset SDK](/concepts/evaluation-dataset-sdk.md). Tags are part of the record's lineage schema and can be set alongside other fields such as `inputs`, `expectations`, and `source`. ^[evaluation-dataset-reference-databricks-on-aws.md]

## Best Practices

- **Use consistent tag keys** across records to enable filtering and grouping during evaluation analysis.
- **Avoid sensitive data** in tag values, as tags are visible to anyone who can read the dataset.
- **Combine tags with source fields** to provide complete lineage information for each record.

## Related Concepts

- [Evaluation Dataset](/concepts/evaluation-dataset.md) — The structured test data containing tagged records
- [MLflow experiments](/concepts/mlflow-experiment.md) — The organizational unit that hosts datasets and their records
- [MLflow GenAI](/concepts/mlflow-3-for-genai.md) — The framework for developing and evaluating generative AI applications
- [Data Lineage](/concepts/data-lineage.md) — Tracking the origin and transformation of evaluation records

## Sources

- evaluation-dataset-reference-databricks-on-aws.md

# Citations

1. [evaluation-dataset-reference-databricks-on-aws.md](/references/evaluation-dataset-reference-databricks-on-aws-b8093309.md)
