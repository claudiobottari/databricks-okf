---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8191d0f79afcbd0f920afb9ee8882af9754c241590c6dc94adeb7af3a0dbba24
  pageDirectory: concepts
  sources:
    - answer-and-context-relevance-judges-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - mlflow-trace-requirements-for-llm-judges
    - MTRFLJ
    - trace-span-requirements-for-mlflow-judges
    - TSRFMJ
  citations:
    - file: answer-and-context-relevance-judges-databricks-on-aws.md
    - file: create-a-custom-judge-using-make_judge-databricks-on-aws.md
title: MLflow Trace Requirements for LLM Judges
description: Technical prerequisites for MLflow LLM judges including that inputs and outputs must be on the Trace's root span (for RelevanceToQuery) and that the Trace must contain at least one span with span_type set to RETRIEVER (for RetrievalRelevance).
tags:
  - mlflow
  - tracing
  - llm-evaluation
  - prerequisites
timestamp: "2026-06-19T14:01:29.712Z"
---

# MLflow Trace Requirements for LLM Judges

**MLflow Trace Requirements for LLM Judges** defines the minimum [[MLflow Trace]] data that must be present for built-in and custom LLM judges to successfully evaluate GenAI agent outputs. These requirements ensure that judges have access to the inputs, outputs, and intermediate execution steps needed to compute quality scores.

## Overview

LLM judges in MLflow evaluate [GenAI evaluation](/concepts/mlflow-genai-evaluation.md) quality by analyzing traces—structured records of an application's execution. Different judges require different trace components. Understanding these requirements is essential for building evaluable applications and debugging evaluation failures. ^[answer-and-context-relevance-judges-databricks-on-aws.md]

## Input/Output Requirements for Built-in Judges

### `RelevanceToQuery` Judge

The `RelevanceToQuery` judge evaluates whether an application's response directly addresses the user's input. To function, the MLflow Trace **must** contain `inputs` and `outputs` on the Trace's root span. ^[answer-and-context-relevance-judges-databricks-on-aws.md]

### `RetrievalRelevance` Judge

The `RetrievalRelevance` judge evaluates whether each document returned by the application's retriever is relevant to the input request. To function, the MLflow Trace **must** contain at least one span with `span_type` set to `RETRIEVER`. ^[answer-and-context-relevance-judges-databricks-on-aws.md]

## Trace Requirements for Custom Judges

Custom judges created with `make_judge()` support two evaluation modes, each with distinct trace requirements: ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

### Input/Output Judges

Input/output judges evaluate agent behavior by analyzing conversation history (`inputs`) and agent responses (`outputs`). These judges require the trace to contain `inputs` and `outputs` fields. Common use cases include assessing issue resolution status or adherence to expected behaviors. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

### Trace-Based Judges

Trace-based judges analyze the full execution trace of an agent call, including tool invocations, intermediate reasoning steps, and their results. These judges require the `{{ trace }}` placeholder in the judge instructions and are specified by including `{{ trace }}` in the instructions string passed to `make_judge()`. Trace-based judges require a model specification (e.g., `model="databricks:/databricks-gpt-5-mini"`). ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

Example of a trace-based judge:

```python
tool_call_judge = make_judge(
    name="tool_call_correctness",
    instructions=(
        "Analyze the execution {{ trace }} to determine if the agent "
        "called appropriate tools for the user's request."
    ),
    feedback_value_type=bool,
    model="databricks:/databricks-gpt-5-mini",
)
```

## Common Trace Gaps and Troubleshooting

### Missing Root Span Fields

If the trace's root span lacks required fields (`inputs` or `outputs`), the `RelevanceToQuery` judge will fail to evaluate. Ensure your application function properly captures and returns inputs and outputs. ^[answer-and-context-relevance-judges-databricks-on-aws.md]

### Missing [RETRIEVER Spans](/concepts/retriever-spans.md)

For `RetrievalRelevance` to work, a span with `span_type="RETRIEVER"` must exist in the trace. If your retriever function is not decorated with `@mlflow.trace(span_type="RETRIEVER")`, the judge cannot find the retrieved documents. ^[answer-and-context-relevance-judges-databricks-on-aws.md]

### Model Specification for Trace Judges

Trace-based custom judges require an explicit `model` parameter. If omitted, evaluation will fail. The model must be specified in the format `<provider>:/<model-name>`. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Related Concepts

- [Custom Judges](/concepts/custom-judges.md) — Creating LLM-based evaluators with `make_judge()`
- [Built-in LLM Judges](/concepts/built-in-llm-judges.md) — Pre-configured judges for relevance, groundedness, safety, and correctness
- [MLflow Tracing API](/concepts/mlflow-tracing.md) — The `@mlflow.trace` decorator and span configuration
- [GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) — The `mlflow.genai.evaluate()` API for running judges against datasets
- [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) — Using judges to compare agent variants

## Sources

- answer-and-context-relevance-judges-databricks-on-aws.md
- create-a-custom-judge-using-make_judge-databricks-on-aws.md

# Citations

1. [answer-and-context-relevance-judges-databricks-on-aws.md](/references/answer-and-context-relevance-judges-databricks-on-aws-5f3620ab.md)
2. [create-a-custom-judge-using-make_judge-databricks-on-aws.md](/references/create-a-custom-judge-using-make_judge-databricks-on-aws-956237bf.md)
