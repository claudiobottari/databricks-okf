---
title: Manual tracing | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow3/genai/tracing/app-instrumentation/manual-tracing/
ingestedAt: "2026-06-18T08:16:32.094Z"
---

While MLflow's [automatic tracing](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/app-instrumentation/automatic) provides instant observability for supported frameworks, manual tracing gives you complete control over how your GenAI applications are instrumented. This flexibility is essential for building production-ready applications that require detailed monitoring and debugging capabilities.

## When to use manual tracing[​](#when-to-use-manual-tracing "Direct link to When to use manual tracing")

Manual tracing is the right choice when you need:

Fine-grained control over trace structure

*   Define exactly which parts of your code to trace
*   Create custom hierarchies of spans
*   Control span boundaries and relationships

Custom framework instrumentation

*   Instrument proprietary or internal frameworks
*   Add tracing to custom LLM wrappers
*   Support new libraries before official integration

Advanced workflow scenarios

*   Multi-threaded or async operations
*   Streaming responses with custom aggregation
*   Complex nested operations
*   Custom trace metadata and attributes

## Which API should I use?[​](#which-api-should-i-use "Direct link to Which API should I use?")

Choose the right manual tracing approach for your needs:
