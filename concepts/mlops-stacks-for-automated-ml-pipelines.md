---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 698c01a44d0586c94b009071e4b5308f469f0e2b8c030e3b19e0016b367aae07
  pageDirectory: concepts
  sources:
    - databricks-data-science-and-ml-capabilities-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlops-stacks-for-automated-ml-pipelines
    - MSFAMP
    - Automated CI/CD pipeline for ML
  citations:
    - file: databricks-data-science-and-ml-capabilities-databricks-on-aws.md
title: MLOps Stacks for Automated ML Pipelines
description: Infrastructure-as-code templates enabling automated, repeatable promotion from development to production, integrated with Unity Catalog and AI Gateway for full governance.
tags:
  - mlops
  - ci-cd
  - infrastructure-as-code
timestamp: "2026-06-18T15:05:59.248Z"
---

# MLOps Stacks for Automated ML Pipelines

**MLOps Stacks** are a set of templates provided by Databricks that enable teams to build automated, repeatable machine learning pipelines that progress models from development through testing to production using infrastructure-as-code principles. They are one component of Databricks’ broader MLOps and governance tooling. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

## Overview

MLOps Stacks standardise the workflow for promoting ML models across environments by codifying the pipeline definition, testing, and deployment steps. The templates are designed to remove manual hand‑offs and reduce configuration errors, making it easier to maintain compliance and audit trails in enterprise settings. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

## Key Characteristics

- **Infrastructure-as-Code**: Pipeline definitions, environment configurations, and deployment targets are declared in code (e.g., Terraform, YAML) and version‑controlled. This allows teams to reproduce environments consistently across development, staging, and production. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]
- **Automated Promotion**: The templates define stages for model validation, staging, and production promotion. Automation gates (e.g., test suites, performance thresholds) can be triggered to advance a model to the next stage. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]
- **Integration with Unity Catalog**: All pipeline artifacts—datasets, features, models, and endpoints—are governed by [Unity Catalog](/concepts/unity-catalog.md), ensuring fine-grained access control and full lineage tracking. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]
- **Support for AI Gateway**: Deployed endpoints can be managed and monitored through [AI Gateway](/concepts/ai-gateway.md), which provides rate limiting, cost controls, and observability for serving. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

## Relationship to Other MLOps Tooling

MLOps Stacks complement other Databricks capabilities:

| Capability | Role in the Pipeline |
|------------|----------------------|
| [MLflow](/concepts/mlflow.md) | Experiment tracking, model registry, and reproducible runs. |
| [Unity Catalog](/concepts/unity-catalog.md) | Governance of data, features, models, and endpoints. |
| Batch Inference | Offline scoring for scheduled or bulk workloads. |
| Real-time Serving | Low-latency API endpoints for production predictions. |
| [Data Quality Monitoring](/concepts/data-quality-monitoring.md) | Continuous monitoring of input and output data. |

The stacks tie these together by providing a repeatable scaffold that enforces best practices for CI/CD and environment isolation. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

## Typical Use Cases

- **Enterprise MLOps**: Organisations with multiple data scientists who need consistent promotion workflows and auditability.
- **Regulatory Compliance**: Pipelines that must demonstrate a clear audit trail from raw data to deployed model.
- **Multi‑environment Deployments**: Teams that maintain separate development, staging, and production clusters with different configuration and access policies.

## Getting Started

Because MLOps Stacks are templates, the recommended starting point is to review the official Databricks documentation on [MLOps Stacks](/concepts/mlops-stacks.md) and then customise the provided templates to fit the organisation’s governance requirements and tool preferences. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

## Related Concepts

- MLOps
- Infrastructure-as-Code
- [CI/CD for Machine Learning](/concepts/cicd-for-machine-learning.md)
- [Model Registry](/concepts/mlflow-model-registry.md)
- [Model Serving](/concepts/model-serving.md)

## Sources

- databricks-data-science-and-ml-capabilities-databricks-on-aws.md

# Citations

1. [databricks-data-science-and-ml-capabilities-databricks-on-aws.md](/references/databricks-data-science-and-ml-capabilities-databricks-on-aws-8cf8bf4a.md)
