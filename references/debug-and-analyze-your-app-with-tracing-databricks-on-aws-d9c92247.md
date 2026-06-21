---
title: Debug and analyze your app with tracing | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow3/genai/tracing/observe-with-traces/
ingestedAt: "2026-06-18T08:17:51.336Z"
---

MLflow Tracing provides deep insights into your application's behavior, facilitating a complete debugging experience across different environments. By capturing the complete request-response cycle (Input/Output Tracking) and the execution flow, you can visualize and understand your application's logic and decision-making process.

Examining the inputs, outputs, and metadata for each intermediate step (for example, retrieval, tool calls, LLM interactions) and associated [user feedback](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/collect-user-feedback/) or the results of [quality evaluations](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/) allows you to:

*   **In Development**: Get detailed visibility into what happens beneath the abstractions of GenAI libraries, helping you precisely identify where issues or unexpected behaviors occur.
*   **In Production**: Monitor and debug issues in real-time. Traces capture errors and can include operational metrics like latency at each step, aiding in quick diagnostics.

MLflow Tracing offers a unified experience between development and production: you instrument your application once, and tracing works consistently in both environments. This allows you to navigate traces seamlessly within your preferred environment—be it your IDE, notebook, or production monitoring dashboard—eliminating the hassle of switching between multiple tools or searching through overwhelming logs.

![Tracing Error Screenshot](https://docs.databricks.com/aws/en/assets/images/tracing-error-efd99abec05dbc9cb49d1332f241c620.png)

## Monitor performance and optimize costs[​](#monitor-performance-and-optimize-costs "Direct link to Monitor performance and optimize costs")

Understanding and optimizing the performance and cost of your GenAI applications is crucial. MLflow Tracing enables you to capture and monitor key operational metrics such as latency, cost, and resource utilization at each step of your application's execution.

This allows you to:

*   Track and identify performance bottlenecks within complex pipelines.
*   Monitor resource utilization to ensure efficient operation.
*   Optimize cost efficiency by understanding where resources or tokens are consumed.
*   Identify areas for performance improvement in your code or model interactions.

Furthermore, MLflow Tracing is compatible with **OpenTelemetry**, an industry-standard observability specification. This compatibility allows you to export your trace data to various services in your existing observability stack. See [OpenTelemetry Export](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/integrations/open-telemetry) for more details.

## Analyze traces with Genie Code[​](#analyze-traces-with-genie-code "Direct link to Analyze traces with Genie Code")

Genie Code provides a natural language interface for exploring and debugging your traces. Instead of writing queries or navigating multiple UI pages, you can ask questions like "Are there any error traces in this experiment?" or "What's the P95 latency for my traces?" and get immediate answers.

Genie Code has read access to your traces, sessions, evaluation runs, scorers, datasets, labeling sessions, and more — so you can go from a high-level question to a root cause analysis in a single conversation.

See [Genie Code for agent observability and evaluation](https://docs.databricks.com/aws/en/mlflow3/genai/getting-started/genie-code) for the full list of capabilities and example questions.
