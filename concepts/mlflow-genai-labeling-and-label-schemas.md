---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 618277c99a4c539d50137e726e68b99d33020cdfda7ead19e03fa9cc17d7afbe
  pageDirectory: concepts
  sources:
    - migrate-to-mlflow-3-from-agent-evaluation-quick-reference-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-genai-labeling-and-label-schemas
    - Label Schemas and MLflow GenAI Labeling
    - MGLALS
  citations:
    - file: migrate-to-mlflow-3-from-agent-evaluation-quick-reference-databricks-on-aws.md
title: MLflow GenAI Labeling and Label Schemas
description: New mlflow.genai.labeling and mlflow.genai.label_schemas modules for defining and managing evaluation label schemas.
tags:
  - mlflow
  - labeling
  - data-labeling
  - schemas
timestamp: "2026-06-19T19:35:47.498Z"
---

# MLflow GenAI Labeling and Label Schemas

**MLflow GenAI Labeling and Label Schemas** provide a structured framework for defining, managing, and validating labels used in [Generative AI](/concepts/mlflow-tracing-for-generative-ai.md) evaluation workflows within the MLflow ecosystem. These components enable consistent and reproducible labeling practices across [MLflow experiments](/concepts/mlflow-experiment.md) and model evaluation pipelines.

## Overview

MLflow GenAI introduces dedicated modules for managing labels and label schemas through the `mlflow.genai.labeling` and `mlflow.genai.label_schemas` namespaces. These modules are designed to support [agent evaluation](/concepts/mlflow-agent-evaluation.md) and other generative AI scoring tasks where consistent label definitions are critical for model assessment. ^[migrate-to-mlflow-3-from-agent-evaluation-quick-reference-databricks-on-aws.md]

### Labeling Module

The `mlflow.genai.labeling` module (`import mlflow.genai.labeling as labeling`) provides tools for creating, managing, and applying labels to evaluation data. Labels serve as ground truth or reference annotations that scoring functions use to assess model performance. The module supports:

- Programmatic label definition
- Label validation
- Integration with [[Scorers|scorer]] implementations

### Label Schemas Module

The `mlflow.genai.label_schemas` module (`import mlflow.genai.label_schemas as schemas`) defines structured schemas for label containers, ensuring that label metadata follows consistent formats and data types. Schema validation helps maintain data quality across evaluation runs.

## Usage Patterns

### Migration from Earlier APIs

When migrating from earlier evaluation APIs to MLflow GenAI, the labeling and schema modules replace or supplement previous approaches:

- **Old pattern:** Used `from mlflow import evaluate` with `databricks.agents.evals` modules
- **New pattern:** Uses `from mlflow.genai import evaluate` with dedicated `scorer`, `judges`, and `labeling` modules

For predefined scoring components, import from `mlflow.genai.scorers`:

```python
from mlflow.genai.scorers import (
    Correctness, 
    Guidelines, 
    ExpectationsGuidelines, 
    RelevanceToQuery, 
    Safety, 
    RetrievalGroundedness, 
    RetrievalRelevance, 
    RetrievalSufficiency
)
```

## Integration with Scorers

Labels and label schemas work with predefined scorers to provide:

- **Structured annotations** for evaluation datasets
- **Schema enforcement** to ensure label consistency
- **Validation rules** for label format and content

The typical workflow involves:
1. Define label schemas using `mlflow.genai.label_schemas`
2. Apply labels using `mlflow.genai.labeling`
3. Pass labeled data to scorers for quality assessment

## Related Concepts

- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) - The evaluation framework that uses labeling and schemas
- [[Scorers|Scorer]] - Scoring components that consume labeled data
- [Judges](/concepts/llm-judges.md) - Evaluation judges that reference labels
- [Agent Evaluation](/concepts/mlflow-agent-evaluation.md) - Evaluation type that benefits from structured labeling
- Model Performance - Metric influenced by label quality
- Data Quality - Data quality maintained through schema validation
- Reproducibility - Consistent labeling supports reproducible evaluations

## Sources

- migrate-to-mlflow-3-from-agent-evaluation-quick-reference-databricks-on-aws.md

# Citations

1. [migrate-to-mlflow-3-from-agent-evaluation-quick-reference-databricks-on-aws.md](/references/migrate-to-mlflow-3-from-agent-evaluation-quick-reference-databricks-on-aws-4733fb1b.md)
