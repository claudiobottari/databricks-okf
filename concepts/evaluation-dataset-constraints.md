---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b9f5a2c19b1a2c7d539374fd12ff18a71234165f873ffa9fd4b27cb304a8a657
  pageDirectory: concepts
  sources:
    - building-mlflow-evaluation-datasets-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - evaluation-dataset-constraints
    - EDC
  citations:
    - file: building-mlflow-evaluation-datasets-databricks-on-aws.md
title: Evaluation Dataset Constraints
description: Technical limitations for MLflow evaluation datasets including a maximum of 2000 rows per dataset, 20 expectations per record, and incompatibility with CMK-encrypted Unity Catalog catalogs.
tags:
  - limitations
  - mlflow
  - constraints
timestamp: "2026-06-18T14:34:18.669Z"
---

# Evaluation Dataset Constraints

**Evaluation Dataset Constraints** refer to the limitations and requirements placed on [MLflow Evaluation Datasets](/concepts/mlflow-evaluation-datasets.md) used for GenAI application testing. These constraints govern storage, size, and structure, and are enforced by the Unity Catalog and MLflow framework to ensure governance and performance.

## Storage Constraints

Evaluation datasets must be stored in Unity Catalog within a schema where the creator has `CREATE TABLE` permissions. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

A critical storage constraint is that evaluation datasets **cannot be stored in catalogs encrypted with customer-managed keys (CMK)**. Workspaces that use CMK are supported only if the dataset is placed in a non-CMK catalog. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Size Constraints

Each evaluation dataset is subject to the following maximum limits:

- **Maximum of 2000 rows** per evaluation dataset. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]
- **Maximum of 20 expectations** per dataset record. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

If a use case requires larger limits, users can contact their Databricks representative to request relaxation of these constraints. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Related Concepts

- [MLflow Evaluation Datasets](/concepts/mlflow-evaluation-datasets.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- Customer-managed keys (CMK)
- [GenAI evaluation](/concepts/mlflow-genai-evaluation.md)

## Sources

- building-mlflow-evaluation-datasets-databricks-on-aws.md

# Citations

1. [building-mlflow-evaluation-datasets-databricks-on-aws.md](/references/building-mlflow-evaluation-datasets-databricks-on-aws-a5b14a92.md)
