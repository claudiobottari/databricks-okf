---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 328ec2604e8f5e2ab7bf1b4880f34920961126d6e7d1608d0a2a0f2c749689f5
  pageDirectory: concepts
  sources:
    - code-based-scorers-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - notebook-environment-requirement
    - NER
  citations:
    - file: code-based-scorers-databricks-on-aws.md
title: Notebook environment requirement
description: "@scorer-decorated functions used in production monitoring must be defined and registered from a Databricks notebook due to serialization constraints"
tags:
  - mlflow
  - databricks
  - environment
timestamp: "2026-06-19T09:14:38.585Z"
---

# Notebook Environment Requirement

The **notebook environment requirement** is a constraint for production monitoring with custom scorer functions in Databricks: any function decorated with `@scorer` that is used for production monitoring must be defined and registered from a Databricks notebook. This requirement exists because the monitoring service serializes the function’s code for remote execution, and the serialization process depends on the notebook runtime environment. ^[code-based-scorers-databricks-on-aws.md]

## Scope

The requirement applies only to `@scorer`-decorated functions. Class-based `Scorer` subclasses are **not supported** for production monitoring at all; if stateful scoring is needed in production, developers must use the `@scorer` decorator and manage state inside the function body instead of subclassing. ^[code-based-scorers-databricks-on-aws.md]

## Workflow Implication

Because the notebook environment is mandatory, developers cannot define production-ready `@scorer` functions in arbitrary Python scripts or libraries outside of a Databricks notebook and still use them with production monitoring. The function must be authored and registered from within a notebook that runs on a Databricks cluster.

## Related Concepts

- [Production monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) – the monitoring system that consumes the scorer functions.
- [@scorer decorator](/concepts/scorer-decorator.md) – the decorator used to mark custom scoring functions.
- [Custom scorer functions](/concepts/custom-scorer-definition-in-mlflow.md) – the broader concept of user-defined evaluation logic.

## Sources

- code-based-scorers-databricks-on-aws.md

# Citations

1. [code-based-scorers-databricks-on-aws.md](/references/code-based-scorers-databricks-on-aws-2a1f1dbe.md)
