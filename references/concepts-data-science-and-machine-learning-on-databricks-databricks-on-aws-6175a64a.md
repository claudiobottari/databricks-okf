---
title: "Concepts: Data science and machine learning on Databricks | Databricks on AWS"
source: https://docs.databricks.com/aws/en/machine-learning/concepts/
ingestedAt: "2026-06-18T08:09:54.678Z"
---

Data science and machine learning (DS and ML) extract insight and build predictive models from data. DS and ML include both interactive exploration and modeling and automated production systems. Classic ML includes techniques like classification, regression, anomaly detection, forecasting, and recommendation.

Modern deep learning and generative AI (GenAI) methods are technically types of ML. This section covers deep learning. For GenAI, see [Concepts: Generative AI on Databricks](https://docs.databricks.com/aws/en/agents/concepts/).

## The ML lifecycle[​](#the-ml-lifecycle "Direct link to The ML lifecycle")

The ML lifecycle covers the end-to-end journey from raw data to a production model and back again through monitoring and retraining. Key stages include:

1.  **Scope the use case** by defining the prediction target, success metrics, and production requirements.
2.  **Run exploratory data analysis (EDA)** to understand data distributions, predictive signals, and data quality issues before modeling.
3.  **Prepare data and features**, managed within a feature store.
4.  **Train models and track experiments**, logging experiment metadata for analysis and for deployment.
5.  **Evaluate** model quality against held-out data and stakeholder criteria.
6.  **Register, stage and test** models before promoting to production.
7.  **Deploy to production** in real-time endpoints or batch inference jobs.
8.  **Monitor and retrain** to adapt models to changing data or user behavior.

See [Machine learning lifecycle](https://docs.databricks.com/aws/en/machine-learning/concepts/ml-lifecycle) for a guide to each stage.

## AI-assisted development and operations[​](#ai-assisted-development-and-operations "Direct link to AI-assisted development and operations")

Databricks has Genie Code, an AI assistant integrated across notebooks and the workspace. Use it for development, debugging, and ongoing operations, drawing on its specialized knowledge of your enterprise context. See [Use Genie Code for data science](https://docs.databricks.com/aws/en/notebooks/ds-agent).

You can use Genie Code at every step of your workflow:

*   Start with [Genie chat](https://docs.databricks.com/aws/en/genie-one/chat) to discover relevant models, data, and features in your workspace and Unity Catalog.
*   [Use Genie Code](https://docs.databricks.com/aws/en/notebooks/ds-agent) to prototype pipelines for featurization, model training and tuning, evaluation and deployment.
*   [Analyze model serving endpoints with Genie Code](https://docs.databricks.com/aws/en/machine-learning/model-serving/model-serving-genie-code) to diagnose and investigate issues in production.

You can also use third-party coding tools to develop and maintain ML pipelines on Databricks. See [Agent skills for AI coding assistants](https://docs.databricks.com/aws/en/agent-skills/).

## What is an ML platform?[​](#what-is-an-ml-platform "Direct link to What is an ML platform?")

An ML platform is the combined infrastructure, tooling, and governance layer that supports the full ML lifecycle, from raw data to production models. A well-designed ML platform connects data engineering, interactive data science and production ML in a single governed system.

Key components include:

*   Data assets such as files, tables, processing pipelines, and feature stores
*   Experimentation tools such as notebooks and visualizations, with simple collaboration and AI assistance
*   Training infrastructure with customizable environments and flexible compute resources
*   Deployment and monitoring infrastructure for batch and real-time serving, with production dashboards and alerts
*   MLOps and governance tools for orchestration, CI/CD, lineage, access management and audit logging

Key governance capabilities include:

*   Unified governance of data and ML assets. Learn more at [What is Unity Catalog?](https://docs.databricks.com/aws/en/data-governance/unity-catalog/).
*   Unified governance of model endpoints. Learn more at [Unity AI Gateway for serving endpoints](https://docs.databricks.com/aws/en/ai-gateway/overview-serving-endpoints).
*   Unified security approach. Learn more at [Databricks AI Security](https://www.databricks.com/trust/ai-security).
*   Unified administration of data and ML tooling. Learn more at [Administration](https://docs.databricks.com/aws/en/admin/).

Also see [Databricks data science and ML capabilities](https://docs.databricks.com/aws/en/machine-learning/concepts/ml-capabilities) and [Databricks architecture](https://docs.databricks.com/aws/en/getting-started/architecture).

## ML vs. deep learning vs. GenAI[​](#ml-vs-deep-learning-vs-genai "Direct link to ML vs. deep learning vs. GenAI")

The boundaries between machine learning (ML), deep learning (DL), and generative AI (GenAI) can be fuzzy. This guide focuses on ML and deep learning, but the following platform features support all three paradigms:

*   [Model Serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/) supports classic ML, deep learning, and custom GenAI models for both real-time and batch inference.
*   [`ai_query`](https://docs.databricks.com/aws/en/large-language-models/ai-query#custom-model) supports SQL queries and batch inference workloads for all three paradigms.

*   [AI Runtime](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/) and GPU-enabled [Databricks Runtime for Machine Learning](https://docs.databricks.com/aws/en/machine-learning/databricks-runtime-ml) support training and fine-tuning across all three paradigms.

*   [MLflow experiment tracking](https://docs.databricks.com/aws/en/mlflow/tracking) tracks runs and experiments for all three paradigms.
*   [Databricks AI Search](https://docs.databricks.com/aws/en/ai-search/ai-search) serves unstructured data for all three paradigms.

## Learn more[​](#learn-more "Direct link to Learn more")

*   [Machine learning lifecycle](https://docs.databricks.com/aws/en/machine-learning/concepts/ml-lifecycle) - ML lifecycle stages and best practices
*   [Databricks data science and ML capabilities](https://docs.databricks.com/aws/en/machine-learning/concepts/ml-capabilities) - Databricks ML capabilities by workflow stage
*   [AI on Databricks](https://www.databricks.com/product/artificial-intelligence) - Use cases, customers, and other resources
