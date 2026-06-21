---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 044fb8e0376663fd4952b2f04061b71404fa4126d1e617d5a93e29789ac76a54
  pageDirectory: concepts
  sources:
    - mlops-workflows-on-databricks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-for-model-governance
    - UCFMG
  citations:
    - file: mlops-workflows-on-databricks-databricks-on-aws.md
    - file: abac-grant-policies-for-models-beta-databricks-on-aws.md
    - file: data-classification-databricks-on-aws.md
    - file: abac-policy-audit-logging.md
    - file: distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md
    - file: ab-comparison-of-agent-configurations.md
title: Unity Catalog for Model Governance
description: Using Models in Unity Catalog to manage model versioning, governance, deployment status, access control, and catalog-per-environment isolation across the MLOps workflow.
tags:
  - unity-catalog
  - governance
  - model-management
timestamp: "2026-06-19T19:41:57.774Z"
---

# Unity Catalog for Model Governance

**Unity Catalog for Model Governance** provides a centralized platform for managing, securing, and governing machine learning models throughout their lifecycle within the Databricks environment. It integrates model versioning, access control, auditing, and deployment management under a unified governance framework. ^[mlops-workflows-on-databricks-databricks-on-aws.md]

## Overview

Unity Catalog organizes models under a three-level namespace (`catalog.schema.model_name`) and enables organizations to apply consistent governance policies across all ML assets. This includes attribute-based access control (ABAC), data classification and tagging, audit logging, and lifecycle management from development through production. ^[mlops-workflows-on-databricks-databricks-on-aws.md]

## Core Governance Mechanisms

### Attribute-Based Access Control (ABAC)

Unity Catalog provides ABAC capabilities for models through two primary policy types:

- **ABAC GRANT Policy** – Dynamically grants privileges (such as `EXECUTE`) to securable objects whose governed tags match specified conditions. These policies are evaluated at every access check, granting the privilege on every matching object without requiring a separate grant per model. GRANT policies are currently in Beta and support `EXECUTE` on models. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

- **ABAC Policies from Data Classification** – Uses the results of Data Classification in Unity Catalog to automatically create ABAC policies that mask sensitive data based on classification tags. This serves as the primary method for applying governance controls derived from data classification outputs. ^[data-classification-databricks-on-aws.md]

### Data Classification and Tagging

The [Data Classification](/concepts/data-classification.md) feature automatically identifies and tags sensitive columns (e.g., `class.email_address`, `class.phone_number`) within a catalog. These governed tags then serve as the foundation for ABAC policies, enabling dynamic access control based on data sensitivity. ^[data-classification-databricks-on-aws.md]

### Audit Logging

All ABAC policy and governed tag operations are recorded in the `system.access.audit` system table, allowing administrators to monitor policy changes and investigate access-related issues. Logged actions include:

| Action Name | Description |
|-------------|-------------|
| `createPolicy` | A new policy is created |
| `deletePolicy` | An existing policy is deleted |
| `getPolicy` | Policy details are retrieved |
| `listPolicies` | Policies are listed for a securable object |

These actions cover all ABAC policy types, including row filter, column mask, and GRANT policies for models. ^[abac-policy-audit-logging.md]

## Model Registration and Lifecycle Management

Models are registered and versioned within Unity Catalog as part of the [MLflow](/concepts/mlflow.md) tracking workflow, providing a central, governed location for model artifacts, metadata, and deployment information. The registration process logs essential metadata such as the task type, pretrained model name, and model family. ^[distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md]

### Stage-Based Environments

Unity Catalog MLflow supports MLOps workflows by organizing model development into separate environments corresponding to different lifecycle stages:

- **Development stage:** The development environment is represented by a dev catalog in Unity Catalog. Data scientists have read-write access as they create temporary data and feature tables. Models created here are registered to the dev catalog. Data scientists should ideally have read-only access to production data in the prod catalog to analyze current production model predictions and performance. ^[mlops-workflows-on-databricks-databricks-on-aws.md]

- **Staging stage:** A separate staging catalog in Unity Catalog is used for testing ML pipelines. Assets written to this catalog are generally temporary and retained only until testing is complete. ^[mlops-workflows-on-databricks-databricks-on-aws.md]

- **Production stage:** ML engineers own the production environment. Models are registered at specified model paths in the production catalog. Data scientists typically have read-only access to assets in the production catalog for visibility into test results, logs, model artifacts, and monitoring tables. ^[mlops-workflows-on-databricks-databricks-on-aws.md]

### Model Aliases and Deployment

Unity Catalog supports model aliases such as "Champion" and "Challenger" to manage model versions through the deployment pipeline:

