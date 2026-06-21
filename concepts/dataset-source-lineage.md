---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 61fb42e1586db21c7ff1660f9a1703de597091cadcbe1d913e00127671382f9b
  pageDirectory: concepts
  sources:
    - evaluation-dataset-reference-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - dataset-source-lineage
    - DSL
    - evaluation-dataset-source-lineage
    - EDSL
  citations:
    - file: evaluation-dataset-reference-databricks-on-aws.md
title: Dataset Source Lineage
description: The source field in evaluation datasets for tracking record provenance via human, document, or trace origin types.
tags:
  - mlflow
  - lineage
  - provenance
  - data-governance
timestamp: "2026-06-19T18:42:53.079Z"
---

# Dataset Source Lineage

**Dataset Source Lineage** refers to the provenance information captured for each record in an [Evaluation Dataset](/concepts/evaluation-dataset.md) on Databricks. The lineage is recorded in a `source` field that documents where a dataset record originated. This field is part of the evaluation dataset schema and is used to track version history and traceability for GenAI app evaluation. ^[evaluation-dataset-reference-databricks-on-aws.md]

## Source Field

Each record in an evaluation dataset has a `source` field that can contain **exactly one** of three source types: `human`, `document`, or `trace`. These types describe the origin of the record and are mutually exclusive for a given record. ^[evaluation-dataset-reference-databricks-on-aws.md]

### Human Source

A record created manually by a person. The source object includes the `user_name` of the creator.

```json
{
    "source": {
        "human": {
            "user_name": "jane.doe@company.com"
        }
    }
}
```

### Document Source

A record synthesized from a document. The source object includes a `doc_uri` (URI or path to the source document) and an optional `content` field that may contain an excerpt or the full document text (e.g., the first 500 characters).

```json
{
    "source": {
        "document": {
            "doc_uri": "s3://bucket/docs/product-manual.pdf",
            "content": "The first 500 chars of the document..."
        }
    }
}
```

### Trace Source

A record created from a production trace. The source object includes a `trace_id`, the unique identifier of the source trace.

```json
{
    "source": {
        "trace": {
            "trace_id": "tr-abc123def456"
        }
    }
}
```

## Viewing Source Lineage in the UI

In the [MLflow Experiments](/concepts/mlflow-experiment.md) UI, the **Datasets** tab provides a visual interface for managing evaluation datasets. For records created from production traces, the **Source** column shows the trace. Clicking the trace opens an interactive window displaying the full trace and its assessments, enabling users to inspect the origin of the record directly. ^[evaluation-dataset-reference-databricks-on-aws.md]

## Related Concepts

- [Evaluation Dataset](/concepts/evaluation-dataset.md) – The structured test data that contains source lineage fields.
- [MLflow Experiments](/concepts/mlflow-experiment.md) – The organizational unit for GenAI evaluation datasets.
- [Data Lineage](/concepts/data-lineage.md) – General concept of tracking data origin and transformations.
- [Trace](/concepts/traces.md) – Production trace that can serve as a source for dataset records.
- [Unity Catalog](/concepts/unity-catalog.md) – Where evaluation datasets are stored as tables.
- [GenAI App Evaluation](/concepts/genai-application-evaluation-lifecycle.md) – The broader workflow for evaluating generative AI applications.

## Sources

- evaluation-dataset-reference-databricks-on-aws.md

# Citations

1. [evaluation-dataset-reference-databricks-on-aws.md](/references/evaluation-dataset-reference-databricks-on-aws-b8093309.md)
