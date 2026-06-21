---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e530fb46c5bb20d926b790842dda27c5bd04563e6e2c5162ca314ac1edca948b
  pageDirectory: concepts
  sources:
    - evaluation-dataset-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - dataset-lineage-tracking
    - DLT
  citations:
    - file: evaluation-dataset-reference-databricks-on-aws.md
title: Dataset Lineage Tracking
description: The mechanism for tracking provenance of evaluation dataset records using source fields that identify whether a record came from a human, a document, or a production trace.
tags:
  - mlflow
  - evaluation
  - lineage
  - provenance
timestamp: "2026-06-18T12:13:12.768Z"
---

# Dataset Lineage Tracking

**Dataset Lineage Tracking** refers to the practice of recording the origin, transformation history, and provenance of evaluation datasets used in [GenAI](/concepts/mlflow-genai-evaluate-api.md) application development and evaluation. In [MLflow GenAI](/concepts/mlflow-3-for-genai.md), lineage is tracked through structured fields in the evaluation dataset schema, enabling teams to understand where data comes from, how it was created, and how it relates to production traces and evaluation results. ^[evaluation-dataset-reference-databricks-on-aws.md]

## Overview

Lineage tracking for evaluation datasets provides visibility into the lifecycle of test data used to assess GenAI agent quality. Each record in an evaluation dataset can carry metadata about its origin, allowing developers to trace back from evaluation results to the source of test inputs. This traceability is essential for debugging quality issues, auditing evaluation processes, and ensuring reproducibility of experiments. ^[evaluation-dataset-reference-databricks-on-aws.md]

## Source Field Types

The `source` field in an evaluation dataset record captures where the record originated. Each record can have **only one** source type. ^[evaluation-dataset-reference-databricks-on-aws.md]

### Human Source

Records created manually by a person are tracked with the user's identity:

```python
{
    "source": {
        "human": {
            "user_name": "jane.doe@company.com"  # user who created the record
        }
    }
}
```

^[evaluation-dataset-reference-databricks-on-aws.md]

### Document Source

Records synthesized from documents include a URI pointing to the source document and optional content excerpt:

```python
{
    "source": {
        "document": {
            "doc_uri": "s3://bucket/docs/product-manual.pdf",  # URI or path to the source document
            "content": "The first 500 chars of the document..."  # Optional, excerpt or full content
        }
    }
}
```

^[evaluation-dataset-reference-databricks-on-aws.md]

### Trace Source

Records created from production traces reference the original trace identifier:

```python
{
    "source": {
        "trace": {
            "trace_id": "tr-abc123def456"  # unique identifier of the source trace
        }
    }
}
```

^[evaluation-dataset-reference-databricks-on-aws.md]

## Viewing Source Traces in the UI

In the **Datasets** tab of the MLflow experiment page, the **Source** column displays the origin type for each record. For trace-sourced records, clicking the trace identifier opens an interactive window showing the full source trace and its associated assessments. This allows developers to inspect the exact production context from which a test case was derived. ^[evaluation-dataset-reference-databricks-on-aws.md]

## Dataset Metadata and Version History

Beyond individual record lineage, the evaluation dataset abstraction stores metadata including creation time, last update time, source information, and a link to view the dataset in [Unity Catalog](/concepts/unity-catalog.md). This metadata is accessible through the dataset details pane in the UI and through the SDK. ^[evaluation-dataset-reference-databricks-on-aws.md]

## Tags for Lineage

Tags can be added to individual dataset records to supplement the structured source fields with custom lineage metadata. Tags are editable directly in the UI and can encode workflow-specific information such as environment, data version, or quality checks applied. ^[evaluation-dataset-reference-databricks-on-aws.md]

## Relationship Between Lineage and Evaluation

Lineage tracking connects evaluation datasets to their evaluation results. When running `mlflow.genai.evaluate()` with a dataset, each evaluation output is linked back to the source record. This enables:

- Tracing a failed evaluation back to the specific production trace or document that generated the test case
- Understanding whether evaluation datasets are representative of actual production traffic
- Auditing which data sources contributed to a given experiment's results

## Best Practices

- **Always populate the source field** when creating datasets programmatically, especially when extracting records from production traces.
- **Use consistent tag taxonomies** across experiments to enable cross-experiment lineage queries.
- **Document the document corpus** referenced in document-sourced records to maintain an auditable chain from raw documents to test cases.
- **Audit production traces** before using them as dataset sources to ensure compliance with data governance policies.

## Related Concepts

- Evaluation Dataset Reference — The full schema for evaluation dataset records
- [MLflow Experiments](/concepts/mlflow-experiment.md) — The organizational container for runs and evaluation datasets
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — The source of trace-based dataset records
- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) — The evaluation framework that consumes lineage-enriched datasets
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer that stores dataset tables with lineage metadata

## Sources

- evaluation-dataset-reference-databricks-on-aws.md

# Citations

1. [evaluation-dataset-reference-databricks-on-aws.md](/references/evaluation-dataset-reference-databricks-on-aws-b8093309.md)
