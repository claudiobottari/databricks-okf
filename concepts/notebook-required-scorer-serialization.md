---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 974140f8c9d8bcda8a20b86fd80447d8e61704db0e2b4d0b204b6b9ac53c0346
  pageDirectory: concepts
  sources:
    - code-based-scorers-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - notebook-required-scorer-serialization
    - NSS
    - notebook-required-function-serialization
    - NFS
  citations:
    - file: code-based-scorers-databricks-on-aws.md
    - file: code-based-scorer-reference-databricks-on-aws.md
title: Notebook-Required Scorer Serialization
description: "@scorer-decorated functions used in production monitoring must be defined and registered from a Databricks notebook because the monitoring service serializes function code for remote execution and requires the notebook environment."
tags:
  - mlflow
  - databricks
  - serialization
  - notebook
timestamp: "2026-06-18T10:58:38.740Z"
---

# Notebook-Required Scorer Serialization

**Notebook-Required Scorer Serialization** refers to the constraint that `@scorer`-decorated functions used in production monitoring must be defined and registered from a **Databricks notebook**, because the monitoring service serializes the function code for remote execution and this serialization process requires the notebook environment.^[code-based-scorers-databricks-on-aws.md]

## Background

Production monitoring supports both [built-in LLM judges](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/judges/) and `@scorer`-decorated functions. Class-based `Scorer` subclasses are **not supported** for production monitoring. If you need stateful scorers in production, use the `@scorer` decorator and manage state inside the function body.^[code-based-scorers-databricks-on-aws.md]

## Serialization requirement

When a `@scorer`-decorated function is registered from a Databricks notebook, the monitoring service captures the function’s code and serializes it for remote execution on the inference evaluation infrastructure. This serialization relies on the notebook environment to correctly capture dependencies and closure variables. Defining or registering the function outside a notebook (for example, from a Python script or an IDE) is not supported for production monitoring.^[code-based-scorers-databricks-on-aws.md]

## Workflow

1. Write your custom scorer as a `@scorer`-decorated function in a Databricks notebook.
2. Register the scorer using the notebook environment.
3. Start the scorer with a sampling configuration (e.g., `scorer.start(sampling_config=...)`) to enable production monitoring.

If you need to access Databricks secrets or other runtime resources inside the scorer, you must import `dbutils` explicitly inside the function body (see [Accessing Databricks secrets in scorers](/concepts/accessing-secrets-in-scorers.md)).^[code-based-scorer-reference-databricks-on-aws.md]

## Related concepts

- [Code-based Scorers](/concepts/code-based-scorers.md) — The `@scorer` decorator and custom evaluation functions.
- [Production Monitoring](/concepts/production-monitoring.md) — The inference table pipeline that uses registered scorers.
- [Scorer class](/concepts/scorer-class.md) — Alternative class-based approach (not supported for production monitoring).
- [Accessing Databricks secrets in scorers](/concepts/accessing-secrets-in-scorers.md) — How to securely use `dbutils` inside a scorer.

## Sources

- code-based-scorers-databricks-on-aws.md

# Citations

1. [code-based-scorers-databricks-on-aws.md](/references/code-based-scorers-databricks-on-aws-2a1f1dbe.md)
2. [code-based-scorer-reference-databricks-on-aws.md](/references/code-based-scorer-reference-databricks-on-aws-b52e32c9.md)
