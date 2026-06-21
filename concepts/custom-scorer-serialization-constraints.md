---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e808327892efd0cac882f78bab60844157f09e872056ae30f976782121a5518b
  pageDirectory: concepts
  sources:
    - monitor-genai-apps-in-production-databricks-on-aws.md
  confidence: 0.99
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - custom-scorer-serialization-constraints
    - CSSC
  citations:
    - file: monitor-genai-apps-in-production-databricks-on-aws.md
title: Custom Scorer Serialization Constraints
description: "Constraints for custom @scorer functions in production monitoring: must be defined in notebooks, self-contained with inline imports, no class-based scorers, and no type hints requiring imports."
tags:
  - mlflow
  - serialization
  - scorers
  - constraints
timestamp: "2026-06-19T19:46:50.319Z"
---

# Custom Scorer Serialization Constraints

**Custom Scorer Serialization Constraints** refer to the limitations imposed when defining custom scorer functions for MLflow 3 Production Monitoring. The monitoring service serializes custom scorer code for remote execution, which requires that scorers be self-contained and defined in a notebook environment. ^[monitor-genai-apps-in-production-databricks-on-aws.md]

## Overview

When custom scorers are registered for production monitoring, the monitoring service serializes the scorer function code so it can be executed remotely. This serialization process places several constraints on how custom scorers can be defined. Violating these constraints leads to serialization failures and prevents the scorer from being registered. ^[monitor-genai-apps-in-production-databricks-on-aws.md]

## Constraints

### Notebook Requirement
Custom `@scorer` functions must be defined and registered from a Databricks notebook. The serialization mechanism relies on the notebook environment to capture and serialize the function code. Scorers defined in standalone Python files or local IDE environments cannot be serialized for production monitoring. ^[monitor-genai-apps-in-production-databricks-on-aws.md]

### Self-Contained Functions
All imports must be included inline within the function body. The function cannot reference variables, objects, or modules defined outside of it. References to external definitions are not captured during serialization. ^[monitor-genai-apps-in-production-databricks-on-aws.md]

The following example shows the correct and incorrect approaches:

```python
# Incorrect: external dependency outside function
import external_library  # Outside function
@scorer
def bad_scorer(outputs):
    return external_library.process(outputs)

# Correct: imports inside the function body
@scorer
def good_scorer(outputs):
    import json  # Inside function
    return len(json.dumps(outputs))
```

^[monitor-genai-apps-in-production-databricks-on-aws.md]

### No Class-Based Scorers
Only `@scorer` decorator-based scorers can be registered for production monitoring. Class-based `Scorer` subclasses cannot be serialized for remote execution. If you need a class-based scorer, you must refactor it to use the `@scorer` decorator instead. ^[monitor-genai-apps-in-production-databricks-on-aws.md]

### No Type Hints Requiring Imports
Type hints in the function signature that require import statements (for example, `List` from `typing`) cause serialization failures. Avoid using type hints that need imports in the scorer function signature. ^[monitor-genai-apps-in-production-databricks-on-aws.md]

```python
# Incorrect: type hint requiring import
from typing import List
@scorer
def scorer_with_bad_types(outputs: List[str]):
    return False
```

^[monitor-genai-apps-in-production-databricks-on-aws.md]

## Packages Available Without Inline Import

Some packages are available by default and do not need inline imports. These include `databricks-agents`, `mlflow-skinny`, `openai`, and all packages included in Serverless environment version 2. ^[monitor-genai-apps-in-production-databricks-on-aws.md]

## Best Practices for Custom Scorer Design

Keep custom scorers self-contained by following these practices:

- Include all imports inside the function body using inline import statements.
- Handle missing data gracefully using methods like `outputs.get("response", "")`.
- Return consistent data types to avoid evaluation errors.

```python
@scorer
def well_designed_scorer(inputs, outputs):
    # All imports inside the function
    import re
    import json
    # Handle missing data gracefully
    response = outputs.get("response", "")
    if not response:
        return 0.0
    # Return consistent types
    return float(len(response) > 100)
```

^[monitor-genai-apps-in-production-databricks-on-aws.md]

## Related Concepts

- Production Monitoring Scorer Lifecycle — Managing the lifecycle of registered scorers.
- [Code-based Scorers](/concepts/code-based-scorers.md) — Building self-contained scorer functions.
- [Scorers and LLM Judges](/concepts/scorers-and-llm-judges.md) — The metrics that power production monitoring.
- [Scorer Sampling Configuration](/concepts/scorer-sampling-configuration.md) — Controlling which traces a scorer evaluates.

## Sources

- monitor-genai-apps-in-production-databricks-on-aws.md

# Citations

1. [monitor-genai-apps-in-production-databricks-on-aws.md](/references/monitor-genai-apps-in-production-databricks-on-aws-41428693.md)
