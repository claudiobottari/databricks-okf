---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 46be67868c96a828a15f9663099794e92680b3ff64af22517658bb41e2979b29
  pageDirectory: concepts
  sources:
    - guardrails-ai-scorers-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - dynamic-scorer-creation-with-get_scorer
    - DSCWG
  citations:
    - file: guardrails-ai-scorers-databricks-on-aws.md
title: Dynamic Scorer Creation with get_scorer
description: A method to dynamically create Guardrails AI scorers at runtime by passing the validator name as a string to the get_scorer function.
tags:
  - mlflow
  - scorer-creation
  - dynamic-configuration
timestamp: "2026-06-19T19:02:56.450Z"
---

# Dynamic Scorer Creation with `get_scorer`

**Dynamic Scorer Creation with `get_scorer`** refers to the ability to instantiate Guardrails AI scorer objects at runtime by passing the validator name as a string argument to the `get_scorer` function. This approach enables flexible, configuration-driven validation workflows within the MLflow GenAI evaluation framework.

## Overview

The `get_scorer` function is available from `mlflow.genai.scorers.guardrails`. It allows developers to create scorer instances programmatically based on a string validator name, rather than requiring an upfront import of a specific scorer class. This is particularly useful when the set of validators to apply is determined at runtime (e.g., from a configuration file or user input). ^[guardrails-ai-scorers-databricks-on-aws.md]

## Guardrails AI Implementation

To dynamically create a Guardrails AI scorer, import `get_scorer` and pass the `validator_name` parameter along with any validator-specific keyword arguments:

```python
from mlflow.genai.scorers.guardrails import get_scorer

scorer = get_scorer(
    validator_name="ToxicLanguage",
    threshold=0.7,
)

feedback = scorer(
    outputs="This is a professional response.",
)
```

^[guardrails-ai-scorers-databricks-on-aws.md]

The function accepts any keyword arguments that the corresponding Guardrails validator constructor accepts. For example, `DetectPII` can be configured with `pii_entities`, and `DetectJailbreak` with `threshold`. ^[guardrails-ai-scorers-databricks-on-aws.md]

## Use Cases

Using `get_scorer` is valuable when:

- Validation criteria are stored in external configuration files (e.g., YAML or JSON) and need to be instantiated dynamically.
- Evaluation pipelines are parameterized to accept validator names as arguments, enabling reusable templates.
- Users or external systems select which validators to apply at evaluation time through a UI or API.

(These use cases are inferred from the dynamic creation pattern; the source material directly describes only the mechanism.)

## Related Concepts

- Guardrails AI scorers — The full set of rule-based validators available for LLM output validation.
- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) — The broader framework for evaluating generative AI models.
- Scorer Configuration — How to parameterize scorers through constructor arguments.

## Sources

- guardrails-ai-scorers-databricks-on-aws.md

# Citations

1. [guardrails-ai-scorers-databricks-on-aws.md](/references/guardrails-ai-scorers-databricks-on-aws-14c3c865.md)
