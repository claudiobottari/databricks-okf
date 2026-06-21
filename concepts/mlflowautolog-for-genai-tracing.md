---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 74dfcc61bd6b383b9395ee8f40734d3695adaf96590d9020a9d4a304b03f6d32
  pageDirectory: concepts
  sources:
    - automatic-tracing-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflowautolog-for-genai-tracing
    - MFGT
  citations:
    - file: automatic-tracing-databricks-on-aws.md
title: mlflow.autolog() for GenAI Tracing
description: One-line automatic tracing for generative AI applications using mlflow.<library>.autolog(), supporting 20+ libraries and frameworks out of the box.
tags:
  - mlflow
  - tracing
  - generative-ai
  - instrumentation
timestamp: "2026-06-19T17:37:54.069Z"
---

## mlflow.autolog() for GenAI Tracing

`mlflow.autolog()` for GenAI Tracing is a one-line instrumentation method that enables automatic trace collection for generative AI applications built with 20+ supported libraries and frameworks. By calling `mlflow.<library>.autolog()` (e.g., `mlflow.openai.autolog()`), MLflow records spans for every call made through that library without requiring any further code changes. ^[automatic-tracing-databricks-on-aws.md]

### Prerequisites

Databricks recommends using MLflow 3 for the latest GenAI tracing capabilities. The core requirement is `mlflow[databricks]>=3.1`. For a specific integration such as OpenAI, the appropriate SDK must also be installed (e.g., `openai>=1.0.0`). On **serverless compute clusters**, autologging for GenAI tracing frameworks is not automatically enabled — you must explicitly call the relevant `mlflow.<library>.autolog()` function for the integrations you want to trace. ^[automatic-tracing-databricks-on-aws.md]

LLM API keys (e.g., `OPENAI_API_KEY`) must be set as environment variables. For Databricks Foundation Model APIs, the Databricks token and host must be configured. ^[automatic-tracing-databricks-on-aws.md]

### Basic Automatic Tracing Example

After installing dependencies and setting credentials, enable auto-tracing for a library (e.g., OpenAI) and then use the library normally. MLflow automatically generates a trace for each API call. The following example traces calls to Databricks Foundation Model APIs via an OpenAI client:

```python
import mlflow
import os
from openai import OpenAI

mlflow.set_tracking_uri("databricks")
mlflow.set_experiment("/Shared/databricks-sdk-autolog-example")

mlflow.openai.autolog()

client = OpenAI(
    api_key=os.environ.get("DATABRICKS_TOKEN"),
    base_url=f"{os.environ.get('DATABRICKS_HOST')}/serving-endpoints"
)

response = client.chat.completions.create(
    model="databricks-llama-4-maverick",
    messages=[...],
    max_tokens=150,
    temperature=0.7
)
print(response.choices[0].message.content)
```

Every call to the Databricks Foundation Model API is automatically traced. ^[automatic-tracing-databricks-on-aws.md]

### Auto-Tracing Multiple Frameworks

You can enable auto-tracing for several frameworks in the same agent by calling each library’s `autolog()` method. For example, `mlflow.openai.autolog()` and `mlflow.langchain.autolog()` can both be active, combining direct OpenAI calls, LangChain chains, and custom logic into a single unified trace. ^[automatic-tracing-databricks-on-aws.md]

```python
mlflow.openai.autolog()
mlflow.langchain.autolog()
```

### Combining Manual and Automatic Tracing

The `@mlflow.trace` decorator (with an optional `span_type` argument such as `SpanType.CHAIN`) can be used alongside automatic tracing to capture custom business logic, multi‑LLM workflows, and function calls that sit between instrumented library calls. All spans—both manually created and auto‑traced—are merged into a single trace for debugging and monitoring. ^[automatic-tracing-databricks-on-aws.md]

```python
import mlflow
from mlflow.entities import SpanType

mlflow.openai.autolog()

@mlflow.trace(span_type=SpanType.CHAIN)
def run(question):
    messages = build_messages(question)
    response = client.chat.completions.create(...)
    return parse_response(response)

@mlflow.trace
def build_messages(question): ...

@mlflow.trace
def parse_response(response): ...
```

In this pattern, a parent span (`run`) automatically captures child spans for the OpenAI call (from auto‑tracing) and for the `build_messages` and `parse_response` functions (from the `@mlflow.trace` decorators). ^[automatic-tracing-databricks-on-aws.md]

### Advanced Example: Multiple LLM Calls

Automatic tracing captures every LLM call made within a workflow. For example, a function may first use one OpenAI call to analyze a query and then a second call (possibly with different model parameters) to generate a response. Each call becomes a child span under the parent trace, providing granular visibility. ^[automatic-tracing-databricks-on-aws.md]

```python
@mlflow.trace(span_type=SpanType.CHAIN)
def process_user_query(query: str):
    analysis = client.chat.completions.create(...)
    # ...
    if "factual" in analysis_result.lower():
        response = client.chat.completions.create(model="gpt-4o-mini", ...)
    else:
        response = client.chat.completions.create(model="gpt-4o-mini", ...)
    return response.choices[0].message.content
```

### Related Concepts

- Auto‑Tracing Integrations – Full list of 20+ supported libraries and frameworks.
- [Manual Tracing with Decorators](/concepts/mlflowtrace-decorator.md) – Using `@mlflow.trace` for custom spans.
- [Trace](/concepts/traces.md) – The top‑level record of a request’s execution path.
- Span – A single unit of work within a trace.
- SpanType – Enum used to classify spans (e.g., CHAIN, LLM, PARSER).
- [MLflow Tracing](/concepts/mlflow-tracing.md) – Overview of the GenAI tracing feature.

### Sources

- automatic-tracing-databricks-on-aws.md

# Citations

1. [automatic-tracing-databricks-on-aws.md](/references/automatic-tracing-databricks-on-aws-ff944f8c.md)
