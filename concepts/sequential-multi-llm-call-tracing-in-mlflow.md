---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4204f89fcf5fca70e97ce44cb387e4c1336e12406c65e334c0c1cd76973e1c94
  pageDirectory: concepts
  sources:
    - automatic-tracing-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sequential-multi-llm-call-tracing-in-mlflow
    - SMCTIM
  citations:
    - file: automatic-tracing-databricks-on-aws.md
title: Sequential Multi-LLM Call Tracing in MLflow
description: Tracing workflows that make multiple sequential LLM calls (e.g., analysis followed by response generation) within a single traced function.
tags:
  - mlflow
  - tracing
  - workflow
timestamp: "2026-06-19T09:06:18.611Z"
---

# Sequential Multi-LLM Call Tracing in MLflow

**Sequential Multi-LLM Call Tracing in MLflow** refers to the ability to capture and visualize a chain of successive large language model (LLM) invocations within a single trace. This pattern is common in AI agents that decompose a task into steps — for example, analyzing a query first and then generating a response based on that analysis. MLflow’s tracing infrastructure automatically records each call as a child span under a parent workflow span, giving developers a unified view of the entire sequence. ^[automatic-tracing-databricks-on-aws.md]

## How Automatic Tracing Enables It

MLflow provides automatic tracing for over 20 supported libraries and frameworks, including OpenAI and LangChain. By calling `mlflow.<library>.autolog()`, every LLM call made through that library is automatically captured as a span. When these calls are made sequentially inside a single function, they become nested child spans, forming a coherent trace that shows the order, duration, and inputs/outputs of each step. ^[automatic-tracing-databricks-on-aws.md]

### Multiple Frameworks in One Workflow

You can enable auto-tracing for multiple frameworks simultaneously. For instance, a workflow might make a direct OpenAI API call and then use a LangChain chain. When both `mlflow.openai.autolog()` and `mlflow.langchain.autolog()` are called, the resulting trace includes spans from both libraries, all nested under a single parent span created with [`@mlflow.trace`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.trace). ^[automatic-tracing-databricks-on-aws.md]

## Example: Sequential LLM Calls with OpenAI

The following example shows a function that makes two sequential LLM calls. The first call analyzes the query to decide whether it requires factual or creative writing; the second call generates the response using a different system prompt based on that analysis. MLflow’s automatic tracing creates one trace with a parent span for `process_user_query` and two child spans for the individual OpenAI calls. ^[automatic-tracing-databricks-on-aws.md]

```python
import mlflow
import openai
from mlflow.entities import SpanType

mlflow.openai.autolog()

client = openai.OpenAI()

@mlflow.trace(span_type=SpanType.CHAIN)
def process_user_query(query: str):
    # First LLM call: Analyze the query
    analysis = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Analyze the user's query and determine if it requires factual information or creative writing."},
            {"role": "user", "content": query}
        ]
    )
    analysis_result = analysis.choices[0].message.content

    # Second LLM call: Generate response based on analysis
    if "factual" in analysis_result.lower():
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Provide a factual, well-researched response."},
                {"role": "user", "content": query}
            ]
        )
    else:
        response = client.chat.commpletions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Provide a creative, engaging response."},
                {"role": "user", "content": query}
            ]
        )
    return response.choices[0].message.content

result = process_user_query("Tell me about the history of artificial intelligence")
```

## Combining Manual and Automatic Tracing

For workflows that mix custom logic with LLM calls, you can combine `@mlflow.trace` (manual tracing) with auto-tracing. This allows you to annotate business logic steps (e.g., building messages, parsing responses) as spans while the LLM calls are automatically traced by the integration. The result is a single, unified trace that shows the entire sequence — both custom operations and LLM invocations — in one view. ^[automatic-tracing-databricks-on-aws.md]

## Benefits

- **End-to-end visibility** into multi-step agent behaviors, enabling debugging and optimization of sequential decisions. ^[automatic-tracing-databricks-on-aws.md]
- **Performance monitoring** of each LLM call within the sequence — latency, token usage, and errors are captured per span. ^[automatic-tracing-databricks-on-aws.md]
- **Simplified instrumentation** – a single line (`mlflow.<library>.autolog()`) is enough to trace all LLM calls in the workflow. ^[automatic-tracing-databricks-on-aws.md]

## Related Concepts

- [Automatic Tracing](/concepts/automatic-tracing.md) – Enables capture of LLM calls without manual instrumentation.
- [Manual Tracing](/concepts/manual-tracing.md) – Adding custom spans with `@mlflow.trace` for business logic.
- LangChain Integration – Auto-tracing for LangChain chains and agents.
- OpenAI Integration – Auto-tracing for direct OpenAI API calls.
- Trace Visualization – Viewing and analyzing traces in the MLflow UI.

## Sources

- automatic-tracing-databricks-on-aws.md

# Citations

1. [automatic-tracing-databricks-on-aws.md](/references/automatic-tracing-databricks-on-aws-ff944f8c.md)
