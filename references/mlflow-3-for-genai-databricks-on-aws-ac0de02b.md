---
title: MLflow 3 for GenAI | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow3/genai/
ingestedAt: "2026-06-18T08:14:23.947Z"
---

MLflow 3 for GenAI is an open platform that unifies tracking, evaluation, and observability for GenAI apps and agents throughout the development and production lifecycle. It includes realtime trace logging, built-in and custom scorers, incorporation of human feedback, and version tracking to help you efficiently evaluate and improve app quality during development and continue tracking and improving quality in production.

Managed MLflow on Databricks extends open source MLflow with capabilities designed for production GenAI applications, including enterprise-ready governance, fully managed hosting, production-level scaling, and integration with your data in the Databricks lakehouse and Unity Catalog.

For information about agent evaluation in MLflow 2, see [Agent Evaluation (MLflow 2)](https://docs.databricks.com/aws/en/generative-ai/agent-evaluation/) and the [migration guide](https://docs.databricks.com/aws/en/mlflow3/genai/agent-eval-migration). For MLflow 3, the Agent Evaluation SDK methods have been integrated with Databricks-managed MLflow.

For a set of tutorials to get you started, see [Get started](#get-started).

## How MLflow 3 helps optimize GenAI app quality[​](#how-mlflow-3-helps-optimize-genai-app-quality "Direct link to How MLflow 3 helps optimize GenAI app quality")

Evaluating GenAI applications and agents is more complex than evaluating traditional software. Inputs and outputs are often free-form text, and many different outputs can be considered correct. Quality depends not only on correctness but also on factors like precision, length, completeness, appropriateness, and other criteria specific to the use case. Because LLMs are inherently non-deterministic, and GenAI agents include additional components such as retrievers and tools, their responses can vary from run to run.

Developers need concrete quality metrics, automated evaluation, and continuous monitoring to build and deploy robust AI apps. MLflow 3 for GenAI provides these key pieces for efficient development, deployment, and continuous improvement:

*   [Tracing](#tracing) automatically logs inputs, intermediate steps, and outputs and provides the data foundation for evaluation and monitoring.
*   [Built-in and custom LLM judges and scorers](#eval-and-monitoring) let you define various aspects of quality and customize metrics to your use case.
*   [Review apps for expert feedback](#eval-and-monitoring) allow you to collect and label datasets for evaluation and to align automated judges and scorers with expert judgement.
*   [Automated evaluation and monitoring](#eval-and-monitoring) leverage the same judges and scorers during development and production.
*   [App and prompt versioning](#ai-lifecycle) allow you to compare versions and track improvements over iterations.

Using MLflow 3 on Databricks, you can bring AI to your data to help you deeply understand and improve quality. Unity Catalog provides consistent governance for prompts, apps, and traces. Using any model or framework, MLflow supports you throughout the development loop all the way to and in production.

## Get started[​](#get-started "Direct link to Get started")

Start building better GenAI applications with comprehensive observability and evaluation tools.

## Tracing[​](#-tracing "Direct link to -tracing")

MLflow Tracing provides observability and logs the trace data required for evaluation and monitoring.

## Evaluation and monitoring[​](#-evaluation-and-monitoring "Direct link to -evaluation-and-monitoring")

Replace manual testing with automated evaluation using built-in and custom LLM judges and scorers that match human expertise and can be applied in both development and production. Every production interaction becomes an opportunity to improve with integrated feedback and evaluation workflows.

## Manage the GenAI app lifecycle[​](#-manage-the-genai-app-lifecycle "Direct link to -manage-the-genai-app-lifecycle")

Version, track, and govern your entire GenAI application with enterprise-grade lifecycle management and governance tools.
