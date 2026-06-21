---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d8a4839f7d23e8c978566b18386fd0c6206a3b6b8a8fdd5267c3f2f55aea045b
  pageDirectory: concepts
  sources:
    - finetune-llama-32-3b-with-unsloth-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-for-ml-model-management
    - UCFMMM
  citations:
    - file: finetune-llama-32-3b-with-unsloth-databricks-on-aws.md
    - file: abac-grant-policies-for-models-beta-databricks-on-aws.md
    - file: configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
title: Unity Catalog for ML Model Management
description: A Databricks feature for registering, versioning, and managing machine learning models as first-class assets within a governed catalog-schema hierarchy, enabling deployment to model serving endpoints.
tags:
  - mlops
  - model-registry
  - databricks
timestamp: "2026-06-18T12:22:45.962Z"
---

# Unity Catalog for ML Model Management

**Unity Catalog** is the unified governance solution for data and AI assets on the Databricks Lakehouse Platform. For ML model management, Unity Catalog provides a centralized registry where teams can register, version, discover, govern, and deploy machine learning models alongside their data assets.

## Core Concepts

### Model Registry

Unity Catalog serves as the primary model registry for MLflow, replacing the legacy workspace-level model registry. Models are organized within the Unity Catalog **three-level namespace** (`catalog.schema.model_name`), enabling consistent governance across data and AI assets. ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]

### Model Versioning

Every model registered in Unity Catalog has a version history. When a model is registered (for example, via `mlflow.transformers.log_model()`), Unity Catalog creates a new model version. Each version can have its own stage (such as "Staging" or "Production"), loaded model signature, and associated metadata. ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]

## Key Capabilities

### Centralized Model Storage

Models are stored in Unity Catalog-managed volumes, providing a single location for model artifacts, checkpoints, and deployment artifacts. This eliminates the need for separate model storage systems and enables cross-team discovery. ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]

### Access Control

Unity Catalog provides three layers of access control for models:

- **Catalog-level permissions** (`USE CATALOG`, `CREATE MODEL`, etc.)
- **Schema-level permissions** (`USE SCHEMA`, `CREATE MODEL`, etc.)
- **Model-level permissions** (`EXECUTE`, `APPLY TAG`, etc.)

The `EXECUTE` privilege on a model allows a principal to call that model via inference. It is the primary privilege for model consumption. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

### Governance with Tags and ABAC

Models can carry **governed tags** — key-value pairs defined in the Unity Catalog tag taxonomy. These tags serve as the basis for **Attribute-Based Access Control (ABAC)** policies:

- **[ABAC GRANT Policy](/concepts/abac-grant-policy.md)**: Dynamically grants `EXECUTE` on models whose tags match a condition, without enumerating individual model names.
- **[Column Mask Policies](/concepts/column-mask-policies.md)** and **[Row Filter Policies](/concepts/row-filter-policies.md)**: Although designed for tables, these policies can also be applied to model metadata stored as tables in Unity Catalog. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

### Model Lineage

Unity Catalog tracks model lineage automatically. When a model is created from an [MLflow Run](/concepts/mlflow-run.md), the model version is linked to the training run, experiment, and source code. This lineage information is visible in the Unity Catalog UI and can be queried via the `system.access.audit` system table. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Workflow for Model Management

### 1. Training

Models are trained in notebooks or jobs, with training metrics logged to MLflow. The training run is automatically associated with the Unity Catalog experiment. ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]

### 2. Registration

After training, the model is registered in Unity Catalog using `mlflow.<framework>.log_model()` (e.g., `mlflow.transformers.log_model()`). This creates a model version in the specified `catalog.schema.model_name` namespace. ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]

### 3. Versioning

Each registration creates a new version. Versions can be promoted through stages (Staging → Production → Archived) using the Unity Catalog UI or API. ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]

### 4. Deployment

Models are deployed to **Model Serving endpoints**, which read the model version from Unity Catalog. The serving infrastructure can access the model because the `EXECUTE` privilege is granted to the serving role or service principal. ^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]

### 5. Monitoring

Deployed models can be monitored via:

- **Scheduled scorers** (production monitoring) that run against the registered model
- **Agent evaluation** workflows that use the model as a judge or generator
- **Audit logs** (`system.access.audit`) that record every inference call

^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Integration with MLflow

Unity Catalog for model management is tightly integrated with MLflow:

| MLflow Feature | Unity Catalog Role |
|---------------|-------------------|
| `mlflow.set_experiment()` | Sets the active Unity Catalog experiment |
| `mlflow.transformers.log_model()` | Registers a model in Unity Catalog |
| `mlflow.<framework>.log_model(registered_model_name=...)` | Registers with a specific model name in Unity Catalog |
| `mlflow.start_run()` | Tracks training runs under an experiment |
| `mlflow.set_experiment_tag()` | Sets governed tags on the experiment |
| `model_info.model_uri` | Returns the Unity Catalog URI for the registered model |

^[finetune-llama-32-3b-with-unsloth-databricks-on-aws.md]

## Best Practices

- **Use the three-level namespace**: Always specify `catalog.schema.model_name` when registering models to leverage Unity Catalog governance.
- **Set governed tags on models**: Apply lifecycle tags (e.g., `lifecycle = 'production'`) so ABAC policies can control access without explicit grants per model.
- **Audit model access**: Regularly run `SHOW GRANTS` and `SHOW EFFECTIVE POLICIES` on models to ensure only intended principals have `EXECUTE`.
- **Use serverless budget policies**: For MLflow experiments that create serverless workloads (scheduled scorers, evaluations), set a budget policy to avoid `403 PERMISSION_DENIED` errors. See 403 PERMISSION_DENIED Serverless Budget Policy Error.
- **Register models with a consistent naming convention**: Use meaningful model names that reflect the model's purpose and lineage.

## Related Concepts

- MLflow Models — The MLflow model format and registry
- [ABAC GRANT Policy](/concepts/abac-grant-policy.md) — Attribute-based grant policies for models (Beta)
- [Governed Tags](/concepts/governed-tags.md) — Tags that drive ABAC policy evaluation
- [Model Serving](/concepts/model-serving.md) — Deploying models from Unity Catalog to serving endpoints
- [MLflow Experiments](/concepts/mlflow-experiment.md) — The organizational unit for MLflow runs
- [Serverless Budget Policy](/concepts/serverless-budget-policy.md) — Controlling spending for serverless ML workloads

## Sources

- finetune-llama-32-3b-with-unsloth-databricks-on-aws.md
- configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
- abac-grant-policies-for-models-beta-databricks-on-aws.md

# Citations

1. [finetune-llama-32-3b-with-unsloth-databricks-on-aws.md](/references/finetune-llama-32-3b-with-unsloth-databricks-on-aws-83073ff0.md)
2. [abac-grant-policies-for-models-beta-databricks-on-aws.md](/references/abac-grant-policies-for-models-beta-databricks-on-aws-49466796.md)
3. [configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md](/references/configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws-cb1d8a65.md)
