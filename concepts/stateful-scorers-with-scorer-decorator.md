---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ad19c72e510a6567cb4a70707501786079a7842bf59bfdc0bf905c3e6d04e1fb
  pageDirectory: concepts
  sources:
    - code-based-scorers-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - stateful-scorers-with-scorer-decorator
    - SSW@D
  citations:
    - file: code-based-scorers-databricks-on-aws.md
title: Stateful scorers with @scorer decorator
description: For stateful scorers in production, use the @scorer decorator and manage state inside the function body
tags:
  - databricks
  - mlflow
  - pattern
timestamp: "2026-06-19T17:45:11.405Z"
---

---

title: Stateful scorers with @scorer decorator
summary: The recommended pattern for implementing stateful evaluation scorers in Databricks production monitoring — use the @scorer decorator and manage state inside the function body, because class-based Scorer subclasses are not supported.
sources:
  - code-based-scorers-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T14:37:06.095Z"
updatedAt: "2026-06-18T14:37:06.095Z"
tags:
  - databricks
  - production-monitoring
  - mlflow
  - evaluation
  - design-pattern
aliases:
  - stateful-scorers-with-scorer-decorator
  - SSW@D
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0

---

# Stateful scorers with `@scorer` decorator

Production monitoring supports two types of custom evaluators: built-in [LLM judges](/concepts/llm-judges.md) and functions decorated with the `@scorer` decorator. Class-based `Scorer` subclasses – a common way to implement stateful scoring logic in offline evaluation – are **not supported** for production monitoring. Stateful scorers in production must use the `@scorer` decorator, with all state managed directly inside the function body. ^[code-based-scorers-databricks-on-aws.md]

A `@scorer`-decorated function used in production monitoring must be **defined and registered from a Databricks notebook**. The monitoring service serialises the function’s code for remote execution, and this serialisation mechanism depends on the notebook environment. Defining the scorer outside a notebook (for example, in a Python wheel or library file) will not work with production monitoring. For more details, see [Use custom scorer functions](/concepts/custom-scorers-for-llm-evaluation.md). ^[code-based-scorers-databricks-on-aws.md]

## Related concepts

- [Custom scorers](/concepts/custom-scorers-mlflow-genai.md) – General guide for writing `@scorer` functions.
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) – The service that invokes scorers at inference time.
- [LLM Judges](/concepts/llm-judges.md) – Built-in stateful evaluators that can be used without custom code.
- Databricks notebooks – The required environment for defining production‑scoped scorers.

## Sources

- code-based-scorers-databricks-on-aws.md

# Citations

1. [code-based-scorers-databricks-on-aws.md](/references/code-based-scorers-databricks-on-aws-2a1f1dbe.md)
