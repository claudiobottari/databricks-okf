---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 40ba91e60136daed1f148ebee803d5b8a5805068683dfe76171ee49a509d3cb1
  pageDirectory: concepts
  sources:
    - code-based-scorers-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - class-based-scorer-subclasses-limitation
    - CSSL
  citations:
    - file: code-based-scorers-databricks-on-aws.md
title: Class-based Scorer subclasses limitation
description: Class-based Scorer subclasses are not supported for production monitoring in Databricks
tags:
  - databricks
  - mlflow
  - limitation
timestamp: "2026-06-19T17:44:49.094Z"
---

# Class-based Scorer subclasses limitation

**Class-based Scorer subclasses limitation** refers to the restriction that class-based `Scorer` subclasses are not supported for production monitoring in Databricks. Only built-in LLM judges and `@scorer`-decorated functions can be used for production monitoring workloads. ^[code-based-scorers-databricks-on-aws.md]

## Overview

When implementing custom scoring logic for production monitoring, users must use the `@scorer` decorator approach rather than creating class-based subclasses of `Scorer`. The class-based inheritance pattern is explicitly unsupported in the production monitoring context. ^[code-based-scorers-databricks-on-aws.md]

## Workaround for Stateful Scorers

If your scoring logic requires maintaining state (such as counters, caches, or configuration objects), you can still use the `@scorer` decorator by managing state inside the function body. This allows you to maintain stateful behavior while complying with the production monitoring requirements. ^[code-based-scorers-databricks-on-aws.md]

## Notebook Requirement

`@scorer`-decorated functions used in production monitoring must be defined and registered from a **Databricks notebook**. The monitoring service serializes the function code for remote execution, and this serialization process requires the notebook environment. ^[code-based-scorers-databricks-on-aws.md]

For more details on using custom scorer functions in production monitoring, see the documentation on [custom scorer functions](/concepts/custom-scorers-for-llm-evaluation.md). ^[code-based-scorers-databricks-on-aws.md]

## Related Concepts

- [Production Monitoring](/concepts/production-monitoring.md) — The context where this limitation applies
- [Built-in LLM Judges](/concepts/built-in-llm-judges.md) — Supported alternative for production monitoring
- [@scorer decorator](/concepts/scorer-decorator.md) — The supported approach for custom scoring logic
- [Custom scorer functions](/concepts/custom-scorer-definition-in-mlflow.md) — Detailed guidance on implementing scorers
- [MLflow evaluation](/concepts/mlflow-evaluation-ui.md) — Broader evaluation framework that includes scoring

## Sources

- code-based-scorers-databricks-on-aws.md

# Citations

1. [code-based-scorers-databricks-on-aws.md](/references/code-based-scorers-databricks-on-aws-2a1f1dbe.md)
