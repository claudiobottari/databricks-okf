---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 86f36867f6972f13dd09d8ddd82844dc5c14e77cf284c6805b3cd92ed0262c8f
  pageDirectory: concepts
  sources:
    - code-based-scorers-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - stateful-scorers-in-production-using-scorer
    - SSIPU@
  citations:
    - file: code-based-scorers-databricks-on-aws.md
title: Stateful scorers in production using @scorer
description: For stateful scoring logic in production, use the @scorer decorator and manage state inside the function body instead of class-based subclasses.
tags:
  - mlflow
  - state-management
  - production-monitoring
timestamp: "2026-06-19T14:13:20.532Z"
---

## Stateful scorers in production using `@scorer`

**Stateful scorers in production using `@scorer`** refers to the recommended pattern for deploying custom evaluation logic that requires maintaining internal state (e.g., counters, accumulated scores, or external connections) within a production monitoring environment. The Databricks production monitoring system supports only function-based scorers created with the `@scorer` decorator; class-based `Scorer` subclasses are explicitly **not supported** for production monitoring. ^[code-based-scorers-databricks-on-aws.md]

### Using the `@scorer` decorator

If you need a stateful scorer in production, use the `@scorer` decorator and manage the state entirely inside the function body. Because class-based approaches are disallowed, all state must be encapsulated within the function scope—for example, by using closures, global variables (with caution for concurrency), or by reading/writing external storage inside the function. The decorated function is serialized and executed remotely, so any state must be re‑created at each invocation or persisted appropriately. ^[code-based-scorers-databricks-on-aws.md]

```python
from mlflow.pyfunc import scorer

@scorer
def my_stateful_scorer(model_input, model_output, context):
    # Manage state inside the function body
    # e.g., accumulate a counter or read a config file
    ...
    return {"score": value}
```

### Notebook requirement

`@scorer`-decorated functions used in production monitoring **must be defined and registered from a Databricks notebook**. The monitoring service serializes the function code for remote execution, and this serialization process requires the notebook environment. If you attempt to define or register the scorer outside of a notebook, serialization will fail, preventing the scorer from being used in production. ^[code-based-scorers-databricks-on-aws.md]

### Related concepts

- [Production monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) – The context where these scorers are deployed.
- [Built-in LLM Judges](/concepts/built-in-llm-judges.md) – The alternative supported approach for scoring.
- [@scorer decorator](/concepts/scorer-decorator.md) – The decorator used to create function‑based scorers.
- Databricks notebooks – The required environment for defining production scorers.

## Sources

- code-based-scorers-databricks-on-aws.md

# Citations

1. [code-based-scorers-databricks-on-aws.md](/references/code-based-scorers-databricks-on-aws-2a1f1dbe.md)
