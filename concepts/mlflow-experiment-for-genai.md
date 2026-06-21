---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cf08a6f7630fac9ed90aad67b2eba64981a590f062d6bd804e3183fb3da43d3e
  pageDirectory: concepts
  sources:
    - get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-experiment-for-genai
    - MEFG
    - mlflow-experiments-for-genai-applications
    - MEFGA
  citations:
    - file: get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md
    - file: configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
title: MLflow Experiment for GenAI
description: A container in Databricks used to organize and manage GenAI application traces, runs, and experiment metadata, accessible via the Experiments UI under 'GenAI apps & agents'.
tags:
  - mlflow
  - experiments
  - databricks
  - genai
timestamp: "2026-06-19T10:44:31.694Z"
---

# MLflow Experiment for GenAI

An **MLflow Experiment** is the central organizational unit for [GenAI](/concepts/mlflow-genai-evaluate-api.md) application development and evaluation within the Databricks platform. It serves as a container for traces, runs, evaluations, and configurations related to a specific GenAI agent or application. Experiments enable teams to track, compare, and manage multiple iterations of their AI systems in a structured way.

## Overview

In the context of GenAI, an MLflow experiment acts as the top-level container for your application’s observability and evaluation data. It holds [Traces](/concepts/traces.md) (execution records of agent calls), runs (training or evaluation runs), and associated metadata. It also provides a workspace for configuring serverless budget policies that govern the compute resources used by scheduled scorers, synthetic evaluation generation, and agent evaluation workloads.^[get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md, configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Creating an MLflow Experiment

Experiments are created through the Databricks workspace UI:

1. In the left sidebar, under **AI/ML**, click **Experiments**.
2. At the top of the Experiments page, click **GenAI apps & agents**.
3. A new experiment is created. To obtain its ID and path for use in your application code, click the information icon (ⓘ) in the upper-left corner.

After creation, the experiment appears on the Experiments page and is ready to receive traces and runs from your GenAI application.^[get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md]

## Connecting to an Experiment

To send traces and run evaluations against an experiment, you configure your development environment to point to that experiment. Using the MLflow client library (`mlflow>=3.1` with Databricks connectivity), you set the tracking URI and experiment ID. The following environment variables are commonly used:

| Variable | Value |
|----------|-------|
| `DATABRICKS_TOKEN` | Your Databricks personal access token |
| `DATABRICKS_HOST` | Your workspace URL (e.g., `https://<workspace>.cloud.databricks.com`) |
| `MLFLOW_TRACKING_URI` | `databricks` |
| `MLFLOW_REGISTRY_URI` | `databricks-uce` |
| `MLFLOW_EXPERIMENT_ID` | The experiment ID obtained from the UI |

In application code, you can also call `mlflow.set_experiment()` with the experiment name or path to log traces and runs to that experiment.^[get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md]

## Configuring a Serverless Budget Policy

Experiments can be assigned a serverless budget policy to control which policy MLflow uses for any serverless workloads it creates on behalf of that experiment. This is essential when the workspace’s default budget policy is disabled, otherwise MLflow will return a `403 PERMISSION_DENIED` error when trying to run scheduled scorers, synthetic evaluation generation, or agent evaluation.^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

To assign a policy:

- **Via the UI**: Open the experiment, locate the **Details** panel, and set the **Budget policy** dropdown to a policy you have permission to use.
- **Via the API**: Use `mlflow.set_experiment_tag()` with the key `mlflow.workload_creation_policy_id` and the policy ID as the value. Users must have entitlement to use the specified policy.^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) – Observability for GenAI application execution.
- [GenAI apps & agents](/concepts/genai-app-lifecycle-management.md) – The experiment type used for GenAI workloads.
- [Serverless Budget Policy](/concepts/serverless-budget-policy.md) – Controls spending on serverless workloads.
- 403 PERMISSION_DENIED Serverless Budget Policy Error – Error when no budget policy is assigned.
- [GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) – Assessing agent quality using MLflow experiments.
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) – Ongoing quality checks with scheduled scorers.

## Sources

- get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md
- configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md

# Citations

1. [get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md](/references/get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws-58181913.md)
2. [configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md](/references/configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws-cb1d8a65.md)
