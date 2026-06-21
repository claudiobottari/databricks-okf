---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6de2e79d63f3d66cb587e7fe2efcc29968e32e5d9ded9e5c1623901d5c1f2a1f
  pageDirectory: concepts
  sources:
    - scorer-lifecycle-management-api-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - scorer-registration-and-registry
    - Registry and Scorer Registration
    - SRAR
    - Scorer Registration
  citations:
    - file: scorer-lifecycle-management-api-reference-databricks-on-aws.md
title: Scorer Registration and Registry
description: API functions to register, retrieve, list, and delete scorers via get_scorer(), list_scorers(), delete_scorer(), and Scorer.register()
tags:
  - mlflow
  - registry
  - scorers
timestamp: "2026-06-19T20:19:06.870Z"
---

# Scorer Registration and Registry

The **Scorer Registration and Registry** system in MLflow provides the infrastructure for registering, managing, and discovering [[Scorers|scorer]] functions used for continuous quality assessment on production traces. Scorers must be registered with a [MLflow Experiment](/concepts/mlflow-experiment.md) before they can be used for online evaluation or backfill operations. ^[scorer-lifecycle-management-api-reference-databricks-on-aws.md]

## Scorer Registration

### `Scorer.register()`

Scorers created with the `@scorer` decorator must be registered with the server before they can be started. The `register()` method registers a custom scorer function and assigns it a unique name within the experiment. ^[scorer-lifecycle-management-api-reference-databricks-on-aws.md]

```python
from mlflow.genai.scorers import scorer

@scorer
def custom_scorer(outputs):
    return len(str(outputs.get("response", "")))

# Register the custom scorer
my_scorer = custom_scorer.register(name="response_length")
```

**Parameters:**
- `name` (str): Unique name for the scorer within the experiment. Defaults to the existing name of the scorer.

**Returns:** A new [[Scorers|Scorer]] instance with server registration. ^[scorer-lifecycle-management-api-reference-databricks-on-aws.md]

## Scorer Registry Functions

The scorer registry provides functions for discovering and managing registered scorers across an experiment. ^[scorer-lifecycle-management-api-reference-databricks-on-aws.md]

### `mlflow.genai.scorers.get_scorer()`

Retrieve a registered scorer by name. This function allows you to access an existing scorer's configuration and state. ^[scorer-lifecycle-management-api-reference-databricks-on-aws.md]

```python
from mlflow.genai.scorers import get_scorer

# Get existing scorer by name
existing_scorer = get_scorer(name="safety_monitor")
print(f"Current sample rate: {existing_scorer.sample_rate}")
```

**Parameters:**
- `name` (str): Name of the registered scorer

**Returns:** [[Scorers|Scorer]] instance. ^[scorer-lifecycle-management-api-reference-databricks-on-aws.md]

### `mlflow.genai.scorers.list_scorers()`

List all registered scorers for the current experiment. This provides an overview of all available scorers and their current configurations. ^[scorer-lifecycle-management-api-reference-databricks-on-aws.md]

```python
from mlflow.genai.scorers import list_scorers

# List all registered scorers
all_scorers = list_scorers()
for scorer in all_scorers:
    print(f"Name: {scorer._server_name}")
    print(f"Sample rate: {scorer.sample_rate}")
    print(f"Filter: {scorer.filter_string}")
```

**Returns:** List of [[Scorers|Scorer]] instances. ^[scorer-lifecycle-management-api-reference-databricks-on-aws.md]

### `mlflow.genai.scorers.delete_scorer()`

Delete a registered scorer by name. This permanently removes the scorer from the registry. ^[scorer-lifecycle-management-api-reference-databricks-on-aws.md]

```python
from mlflow.genai.scorers import delete_scorer

# Delete existing scorer by name
delete_scorer(name="safety_monitor")
```

**Parameters:**
- `name` (str): Name of the registered scorer

**Returns:** None. ^[scorer-lifecycle-management-api-reference-databricks-on-aws.md]

## Scorer Properties

Registered scorers expose two key properties for inspection: ^[scorer-lifecycle-management-api-reference-databricks-on-aws.md]

### `Scorer.sample_rate`

Current sampling rate (0.0–1.0). Returns 0 for stopped scorers. ^[scorer-lifecycle-management-api-reference-databricks-on-aws.md]

```python
print(f"Sampling {scorer.sample_rate * 100}% of traces")
```

### `Scorer.filter_string`

Current trace filter string for MLflow trace selection. ^[scorer-lifecycle-management-api-reference-databricks-on-aws.md]

```python
print(f"Filter: {scorer.filter_string}")
```

## Scorer Lifecycle

The registry is part of a broader scorer lifecycle that includes:

- **Registration** — Registering a scorer with `Scorer.register()` makes it available in the experiment. ^[scorer-lifecycle-management-api-reference-databricks-on-aws.md]
- **Starting** — `Scorer.start()` begins online evaluation with the specified sampling configuration. ^[scorer-lifecycle-management-api-reference-databricks-on-aws.md]
- **Updating** — `Scorer.update()` modifies the sampling configuration of an active scorer (an immutable operation that returns a new instance). ^[scorer-lifecycle-management-api-reference-databricks-on-aws.md]
- **Stopping** — `Scorer.stop()` halts online evaluation by setting sample rate to 0, but keeps the scorer registered. ^[scorer-lifecycle-management-api-reference-databricks-on-aws.md]
- **Deletion** — `delete_scorer()` permanently removes the scorer from the registry. ^[scorer-lifecycle-management-api-reference-databricks-on-aws.md]

## Related Concepts

- [Scorer Lifecycle Management](/concepts/scorer-lifecycle-management.md) — Complete lifecycle of scorer creation, registration, and monitoring
- [MLflow Experiments](/concepts/mlflow-experiment.md) — Organizational unit for scorers and traces
- [Production Monitoring](/concepts/production-monitoring.md) — Continuous quality assessment of GenAI applications
- [Metric Backfill](/concepts/metric-backfill.md) — Backfilling evaluation metrics for historical traces
- [ScorerSamplingConfig](/concepts/scorersamplingconfig.md) — Configuration for trace sampling during evaluation

## Sources

- scorer-lifecycle-management-api-reference-databricks-on-aws.md

# Citations

1. [scorer-lifecycle-management-api-reference-databricks-on-aws.md](/references/scorer-lifecycle-management-api-reference-databricks-on-aws-55d28735.md)
