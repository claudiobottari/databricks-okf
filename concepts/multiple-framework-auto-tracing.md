---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 98a0094d31b251b9998e3303843cea99b3ea3a8a865fbe57c5e4ba1695a03a15
  pageDirectory: concepts
  sources:
    - automatic-tracing-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - multiple-framework-auto-tracing
    - MFA
  citations:
    - file: automatic-tracing-databricks-on-aws.md
      start: 55
      end: 78
    - file: automatic-tracing-databricks-on-aws.md
      start: 8
      end: 13
    - file: 55-63
    - file: automatic-tracing-databricks-on-aws.md
      start: 28
      end: 34
    - file: automatic-tracing-databricks-on-aws.md
      start: 65
      end: 78
    - file: automatic-tracing-databricks-on-aws.md
      start: 71
      end: 78
    - file: automatic-tracing-databricks-on-aws.md
      start: 80
      end: 85
    - file: automatic-tracing-databricks-on-aws.md
      start: 88
      end: 117
    - file: automatic-tracing-databricks-on-aws.md
      start: 119
      end: 121
    - file: automatic-tracing-databricks-on-aws.md
      start: 131
      end: 157
    - file: automatic-tracing-databricks-on-aws.md
      start: 158
      end: 159
title: Multiple Framework Auto-Tracing
description: Pattern enabling simultaneous automatic tracing of multiple AI frameworks (e.g., OpenAI and LangChain) in a single agent workflow to produce unified, debuggable traces.
tags:
  - mlflow
  - tracing
  - multi-framework
  - observability
timestamp: "2026-06-18T10:50:31.475Z"
---

# Multiple Framework Auto-Tracing

**Multiple framework auto-tracing** refers to the practice of enabling [MLflow](/concepts/mlflow.md) automatic tracing for two or more supported generative AI frameworks or libraries in the same application or agent. By calling separate `mlflow.<library>.autolog()` functions, you can instrument calls to different LLM providers (e.g., OpenAI, Anthropic), orchestration layers (e.g., LangChain, LlamaIndex), and custom logic within a single trace, producing a unified view of the entire workflow.^[automatic-tracing-databricks-on-aws.md:55-78]

## Prerequisites

Databricks recommends MLflow 3 for the latest GenAI tracing capabilities. You must install the core MLflow package and any integration-specific libraries you plan to trace. For multi-framework usage, install the packages for each framework you intend to auto-trace. The following example installs both the OpenAI SDK and LangChain:

```python
%pip install --upgrade "mlflow[databricks]>=3.1" openai>=1.0.0 langchain langchain-openai
dbutils.library.restartPython()
```

^[automatic-tracing-databricks-on-aws.md:8-13, 55-63]

After installation, configure any necessary LLM API credentials – for example, setting `OPENAI_API_KEY` or `ANTHROPIC_API_KEY` as environment variables. In a Databricks notebook this is done directly; in external environments you can use secrets or environment variables.^[automatic-tracing-databricks-on-aws.md:28-34]

## Enabling auto-tracing for multiple frameworks

Once the required libraries are installed, you can enable auto-tracing for each framework independently. For example, to trace both direct OpenAI API calls and LangChain chains in the same Python process:

```python
import mlflow
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

mlflow.openai.autolog()
mlflow.langchain.autolog()

# ... subsequent calls to OpenAI and LangChain are automatically traced
```

^[automatic-tracing-databricks-on-aws.md:65-78]

After calling `autolog()`, every invocation of the instrumented library (e.g., `client.chat.completions.create()` for OpenAI, `chain.invoke()` for LangChain) will be captured as spans in an [[MLflow Trace]]. The trace preserves the parent–child relationships between the orchestration layer and lower-level provider calls.^[automatic-tracing-databricks-on-aws.md:71-78]

## Combining manual and automatic tracing

You can augment automatic tracing with [Manual Tracing](/concepts/manual-tracing.md) using the `@mlflow.trace` decorator. This is useful for capturing business logic that sits between framework calls – for example, preprocessing input, post-processing output, or routing decisions. The manual spans are automatically nested inside the same trace alongside auto-generated spans.^[automatic-tracing-databricks-on-aws.md:80-85]

