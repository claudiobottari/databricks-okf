---
title: Databricks data science and ML capabilities | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/concepts/ml-capabilities
ingestedAt: "2026-06-18T08:09:56.174Z"
---

Databricks has a unified platform for the full data science (DS) and machine learning (ML) lifecycle, from raw data ingestion through feature engineering, model training, deployment, and production monitoring. Databricks integrates with popular open-source ML frameworks, adding enterprise-grade governance, observability, and operational tooling, collectively known as MLOps.

This page lists major DS and ML capabilities, organized by workflow stage.

## Exploratory data analysis[​](#exploratory-data-analysis "Direct link to Exploratory data analysis")

Databricks simplifies exploratory data analysis (EDA) by providing interactive, collaborative, and AI-assisted tools for data scientists. Data scientists can explore data using natural language chat, UIs, or code, and they can collaborate using both real-time co-editing and Git-based code sharing. [Genie Code](https://docs.databricks.com/aws/en/notebooks/ds-agent) can do fully automated EDA or act as an interactive assistant.

## Prepare and serve features[​](#prepare-and-serve-features "Direct link to Prepare and serve features")

Databricks simplifies data for ML by unifying governance of data and ML workloads. With all data managed under [Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/) with fine-grained access controls, you can adjust data engineering and ML boundaries to fit your organization. Data can be prepared for ML using any [data engineering tools](https://docs.databricks.com/aws/en/data-engineering/) such as [Lakeflow Spark Declarative Pipelines](https://docs.databricks.com/aws/en/ldp/). Features are managed in a [Feature Store](https://docs.databricks.com/aws/en/machine-learning/feature-store/) for both batch and real-time serving, with a single, governed source of truth for features.

[Genie Code](https://docs.databricks.com/aws/en/notebooks/ds-agent) accelerates data discovery and preparation by browsing Unity Catalog to discover relevant tables, suggesting feature transformations, and generating code for ingestion and feature pipelines.

## Train ML models[​](#train-ml-models "Direct link to Train ML models")

Databricks has flexible tools for training ML and deep learning models. Pre-configured and customizable environments allow you to use custom ML libraries, and serverless CPU and GPU-accelerated compute resources allow scaling up and scaling out on demand. [Genie Code](https://docs.databricks.com/aws/en/notebooks/ds-agent) provides intelligent AutoML, taking natural language requests and building full multi-notebook workflows for featurization, training, tuning, evaluation, and deployment.

## Track and manage experiments[​](#track-and-manage-experiments "Direct link to Track and manage experiments")

[Databricks\-managed MLflow](https://www.databricks.com/product/managed-mlflow) provides the foundation for reproducible, auditable ML development. Its integrations with [Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/) and Git provide tracking and lineage for data and code assets. Each model version in the registry links back to the training run, dataset, environment, and git commit that produced it, providing a complete audit trail for any deployed model.

## Deploy and serve models[​](#deploy-and-serve-models "Direct link to Deploy and serve models")

Databricks supports both [batch inference](https://docs.databricks.com/aws/en/machine-learning/model-inference/) and [real-time serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/custom-models). Batch inference applies models efficiently to large datasets, whereas real-time serving provides models as low-latency API endpoints. [Genie Code](https://docs.databricks.com/aws/en/notebooks/ds-agent) can both generate code for model deployment and [diagnose issues and performance for model serving endpoints](https://docs.databricks.com/aws/en/machine-learning/model-serving/model-serving-genie-code).

## Evaluate and monitor[​](#evaluate-and-monitor "Direct link to Evaluate and monitor")

Databricks provides flexible evaluation for training and continuous monitoring for production. Real-time serving logs to inference tables governed in [Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/), and [data quality monitoring](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/) provides monitoring with custom metrics, dashboards, and alerts.

## MLOps and governance[​](#mlops-and-governance "Direct link to MLOps and governance")

Databricks provides a full suite of tools for ML operations (MLOps) and governance. [MLOps Stacks](https://docs.databricks.com/aws/en/machine-learning/mlops/mlops-stacks) provides templates for enabling automated, repeatable promotion from development to production using infrastructure-as-code. Data, features, models, and endpoints are fully governed by [Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/) and [AI Gateway](https://docs.databricks.com/aws/en/ai-gateway/).

## Open source support[​](#open-source-support "Direct link to Open source support")

Databricks provides full support for the open-source ML ecosystem.

You can use any open-source ML framework on Databricks: scikit-learn, XGBoost, LightGBM, PyTorch, TensorFlow, Hugging Face Transformers, Ray, and more. MLflow or your custom tools can store model artifacts in open formats that can be exported and run outside Databricks.

[MLflow](https://mlflow.org/) is open-source, created by Databricks and used by 10,000+ organizations. Your experiment tracking data, model artifacts, and pipeline definitions are stored in open formats.

Data and AI governance are built upon the open-source [Unity Catalog](https://unitycatalog.io/) APIs, and data storage is based upon the open [Delta Lake](https://delta.io/) format. Your feature data and training datasets remain in open, portable files.

## Learn more[​](#learn-more "Direct link to Learn more")

*   [Machine learning on Databricks](https://docs.databricks.com/aws/en/machine-learning/)
*   [Open source vs. managed MLflow on Databricks](https://docs.databricks.com/aws/en/mlflow3/genai/overview/oss-managed-diff)
