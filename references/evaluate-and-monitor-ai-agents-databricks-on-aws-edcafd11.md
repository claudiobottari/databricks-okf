---
title: Evaluate and monitor AI agents | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/
ingestedAt: "2026-06-18T08:14:33.797Z"
---

MLflow provides comprehensive agent evaluation and LLM evaluation capabilities to help you measure, improve, and maintain the quality of your AI applications. MLflow supports the entire development lifecycle from testing through production monitoring for LLMs, agents, RAG systems, or other GenAI applications.

Evaluating AI agents and LLMs is more complex than traditional ML model evaluation. These applications involve multiple components, multi-turn conversations, and nuanced quality criteria. Both qualitative and quantitative metrics require specialized evaluation approaches to accurately assess performance.

The evaluation and monitoring component of MLflow 3 is designed to help you iteratively optimize the quality of your GenAI app. Evaluation and monitoring build upon [MLflow Tracing](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/), which provides real-time trace logging in the development, testing, and production phases. Traces can be [evaluated during development](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/eval-harness) using built-in or custom [LLM judges and scorers](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/scorers), and [production monitoring](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/production-monitoring) can reuse the same judges and scorers, ensuring consistent evaluation throughout the application lifecycle. Domain experts can provide feedback using an integrated [Review App](https://docs.databricks.com/aws/en/mlflow3/genai/human-feedback/expert-feedback/live-app-testing) for collecting human feedback, producing evaluation data for further iteration.

The diagram shows this high-level iterative workflow.

![Overview diagram of MLflow 3 evaluation and monitoring](https://docs.databricks.com/aws/en/assets/images/flowchart-00c729ac75207b58d9c2243583a30d5a.png)

note

Agent Evaluation is integrated with managed MLflow 3. The Agent Evaluation SDK methods are now available using the `mlflow[databricks]>=3.1` SDK. See [Migrate to MLflow 3 from Agent Evaluation](https://docs.databricks.com/aws/en/mlflow3/genai/agent-eval-migration) to update your MLflow 2 Agent Evaluation code to use MLflow 3.
