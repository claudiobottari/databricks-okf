---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 62bb72d5f022607d38b875412cbb5e2065163eb85ab964287c39eddff3ee6500
  pageDirectory: concepts
  sources:
    - debug-and-analyze-your-app-with-tracing-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - genie-code-for-trace-analysis
    - GCFTA
  citations:
    - file: debug-and-analyze-your-app-with-tracing-databricks-on-aws.md
title: Genie Code for Trace Analysis
description: A natural language interface that allows users to query, explore, and debug traces using plain English questions instead of writing queries or navigating UI pages.
tags:
  - observability
  - natural-language-interface
  - debugging
timestamp: "2026-06-19T18:16:35.586Z"
---

```markdown
---
title: Genie Code for Trace Analysis
summary: A natural language interface within [[mlflow-tracing|MLflow Tracing]] that lets you debug and analyze traces by asking plain‑language questions about errors, latency, cost, and more.
sources:
  - debug-and-analyze-your-app-with-tracing-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:42:57.598Z"
updatedAt: "2026-06-18T15:11:04.221Z"
tags:
  - natural-language
  - debugging
  - genai
  - observability
aliases:
  - genie-code-for-trace-analysis
  - GCFTA
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# Genie Code for Trace Analysis

**Genie Code for Trace Analysis** is a natural language interface integrated with [[MLflow Tracing]] that enables you to explore and debug traces without writing queries or navigating multiple UI pages. By asking questions in plain English, you can move from a high‑level observation to a root‑cause analysis in a single conversation.^[debug-and-analyze-your-app-with-tracing-databricks-on-aws.md]

## Overview

[[mlflow-tracing|MLflow Tracing]] captures the complete request‑response cycle of a [[MLflow GenAI Evaluate API|GenAI]] application, including the inputs, outputs, and metadata of every intermediate step (for example, retrieval, tool calls, and LLM interactions). Genie Code has read access to these traces as well as to related artifacts such as sessions, evaluation runs, scorers, datasets, and labeling sessions. This means you can ask questions that span both trace observations and the results of quality evaluations or user feedback.^[debug-and-analyze-your-app-with-tracing-databricks-on-aws.md]

## Capabilities

You can use Genie Code to perform a wide variety of analysis tasks. The following table gives representative examples:

| Goal | Example question |
|------|------------------|
| **Error detection** | “Are there any error traces in this experiment?” |
| **Performance analysis** | “What's the P95 latency for my traces?” |
| **Cost optimisation** | “Where are most tokens consumed in my pipeline?” |
| **Resource utilisation** | “Which steps show high resource usage?” |
| **Root‑cause investigation** | “Why did this trace fail?” |

These capabilities apply both in development (where you gain detailed visibility into the behaviour of GenAI libraries) and in production (where you can monitor and debug issues in real time).^[debug-and-analyze-your-app-with-tracing-databricks-on-aws.md]

## How it works

You instrument your application once using [[mlflow-tracing|MLflow Tracing]], and the same trace data is available to Genie Code in your IDE, notebook, or production monitoring dashboard. There is no need to switch between tools or search through logs.^[debug-and-analyze-your-app-with-tracing-databricks-on-aws.md]

For the complete list of capabilities and example questions, see the dedicated Genie Code for agent observability and evaluation documentation.

## Related Concepts

- [[MLflow Tracing]] — The underlying trace‑capture framework.
- GenAI Application Observability — Broader observability for GenAI systems.
- [[MLflow OpenTelemetry Metrics Export|OpenTelemetry Export]] — Exporting traces to industry‑standard observability backends.
- [[End-User Feedback Collection via SDK|User Feedback Collection]] — Capturing human feedback on trace outputs.
- Quality Evaluation — Evaluating trace results with scorers and judges.

## Sources

- debug-and-analyze-your-app-with-tracing-databricks-on-aws.md
```

# Citations

1. [debug-and-analyze-your-app-with-tracing-databricks-on-aws.md](/references/debug-and-analyze-your-app-with-tracing-databricks-on-aws-d9c92247.md)
