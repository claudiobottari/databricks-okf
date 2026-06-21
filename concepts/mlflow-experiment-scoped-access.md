---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1dabedebc1ad81f611dc487b9426371268f0d69ab9e97c01acff4a51d52cf2ba
  pageDirectory: concepts
  sources:
    - add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-experiment-scoped-access
    - MESA
  citations:
    - file: add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md
    - file: configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
title: MLflow Experiment Scoped Access
description: When an MLflow experiment is added as a resource, the app's access is scoped exclusively to that specific experiment; other experiments must be added as separate resources.
tags:
  - databricks-apps
  - mlflow
  - security
timestamp: "2026-06-18T14:19:01.057Z"
---

# MLflow Experiment Scoped Access

**MLflow Experiment Scoped Access** refers to the mechanisms that control and restrict which principals, applications, and workloads can interact with a given [MLflow Experiment](/concepts/mlflow-experiment.md) and at what permission level. Scoping ensures that access is limited to only the experiment explicitly designated, preventing unintended cross-experiment visibility or modification.

## Types of Scoped Access

### User and Application Permissions

When an [MLflow Experiment](/concepts/mlflow-experiment.md) is added as a resource to a Databricks App, the app's service principal receives permissions that are scoped exclusively to that experiment. The app cannot access other experiments unless they are added as separate resources. Three permission levels are available:

- **Can read** – View experiment metadata, runs, parameters, and metrics.
- **Can edit** – Modify experiment settings and metadata.
- **Can manage** – Full administrative access to the experiment.

^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

This scoping mechanism works by granting the app's service principal the specified permissions on the selected experiment. Because access is tied to a single experiment, a Databricks App can only log runs and retrieve data from the experiments it explicitly references. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

When the experiment resource is removed from an app, the app’s service principal loses access to that experiment. The experiment itself remains available to other users and applications with appropriate permissions. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

### Serverless Budget Policy Scoping

For experiments that run serverless workloads (such as scheduled scorers, synthetic evaluation set generation, or agent evaluation), you can set a **serverless budget policy** directly on the experiment. This controls which policy MLflow uses for serverless workloads it creates against that experiment, resolving the `403 PERMISSION_DENIED – unable to use fallback policies` error when the workspace’s default policy is disabled. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

The budget policy is scoped to the experiment: MLflow uses the specified policy for every serverless workload it creates for that particular experiment. This can be configured either through the experiment’s **Details** panel in the UI or by setting the `mlflow.workload_creation_policy_id` tag via the API: ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

```python
import mlflow

mlflow.set_experiment_tag(
    experiment_id="<your-experiment-id>",
    key="mlflow.workload_creation_policy_id",
    value="<your-policy-id>",
)
```

^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

After the tag is set, subsequent calls that create serverless workloads from the experiment (such as `Scorer.register()`) use the specified policy, effectively scoping the serverless spending authority to that experiment. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Best Practices

- **Organize experiments logically by project or model type** to keep scoped access boundaries clear and to improve discoverability. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]
- **Use consistent naming conventions for runs and parameters** to simplify access audits and debugging. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]
- **Set the serverless budget policy at the experiment level** when the workspace default policy is disabled, to avoid `403` errors on evaluation or monitoring workloads. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]
- **Assign the minimum permission level needed** for Databricks App resources (read vs. edit vs. manage) to follow the principle of least privilege. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Related Concepts

- [MLflow Experiments](/concepts/mlflow-experiment.md)
- Databricks Apps
- [Serverless Budget Policy](/concepts/serverless-budget-policy.md)
- 403 PERMISSION_DENIED Serverless Budget Policy Error
- MLflow Resources in Databricks Apps

## Sources

- add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md
- configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md

# Citations

1. [add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md](/references/add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws-2dc6c6e2.md)
2. [configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md](/references/configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws-cb1d8a65.md)
