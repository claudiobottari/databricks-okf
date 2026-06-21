---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8d74f24fef49787e5e2b0464c81635b00d72bc3ac2486dc11395a00b8b4f5722
  pageDirectory: concepts
  sources:
    - migrate-to-mlflow-3-from-agent-evaluation-quick-reference-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - migration-from-databricks-agent-evaluation-to-mlflow-3
    - MFDAETM3
  citations:
    - file: migrate-to-mlflow-3-from-agent-evaluation-quick-reference-databricks-on-aws.md
title: Migration from Databricks Agent Evaluation to MLflow 3
description: The process and code changes required to migrate from the legacy databricks.agents.evals API to the new mlflow.genai API.
tags:
  - mlflow
  - migration
  - agent-evaluation
timestamp: "2026-06-19T19:35:31.114Z"
---

# Migration from Databricks Agent Evaluation to MLflow 3

This page describes the key changes when migrating from Databricks Agent Evaluation to MLflow 3 (the MLflow GenAI module). The migration primarily involves updating import paths, function names, and module references.

## Overview

MLflow 3 introduces a dedicated GenAI module (`mlflow.genai`) that consolidates the evaluation, scoring, and labeling capabilities previously provided by Databricks Agent Evaluation (`databricks.agents.evals`). The migration requires updating your Python imports and using the new MLflow GenAI APIs. ^[migrate-to-mlflow-3-from-agent-evaluation-quick-reference-databricks-on-aws.md]

## Key Changes

### Import Paths

All imports from `databricks.agents` and `databricks.agents.evals` must be replaced with imports from `mlflow.genai` and its submodules. Below is a side-by-side comparison:

| Old Import (Databricks Agent Evaluation) | New Import (MLflow 3) |
|-------------------------------------------|------------------------|
| `from mlflow import evaluate` | `from mlflow.genai import evaluate` |
| `from databricks.agents.evals import metric` | `from mlflow.genai.scorers import scorer` |
| `from databricks.agents.evals import judges` | `from mlflow.genai import judges` |
| `from databricks.agents import review_app` | Not shown in new imports (workflow continues via MLflow GenAI) |

^[migrate-to-mlflow-3-from-agent-evaluation-quick-reference-databricks-on-aws.md]

### Evaluation Function

The main evaluation function moves from `mlflow.evaluate` to `mlflow.genai.evaluate`. All evaluation calls should be updated to use the new module.

### Scorers and Judges

- The old `metric` import from `databricks.agents.evals` becomes `scorer` from `mlflow.genai.scorers`.
- The old `judges` import from `databricks.agents.evals.judges` becomes `judges` from `mlflow.genai`.
- Predefined scorers are available from `mlflow.genai.scorers`, including:
  - `Correctness`
  - `Guidelines`
  - `ExpectationsGuidelines`
  - `RelevanceToQuery`
  - `Safety`
  - `RetrievalGroundedness`
  - `RetrievalRelevance`
  - `RetrievalSufficiency`

^[migrate-to-mlflow-3-from-agent-evaluation-quick-reference-databricks-on-aws.md]

### Labeling

New imports for labeling functionality are added, available under `mlflow.genai.labeling` and `mlflow.genai.label_schemas`. These replace any previous labeling utilities from Agent Evaluation. ^[migrate-to-mlflow-3-from-agent-evaluation-quick-reference-databricks-on-aws.md]

### Review App

The old import `from databricks.agents import review_app` is no longer used. The review app functionality is now part of [MLflow GenAI](/concepts/mlflow-3-for-genai.md), though the migration reference does not explicitly list a replacement import.

## Migration Steps

1. Update all `import` statements as shown in the table above.
2. Replace calls to `mlflow.evaluate()` with `mlflow.genai.evaluate()`.
3. Replace `metric` instances with `scorer` from `mlflow.genai.scorers`.
4. Replace `judges` import path from `databricks.agents.evals` to `mlflow.genai`.
5. Import predefined scorers from `mlflow.genai.scorers` as needed.
6. For labeling, add imports from `mlflow.genai.labeling` and `mlflow.genai.label_schemas`.
7. Remove imports from `databricks.agents` and `databricks.agents.evals`.

## Related Concepts

- [MLflow GenAI](/concepts/mlflow-3-for-genai.md) – The new module replacing Agent Evaluation
- [Scorers in MLflow GenAI](/concepts/scorers-mlflow-genai.md) – Definition and usage of scorers
- Judges in MLflow GenAI – LLM-as-judge evaluation models
- [Predefined Scorers](/concepts/mlflow-genai-predefined-scorers.md) – Built-in evaluation metrics (correctness, safety, etc.)
- Labeling – Human-in-the-loop labeling workflows

## Sources

- migrate-to-mlflow-3-from-agent-evaluation-quick-reference-databricks-on-aws.md

# Citations

1. [migrate-to-mlflow-3-from-agent-evaluation-quick-reference-databricks-on-aws.md](/references/migrate-to-mlflow-3-from-agent-evaluation-quick-reference-databricks-on-aws-4733fb1b.md)
