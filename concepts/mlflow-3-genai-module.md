---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 25cb876ccb1f307a284ad5c5890dab4878f341fa492b32e1e9052ddbebcf7638
  pageDirectory: concepts
  sources:
    - migrate-to-mlflow-3-from-agent-evaluation-quick-reference-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-3-genai-module
    - M3GM
  citations:
    - file: migrate-to-mlflow-3-from-agent-evaluation-quick-reference-databricks-on-aws.md
title: MLflow 3 GenAI Module
description: The new mlflow.genai package that unifies GenAI evaluation functionality, replacing the separate Databricks Agent Evaluation API.
tags:
  - mlflow
  - generative-ai
  - evaluation
  - migration
timestamp: "2026-06-19T19:35:08.832Z"
---

# MLflow 3 GenAI Module

The **MLflow 3 GenAI Module** (`mlflow.genai`) is the primary namespace in [MLflow 3](/concepts/mlflow-3.md) for evaluating generative AI models, agents, and retrieval-augmented generation (RAG) systems. It consolidates the evaluation, scoring, judging, labeling, and label-schema functionality that was previously spread across `mlflow.evaluate` and the `databricks.agents.evals` modules. ^[migrate-to-mlflow-3-from-agent-evaluation-quick-reference-databricks-on-aws.md]

## Key Components

### `mlflow.genai.evaluate`
The top-level evaluation entry point. It replaces `mlflow.evaluate` for GenAI workloads and is imported as:

```python
from mlflow.genai import evaluate
```

^[migrate-to-mlflow-3-from-agent-evaluation-quick-reference-databricks-on-aws.md]

### `mlflow.genai.scorers`
A submodule providing both a `scorer` utility and a set of **predefined scorers** for common GenAI quality dimensions. Import:

```python
from mlflow.genai.scorers import scorer
from mlflow.genai.scorers import (
    Correctness, Guidelines, ExpectationsGuidelines,
    RelevanceToQuery, Safety, RetrievalGroundedness,
    RetrievalRelevance, RetrievalSufficiency
)
```

The predefined scorers cover:
- **Correctness** – Answer accuracy against ground truth.
- **Guidelines** – Adherence to provided guidelines.
- **ExpectationsGuidelines** – Compliance with expected behavior rules.
- **RelevanceToQuery** – Relevance of response to the original query.
- **Safety** – Harmful or unsafe content detection.
- **RetrievalGroundedness** – Whether the response is grounded in retrieved documents.
- **RetrievalRelevance** – Relevance of retrieved documents.
- **RetrievalSufficiency** – Whether retrieved documents contain enough information. ^[migrate-to-mlflow-3-from-agent-evaluation-quick-reference-databricks-on-aws.md]

### `mlflow.genai.judges`
Provides AI judge utilities for automated evaluation. It replaces `databricks.agents.evals.judges`.

```python
from mlflow.genai import judges
```

^[migrate-to-mlflow-3-from-agent-evaluation-quick-reference-databricks-on-aws.md]

### `mlflow.genai.labeling`
Handles labeling of evaluation data. It replaces labeling functionality that was part of the old Agent Evaluation workflow.

```python
import mlflow.genai.labeling as labeling
```

^[migrate-to-mlflow-3-from-agent-evaluation-quick-reference-databricks-on-aws.md]

### `mlflow.genai.label_schemas`
Provides label schemas for structured labeling tasks.

```python
import mlflow.genai.label_schemas as schemas
```

^[migrate-to-mlflow-3-from-agent-evaluation-quick-reference-databricks-on-aws.md]

## Migration from Agent Evaluation

The GenAI Module is the target for migration away from the deprecated `databricks.agents.evals` module (often called **Agent Evaluation**). The following substitutions should be made:

| Old Import | New Import |
|---|---|
| `from mlflow import evaluate` | `from mlflow.genai import evaluate` |
| `from databricks.agents.evals import metric` | `from mlflow.genai.scorers import scorer` |
| `from databricks.agents.evals import judges` | `from mlflow.genai import judges` |
| `from databricks.agents import review_app` | (use `mlflow.genai` evaluation and review workflows) |

The predefined scorer classes (e.g., `Correctness`, `Guidelines`) replace the old metric objects. ^[migrate-to-mlflow-3-from-agent-evaluation-quick-reference-databricks-on-aws.md]

## Related Concepts

- [MLflow 3](/concepts/mlflow-3.md) – Overview of the MLflow 3 release and its new module structure.
- [Agent Evaluation](/concepts/mlflow-agent-evaluation.md) – The deprecated workflow that the GenAI Module replaces.
- RAG Evaluation – Evaluation of retrieval-augmented generation systems, supported by the `Retrieval*` scorers.
- [AI Judges](/concepts/llm-as-a-judge.md) – Automated judging for evaluation, provided by `mlflow.genai.judges`.
- [Predefined Scorers](/concepts/mlflow-genai-predefined-scorers.md) – Standalone documentation for each scorer.

## Sources

- migrate-to-mlflow-3-from-agent-evaluation-quick-reference-databricks-on-aws.md

# Citations

1. [migrate-to-mlflow-3-from-agent-evaluation-quick-reference-databricks-on-aws.md](/references/migrate-to-mlflow-3-from-agent-evaluation-quick-reference-databricks-on-aws-4733fb1b.md)
