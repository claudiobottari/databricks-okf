---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 27c0a7c65abf3e336965cd0f478a5c1163355b34821a6d50013c36cf05e59042
  pageDirectory: concepts
  sources:
    - code-based-scorers-databricks-on-aws.md
  confidence: 0.94
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - production-monitoring-with-custom-scorer-functions
    - PMWCSF
    - Production monitoring with scorers
  citations:
    - file: code-based-scorers-databricks-on-aws.md
title: Production monitoring with custom scorer functions
description: Production monitoring supports built-in LLM judges and @scorer-decorated functions, but not class-based Scorer subclasses
tags:
  - databricks
  - monitoring
  - mlflow
timestamp: "2026-06-19T17:45:02.326Z"
---

---
title: Production monitoring with custom scorer functions
summary: How to use `@scorer`-decorated functions for production monitoring, including constraints on class-based scorers and notebook registration.
sources:
  - code-based-scorers-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T12:00:00.000Z"
updatedAt: "2026-06-18T12:00:00.000Z"
tags:
  - production-monitoring
  - custom-scorers
  - mlflow
aliases:
  - production-monitoring-with-custom-scorer-functions
  - PMCSF
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Production monitoring with custom scorer functions

Production monitoring in MLflow supports both [Built-in LLM Judges](/concepts/built-in-llm-judges.md) and custom scorer functions defined with the `@scorer` decorator. This page describes the requirements and limitations for using custom scorer functions in production monitoring.

## Overview

To extend the evaluation capabilities of production monitoring beyond the built-in LLM judges, you can write your own scoring logic using the `@scorer` decorator. However, class-based `Scorer` subclasses are **not supported** for production monitoring. Only `@scorer`-decorated functions can be used. ^[code-based-scorers-databricks-on-aws.md]

## Key requirements

`@scorer`-decorated functions used in production monitoring must be **defined and registered from a Databricks notebook**. The monitoring service serializes the function code for remote execution, and this serialization step requires the notebook environment. You cannot define or register these scorer functions from other contexts such as scripts or IDEs. ^[code-based-scorers-databricks-on-aws.md]

For a detailed walkthrough of registering and using custom scorer functions, see the documentation on [Custom scorer functions](/concepts/custom-scorer-definition-in-mlflow.md) under the production monitoring guide. ^[code-based-scorers-databricks-on-aws.md]

## Handling stateful scorers

If you need a stateful scorer (for example, one that caches results or holds configuration loaded at startup), you must use the `@scorer` decorator and manage state **inside the function body**. Because class-based `Scorer` subclasses are disallowed, any state must be encapsulated within the function closure or by using module-level variables accessible from the function body. ^[code-based-scorers-databricks-on-aws.md]

## Related concepts

- [Production Monitoring](/concepts/production-monitoring.md) – The overarching system that runs scheduled evaluations.
- [Built-in LLM Judges](/concepts/built-in-llm-judges.md) – Pre-built evaluation judges provided by MLflow.
- [@scorer decorator](/concepts/scorer-decorator.md) – The decorator used to define custom scorer functions.
- [Scorer class](/concepts/scorer-class.md) – The base class for MLflow scorers (not supported for production monitoring).
- [Custom scorer functions](/concepts/custom-scorer-definition-in-mlflow.md) – Full documentation for registering and using scorer functions in production.
- Databricks notebook – The required environment for defining and registering production scorers.

## Sources

- code-based-scorers-databricks-on-aws.md

# Citations

1. [code-based-scorers-databricks-on-aws.md](/references/code-based-scorers-databricks-on-aws-2a1f1dbe.md)
