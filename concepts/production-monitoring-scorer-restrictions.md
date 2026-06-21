---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 474b2736985feaf9940fb5ccb2d9e8e8d8c9407b526fd34cacbd1f84e220b4cf
  pageDirectory: concepts
  sources:
    - code-based-scorers-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - production-monitoring-scorer-restrictions
    - PMSR
  citations:
    - file: code-based-scorers-databricks-on-aws.md
title: Production Monitoring Scorer Restrictions
description: Class-based Scorer subclasses are not supported for production monitoring; only @scorer-decorated functions are allowed.
tags:
  - mlflow
  - production-monitoring
  - limitations
timestamp: "2026-06-18T10:58:44.893Z"
---

# Production Monitoring Scorer Restrictions

**Production Monitoring Scorer Restrictions** are the constraints and requirements that govern which custom scoring functions can be used with Databricks production monitoring for generative AI applications. These restrictions ensure that scorers can be reliably serialized and executed in the production monitoring environment.

## Supported Scorer Types

Production monitoring supports two types of scoring mechanisms for evaluating model outputs:

- **Built-in LLM judges** — Predefined evaluators provided by Databricks.
- **`@scorer`-decorated functions** — Custom scoring functions defined using the `@scorer` decorator pattern. ^[code-based-scorers-databricks-on-aws.md]

## Unsupported Scorer Types

Class-based `Scorer` subclasses are **not supported** for production monitoring. If you need stateful scorers in a production environment, you must use the `@scorer` decorator and manage state inside the function body instead of relying on class instances. ^[code-based-scorers-databricks-on-aws.md]

## Notebook Requirement

`@scorer`-decorated functions used in production monitoring must be defined and registered from a **Databricks notebook**. This requirement exists because the monitoring service serializes the function code for remote execution, and this serialization process requires the notebook environment. Functions defined outside of a notebook context cannot be properly serialized and executed by the monitoring service. ^[code-based-scorers-databricks-on-aws.md]

## Related Concepts

- [Built-in LLM Judges](/concepts/built-in-llm-judges.md) — Predefined evaluators for common quality and safety metrics
- [@scorer decorator](/concepts/scorer-decorator.md) — The decorator pattern for creating custom scoring functions
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — The monitoring system that consumes these scorers
- [Custom Scorer Functions](/concepts/custom-scorer-definition-in-mlflow.md) — Best practices for writing scoring functions for production

## Sources

- code-based-scorers-databricks-on-aws.md

# Citations

1. [code-based-scorers-databricks-on-aws.md](/references/code-based-scorers-databricks-on-aws-2a1f1dbe.md)
