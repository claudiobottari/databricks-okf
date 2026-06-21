---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4a652fe11e68d362b135036e1690875eb949c5f0fb081d0df6420cf031c39eba
  pageDirectory: concepts
  sources:
    - building-mlflow-evaluation-datasets-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - evaluation-dataset-limitations
    - EDL
    - evaluation-dataset-constraints
    - EDC
    - mlflow-evaluation-dataset-limitations
    - MEDL
  citations:
    - file: building-mlflow-evaluation-datasets-databricks-on-aws.md
title: Evaluation Dataset Limitations
description: Known constraints on MLflow evaluation datasets including a maximum of 2000 rows per dataset, 20 expectations per record, and incompatibility with CMK-encrypted catalogs.
tags:
  - limitations
  - evaluation
  - databricks
timestamp: "2026-06-19T14:10:40.324Z"
---

# Evaluation Dataset Limitations

**Evaluation Dataset Limitations** refers to the constraints that apply when creating or using [MLflow Evaluation Datasets](/concepts/evaluation-datasets.md) for GenAI applications. These limitations are enforced to ensure storage compatibility, performance, and manageability within the [Unity Catalog](/concepts/unity-catalog.md) governance framework.

## Storage Constraints

Evaluation datasets cannot be stored in catalogs that are encrypted with customer-managed keys (CMK). Workspaces that use CMK encryption are still supported, provided the evaluation dataset is placed in a non‑CMK catalog. This restriction exists because MLflow evaluation datasets rely on Unity Catalog tables that require a specific storage configuration.^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Size Limits

- **Maximum rows per dataset:** 2,000 records. This limit helps maintain query performance and manageable dataset sizes during iterative evaluation cycles.^[building-mlflow-evaluation-datasets-databricks-on-aws.md]
- **Maximum expectations per record:** 20 expectations. Expectations are optional ground‑truth or quality indicators that judges can reference, and the cap prevents overly complex single records.^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Requesting Relaxation

If your use case requires exceeding these limits (for example, storing more than 2,000 rows or using more than 20 expectations per record), contact your Databricks representative to discuss custom allowances.^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Related Concepts

- [GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) — The broader practice of using evaluation datasets to measure application quality.
- [Evaluation Dataset](/concepts/evaluation-dataset.md) — The concept of curated example inputs for systematic testing.
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer that stores and version‑controls evaluation datasets.
- [Customer-Managed Keys (CMK)](/concepts/customer-managed-keys-for-online-feature-stores.md) — The encryption mechanism that conflicts with evaluation dataset storage.

## Sources

- building-mlflow-evaluation-datasets-databricks-on-aws.md

# Citations

1. [building-mlflow-evaluation-datasets-databricks-on-aws.md](/references/building-mlflow-evaluation-datasets-databricks-on-aws-a5b14a92.md)
