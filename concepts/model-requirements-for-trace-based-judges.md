---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9397b0850832dbcda440cb4528f1ee00011c0bda6fd414bf06439c5c7e6157f3
  pageDirectory: concepts
  sources:
    - custom-judges-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-requirements-for-trace-based-judges
    - MRFTJ
  citations:
    - file: custom-judges-databricks-on-aws.md
title: Model Requirements for Trace-based Judges
description: Trace-based judges require a capable model served via Foundation Model APIs, External Model Serving Endpoints, or Custom Model Serving Endpoints, with specific recommended models listed.
tags:
  - mlflow
  - model-serving
  - genai
timestamp: "2026-06-19T18:03:21.493Z"
---

```markdown
---
title: Model Requirements for Trace-based Judges
summary: Trace-based judges require a model capable of trace analysis (recommended: databricks-gpt-5-mini, databricks-gpt-5, databricks-gpt-oss-120b, databricks-claude-opus-4-5) served via Foundation Model APIs, External Model Serving, or Custom Model Serving Endpoints.
sources:
  - custom-judges-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:26:49.157Z"
updatedAt: "2026-06-19T14:39:42.300Z"
tags:
  - mlflow
  - model-serving
  - agent-evaluation
aliases:
  - model-requirements-for-trace-based-judges
  - MRFTJ
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# Model Requirements for Trace-based Judges

**Trace-based judges** are a type of [[Custom Judges|custom LLM judge]] that analyze the full execution trace of a GenAI agent, including tool invocations, intermediate reasoning steps, and their results. These judges require a model capable of trace analysis, served through specific endpoints, and the `model` argument must be specified in `make_judge()`. ^[custom-judges-databricks-on-aws.md]

## Overview

Trace-based judges are created using the `make_judge()` function with `{{ trace }}` as a template variable in the judge's instructions. Unlike standard judges that evaluate only inputs and outputs, trace-based judges autonomously explore execution traces using Model Context Protocol (MCP) tools. This enables them to validate tool usage patterns, identify performance bottlenecks, investigate execution failures, and verify multi-step workflows. ^[custom-judges-databricks-on-aws.md]

The `model` argument must be specified in `make_judge()` for trace-based judges to analyze the full trace. This is a requirement that distinguishes them from input/output judges, which can function without an explicit model specification. ^[custom-judges-databricks-on-aws.md]

## Model Serving Options

The model used by a trace-based judge can be served through any of the following endpoints: ^[custom-judges-databricks-on-aws.md]

| Serving Option | Description |
|----------------|-------------|
| [[Foundation Model APIs]] | Recommended — provides access to Databricks-hosted models |
| External Model Serving Endpoints | For models hosted outside Databricks |
| [[Custom Model Serving Endpoint Support|Custom Model Serving Endpoints]] | For self-deployed models on Databricks |

## Recommended Models

Databricks recommends the following models for use with trace-based judges: ^[custom-judges-databricks-on-aws.md]

| Model Reference | Description |
|-----------------|-------------|
| `databricks:/databricks-gpt-5-mini` | Lightweight model for trace analysis |
| `databricks:/databricks-gpt-5` | Full-capability model for trace analysis |
| `databricks:/databricks-gpt-oss-120b` | Large open-source model variant |
| `databricks:/databricks-claude-opus-4-5` | Claude-powered model for trace analysis |

These models are accessed using the `databricks:/` URI scheme, which routes requests through Databricks' serving infrastructure. ^[custom-judges-databricks-on-aws.md]

## Example Usage

The following example demonstrates creating a trace-based judge with the required model specification: ^[custom-judges-databricks-on-aws.md]

```python
from mlflow.genai.judges import make_judge
from typing import Literal

tool_usage_judge = make_judge(
    name="tool_usage_validator",
    instructions=(
        "Analyze the {{ trace }} to verify correct tool usage.\n\n"
        "Check that the agent selected appropriate tools for the user's request "
        "and called them with correct parameters."
    ),
    feedback_value_type=Literal["correct", "incorrect"],
    model="databricks:/databricks-gpt-5-mini"  # Required for trace-based judges
)
```

## Requirements Summary

To create a trace-based judge, you must: ^[custom-judges-databricks-on-aws.md]

1. Include `{{ trace }}` as a template variable in the judge's instructions.
2. Specify the `model` argument in `make_judge()` with a reference to a model capable of trace analysis.
3. Ensure the model is accessible through one of the supported serving endpoints (Foundation Model APIs, External Model Serving Endpoints, or Custom Model Serving Endpoints).
4. Choose a model from the recommended list or an equivalent model with sufficient capability for trace analysis.

## Limitations

Trace-based judges cannot use custom template variables. Only `{{ trace }}` along with the standard variables (`{{ inputs }}`, `{{ outputs }}`, `{{ expectations }}`) are allowed. Custom variables like `{{ question }}` will throw validation errors. ^[custom-judges-databricks-on-aws.md]

## Related Concepts

- [[Custom Judges]] — LLM-based scorers for GenAI evaluation
- make_judge()|Make Judge API — The `make_judge()` function for creating custom evaluators
- [[A/B Comparison of Agent Configurations]] — Using judges to compare agent variants
- [[Production Quality Monitoring (MLflow GenAI)|Production Monitoring for GenAI]] — Deploying judges for continuous quality monitoring
- [[MLflow Evaluation UI|MLflow Evaluation]] — The `mlflow.genai.evaluate()` API for offline assessment
- [[Foundation Model APIs]] — Databricks-hosted model serving

## Sources

- custom-judges-databricks-on-aws.md
```

# Citations

1. [custom-judges-databricks-on-aws.md](/references/custom-judges-databricks-on-aws-7a56fe4f.md)