- After a model passes validation checks, it can be assigned the "Challenger" alias. ^[mlops-workflows-on-databricks-databricks-on-aws.md]
- The "Challenger" model is compared to the current "Champion" model, either offline against held-out data or through online A/B tests and gradual rollouts. ^[mlops-workflows-on-databricks-databricks-on-aws.md]
- If the "Challenger" performs better, it replaces the "Champion" alias. Inference pipelines are configured to load and apply the "Champion" model version automatically. ^[mlops-workflows-on-databricks-databricks-on-aws.md]

## Model Governance with A/B Comparison

Unity Catalog's integration with [MLflow GenAI](/concepts/mlflow-3-for-genai.md) enables A/B comparison of agent configurations to evaluate different model versions against consistent quality criteria. By running the same evaluation dataset against multiple agent configurations and scoring them with consistent custom judges, teams can quantify the impact of changes before promoting a configuration to production. ^[ab-comparison-of-agent-configurations.md]

## Security and Access Control

### Separate Environments

Creating separate environments (development, staging, production) with clearly defined transitions between stages is a key recommendation. Each execution environment consists of compute instances, runtimes and libraries, and automated jobs. ^[mlops-workflows-on-databricks-databricks-on-aws.md]

### Access Control and Versioning

Databricks recommends the following governance practices for model management:

- **Use Git for version control:** Pipelines and code should be stored in Git. Moving ML logic between stages corresponds to moving code from development branch to staging branch to release branch. Use [Databricks Git folders](/concepts/databricks-git-folders-for-cicd.md) to integrate with Git providers. ^[mlops-workflows-on-databricks-databricks-on-aws.md]
- **Store data in a lakehouse architecture:** Data should be stored using [Delta tables](/concepts/delta-lake-table.md) with access controls. ^[mlops-workflows-on-databricks-databricks-on-aws.md]
- **Manage model development with MLflow:** Track the model development process and save code snapshots, model parameters, metrics, and other metadata. ^[mlops-workflows-on-databricks-databricks-on-aws.md]
- **Use Models in Unity Catalog:** Manage model versioning, governance, and deployment status through the Unity Catalog interface. ^[mlops-workflows-on-databricks-databricks-on-aws.md]

### Deploy Code, Not Models

Databricks recommends promoting code rather than models between environments during the ML development process. This ensures that all code goes through the same code review and integration testing processes, and that the production version of the model is trained on production code. ^[mlops-workflows-on-databricks-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) – The data governance layer providing ABAC, classification, and auditing capabilities
- [MLflow](/concepts/mlflow.md) – The tracking and model management framework integrated with Unity Catalog
- [ABAC GRANT Policy](/concepts/abac-grant-policy.md) – Dynamic attribute-based access control for model `EXECUTE` privileges
- [ABAC Policies from Data Classification](/concepts/abac-policies-from-data-classification.md) – Automated policy creation from classification tags
- [Data Classification](/concepts/data-classification.md) – Automatic identification and tagging of sensitive columns
- [ABAC Policy Audit Logging](/concepts/abac-policy-audit-logging.md) – Recording of policy CRUD and tag operations for compliance
- MLflow Models – Models registered and governed within Unity Catalog
- MLOps Workflows – End-to-end ML lifecycle management on Databricks
- [Model Serving](/concepts/model-serving.md) – Infrastructure for deploying and serving models
- [Data Profiling](/concepts/data-profiling.md) – Monitoring statistical properties of input data and model predictions
- [Governed Tags](/concepts/governed-tags.md) – Tags that drive ABAC policy evaluation
- [Row Filter Policies](/concepts/row-filter-policies.md) – ABAC policies that restrict data content rather than model access
- [Column Mask Policies](/concepts/column-mask-policies.md) – ABAC policies that mask sensitive data columns
- [Delta Tables](/concepts/delta-lake-table.md) – The storage format for data in Unity Catalog

## Sources

- mlops-workflows-on-databricks-databricks-on-aws.md
- abac-grant-policies-for-models-beta-databricks-on-aws.md
- data-classification-databricks-on-aws.md
- abac-policy-audit-logging.md
- distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md
- ab-comparison-of-agent-configurations.md

# Citations

1. [mlops-workflows-on-databricks-databricks-on-aws.md](/references/mlops-workflows-on-databricks-databricks-on-aws-a1b056b9.md)
2. [abac-grant-policies-for-models-beta-databricks-on-aws.md](/references/abac-grant-policies-for-models-beta-databricks-on-aws-49466796.md)
3. [data-classification-databricks-on-aws.md](/references/data-classification-databricks-on-aws-066fe683.md)
4. abac-policy-audit-logging.md
5. [distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws.md](/references/distributed-fine-tuning-of-qwen2-05b-with-lora-databricks-on-aws-507af04a.md)
6. ab-comparison-of-agent-configurations.md
