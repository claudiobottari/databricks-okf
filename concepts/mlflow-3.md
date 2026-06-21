---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 33ed1663b9d0eedff3d1b05882239d1a6e2aef2bdddb5d91ee859b4b68164638
  pageDirectory: concepts
  sources:
    - mlflow-on-databricks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-3
  citations:
    - file: mlflow-on-databricks-databricks-on-aws.md
title: MLflow 3
description: The latest major version of MLflow on Databricks, delivering observability, evaluation, prompt management, and new concepts like Logged Models and Deployment Jobs.
tags:
  - mlflow
  - versioning
  - features
timestamp: "2026-06-19T19:39:31.696Z"
---

---
title: MLflow 3
summary: The latest major version of MLflow on Databricks, delivering state-of-the-art observability, evaluation, and prompt management for agents and LLM applications, along with enhanced experiment tracking and model registry features.
sources:
  - mlflow-on-databricks-databricks-on-aws.md
kind: concept
createdAt: "2026-07-05T11:30:00.000Z"
updatedAt: "2026-07-05T11:30:00.000Z"
tags:
  - mlflow
  - mlflow-3
  - model-registry
  - experiment-tracking
  - llm
aliases:
  - mlflow-3
  - MLflow3
  - MLflow 3 on Databricks
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# MLflow 3

**MLflow 3** is the latest major version of the MLflow AI engineering platform on Databricks. It delivers state-of-the-art observability, evaluation, and prompt management for agents and LLM applications, while also providing enhanced experiment tracking, model evaluation, a production model registry, and model deployment tools for traditional [Machine Learning](/concepts/cicd-for-machine-learning.md) model development. ^[mlflow-on-databricks-databricks-on-aws.md]

## Overview

MLflow 3 on Databricks enables teams to centrally track and analyze the performance of models, AI applications, and agents across all environments — from interactive queries in a development notebook through production batch or real-time serving deployments. Users can orchestrate evaluation and deployment workflows using [Unity Catalog](/concepts/unity-catalog.md) and access comprehensive status logs for each version of their model, AI application, or agent. ^[mlflow-on-databricks-databricks-on-aws.md]

Key capabilities include:
- Viewing and accessing model metrics and parameters from the model version page in Unity Catalog and from the REST API. ^[mlflow-on-databricks-databricks-on-aws.md]
- Annotating requests and responses (*traces*) for all generative AI applications and agents, enabling human experts and automated techniques (such as LLM-as-a-judge) to provide rich feedback. This feedback can be leveraged to assess and compare application versions and to build datasets for improving quality. ^[mlflow-on-databricks-databricks-on-aws.md]

## New Concepts

MLflow 3 introduces two important new concepts:

- **Logged Models** help track a model's progress throughout its lifecycle. When a model is logged using `log_model()`, a `LoggedModel` is created that persists throughout the model's lifecycle, across different environments and runs. It contains links to artifacts such as metadata, metrics, parameters, and the code used to generate the model. Users can use the Logged Model to compare models against each other, find the most performant model, and track down information during debugging. ^[mlflow-on-databricks-databricks-on-aws.md]
- **Deployment jobs** manage the model lifecycle, including steps like evaluation, approval, and deployment. These model workflows are governed by Unity Catalog, and all events are saved to an activity log available on the model version page in Unity Catalog. ^[mlflow-on-databricks-databricks-on-aws.md]

## Agents and LLM Applications

MLflow 3 provides a complete platform for developing, evaluating, and monitoring agents and LLM applications:

- **Observability:** [MLflow Tracing](/concepts/mlflow-tracing.md) records the inputs, outputs, and metadata associated with each intermediate step of a request, helping quickly find the source of unexpected behavior in agents. ^[mlflow-on-databricks-databricks-on-aws.md]
- **Evaluation:** [Agent Evaluation](/concepts/mlflow-agent-evaluation.md) measures and improves agent quality, powered by MLflow evaluation. ^[mlflow-on-databricks-databricks-on-aws.md]
- **Prompt management:** Version, manage, and iterate on prompt templates used across AI applications. ^[mlflow-on-databricks-databricks-on-aws.md]
- **Agent development:** Custom Agents rely on MLflow to track agent code, performance metrics, and traces. ^[mlflow-on-databricks-databricks-on-aws.md]
- **Interactive debugging:** [Genie Code](/concepts/genie-code.md) provides natural language access to traces, evaluation runs, scorers, and more within MLflow experiments. ^[mlflow-on-databricks-databricks-on-aws.md]

## ML Model Development

For ML model development, MLflow 3 provides a complete workflow integrated with Databricks infrastructure:

1. **Feature Store:** Automated feature lookups simplify integration and reduce mistakes.
2. **Train models:** Use Databricks AI features to train models or fine-tune foundation models.
3. **Tracking:** MLflow tracks training by logging parameters, metrics, and artifacts to evaluate and compare model performance.
4. **Model Registry:** [MLflow Model Registry](/concepts/mlflow-model-registry.md), integrated with Unity Catalog, centralizes AI models and artifacts.
5. **Model Serving:** [Model Serving](/concepts/model-serving.md) deploys models to a REST API endpoint.
6. **Monitoring:** Model Serving automatically captures requests and responses to monitor and debug models. MLflow augments this data with trace data for each request.

^[mlflow-on-databricks-databricks-on-aws.md]

## Telemetry

Open source telemetry collection was introduced in MLflow 3.2.0 and is **disabled on Databricks by default**. ^[mlflow-on-databricks-databricks-on-aws.md]

## Further Reading

- [Get started with MLflow 3 for models](https://docs.databricks.com/aws/en/mlflow/mlflow-3-install)
- [Track and compare models using MLflow Logged Models](https://docs.databricks.com/aws/en/mlflow/logged-model)
- [Model Registry improvements with MLflow 3](https://docs.databricks.com/aws/en/mlflow/model-registry-3)
- [MLflow 3 deployment jobs](https://docs.databricks.com/aws/en/mlflow/deployment-job)

## Related Concepts

- [MLflow on Databricks](/concepts/mlflow-on-databricks.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Model Serving](/concepts/model-serving.md)
- [Agent Evaluation](/concepts/mlflow-agent-evaluation.md)
- [Logged Model](/concepts/loggedmodel.md)
- [Deployment Job](/concepts/mlflow-deployment-jobs.md)

## Sources

- mlflow-on-databricks-databricks-on-aws.md

# Citations

1. [mlflow-on-databricks-databricks-on-aws.md](/references/mlflow-on-databricks-databricks-on-aws-bc75dc1f.md)
