---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: db74611e3a41f2f23bdc94f126936ab35badcdd2d9313240e520c72f0560d9bc
  pageDirectory: concepts
  sources:
    - building-mlflow-evaluation-datasets-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-evaluation-dataset-limitations
    - MEDL
  citations:
    - file: building-mlflow-evaluation-datasets-databricks-on-aws.md
title: MLflow Evaluation Dataset Limitations
description: Constraints on evaluation datasets including a maximum of 2000 rows per dataset, 20 expectations per record, and incompatibility with customer-managed key (CMK) encrypted catalogs.
tags:
  - mlflow
  - evaluation
  - limitations
  - databricks
timestamp: "2026-06-19T17:42:02.593Z"
---

```markdown
---
title: MLflow Evaluation Dataset Limitations
summary: Technical constraints on evaluation datasets including a maximum of 2000 rows per dataset, maximum of 20 expectations per record, and prohibition on storage in customer-managed key (CMK) encrypted catalogs.
sources:
  - building-mlflow-evaluation-datasets-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T10:54:52.675Z"
updatedAt: "2026-06-19T09:11:17.211Z"
tags:
  - limitations
  - mlflow
  - evaluation
aliases:
  - mlflow-evaluation-dataset-limitations
  - MEDL
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# MLflow Evaluation Dataset Limitations

MLflow evaluation datasets are stored in [[Unity Catalog]] and provide built-in versioning, lineage, sharing, and governance. However, they come with several constraints that affect storage, size, and structure. This page documents those limitations so that you can plan your evaluation workflows accordingly. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Storage Restrictions

Evaluation datasets cannot be stored in catalogs encrypted with [[Customer-Managed Keys (CMK) for Online Feature Stores|customer-managed keys (CMK)]]. Workspaces that use CMK are supported only if the dataset is placed in a non-CMK catalog. This restriction applies regardless of whether the dataset is created through the UI or the [[MLflow|MLflow SDK]]. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Row Limit

Each evaluation dataset is capped at a maximum of **2,000 rows**. This limit applies to the total number of records in the dataset, whether they are added from traces, manually entered, or generated synthetically. If you need more than 2,000 rows per dataset, contact your Databricks representative to discuss relaxing the constraint. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Expectations Limit

Every record in an evaluation dataset can contain at most **20 expectations** (ground-truth answers or expected outputs). This limit is per record, not per dataset. Attempting to add more than 20 expectations to a single record will be rejected. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Additional Requirements

While not strict limitations, creating an evaluation dataset also requires:

- `CREATE TABLE` permission on a Unity Catalog schema.
- An existing [[MLflow Experiment]] to attach the dataset to.

These prerequisites are enforced at dataset creation time. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Requesting Limit Relaxation

If your use case requires exceeding any of the above limits (storage in CMK catalogs, more than 2,000 rows, or more than 20 expectations per record), you can contact your Databricks representative to request an exception. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Related Concepts

- [[MLflow Evaluation Datasets]] — Overview and creation workflows
- [[Unity Catalog]] — Governance layer that stores evaluation datasets
- [[Customer-Managed Keys (CMK) for Online Feature Stores|Customer-Managed Keys (CMK)]] — Encryption option incompatible with dataset storage
- [[MLflow Experiment]] — Required parent container for datasets
- [[MLflow Tracing]] — Source of trace data used to build datasets

## Sources

- building-mlflow-evaluation-datasets-databricks-on-aws.md
```

# Citations

1. [building-mlflow-evaluation-datasets-databricks-on-aws.md](/references/building-mlflow-evaluation-datasets-databricks-on-aws-a5b14a92.md)
