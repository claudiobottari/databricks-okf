---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6a25db2db7654ec65f61ed9f1fd85b552fcabb987665e291761caf28a5fdbf27
  pageDirectory: concepts
  sources:
    - code-based-scorer-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - scorer-inputs
  citations:
    - file: code-based-scorer-reference-databricks-on-aws.md
title: Scorer inputs
description: "The four optional input parameters available to scorers: inputs, outputs, expectations, and trace from MLflow traces"
tags:
  - mlflow
  - scorers
  - traces
timestamp: "2026-06-18T10:58:20.256Z"
---

# Scorer inputs

**Scorer inputs** are the data arguments that a custom code-based scorer receives when evaluating an AI application's performance. Scorers receive the complete [[MLflow Trace]] containing all spans, attributes, and outputs, and MLflow also extracts commonly needed data and passes it as named arguments. All input arguments are optional, so a scorer should declare only what it needs. ^[code-based-scorer-reference-databricks-on-aws.md]

## Available input arguments

Scorers can receive up to four named input arguments, depending on what the scorer function declares in its signature:

- `inputs`: The request sent to your app (for example, user query, context). This is a dictionary of input argument names and values.
- `outputs`: The response from your app (for example, generated text, tool calls).
- `expectations`: Ground truth or labels (for example, expected response, guidelines). This is a dictionary of label names and values.
- `trace`: The complete MLflow trace including all spans, allowing analysis of intermediate steps, latency, tool usage, and more. The trace is passed to the custom scorer as an instantiated [`mlflow.entities.trace` class](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.Trace).

^[code-based-scorer-reference-databricks-on-aws.md]

## Input availability by context

When running [`mlflow.genai.evaluate()`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.evaluate), the `inputs`, `outputs`, and `expectations` parameters can be specified in the `data` argument, or parsed from the trace. ^[code-based-scorer-reference-databricks-on-aws.md]

For [production quality monitoring](/concepts/production-monitoring.md), registered scorers always parse the `inputs` and `outputs` parameters from the trace. The `expectations` parameter is not available in production monitoring contexts. ^[code-based-scorer-reference-databricks-on-aws.md]

## Scorer function signature

Scorers defined using the `@scorer` decorator receive all arguments as keyword-only parameters. The following example shows the full signature with all optional input arguments declared:

```python
from mlflow.genai.scorers import scorer
from typing import Optional, Any
from mlflow.entities import Feedback

@scorer
def my_custom_scorer(
    *,  # All arguments are keyword-only
    inputs: Optional[dict[str, Any]],       # App's raw input
    outputs: Optional[Any],                 # App's raw output
    expectations: Optional[dict[str, Any]], # Ground truth
    trace: Optional[mlflow.entities.Trace]  # Complete trace
) -> Feedback:
    # Your evaluation logic here
```

^[code-based-scorer-reference-databricks-on-aws.md]

## Best practices

- Declare only the input arguments your scorer actually needs. Unused arguments can be omitted from the function signature. ^[code-based-scorer-reference-databricks-on-aws.md]
- Use the `trace` argument when you need to analyze intermediate steps, latency, tool usage, or other span-level details from the full MLflow trace. ^[code-based-scorer-reference-databricks-on-aws.md]
- For production monitoring, design scorers that rely only on `inputs` and `outputs` parsed from the trace, since `expectations` is not available. ^[code-based-scorer-reference-databricks-on-aws.md]

## Related concepts

- [Code-based Scorers](/concepts/code-based-scorers.md) — The broader framework for defining custom evaluation logic
- [[MLflow Trace]] — The complete execution trace that scorers can analyze
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) — The evaluation framework that invokes scorers
- [Production quality monitoring](/concepts/production-monitoring.md) — Production context where scorer inputs are limited
- [Feedback objects](/concepts/feedback-objects.md) — The rich return type for scorer outputs

## Sources

- code-based-scorer-reference-databricks-on-aws.md

# Citations

1. [code-based-scorer-reference-databricks-on-aws.md](/references/code-based-scorer-reference-databricks-on-aws-b52e32c9.md)
