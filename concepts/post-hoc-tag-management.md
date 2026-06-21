---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4456eb7192f2aa4e724be4c1e65552af4286785b8f8f38e72abf937395a2d8a7
  pageDirectory: concepts
  sources:
    - attach-custom-tags-and-metadata-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - post-hoc-tag-management
    - PTM
  citations:
    - file: attach-custom-tags-and-metadata-databricks-on-aws.md
title: Post-hoc Tag Management
description: Setting, updating, and deleting tags on already-completed and logged traces using mlflow.set_trace_tag and mlflow.delete_trace_tag.
tags:
  - mlflow
  - tracing
  - api
timestamp: "2026-06-19T14:04:04.241Z"
---

# Post-hoc Tag Management

**Post-hoc Tag Management** refers to the practice of adding, updating, or deleting tags on [[MLflow Trace|MLflow Traces]] after the trace has been completed and logged to the backend store. This enables dynamic annotation of traces for organization, search, and filtering based on information that may change after execution, such as review status or data quality assessments. ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

## Key Concepts: Tags vs. Metadata

MLflow distinguishes two types of key-value pairs that can be attached to traces:

- **Tags** are mutable. They can be added, updated, or deleted after a trace is logged. Use tags for dynamic information that may change over time, such as user feedback, review status, or data quality assessments. ^[attach-custom-tags-and-metadata-databricks-on-aws.md]
- **Metadata** is write-once and immutable after logging. Once a metadata key is set, any attempt to update it with the same key is silently ignored. Use metadata for fixed information captured during execution, such as model version, environment, or system configuration. ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

Post-hoc operations apply only to tags, because metadata cannot be modified after a trace is created. ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

## Methods for Post-hoc Tagging

### Using the SDK (after trace completion)

The `mlflow.set_trace_tag()` function sets a tag on a trace that has already been completed and logged. The `mlflow.delete_trace_tag()` function removes a tag from such a trace. Both functions require the `trace_id` of the target trace. ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

```python
import mlflow

# Create and execute a traced function
@mlflow.trace
def process_data(data):
    return data.upper()

result = process_data("hello world")

# Get the trace_id from the most recent trace
trace_id = mlflow.get_last_active_trace_id()

# Set a tag on the trace after completion
mlflow.set_trace_tag(trace_id=trace_id, key="review_status", value="approved")

# Delete a tag
mlflow.delete_trace_tag(trace_id=trace_id, key="data_quality")
```

^[attach-custom-tags-and-metadata-databricks-on-aws.md]

### Via the MLflow UI

To update or delete tags on a trace through the UI:

1. Navigate to the **Traces** tab.
2. Click the pencil icon next to the tag you want to update, or use the delete option.

^[attach-custom-tags-and-metadata-databricks-on-aws.md]

## Contrast: Tagging During Execution

If you want to add tags *during* trace execution (e.g., inside a traced function), use `mlflow.update_current_trace(tags={...})`. This method adds the specified tag(s) to the current trace; if the key already exists, it updates the value. After the trace is complete, only post-hoc methods (`set_trace_tag` / `delete_trace_tag`) can modify tags. ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

## Use Cases

Post-hoc tag management supports workflows such as:

- Marking traces as "approved" or "requires review" after a human evaluation.
- Adding data quality scores that become available after the trace is logged.
- Annotating traces with production feedback from monitoring pipelines.
- Cleaning up obsolete tags that are no longer relevant.

## Prerequisites

To use these APIs, ensure you have MLflow 3.1.0 or later with the Databricks extras installed: ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

```bash
pip install --upgrade "mlflow[databricks]>=3.1.0" openai "databricks-connect>=16.1"
```

You also need an MLflow experiment set up. ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

## Related Concepts

- [[MLflow Trace|MLflow Traces]] – The core observation unit for GenAI agent calls.
- Tagging and Filtering – Using tags to organize and search traces.
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) – Applying post-hoc tags as part of a monitoring pipeline.
- [Metadata vs Tags](/concepts/trace-tags-and-metadata.md) – Understanding the immutability distinction.
- Automated Trace Annotation – Potential automation of post-hoc tagging with scoring judges.

## Sources

- attach-custom-tags-and-metadata-databricks-on-aws.md

# Citations

1. [attach-custom-tags-and-metadata-databricks-on-aws.md](/references/attach-custom-tags-and-metadata-databricks-on-aws-e81e9298.md)
