---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1f02d5e84fa78f244ad94c945c785b4305cac7416f204ce5be3e47b27776f282
  pageDirectory: concepts
  sources:
    - code-based-scorers-databricks-on-aws.md
  confidence: 0.8
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - stateful-scorers-in-production
    - SSIP
    - Run scorers in production
  citations:
    - file: code-based-scorers-databricks-on-aws.md
title: Stateful Scorers in Production
description: Technique for implementing stateful scorers by managing state inside the body of a @scorer-decorated function, since class-based Scorer subclasses are not supported.
tags:
  - mlflow
  - scoring
  - state-management
timestamp: "2026-06-18T10:58:30.246Z"
---

# Stateful Scorers in Production

**Stateful Scorers in Production** refers to the practice of creating custom scoring functions that maintain internal state (such as counters, caches, or loaded models) when used with Databricks production monitoring for LLM applications. While Databricks supports both functional (`@scorer`-decorated) and class-based (`Scorer` subclass) approaches for evaluation, only the functional approach with managed state is supported in production monitoring environments.

## Production Monitoring Support

Production monitoring supports [built-in LLM judges](/docs/databricks/genai/eval-monitor/judges) and `@scorer`-decorated functions. Class-based `Scorer` subclasses are **not supported** for production monitoring. If you need stateful scorers in production, you must use the `@scorer` decorator and manage state inside the function body.^[code-based-scorers-databricks-on-aws.md]

## Implementing Stateful Scorers

To create a stateful scorer for production use:

1. **Use the `@scorer` decorator** — Define your scoring logic as a decorated function rather than a class-based `Scorer` subclass.
2. **Manage state within the function body** — Use function-level variables, closures, or module-level singletons to maintain state across invocations.
3. **Define and register from a Databricks notebook** — `@scorer`-decorated functions used in production monitoring must be defined and registered from a Databricks notebook. The monitoring service serializes the function code for remote execution, and this serialization requires the notebook environment.^[code-based-scorers-databricks-on-aws.md]

## Limitations

- Class-based `Scorer` subclasses are not supported in production monitoring, even if they would provide cleaner state management through instance variables or lifecycle methods.
- State managed inside `@scorer` functions must be serializable for remote execution by the monitoring service.
- All custom scorer functions for production monitoring must originate from Databricks notebooks.

## Related Concepts

- Custom Scorers for Evaluation — Scorers used in offline evaluation contexts
- [Built-in LLM Judges](/concepts/built-in-llm-judges.md) — Pre-built evaluation judges provided by Databricks
- [Production Monitoring](/concepts/production-monitoring.md) — The monitoring infrastructure for deployed LLM applications
- LLM Evaluation Concepts — Foundational concepts for LLM evaluation
- [@scorer decorator](/concepts/scorer-decorator.md) — The decorator for defining custom scoring functions

## Sources

- code-based-scorers-databricks-on-aws.md

# Citations

1. [code-based-scorers-databricks-on-aws.md](/references/code-based-scorers-databricks-on-aws-2a1f1dbe.md)
