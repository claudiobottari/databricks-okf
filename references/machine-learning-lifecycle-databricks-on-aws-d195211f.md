---
title: Machine learning lifecycle | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/concepts/ml-lifecycle
ingestedAt: "2026-06-18T08:09:57.970Z"
---

This page describes the end-to-end journey for taking a machine learning (ML) project from initial scoping to production, and keeping it performing well over time. Code, data, and models pass through three broad stages: development, staging, and production. Each stage has distinct goals and requirements:

1.  [Scope the use case and define success](#scope-use-case)
2.  [Explore and understand the data](#explore-data)
3.  [Prepare data and features](#prepare-data)
4.  [Train models and track experiments](#train-track)
5.  [Evaluate](#evaluate)
6.  [Register, stage and test models](#stage)
7.  [Deploy to production](#deploy)
8.  [Monitor and retrain](#monitor)

## 1\. Scope the use case and define success[​](#1-scope-the-use-case-and-define-success "Direct link to 1-scope-the-use-case-and-define-success")

Before building anything, align on what the model needs to do and how you will know it is working.

*   What is the prediction target, and what class of ML problem does that imply: classification, regression, forecasting, recommendation, ranking, anomaly detection, or something else?
*   What input data is available, and is it sufficient to learn the target pattern?
*   What metrics define success: accuracy, AUC, precision at K, or business KPIs?
*   What are the serving and production requirements: latency, throughput, and data freshness?
*   Which stakeholders must sign off on production deployments? What are their requirements around explainability?

The preceding requirements do not dictate the specific ML method. You might begin modeling with a simpler approach like gradient boosted trees, and later decide that more powerful deep learning methods are needed.

## 2\. Explore and understand the data[​](#2-explore-and-understand-the-data "Direct link to 2-explore-and-understand-the-data")

Before preparing features or training a model, explore the data to understand its structure, quality, and relationship to the prediction target. **Exploratory data analysis (EDA)** is the process of summarizing and visualizing a dataset to surface distributions, correlations, missing values, and outliers that shape downstream modeling decisions.

Early on, decide how to verify you have valid test data that is held back from training. Even during EDA, beware making modeling decisions based on your test data.

EDA answers questions that inform the rest of the lifecycle:

*   Which inputs are most predictive of the target, and are any of them unavailable at serving time?
*   Are there missing values, outliers, or skewed distributions that require cleaning or transformation?
*   Is the dataset large enough, and representative enough, to learn the target pattern?

Databricks simplifies EDA with interactive, collaborative, and AI-assisted tools. Explore your data using natural language chat, UIs, or code, and collaborate through both real-time co-editing and Git-based code sharing:

*   [Notebooks](https://docs.databricks.com/aws/en/notebooks/) provide collaborative spaces for exploration, visualization, and documentation.
*   [Dashboards](https://docs.databricks.com/aws/en/dashboards/) provide SQL and visualization-based exploration.
*   [Genie Chat](https://docs.databricks.com/aws/en/genie-one/chat) provides a full-page, natural-language interface for asking data questions.
*   [Genie Code](https://docs.databricks.com/aws/en/notebooks/ds-agent) can perform fully automated EDA or act as an interactive assistant.

## 3\. Prepare data and features[​](#3-prepare-data-and-features "Direct link to 3-prepare-data-and-features")

With the data understood, turn the raw sources and transformations identified during EDA into features for ML models. Assess your data pipelines for training and serving, including speed, volume, freshness, and ownership of data sources. The boundary between **data engineering** (preparing and transforming data) and **feature engineering** (deriving ML inputs) is fuzzy. On Databricks, data engineering and ML share the same platform and governance layer in [Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/), so data prepared by one team can be made available immediately as features for another, without data movement or duplicated pipelines.

Search for existing data and feature definitions:

*   Explore data and features available in [Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/). If your organization has related models in place, use Unity Catalog lineage to discover data sources and features used for those models.
*   [Workspace search](https://docs.databricks.com/aws/en/search/) can help you to discover what governed data, models, or applications already exist.

Create and manage new assets as needed:

*   See [Data engineering with Databricks](https://docs.databricks.com/aws/en/data-engineering/) for more on tools for data ingestion and engineering, including [Lakeflow Designer](https://docs.databricks.com/aws/en/designer/) for an AI-assisted, no-code experience.
*   Use the [Feature Store](https://docs.databricks.com/aws/en/machine-learning/feature-store/) to define and manage features as reusable, governed assets. The same feature definitions are used in training and production, with support for batch and real-time data ingestion and for batch and real-time serving.

Use [Genie Code](https://docs.databricks.com/aws/en/notebooks/ds-agent) to accelerate data discovery and preparation by browsing Unity Catalog to discover relevant tables, suggesting feature transformations, and generating starter code for ingestion and feature pipelines.

## 4\. Train models and track experiments[​](#4-train-models-and-track-experiments "Direct link to 4-train-models-and-track-experiments")

Data science and ML applications use many different approaches, each of which has its own requirements for ML algorithms and libraries, compute requirements, and workflows. Databricks provides flexible environments and compute for different workloads, with experiment tracking unified under [MLflow](https://mlflow.org/).

### Environments and compute[​](#environments-and-compute "Direct link to Environments and compute")

By default, use [serverless compute](https://docs.databricks.com/aws/en/compute/serverless/) for both interactive notebooks and automated jobs. Serverless compute starts instantly and scales up and down automatically with your workload.

For GPU acceleration, attach GPUs to your serverless compute, which then uses the [AI Runtime](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/), an environment preconfigured for GPU training and inference.

For both CPU and GPU workloads, you can also use [classic compute](https://docs.databricks.com/aws/en/compute/use-compute) with the [Databricks Runtime for Machine Learning](https://docs.databricks.com/aws/en/machine-learning/databricks-runtime-ml).

Customize any of the preceding environments with your ML libraries. With environments often highly customized for ML applications, leverage MLflow tracking to record dependencies, verify reproducibility, and avoid training-serving skew.

### MLflow tracking[​](#mlflow-tracking "Direct link to MLflow tracking")

Use [Databricks\-managed MLflow](https://www.databricks.com/product/managed-mlflow) for tracking your experimentation and logging model metadata:

*   [Organize project logs in **experiments**](https://docs.databricks.com/aws/en/mlflow/experiments), with recorded **runs** for training or evaluation.
*   In each run, log parameters, metrics, and artifacts [automatically](https://mlflow.org/docs/latest/ml/tracking/autolog/) or [manually](https://mlflow.org/docs/latest/ml/tracking/quickstart/).
*   During experimentation, [compare runs in the MLflow UI](https://docs.databricks.com/aws/en/mlflow/visualize-runs) to find the best-performing configuration.
*   [Log models with MLflow](https://docs.databricks.com/aws/en/mlflow/logged-model) to store model artifacts with full provenance: which dataset, which code, and which environment produced this model. This metadata simplifies deploying models to production, plus auditing and troubleshooting.

### Get started with modeling[​](#get-started-with-modeling "Direct link to Get started with modeling")

[Genie Code](https://docs.databricks.com/aws/en/notebooks/ds-agent) can generate a complete ML notebook from a plain-language description of the prediction task, including feature selection from the Feature Store, ML training, and MLflow tracking.

Also see [resources for hyperparameter tuning](https://docs.databricks.com/aws/en/machine-learning/automl-hyperparam-tuning/), [model training examples](https://docs.databricks.com/aws/en/machine-learning/train-model/training-examples), and [Ray on Databricks](https://docs.databricks.com/aws/en/machine-learning/ray/).

For deep learning and GPU-accelerated classic ML training, see [example notebooks for the AI Runtime](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/examples/).

## 5\. Evaluate[​](#5-evaluate "Direct link to 5-evaluate")

During development, define quality evaluation metrics based on the requirements from scoping:

*   Your base metrics might be common ML metrics like accuracy, AUC, RMSE or domain-specific metrics.
*   Your evaluation might also include derived metrics, such as bias and fairness across population segments, measured by comparing base metrics across segments of your data.

Define metrics using your chosen ML library or framework, using [MLflow's built-in metrics module](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.metrics.html), or your custom logic. For all metrics, [log metrics in MLflow runs](https://docs.databricks.com/aws/en/mlflow/logged-model) to link them to their corresponding models. The metrics you define during development and training can be reused later as metrics for [production monitoring](#monitor).

## 6\. Register, stage and test models[​](#6-register-stage-and-test-models "Direct link to 6-register-stage-and-test-models")

After training an ML model or pipeline, register it to the [MLflow Model Registry in Unity Catalog](https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/) to simplify governance and management as you promote the model toward production. A registered model has versions, each of which links to the original training run that produced it. Model versions enable safe deployment workflows: you can test a new version in staging before promoting it to production, roll back to a previous version if quality degrades, and maintain a complete audit trail of what was deployed and when.

Before a new model version serves production traffic, test the version in staging under realistic conditions:

*   [Label the candidate model version with aliases](https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/#uc-model-aliases) (`Staging`, `Production`) to signal lifecycle state without renaming artifacts.
*   Run integration tests against staging infrastructure: confirm the serving endpoint starts, latency meets requirements, and outputs are well-formed.
*   Perform A/B or shadow tests on production data to validate performance before full cutover.
*   Collect stakeholder sign-off based on evaluation results.

This description oversimplifies deployment practices and ML operations (MLOps). Learn more details about MLOps at [MLOps workflows on Databricks](https://docs.databricks.com/aws/en/machine-learning/mlops/mlops-workflow).

## 7\. Deploy to production[​](#7-deploy-to-production "Direct link to 7-deploy-to-production")

After staging validation, promote and deploy the model to production to generate predictions for real-world inputs. Databricks supports two primary serving patterns:

*   **Real-time serving**: Deploy the model as a low-latency REST endpoint using [Model Serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/) for use cases that require low-latency decisions, such as fraud interception at transaction time, live personalization, or dynamic pricing.
*   **Batch inference**: [`ai_query`](https://docs.databricks.com/aws/en/large-language-models/ai-query#custom-model) provides efficient batch inference for custom models deployed as [Model Serving endpoints](https://docs.databricks.com/aws/en/machine-learning/model-serving/custom-models). You can also use custom code with Apache Spark UDFs ([example](https://docs.databricks.com/aws/en/machine-learning/reference-solutions/images-etl-inference)) or [`mlflow.pyfunc`](https://docs.databricks.com/aws/en/mlflow/models#generated-code-snippets) for batch inference. Batch pipelines write results to Delta tables for downstream applications, dashboards, or pipelines. This pattern handles daily forecasts, nightly recommendation refreshes, and other periodic jobs.

Both patterns use the same trained model artifact. Train once, and deploy to batch or real-time serving from the same registered version, with the same governance and lineage.

Genie Code can both generate code for deployment and [help to troubleshoot serving issues, explain endpoint behavior, and accelerate iteration when models must be updated or redeployed](https://docs.databricks.com/aws/en/machine-learning/model-serving/model-serving-genie-code).

## 8\. Monitor and retrain[​](#8-monitor-and-retrain "Direct link to 8-monitor-and-retrain")

Production ML systems can degrade over time as user behavior shifts or data pipelines change. Continuously monitor your production data and model predictions:

*   Log inputs and outputs from your deployed models. For real-time serving, [inference tables](https://docs.databricks.com/aws/en/ai-gateway/inference-tables) provide automatic logging without changes to your model code. For batch serving, your pipelines naturally read from and write to Delta tables managed by Unity Catalog.
*   Feed these logs into [data quality monitoring](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/), which tracks data quality, feature drift, and prediction distribution over time. If you have ground truth or feedback data, you can join this data with serving logs to compute prediction quality metrics.
*   Use the [monitoring UI](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/anomaly-detection/#incidents) and [anomaly detection alerts](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/anomaly-detection/alerts) to trigger escalation or retraining before quality noticeably degrades.

Learn more about production ML at [MLOps workflows on Databricks](https://docs.databricks.com/aws/en/machine-learning/mlops/mlops-workflow).

## Learn more[​](#learn-more "Direct link to Learn more")

*   [Databricks data science and ML capabilities](https://docs.databricks.com/aws/en/machine-learning/concepts/ml-capabilities) - Databricks capabilities at each stage of this lifecycle
*   [MLOps workflows on Databricks](https://docs.databricks.com/aws/en/machine-learning/mlops/mlops-workflow) - Production MLOps workflow reference
*   [Manage model lifecycle in Unity Catalog](https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/) - Model versioning and lifecycle management in Unity Catalog
