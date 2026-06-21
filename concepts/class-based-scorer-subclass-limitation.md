---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3ac0167828edcf95725732227daa91db2e0dc7773c9a93392a235f757c5c48ae
  pageDirectory: concepts
  sources:
    - code-based-scorers-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - class-based-scorer-subclass-limitation
    - CSSL
  citations:
    - file: code-based-scorers-databricks-on-aws.md
title: Class-based Scorer subclass limitation
description: Class-based Scorer subclasses are not supported for production monitoring in Databricks; only @scorer-decorated functions work
tags:
  - mlflow
  - limitations
  - production-monitoring
timestamp: "2026-06-19T09:14:40.510Z"
---

```yaml
---
title: Class-based Scorer subclass limitation
summary: Databricks production monitoring does not support class-based Scorer subclasses; only @scorer-decorated functions are allowed.
sources:
  - code-based-scorers-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T14:36:56.298Z"
updatedAt: "2026-06-18T14:36:56.298Z"
tags:
  - databricks
  - production-monitoring
  - limitation
aliases:
  - class-based-scorer-subclass-limitation
  - CSSL
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# Class-based Scorer subclass limitation

**Class-based Scorer subclass limitation** refers to the restriction that production monitoring in MLflow GenAI does not support `Scorer` subclasses created through class-based inheritance. Only built-in LLM judges and `@scorer`-decorated functions are supported for production monitoring workloads. ^[code-based-scorers-databricks-on-aws.md]

## Overview

When implementing custom scorers for production monitoring, developers must use the `@scorer` decorator pattern rather than creating class-based subclasses of the `Scorer` base class. This limitation applies specifically to production monitoring, not to offline evaluation scenarios. ^[code-based-scorers-databricks-on-aws.md]

## Supported Approaches

Production monitoring supports the following scorer types:

- **Built-in LLM judges** — Pre-configured evaluators provided by the platform
- **`@scorer`-decorated functions** — Custom scorer logic defined using the decorator pattern

Class-based `Scorer` subclasses are explicitly **not supported** for production monitoring. ^[code-based-scorers-databricks-on-aws.md]

## Workaround for Stateful Scorers

If you need stateful scorers in production, use the `@scorer` decorator and manage state inside the function body. This approach allows you to maintain state without relying on class-based inheritance. ^[code-based-scorers-databricks-on-aws.md]

## Notebook Requirement

`@scorer`-decorated functions used in production monitoring must be defined and registered from a **Databricks notebook**. The monitoring service serializes the function code for remote execution, and this serialization requires the notebook environment. For details, see Use custom scorer functions for production monitoring. ^[code-based-scorers-databricks-on-aws.md]

## Related Concepts

- [Custom Scorers](/concepts/custom-scorers-mlflow-genai.md) — Implementing custom evaluation logic for GenAI applications
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Continuous quality monitoring in production
- [Built-in LLM Judges](/concepts/built-in-llm-judges.md) — Pre-configured evaluators for common quality criteria
- [@scorer decorator](/concepts/scorer-decorator.md) — The supported pattern for creating custom scorers
- Offline Evaluation — Evaluation scenarios where class-based scorers may still be applicable

## Sources

- code-based-scorers-databricks-on-aws.md

# Citations

1. [code-based-scorers-databricks-on-aws.md](/references/code-based-scorers-databricks-on-aws-2a1f1dbe.md)
