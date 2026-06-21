---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5c5d8c9d3af244254d401b3da95362aaa3c89e2e0be9723dfe446ffa731d1d12
  pageDirectory: concepts
  sources:
    - answer-and-context-relevance-judges-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-trace-requirements-for-judges
    - MTRFJ
    - mlflow-trace-requirements-for-evaluation
    - MTRFE
  citations:
    - file: answer-and-context-relevance-judges-databricks-on-aws.md
    - file: create-a-custom-judge-using-make_judge-databricks-on-aws.md
title: MLflow Trace Requirements for Judges
description: Built-in judges require specific MLflow Trace span data, such as inputs/outputs on the root span for RelevanceToQuery or RETRIEVER-type spans for RetrievalRelevance
tags:
  - mlflow
  - tracing
  - evaluation
timestamp: "2026-06-19T09:00:06.232Z"
---

# MLflow Trace Requirements for Judges

**MLflow Trace Requirements for Judges** defines the specific trace data that must be present in an MLflow Trace for different types of judges to function correctly. Judges — both built-in and custom — rely on trace spans and their attributes to evaluate GenAI application outputs.

## Overview

Judges in MLflow GenAI evaluate the quality of agent responses by analyzing trace data. The specific trace requirements vary depending on the type of judge and what aspect of the application it evaluates. Understanding these requirements is essential for ensuring that judges can access the data they need to produce accurate assessments.^[answer-and-context-relevance-judges-databricks-on-aws.md, create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Trace Requirements for Built-in Judges

### RelevanceToQuery

The `RelevanceToQuery` judge evaluates whether an application's response directly addresses the user's input. This judge requires:

- **Trace requirements**: `inputs` and `outputs` must be present on the Trace's root span.^[answer-and-context-relevance-judges-databricks-on-aws.md]

Without these attributes on the root span, the judge cannot determine what the user asked or what the application responded, and evaluation will fail.

### RetrievalRelevance

The `RetrievalRelevance` judge evaluates whether each document returned by the application's retriever is relevant to the input request. This judge requires:

- **Trace requirements**: The MLflow Trace must contain at least one span with `span_type` set to `RETRIEVER`.^[answer-and-context-relevance-judges-databricks-on-aws.md]

The judge analyzes the documents returned by [RETRIEVER Spans](/concepts/retriever-spans.md) to assess their relevance. If no retriever span exists in the trace, the judge cannot perform its evaluation.

## Trace Requirements for Custom Judges

Custom judges created with `make_judge()` can analyze different parts of the trace depending on how they are configured.

### Input/Output Judges

Input/output judges evaluate the agent's behavior by analyzing conversation history (inputs) and agent responses (outputs). These judges require:

- **Trace requirements**: `inputs` and `outputs` on the root span, similar to the `RelevanceToQuery` built-in judge.^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

### Trace-Based Judges

Trace-based judges analyze the full execution trace of an agent call, including tool invocations, intermediate reasoning steps, and their results. These judges require:

- **Trace requirements**: The trace must contain spans for all tool calls and intermediate steps that the judge needs to evaluate. The judge accesses the trace through the `{{ trace }}` template variable in its instructions.^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

To create a trace-based judge, include `{{ trace }}` in the judge's instructions. This tells MLflow to pass the full trace to the judge for analysis.

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
^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Ensuring Proper Trace Data

To ensure judges have the trace data they need:

1. **Use `@mlflow.trace` decorators** on functions that should be captured in the trace, including retrieval functions, tool calls, and the main application entry point.^[answer-and-context-relevance-judges-databricks-on-aws.md]
2. **Set appropriate `span_type`** on [RETRIEVER Spans](/concepts/retriever-spans.md) using `@mlflow.trace(span_type="RETRIEVER")` to enable `RetrievalRelevance` evaluation.^[answer-and-context-relevance-judges-databricks-on-aws.md]
3. **Ensure root span has inputs and outputs** by tracing the main application function that receives user input and returns a response.^[answer-and-context-relevance-judges-databricks-on-aws.md]
4. **Include all relevant spans** for trace-based judges — any tool call or intermediate step that the judge should analyze must be captured in the trace.^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Related Concepts

- [Built-in LLM Judges](/concepts/built-in-llm-judges.md) — Pre-configured judges for common evaluation criteria
- [Custom Judges](/concepts/custom-judges.md) — User-defined judges created with `make_judge()`
- [MLflow Tracing](/concepts/mlflow-tracing.md) — The tracing infrastructure that captures execution data
- [Retrieval Relevance Judge](/concepts/retrievalrelevance.md) — Judge that evaluates document relevance
- [Relevance to Query Judge](/concepts/relevancetoquery.md) — Judge that evaluates response relevance
- [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) — Using judges to compare agent variants

## Sources

- answer-and-context-relevance-judges-databricks-on-aws.md
- create-a-custom-judge-using-make_judge-databricks-on-aws.md

# Citations

1. [answer-and-context-relevance-judges-databricks-on-aws.md](/references/answer-and-context-relevance-judges-databricks-on-aws-5f3620ab.md)
2. [create-a-custom-judge-using-make_judge-databricks-on-aws.md](/references/create-a-custom-judge-using-make_judge-databricks-on-aws-956237bf.md)
