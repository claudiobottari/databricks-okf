---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 38047889e99170a8dd5cf62f99b12ffe76385ed1dd5d0c8cb53b61a1f0dbe4b6
  pageDirectory: concepts
  sources:
    - apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md
    - databricks-data-science-and-ml-capabilities-databricks-on-aws.md
    - mlflow-on-databricks-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - mlflow
    - MLflow 2
    - MLflow UI
    - MLflow SDK
  citations:
    - file: apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md
    - file: mlflow-on-databricks-databricks-on-aws.md
    - file: databricks-data-science-and-ml-capabilities-databricks-on-aws.md
title: MLflow
description: An open source platform for managing the end-to-end machine learning lifecycle, supporting tracking for model tuning in Python, R, and Scala, and used as the tracking backend for MLlib automated logging.
tags:
  - machine-learning
  - mlflow
  - open-source
timestamp: "2026-06-19T22:07:25.396Z"
---

---

title: MLflow
summary: An open source platform for managing the end-to-end machine learning lifecycle, supporting experiment tracking, model evaluation, model registry, and deployment for ML models and generative AI agents.
sources:
  - apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md
  - mlflow-on-databricks-databricks-on-aws.md
  - databricks-data-science-and-ml-capabilities-databricks-on-aws.md
kind: concept
createdAt: "2026-06-20T12:00:00.000Z"
updatedAt: "2026-06-20T12:00:00.000Z"
tags:
  - machine-learning
  - mlflow
  - platform
  - generative-ai
aliases:
  - mlflow
confidence: 0.95
provenanceState: merged
inferredParagraphs: 0
---

# MLflow

**MLflow** is an open source platform for managing the end-to-end machine learning lifecycle. It supports tracking for model tuning in Python, R, and Scala, and provides experiment tracking, model evaluation, a production model registry, and model deployment tools for both traditional ML models and generative AI agents.^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]^[mlflow-on-databricks-databricks-on-aws.md]

## Overview

MLflow is the largest open source AI engineering platform for agents, LLMs, and ML models. It enables teams to debug, evaluate, monitor, and optimize production-quality AI applications while controlling costs and managing access to models and data. With over 30 million monthly downloads, thousands of organizations rely on MLflow each day to ship AI to production with confidence.^[mlflow-on-databricks-databricks-on-aws.md]

MLflow supports any LLM provider, agent framework, ML library, and programming language. It provides native SDKs for Python, TypeScript/JavaScript, Java, and R.^[mlflow-on-databricks-databricks-on-aws.md] MLflow was created by Databricks and is used by over 10,000 organizations; experiment tracking data, model artifacts, and pipeline definitions are stored in open formats.^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

## MLflow 3

MLflow 3 on Databricks delivers state-of-the-art observability, evaluation, and prompt management for agents and LLM applications. For ML model development, it provides experiment tracking, model evaluation, a production model registry, and model deployment tools.^[mlflow-on-databricks-databricks-on-aws.md]

Key capabilities of MLflow 3 include:

- **Centralized tracking**: Track and analyze the performance of models, AI applications, and agents across all environments, from interactive queries in development notebooks through production batch or real-time serving deployments.^[mlflow-on-databricks-databricks-on-aws.md]
- **Orchestrated workflows**: Evaluate and deploy models using [Unity Catalog](/concepts/unity-catalog.md), with comprehensive status logs for each version of a model, AI application, or agent.^[mlflow-on-databricks-databricks-on-aws.md]
- **Metrics and parameters**: View and access model metrics and parameters from the model version page in Unity Catalog and from the REST API.^[mlflow-on-databricks-databricks-on-aws.md]
- **Traces**: Annotate requests and responses for all generative AI applications and agents, enabling human experts and automated techniques (such as LLM-as-a-judge) to provide rich feedback.^[mlflow-on-databricks-databricks-on-aws.md]

MLflow 3 also introduces **Logged Models** and **Deployment Jobs**:

- **Logged Models**: When you log a model using `log_model()`, a `LoggedModel` is created that persists throughout the model's lifecycle across different environments and runs. It contains links to artifacts such as metadata, metrics, parameters, and the code used to generate the model.^[mlflow-on-databricks-databricks-on-aws.md]
- **Deployment Jobs**: Manage the model lifecycle, including steps like evaluation, approval, and deployment. These workflows are governed by Unity Catalog, and all events are saved to an activity log available on the model version page in Unity Catalog.^[mlflow-on-databricks-databricks-on-aws.md]

## Databricks-managed MLflow

Databricks provides a fully managed and hosted version of MLflow, building on the open source experience to make it more robust and scalable for enterprise use.^[mlflow-on-databricks-databricks-on-aws.md]

### Agents and LLM applications

MLflow on Databricks provides a complete platform for developing, evaluating, and monitoring agents and LLM applications:

- **Observability**: [MLflow Tracing](/concepts/mlflow-tracing.md) records the inputs, outputs, and metadata associated with each intermediate step of a request, helping quickly find the source of unexpected behavior in agents.^[mlflow-on-databricks-databricks-on-aws.md]
- **Evaluation**: Use [Agent Evaluation](/concepts/mlflow-agent-evaluation.md) to measure and improve agent quality, powered by MLflow evaluation.^[mlflow-on-databricks-databricks-on-aws.md]
- **Prompt management**: Version, manage, and iterate on prompt templates used across AI applications.^[mlflow-on-databricks-databricks-on-aws.md]
- **Agent development**: Use Custom Agents to create agents, which rely on MLflow to track agent code, performance metrics, and traces.^[mlflow-on-databricks-databricks-on-aws.md]
- **Interactive debugging**: Use [Genie Code](/concepts/genie-code.md) for natural language access to traces, evaluation runs, scorers, and more within MLflow experiments.^[mlflow-on-databricks-databricks-on-aws.md]

