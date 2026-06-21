---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5931205f84c74c15346c9c662e7dca5bc7c35283ba3cfc5a6a7145cb1e5662ea
  pageDirectory: concepts
  sources:
    - code-based-scorers-databricks-on-aws.md
  confidence: 0.85
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - production-monitoring-custom-scorer-functions
    - PMCSF
  citations:
    - file: code-based-scorers-databricks-on-aws.md
title: Production monitoring custom scorer functions
description: The overall pattern for using user-defined scoring functions in Databricks production monitoring, including serialization and registration requirements
tags:
  - mlflow
  - production-monitoring
  - custom-scorers
timestamp: "2026-06-19T09:14:49.711Z"
---

# Production monitoring custom scorer functions

**Production monitoring custom scorer functions** are user-defined Python functions that evaluate the quality of model outputs in production. They are created using the `@scorer` decorator and registered with [MLflow](/concepts/mlflow.md) to run as part of a production monitoring schedule.

## Overview

Production monitoring supports two types of evaluators: [Built-in LLM Judges](/concepts/built-in-llm-judges.md) and `@scorer`-decorated functions. Custom scorer functions allow teams to define their own evaluation logic tailored to specific use cases, such as checking for response format compliance, domain-specific correctness, or business rule adherence. ^[code-based-scorers-databricks-on-aws.md]

## Requirements

### Decorator-based functions only

Production monitoring supports only `@scorer`-decorated functions. Class-based `Scorer` subclasses are **not supported** for production monitoring. If you need stateful scorers in production, use the `@scorer` decorator and manage state inside the function body. ^[code-based-scorers-databricks-on-aws.md]

### Notebook registration required

`@scorer`-decorated functions used in production monitoring must be defined and registered from a **Databricks notebook**. The monitoring service serializes the function code for remote execution, and this serialization requires the notebook environment. ^[code-based-scorers-databricks-on-aws.md]

## Creating a custom scorer function

### Basic structure

A custom scorer function is defined using the `@scorer` decorator from `mlflow.monitoring`. The function receives model inputs and outputs and returns a score or evaluation result.

```python
from mlflow.monitoring import scorer

@scorer(name="response_length_checker", description="Checks response length constraints")
def response_length_checker(inputs, outputs):
    # Custom evaluation logic
    response = outputs.get("response", "")
    if len(response) > 1000:
        return {"score": 0, "reason": "Response exceeds maximum length"}
    return {"score": 1, "reason": "Response within acceptable length"}
```

### State management

For stateful scorers, manage state inside the function body rather than using class-based approaches. This can include loading external models, caching results, or maintaining counters. ^[code-based-scorers-databricks-on-aws.md]

## Registering a custom scorer

Custom scorer functions are registered through the [MLflow monitoring API](/concepts/mlflow-trace-error-monitoring.md) from a Databricks notebook. The registration process serializes the function code so it can be executed remotely by the monitoring service.

```python
from mlflow.monitoring import register_scorer

register_scorer(response_length_checker)
```

## Using custom scorers in production monitoring

Once registered, custom scorer functions can be added to a production monitoring schedule. The monitoring service invokes the scorer function on each inference request according to the configured sampling rate.

### Integration with built-in judges

Custom scorer functions can be used alongside [Built-in LLM Judges](/concepts/built-in-llm-judges.md) in the same monitoring schedule. This allows teams to combine general-purpose quality checks (e.g., toxicity, relevance) with domain-specific evaluations. ^[code-based-scorers-databricks-on-aws.md]

## Limitations

- **No class-based scorers**: Only `@scorer`-decorated functions are supported. Class-based `Scorer` subclasses cannot be used in production monitoring. ^[code-based-scorers-databricks-on-aws.md]
- **Notebook environment required**: Functions must be defined and registered from a Databricks notebook. Registration from other environments (e.g., local scripts, IDEs) is not supported. ^[code-based-scorers-databricks-on-aws.md]
- **Serialization constraints**: The function code must be serializable for remote execution. Avoid dependencies on local file paths or non-serializable objects. ^[code-based-scorers-databricks-on-aws.md]

## Best practices

- **Keep functions stateless when possible**: If state is needed, manage it within the function body using module-level variables or external storage.
- **Test locally first**: Validate your scorer function in a notebook before registering it for production use.
- **Handle errors gracefully**: Include error handling in your scorer function to prevent evaluation failures from affecting the monitoring pipeline.
- **Document scoring logic**: Clearly document what each scorer evaluates and what the score values mean for downstream consumers.

## Related concepts

- [Built-in LLM Judges](/concepts/built-in-llm-judges.md) — Pre-built evaluators for common quality dimensions
- [Production monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Overview of monitoring GenAI applications in production
- [MLflow monitoring API](/concepts/mlflow-trace-error-monitoring.md) — API for registering and managing scorers
- Production monitoring schedule — Configuration for automated evaluation runs
- Custom Judges (make_judge)|Custom judges using make_judge — Alternative approach for LLM-based evaluation

## Sources

- code-based-scorers-databricks-on-aws.md

# Citations

1. [code-based-scorers-databricks-on-aws.md](/references/code-based-scorers-databricks-on-aws-2a1f1dbe.md)
