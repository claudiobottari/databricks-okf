---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b6a0275ccac47ec7c2d37843beb2ee2856fff511bd274588c6a17f73ffd490ad
  pageDirectory: concepts
  sources:
    - migrate-to-mlflow-3-from-agent-evaluation-quick-reference-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-genai-predefined-scorers
    - MGPS
    - MLflow Predefined Scorers
    - MLflow predefined scorers
    - MLflow predefined scorers documentation
    - Predefined Scorers
    - Predefined scorers
    - predefined scorers documentation
  citations:
    - file: migrate-to-mlflow-3-from-agent-evaluation-quick-reference-databricks-on-aws.md
title: MLflow GenAI Predefined Scorers
description: A set of built-in evaluation scorers in MLflow 3 including Correctness, Guidelines, ExpectationsGuidelines, RelevanceToQuery, Safety, RetrievalGroundedness, RetrievalRelevance, and RetrievalSufficiency.
tags:
  - mlflow
  - evaluation
  - scorers
  - generative-ai
timestamp: "2026-06-19T19:35:39.330Z"
---

# MLflow GenAI Predefined Scorers

**MLflow GenAI Predefined Scorers** are ready-to-use evaluation metrics provided by the `mlflow.genai.scorers` module for assessing generative AI applications. They replace the older `databricks.agents.evals` and `databricks.agents` evaluation APIs as part of the migration to MLflow 3. ^[migrate-to-mlflow-3-from-agent-evaluation-quick-reference-databricks-on-aws.md]

## Available Predefined Scorers

The following predefined scorers are available in the `mlflow.genai.scorers` module: ^[migrate-to-mlflow-3-from-agent-evaluation-quick-reference-databricks-on-aws.md]

- `Correctness`
- `Guidelines`
- `ExpectationsGuidelines`
- `RelevanceToQuery`
- `Safety`
- `RetrievalGroundedness`
- `RetrievalRelevance`
- `RetrievalSufficiency`

Each scorer corresponds to a specific evaluation dimension, such as factual correctness, adherence to guidelines, safety, or retrieval quality. The exact behavior and scoring logic for each scorer is defined within the MLflow GenAI library.

## Usage

To use a predefined scorer, import it directly from `mlflow.genai.scorers`: ^[migrate-to-mlflow-3-from-agent-evaluation-quick-reference-databricks-on-aws.md]

```python
from mlflow.genai.scorers import (
    Correctness,
    Guidelines,
    ExpectationsGuidelines,
    RelevanceToQuery,
    Safety,
    RetrievalGroundedness,
    RetrievalRelevance,
    RetrievalSufficiency,
)
```

Custom scorers can be defined using the generic `scorer` import from the same module. ^[migrate-to-mlflow-3-from-agent-evaluation-quick-reference-databricks-on-aws.md]

## Migration Context

These predefined scorers are part of the broader migration from the previous `databricks.agents.evals` and `databricks.agents` libraries to MLflow 3’s `mlflow.genai` module, which also includes new imports for judges, labeling, and evaluation functions. ^[migrate-to-mlflow-3-from-agent-evaluation-quick-reference-databricks-on-aws.md]

## Related Concepts

- [MLflow GenAI](/concepts/mlflow-3-for-genai.md) — The overarching module for generative AI evaluation.
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) — The general framework for running evaluations.
- Generative AI (GenAI) — The application domain these scorers target.
- [LLM Evaluation](/concepts/llm-as-a-judge-evaluation.md) — The broader practice these scorers support.
- [Custom Scorer (MLflow GenAI)](/concepts/custom-scorers-mlflow-genai.md) — How to define your own scorer using the `scorer` function.
- Agent Evaluation Migration — The migration guide from which this information is drawn.

## Sources

- migrate-to-mlflow-3-from-agent-evaluation-quick-reference-databricks-on-aws.md

# Citations

1. [migrate-to-mlflow-3-from-agent-evaluation-quick-reference-databricks-on-aws.md](/references/migrate-to-mlflow-3-from-agent-evaluation-quick-reference-databricks-on-aws-4733fb1b.md)
