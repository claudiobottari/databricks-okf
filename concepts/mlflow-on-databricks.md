---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fd4ee79b45c8ea6f9603f30d01886d2919dd7172a1b9994ab24226d92559061a
  pageDirectory: concepts
  sources:
    - machine-learning-on-databricks-databricks-on-aws.md
    - mlflow-on-databricks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - mlflow-on-databricks
    - MOD
  citations:
    - file: mlflow-on-databricks-databricks-on-aws.md
title: MLflow on Databricks
description: Integrated MLflow platform on Databricks for experiment tracking, model management in Unity Catalog, model deployment, and evaluation throughout the ML lifecycle.
tags:
  - databricks
  - mlflow
  - experiment-tracking
  - model-management
timestamp: "2026-06-19T19:20:54.787Z"
---

# MLflow on Databricks

**MLflow on Databricks** is the integration of the open-source MLflow platform with the Databricks environment, providing a fully managed and hosted version for developing, evaluating, deploying, and monitoring generative AI agents, large language models (LLMs), and traditional machine learning (ML) models. ^[mlflow-on-databricks-databricks-on-aws.md]

## What is MLflow?

MLflow is the largest open-source AI engineering platform for agents, LLMs, and ML models. It enables teams to debug, evaluate, monitor, and optimise production-quality AI applications while controlling costs and managing access to models and data. Over 30 million monthly downloads support thousands of organisations shipping AI to production. ^[mlflow-on-databricks-databricks-on-aws.md]

For agents and LLMs, MLflow provides production-grade observability, evaluation, prompt management, and an AI Gateway. For ML models, it offers experiment tracking, model evaluation, a production model registry, and deployment tools. MLflow supports any LLM provider, agent framework, ML library, and programming language, with native SDKs for Python, TypeScript/JavaScript, Java, and R. ^[mlflow-on-databricks-databricks-on-aws.md]

## MLflow 3 on Databricks

MLflow 3 on Databricks delivers advanced capabilities for agents and LLM applications, including state-of-the-art observability, evaluation, and prompt management. For ML models, it continues to provide experiment tracking, model evaluation, a production model registry, and deployment tools. ^[mlflow-on-databricks-databricks-on-aws.md]

With MLflow 3 on Databricks you can:
- Track and analyse model, AI application, and agent performance across all environments, from development notebooks to production batch or real-time serving.
- Orchestrate evaluation and deployment workflows using [Unity Catalog](/concepts/unity-catalog.md) and access comprehensive status logs for each model version.
- View model metrics and parameters from the model version page in Unity Catalog and via the REST API.
- Annotate requests and responses ([Traces](/concepts/traces.md)) for generative AI applications and agents, enabling human experts and automated techniques (such as LLM‑as‑a‑judge) to provide feedback for quality improvement.

MLflow 3 introduces **Logged Models** and **Deployment Jobs**. Logged Models track a model's progress throughout its lifecycle, persisting across environments and runs with links to metadata, metrics, parameters, and code. Deployment Jobs manage the model lifecycle—evaluation, approval, deployment—governed by Unity Catalog with a saved activity log on the model version page. ^[mlflow-on-databricks-databricks-on-aws.md]

## Databricks-Managed MLflow

Databricks provides a fully managed and hosted version of MLflow, building on the open-source experience to make it more robust and scalable for enterprise use. The managed version is built on Unity Catalog and the cloud data lake to unify all data and AI assets throughout the ML lifecycle. ^[mlflow-on-databricks-databricks-on-aws.md]

## Agents and LLM Applications

MLflow on Databricks offers a complete platform for developing, evaluating, and monitoring agents and LLM applications:

- **Observability**: [MLflow Tracing](/concepts/mlflow-tracing.md) records inputs, outputs, and metadata for each intermediate step of a request, helping quickly identify unexpected behaviour in agents.
- **Evaluation**: [Agent Evaluation](/concepts/mlflow-agent-evaluation.md) (powered by MLflow evaluation) measures and improves agent quality.
- **Prompt Management**: Version, manage, and iterate on prompt templates used across AI applications.
- **Agent Development**: Custom Agents rely on MLflow to track agent code, performance metrics, and traces.
- **Interactive Debugging**: [Genie Code](/concepts/genie-code.md) provides natural‑language access to traces, evaluation runs, and scorers within an MLflow experiment.

## ML Model Development

For traditional ML, MLflow on Databricks supports the full model lifecycle:

1. **Feature Store**: Automated feature lookups simplify integration and reduce errors.
2. **Train models**: Use Databricks AI features to train or fine-tune foundation models.
3. **Tracking**: MLflow logs parameters, metrics, and artifacts to evaluate and compare model performance.
4. **Model Registry**: The MLflow Model Registry, integrated with Unity Catalog, centralises AI models and artifacts.
5. **Model Serving**: Model Serving deploys models as REST API endpoints.
6. **Monitoring**: Model Serving automatically captures requests and responses; MLflow augments this with trace data.

MLflow Models are the standardised packaging format for ML and generative AI assets, ensuring compatibility with downstream tools and workflows. ^[mlflow-on-databricks-databricks-on-aws.md]

### Experiment Tracking

Databricks uses MLflow experiments as organisational units to track work during model development. Experiment tracking logs and manages parameters, metrics, artifacts, and code versions, enabling comparison and iteration. ^[mlflow-on-databricks-databricks-on-aws.md]

### Model Registry with Unity Catalog

The MLflow Model Registry is a centralised repository, UI, and set of APIs for managing model deployment. Databricks integrates it with Unity Catalog for centralised governance, cross‑workspace access, lineage tracking, and model discovery. ^[mlflow-on-databricks-databricks-on-aws.md]

### Model Serving

Databricks Model Serving tightly integrates with the MLflow Model Registry, providing a unified, scalable interface for deploying, governing, and querying AI models as REST APIs. Model Serving leverages the registry for versioning, dependency management, validation, and governance. ^[mlflow-on-databricks-databricks-on-aws.md]

## Open Source vs. Databricks-Managed MLflow

For general MLflow concepts, APIs, and features shared between open source and managed versions, refer to the [MLflow documentation](https://mlflow.org/docs/latest/). Features exclusive to Databricks-managed MLflow are documented in the Databricks documentation.

Key difference: Open‑source telemetry collection (introduced in MLflow 3.2.0) is **disabled on Databricks by default**. ^[mlflow-on-databricks-databricks-on-aws.md]

## Related Concepts

- Machine Learning on Databricks
- [Unity Catalog](/concepts/unity-catalog.md)
- [MLflow Model Registry](/concepts/mlflow-model-registry.md)
- [Model Serving on Databricks](/concepts/model-serving-on-databricks.md)
- [Agent Evaluation](/concepts/mlflow-agent-evaluation.md)
- [MLflow Tracking](/concepts/mlflow-tracking.md)
- [MLflow Tracing](/concepts/mlflow-tracing.md)
- Feature Store on Databricks
- [Logged Models](/concepts/logged-models.md)
- Deployment Jobs

## Sources

- mlflow-on-databricks-databricks-on-aws.md

# Citations

1. [mlflow-on-databricks-databricks-on-aws.md](/references/mlflow-on-databricks-databricks-on-aws-bc75dc1f.md)
