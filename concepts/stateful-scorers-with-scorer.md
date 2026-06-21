---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 66d341d3554a793dfeef87769c75a9396ffa87b7f690b68758c057bf76e91584
  pageDirectory: concepts
  sources:
    - code-based-scorers-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - stateful-scorers-with-scorer
    - SSW@
  citations:
    - file: code-based-scorers-databricks-on-aws.md
title: Stateful scorers with @scorer
description: To implement stateful scorers in production, use the @scorer decorator and manage state inside the function body, since class-based approaches are unsupported
tags:
  - mlflow
  - state-management
  - scoring
timestamp: "2026-06-19T09:14:51.308Z"
---

# Stateful scorers with `@scorer`

**Stateful scorers** are evaluation functions that maintain internal state (e.g., accumulated counts, shared resources, or external connections) across multiple scoring calls. In production monitoring on Databricks, stateful scorers can only be implemented using the `@scorer` decorator; class-based `Scorer` subclasses are not supported.

## Overview

When a custom scorer needs to hold state — for example, to amortize an expensive model load, track a running metric, or cache intermediate results — the scorer must manage that state inside the body of a `@scorer`-decorated function. The alternative approach, subclassing `Scorer`, is explicitly **not supported** for production monitoring workloads. ^[code-based-scorers-databricks-on-aws.md]

## Stateful Scorers vs. Class-based Scorers

| Approach | Supported in production monitoring? | State management |
|----------|--------------------------------------|-----------------|
| `@scorer`-decorated function | Yes | State is managed inside the function body. |
| Class-based `Scorer` subclass | No | Not available — must migrate to `@scorer`. |

The source documentation recommends: _If you need stateful scorers in production, use the `@scorer` decorator and manage state inside the function body._ ^[code-based-scorers-databricks-on-aws.md]

## Implementing a Stateful Scorer with `@scorer`

A `@scorer`-decorated function is defined like a regular Python function but carries the `@scorer` annotation. To make it stateful, you typically use non-local variables, closures, or function attributes. The exact pattern is not prescribed by the source, but the state must be held within the function’s closure or global scope.

```python
@scorer
def my_stateful_scorer(inputs, outputs, expected=None):
    # Manage state (e.g., a counter) inside the function
    if not hasattr(my_stateful_scorer, "call_count"):
        my_stateful_scorer.call_count = 0
    my_stateful_scorer.call_count += 1
    # ... evaluation logic ...
    return {"score": 0.95}
```

## Production Monitoring Requirements

`@scorer`-decorated functions used in production monitoring **must** be defined and registered from a Databricks notebook. The monitoring service serializes the function code for remote execution, and this serialization relies on the notebook environment. Functions defined in scripts or libraries outside of notebooks may not serialize correctly. ^[code-based-scorers-databricks-on-aws.md]

> For details, see the documentation on [Use custom scorer functions](/concepts/custom-scorers-for-llm-evaluation.md) in production monitoring. ^[code-based-scorers-databricks-on-aws.md]

## Related Concepts

- [Production Monitoring](/concepts/production-monitoring.md) – The context in which stateful scorers are used.
- [Built-in LLM Judges](/concepts/built-in-llm-judges.md) – Alternative to custom scorers, provided out-of-the-box.
- [@scorer decorator](/concepts/scorer-decorator.md) – The decorator used to define custom scorer functions.
- Class-based Scorer subclass – The unsupported alternative for stateful scorers.
- Databricks notebook – Required environment for defining production scorer functions.
- [Custom scorer functions](/concepts/custom-scorer-definition-in-mlflow.md) – General documentation on authoring scorers for production.

## Sources

- code-based-scorers-databricks-on-aws.md

# Citations

1. [code-based-scorers-databricks-on-aws.md](/references/code-based-scorers-databricks-on-aws-2a1f1dbe.md)
