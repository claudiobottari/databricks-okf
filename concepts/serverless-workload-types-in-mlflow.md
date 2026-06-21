---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c45bb7d3c0e4c786978c7874e72e66da3d2a2feeb0fd4f018169ef0b67a1b324
  pageDirectory: concepts
  sources:
    - configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - serverless-workload-types-in-mlflow
    - SWTIM
  citations:
    - file: configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
title: Serverless Workload Types in MLflow
description: "The three types of MLflow serverless workloads affected by budget policies: scheduled scorers, synthetic evaluation set generation, and agent evaluation."
tags:
  - mlflow
  - serverless
  - workloads
  - gen-ai
timestamp: "2026-06-19T09:22:35.158Z"
---

# Serverless Workload Types in MLflow

**Serverless Workload Types in MLflow** refers to the categories of compute workloads that MLflow executes on behalf of users in a serverless architecture, particularly for evaluation, monitoring, and data generation tasks. These workloads require a [Serverless Budget Policy](/concepts/serverless-budget-policy.md) to be configured on the MLflow experiment to control resource usage and costs.

## Overview

MLflow automatically creates serverless workloads for several operational tasks related to [GenAI](/concepts/mlflow-genai-evaluate-api.md) evaluation and monitoring. These workloads run in a serverless compute environment, meaning the infrastructure is managed by the platform rather than the user. However, this requires that a budget policy be assigned to control spending and resource allocation.^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Serverless Workload Types

### Scheduled Scorers (Production Monitoring)

Scheduled scorers are serverless workloads that periodically evaluate [GenAI](/concepts/mlflow-genai-evaluate-api.md) applications in production. They run on a defined schedule to continuously assess the quality of model outputs against specified criteria. These scorers are created and managed through the [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) workflow.^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

### Agent Evaluation

Agent evaluation workloads run assessments of GenAI agents using [judges](/concepts/llm-judges.md) to score agent responses against quality criteria. This includes both offline evaluation during development and ongoing evaluation in production. The [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) API (`mlflow.genai.evaluate()`) triggers these serverless workloads.^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

### Synthetic Evaluation Set Generation

Synthetic evaluation set generation workloads produce test data for evaluating [GenAI](/concepts/mlflow-genai-evaluate-api.md) applications. These workloads use AI models to create realistic input-output pairs that can be used to assess agent quality without requiring manually curated datasets.^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Default Behavior and Error Handling

By default, all serverless workloads created by MLflow use the workspace's default serverless budget policy. If the workspace disables this default policy — which may occur when each user and service principal must select a dedicated policy — MLflow cannot choose a fallback policy. This results in a 403 PERMISSION_DENIED Serverless Budget Policy Error when attempting to register a scorer or run an evaluation.^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Configuration

To enable these serverless workloads, users must assign a budget policy to the MLflow experiment. This can be done through:

- **UI**: Set the **Budget policy** in the experiment's **Details** panel.
- **API**: Use `mlflow.set_experiment_tag()` with the `mlflow.workload_creation_policy_id` tag.

Once configured, MLflow uses the specified policy for every serverless workload it creates for the experiment, including all three workload types.^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Related Concepts

- [Serverless Budget Policy](/concepts/serverless-budget-policy.md) — The control mechanism for workload spending
- [MLflow experiments](/concepts/mlflow-experiment.md) — The organizational unit for runs and evaluations
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Scheduled scoring workflow
- [Agent Evaluation](/concepts/mlflow-agent-evaluation.md) — Assessment workflow for GenAI agents
- [Synthetic Evaluation Generation](/concepts/synthetic-evaluation-data-generation.md) — Test data creation workflow
- [Custom Judges](/concepts/custom-judges.md) — LLM-based scorers used in evaluation workloads
- 403 PERMISSION_DENIED Serverless Budget Policy Error — Error when no policy is available

## Sources

- configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md

# Citations

1. [configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md](/references/configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws-cb1d8a65.md)
