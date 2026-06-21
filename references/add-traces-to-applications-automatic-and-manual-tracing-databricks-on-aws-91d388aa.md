---
title: "Add traces to applications: automatic and manual tracing | Databricks on AWS"
source: https://docs.databricks.com/aws/en/mlflow3/genai/tracing/app-instrumentation/
ingestedAt: "2026-06-18T08:16:28.190Z"
---

Learn about the different approaches you can take to add traces to Python and TypeScript generative AI application.

MLflow has three approaches to tracing for Python and [TypeScript](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/app-instrumentation/typescript-sdk).

*   [**Automatic**](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/app-instrumentation/automatic) - Add one line [`mlflow.<library>.autolog()`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.autolog) to automatically capture app logic for 20+ [supported libraries](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/integrations/).
*   [**Manual**](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/app-instrumentation/manual-tracing/) - Designed for custom logic and complex workflows, control what gets traced using [Function Decorator APIs](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/app-instrumentation/manual-tracing/function-decorator) or [low-level APIs](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/app-instrumentation/manual-tracing/low-level-api).
*   [**Combined**](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/app-instrumentation/automatic#combine-manual-automatic) - Mix both approaches for complete coverage.

## Which approach should I use?[​](#which-approach-should-i-use "Direct link to Which approach should I use?")

Start with automatic tracing. It's the fastest way to get traces working. Add manual tracing later if you need more control.
