---
title: Code-based scorers | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/custom-scorers
ingestedAt: "2026-06-18T08:15:19.342Z"
---

Production monitoring supports [built-in LLM judges](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/judges/) and `@scorer`\-decorated functions. Class-based `Scorer` subclasses are **not supported** for production monitoring. If you need stateful scorers in production, use the `@scorer` decorator and manage state inside the function body.

`@scorer`\-decorated functions used in production monitoring must be defined and registered from a **Databricks notebook**. The monitoring service serializes the function code for remote execution, and this serialization requires the notebook environment. For details, see [Use custom scorer functions](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/production-monitoring#use-custom-scorer-functions).
