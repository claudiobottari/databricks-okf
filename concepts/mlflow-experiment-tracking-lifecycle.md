---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 098d7245c65cabf7efd738f9f3625241c5d10b52530b3c9dabe71aa5a7519b62
  pageDirectory: concepts
  sources:
    - add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md
  confidence: 0.85
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - mlflow-experiment-tracking-lifecycle
    - METL
    - ETL
  citations:
    - file: add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md
    - file: configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
    - file: create-a-custom-judge-using-make_judge-databricks-on-aws.md
title: MLflow Experiment Tracking Lifecycle
description: Structured workflow for organizing AI/ML development lifecycle using MLflow experiments — including logging runs, parameters, metrics, artifacts, debugging agent traces, evaluating LLM quality, and versioning prompt templates.
tags:
  - mlflow
  - experiment-tracking
  - llm
  - mlops
timestamp: "2026-06-19T13:53:34.743Z"
---

# MLflow Experiment Tracking Lifecycle

The **MLflow Experiment Tracking Lifecycle** describes the full set of stages a team works through when using [MLflow experiments](/concepts/mlflow-experiment.md) to develop AI applications, agents, LLMs, and machine learning models. It covers everything from initial experiment creation and configuration, through run logging and evaluation, to ongoing management and eventual cleanup.

## Lifecycle Phases

### 1. Create and Configure

An MLflow experiment is the organizational unit that collects related runs. You can create an experiment directly in the MLflow UI, through the MLflow API, or by adding it as a resource to a Databricks App. When added as an app resource, the app’s service principal receives the specified permission level — **Can read**, **Can edit**, or **Can manage** — scoped to that experiment.^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

Configuration also includes setting a **serverless budget policy** if your experiment will run serverless workloads such as scheduled scorers, synthetic evaluation generation, or agent evaluation. If the workspace’s default budget policy is disabled, you must assign a fallback policy to the experiment; otherwise, MLflow returns a 403 error when trying to start serverless tasks. Use `mlflow.set_experiment_tag()` to set the `mlflow.workload_creation_policy_id` tag on the experiment.^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

### 2. Log Runs

With the experiment active, you log training runs using the MLflow Tracking API. Within a `mlflow.start_run()` context, you can record parameters, metrics, artifacts, and tags. For Databricks Apps, the experiment ID is injected as an environment variable (e.g., `MLFLOW_EXPERIMENT_ID`) so that the app can log runs without hardcoding identifiers.^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

```python
import mlflow

mlflow.set_experiment(experiment_id=os.getenv("MLFLOW_EXPERIMENT_ID"))

with mlflow.start_run():
    mlflow.log_param("learning_rate", 0.01)
    mlflow.log_metric("accuracy", 0.95)
    mlflow.log_artifact("model.pkl")
```

### 3. Evaluate Runs

Evaluation is a key part of the lifecycle for AI agents and LLMs. Use `mlflow.genai.evaluate()` to run offline evaluations against a shared dataset, scoring outputs with [Custom Judges](/concepts/custom-judges.md). Multiple agent configurations can be compared in an A/B test by running separate evaluations on the same data and judges, then comparing the structured feedback values (e.g., `fully_resolved`, `meets_expectations`, `true`).^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

```python
result_a = mlflow.genai.evaluate(
    data=dataset,
    predict_fn=agent_a,
    scorers=[my_judge],
)
result_b = mlflow.genai.evaluate(
    data=dataset,
    predict_fn=agent_b,
    scorers=[my_judge],
)
```

### 4. Manage and Monitor

During and after development, experiments require ongoing management. You can:

- View experiment metadata, run history, parameters, and metrics via the MLflow UI or API.
- Debug agents and LLM applications with execution traces.
- Manage and version prompt templates.
- Update the experiment’s budget policy as needed.
- Grant or revoke app service principal access when adding or removing the experiment as a resource.^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

For production monitoring, scheduled scorers and other serverless workloads rely on the budget policy assigned to the experiment. If the policy is misconfigured, those workloads may fail with a 403 error.^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

### 5. Cleanup and Retention

Experiments accumulate runs, artifacts, and metadata over time. Databricks recommends that you consider retention policies and storage management for long-running projects. Organize experiments logically by project or model type, and use consistent naming conventions for runs and parameters to make cleanup easier. When an experiment resource is removed from an app, the app’s service principal loses access, but the experiment itself remains available to other users and apps with permissions.^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Best Practices

- **Organize experiments logically** by project or model type to improve discoverability.^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]
- **Use consistent naming conventions** for runs and parameters across your organization.^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]
- **Set a budget policy early** if your experiment will run serverless workloads — otherwise, those workloads may fail.^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]
- **Control one variable at a time** in A/B comparisons and use a representative evaluation dataset. Align judges with human feedback as you gather expert annotations.^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]
- **Document experiment configurations** (parameters, prompts, code versions) to ensure reproducibility.^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Related Concepts

- [MLflow experiments](/concepts/mlflow-experiment.md) — The core organizational unit for runs.
- [Serverless Budget Policy](/concepts/serverless-budget-policy.md) — Controls spending for serverless workloads tied to an experiment.
- [Custom Judges](/concepts/custom-judges.md) — LLM-based scorers used during evaluation.
- [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) — Evaluating multiple configurations side-by-side.
- Databricks Apps — Platform for deploying applications that use MLflow experiments.
- [MLflow Tracking API](/concepts/mlflow-tracking.md) — The programmatic interface for logging and querying runs.

## Sources

- add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md
- configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
- create-a-custom-judge-using-make_judge-databricks-on-aws.md

# Citations

1. [add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md](/references/add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws-2dc6c6e2.md)
2. [configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md](/references/configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws-cb1d8a65.md)
3. [create-a-custom-judge-using-make_judge-databricks-on-aws.md](/references/create-a-custom-judge-using-make_judge-databricks-on-aws-956237bf.md)