### ML model development

MLflow on Databricks provides experiment tracking, model evaluation, a production model registry, and model deployment tools. The integration between Databricks and MLflow follows this workflow:^[mlflow-on-databricks-databricks-on-aws.md]

1. **Feature Store**: Databricks automated feature lookups simplifies integration and reduces mistakes.
2. **Train models**: Use Databricks AI features to train models or fine-tune foundation models.
3. **Tracking**: MLflow tracks training by logging parameters, metrics, and artifacts to evaluate and compare model performance.
4. **Model Registry**: MLflow Model Registry, integrated with Unity Catalog, centralizes AI models and artifacts.
5. **Model Serving**: Model Serving deploys models to a REST API endpoint.
6. **Monitoring**: Model Serving automatically captures requests and responses to monitor and debug models. MLflow augments this data with trace data for each request.

### Model training

MLflow Models are a standardized format for packaging machine learning models and generative AI agents. The standardized format ensures that models and agents can be used by downstream tools and workflows on Databricks.^[mlflow-on-databricks-databricks-on-aws.md]

### Experiment tracking

Databricks uses MLflow experiments as organizational units to track work while developing models. Experiment tracking lets you log and manage parameters, metrics, artifacts, and code versions during machine learning training and agent development. Organizing logs into experiments and runs allows you to compare models, analyze performance, and iterate more easily.^[mlflow-on-databricks-databricks-on-aws.md]

### Model Registry with Unity Catalog

MLflow Model Registry is a centralized model repository, UI, and set of APIs for managing the model deployment process. Databricks integrates Model Registry with Unity Catalog to provide centralized governance for models, allowing you to access models across workspaces, track model lineage, and discover models for reuse.^[mlflow-on-databricks-databricks-on-aws.md]

### Model Serving

[Model Serving](/concepts/model-serving.md) is tightly integrated with MLflow Model Registry and provides a unified, scalable interface for deploying, governing, and querying AI models. Each model you serve is available as a REST API that you can integrate into web or client applications. Model Serving relies on MLflow Model Registry to handle model versioning, dependency management, validation, and governance.^[mlflow-on-databricks-databricks-on-aws.md]

## Automated MLflow tracking for [Apache Spark MLlib](/concepts/apache-spark-mllib.md)

For Python notebooks, Databricks supports automated MLflow Tracking for [Apache Spark MLlib](/concepts/apache-spark-mllib.md) model tuning. When you run tuning code that uses `CrossValidator` or `TrainValidationSplit`, hyperparameters and evaluation metrics are automatically logged in MLflow. Without automated tracking, you must make explicit API calls to log to MLflow.^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

**Note**: MLlib automated MLflow tracking is deprecated on clusters that run Databricks Runtime 10.1 ML and above, and it is disabled by default on clusters running Databricks Runtime 10.2 ML and above. Instead, use MLflow PySpark ML autologging by calling `mlflow.pyspark.ml.autolog()`, which is enabled by default with Databricks Autologging.^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

### Managing MLflow runs

`CrossValidator` or `TrainValidationSplit` log tuning results as nested MLflow runs:^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

- **Main or parent run**: Information for `CrossValidator` or `TrainValidationSplit` is logged to the main run. If there is an active run already, information is logged to this active run. If there is no active run, MLflow creates a new run, logs to it, and ends the run before returning.
- **Child runs**: Each hyperparameter setting tested and the corresponding evaluation metric are logged to a child run under the main run.

When calling `fit()`, Databricks recommends wrapping the call inside a `with mlflow.start_run():` statement to ensure information is logged under its own MLflow main run.^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

## Open source vs. Databricks-managed MLflow

For general MLflow concepts, APIs, and features shared between open source and Databricks-managed versions, refer to MLflow documentation. For features exclusive to Databricks-managed MLflow, see Databricks documentation. Open source telemetry collection was introduced in MLflow 3.2.0 and is **disabled on Databricks by default**.^[mlflow-on-databricks-databricks-on-aws.md]

## Related concepts

- [Unity Catalog](/concepts/unity-catalog.md) — Centralized governance for data and AI assets
- MLflow Models — Standardized format for packaging ML models and AI agents
- [MLflow Model Registry](/concepts/mlflow-model-registry.md) — Centralized repository for managing model deployment
- [MLflow Tracing](/concepts/mlflow-tracing.md) — Observability for agents and LLM applications
- [Agent Evaluation](/concepts/mlflow-agent-evaluation.md) — Measuring and improving agent quality
- [Model Serving](/concepts/model-serving.md) — Deploying models to REST API endpoints
- [Feature Store](/concepts/feature-store.md) — Managing features for batch and real-time serving
- [Genie Code](/concepts/genie-code.md) — AI assistant for notebooks and agent debugging
- Custom Agents — Framework for building agents on Databricks

## Sources

- apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md
- mlflow-on-databricks-databricks-on-aws.md
- databricks-data-science-and-ml-capabilities-databricks-on-aws.md

# Citations

1. [apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md](/references/apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws-ff362b6f.md)
2. [mlflow-on-databricks-databricks-on-aws.md](/references/mlflow-on-databricks-databricks-on-aws-bc75dc1f.md)
3. [databricks-data-science-and-ml-capabilities-databricks-on-aws.md](/references/databricks-data-science-and-ml-capabilities-databricks-on-aws-8cf8bf4a.md)
