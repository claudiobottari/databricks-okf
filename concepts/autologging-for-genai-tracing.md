---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3d8de2ea2cb8831e66ca8d4eee063cb5cc34655d3311cabddfed75e1c7d9fdcd
  pageDirectory: concepts
  sources:
    - automatic-tracing-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - autologging-for-genai-tracing
    - AFGT
    - mlflow-autolog-for-genai-tracing
    - MAFGT
    - mlflowautolog-for-genai-tracing
    - MFGT
    - mlflowautolog-for-generative-ai-tracing
    - MFGAT
  citations:
    - file: automatic-tracing-databricks-on-aws.md
title: Autologging for GenAI Tracing
description: One-line code pattern using mlflow.<library>.autolog() to automatically instrument and trace 20+ supported AI libraries and frameworks without manual instrumentation.
tags:
  - mlflow
  - tracing
  - genai
  - observability
timestamp: "2026-06-18T10:50:22.733Z"
---

# Autologging for GenAI Tracing

**Autologging for GenAI Tracing** is a feature of [MLflow](/concepts/mlflow.md) that automatically generates traces for generative AI applications with a single line of code: `mlflow.<library>.autolog()`. It works out of the box with over 20 supported libraries and frameworks, including OpenAI, LangChain, Anthropic, and Mistral.^[automatic-tracing-databricks-on-aws.md]

On serverless compute clusters, autologging for GenAI tracing frameworks is **not** automatically enabled. You must explicitly enable it by calling the appropriate `mlflow.<library>.autolog()` function for the specific integrations you want to trace.^[automatic-tracing-databricks-on-aws.md]

## Prerequisites

Databricks recommends using MLflow 3 for the latest GenAI tracing capabilities. Install the core MLflow package along with the integration package for your chosen framework. For example, for OpenAI:^[automatic-tracing-databricks-on-aws.md]

```python
%pip install --upgrade "mlflow[databricks]>=3.1" openai>=1.0.0
dbutils.library.restartPython()
```

Then configure any necessary LLM API keys as environment variables:^[automatic-tracing-databricks-on-aws.md]

```python
import os
os.environ["OPENAI_API_KEY"] = "your-api-key"
```

## Basic automatic tracing example

The following example enables automatic tracing for OpenAI calls—in this case against Databricks Foundation Model APIs—and logs them to an MLflow experiment:^[automatic-tracing-databricks-on-aws.md]

```python
import mlflow
from openai import OpenAI

mlflow.set_tracking_uri("databricks")
mlflow.set_experiment("/Shared/databricks-sdk-autolog-example")
mlflow.openai.autolog()

client = OpenAI(api_key=..., base_url=f"{DATABRICKS_HOST}/serving-endpoints")
response = client.chat.completions.create(
    model="databricks-llama-4-maverick",
    messages=[{"role": "user", "content": "What are the key features of [[mlflow-tracing|MLflow Tracing]]?"}]
)
```

After running this code, the call to the Foundation Model API is automatically traced.^[automatic-tracing-databricks-on-aws.md]

## Auto-tracing multiple frameworks

You can enable auto-tracing for several frameworks in the same agent. The example below combines direct OpenAI API calls, LangChain chains, and a custom function into a single trace:^[automatic-tracing-databricks-on-aws.md]

```python
mlflow.openai.autolog()
mlflow.langchain.autolog()

@mlflow.trace(span_type=SpanType.CHAIN)
def multi_provider_workflow(query: str):
    # First, use OpenAI directly
    analysis = client.chat.completions.create(...)
    # Then use LangChain
    chain = prompt | llm
    response = chain.invoke(...)
    return response
```

## Combining manual and automatic tracing

Use the `@mlflow.trace` decorator together with auto-tracing to add custom spans that capture business logic between LLM calls. This creates a unified trace that includes automatically generated spans from the framework and manually defined spans from your functions:^[automatic-tracing-databricks-on-aws.md]

```python
mlflow.openai.autolog()

@mlflow.trace(span_type=SpanType.CHAIN)
def run(question):
    messages = build_messages(question)
    response = client.chat.completions.create(model="gpt-4o-mini", messages=messages)
    return parse_response(response)

@mlflow.trace
def build_messages(question):
    return [{"role": "system", "content": "..."}, {"role": "user", "content": question}]

@mlflow.trace
def parse_response(response):
    return response.choices[0].message.content
```

This pattern is useful for scenarios involving multiple LLM calls in a single workflow, multi-agent systems with different providers, or custom logic interleaved with LLM invocations.^[automatic-tracing-databricks-on-aws.md]

## Advanced example: multiple LLM calls

Automatic tracing captures every LLM call made within a traced workflow. The following example shows a two-step decision process where the first call’s output determines which second call to make:^[automatic-tracing-databricks-on-aws.md]

```python
@mlflow.trace(span_type=SpanType.CHAIN)
def process_user_query(query: str):
    analysis = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": "Determine if factual or creative."}, {"role": "user", "content": query}]
    )
    if "factual" in analysis.choices[0].message.content.lower():
        response = client.chat.completions.create(model="gpt-4o-mini", ...)
    else:
        response = client.chat.completions.create(model="gpt-4o-mini", ...)
    return response.choices[0].message.content
```

This creates a trace with one parent span (`process_user_query`) and two child spans (the two OpenAI calls).^[automatic-tracing-databricks-on-aws.md]

## Related concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The underlying tracing infrastructure
- [MLflow Autologging](/concepts/mlflow-autologging.md) — The general autologging mechanism for ML models
- [GenAI Tracing](/concepts/mlflow-genai-tracing.md) — Tracing for generative AI applications
- [Databricks Foundation Model APIs](/concepts/databricks-foundation-model-apis.md) — Hosted model endpoints that can be traced
- [Manual Tracing](/concepts/manual-tracing.md) — Adding custom spans with `@mlflow.trace`
- Span Type — Categorization of spans (e.g., `CHAIN`, `LLM`, `TOOL`)
- LangChain — One of the supported frameworks
- OpenAI — One of the supported frameworks

## Sources

- automatic-tracing-databricks-on-aws.md

# Citations

1. [automatic-tracing-databricks-on-aws.md](/references/automatic-tracing-databricks-on-aws-ff944f8c.md)