The following example uses `@mlflow.trace` on helper functions while auto-tracing OpenAI calls:

```python
import mlflow
from mlflow.entities import SpanType

mlflow.openai.autolog()

@mlflow.trace(span_type=SpanType.CHAIN)
def process_user_query(query):
    analysis = build_analysis(query)
    response = client.chat.completions.create(...)   # auto-traced
    return parse_response(response)

@mlflow.trace
def build_analysis(query): ...

@mlflow.trace
def parse_response(response): ...
```

^[automatic-tracing-databricks-on-aws.md:88-117]

The resulting trace contains both manual spans (e.g., `build_analysis`, `parse_response`) and auto-generated spans for each OpenAI call, all under a single root span. This pattern is especially useful in multi-agent systems or when you need to add custom annotations without losing visibility into framework internals.^[automatic-tracing-databricks-on-aws.md:119-121]

## Advanced example: multiple LLM calls in a workflow

When automatic tracing is enabled for a framework, each call to that framework’s API generates a child span. The following example illustrates a workflow that makes two sequential LLM calls – one for analysis, one for response generation – and captures both within a single trace:

```python
import mlflow
mlflow.openai.autolog()

@mlflow.trace(span_type=SpanType.CHAIN)
def process_user_query(query):
    # First LLM call: analyze query type
    analysis = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": "Analyze the query."},
                  {"role": "user", "content": query}]
    )
    # Second LLM call: generate response based on analysis
    if "factual" in analysis.choices[0].message.content.lower():
        response = client.chat.completions.create(...)
    else:
        response = client.chat.completions.create(...)
    return response.choices[0].message.content
```

^[automatic-tracing-databricks-on-aws.md:131-157]

This creates a trace with a parent span for `process_user_query` and two child spans – one for each OpenAI API call. The same principle applies when mixing frameworks, such as using LangChain for one step and a direct OpenAI call for another.^[automatic-tracing-databricks-on-aws.md:158-159]

## Next steps

- See the [Automatic tracing integrations](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/integrations/) page for the full list of 20+ supported libraries and frameworks.
- Learn how to add [Manual Tracing](/concepts/manual-tracing.md) to capture custom business logic alongside auto-traced calls.

## Related concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md)
- [Automatic Tracing](/concepts/automatic-tracing.md)
- [Manual Tracing](/concepts/manual-tracing.md)
- [MLflow 3](/concepts/mlflow-3.md)
- LangChain
- OpenAI

## Sources

- automatic-tracing-databricks-on-aws.md

# Citations

1. [automatic-tracing-databricks-on-aws.md:55-78](/references/automatic-tracing-databricks-on-aws-ff944f8c.md)
2. [automatic-tracing-databricks-on-aws.md:8-13](/references/automatic-tracing-databricks-on-aws-ff944f8c.md)
3. 55-63
4. [automatic-tracing-databricks-on-aws.md:28-34](/references/automatic-tracing-databricks-on-aws-ff944f8c.md)
5. [automatic-tracing-databricks-on-aws.md:65-78](/references/automatic-tracing-databricks-on-aws-ff944f8c.md)
6. [automatic-tracing-databricks-on-aws.md:71-78](/references/automatic-tracing-databricks-on-aws-ff944f8c.md)
7. [automatic-tracing-databricks-on-aws.md:80-85](/references/automatic-tracing-databricks-on-aws-ff944f8c.md)
8. [automatic-tracing-databricks-on-aws.md:88-117](/references/automatic-tracing-databricks-on-aws-ff944f8c.md)
9. [automatic-tracing-databricks-on-aws.md:119-121](/references/automatic-tracing-databricks-on-aws-ff944f8c.md)
10. [automatic-tracing-databricks-on-aws.md:131-157](/references/automatic-tracing-databricks-on-aws-ff944f8c.md)
11. [automatic-tracing-databricks-on-aws.md:158-159](/references/automatic-tracing-databricks-on-aws-ff944f8c.md)
