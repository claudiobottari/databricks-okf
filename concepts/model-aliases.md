---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 408a64ce38957bd5d753cd260c9a1eecfa4aa38db3f8956f9633e9e43b4be771
  pageDirectory: concepts
  sources:
    - manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-aliases
    - Aliases
    - Model Aliases and Stages
  citations:
    - file: manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md
title: Model Aliases
description: Mutable, named references assigned to specific model versions for indicating deployment status (e.g., 'Champion'), enabling decoupled deployment workflows.
tags:
  - machine-learning
  - model-registry
  - deployment
timestamp: "2026-06-19T19:24:11.815Z"
---

```markdown
---
title: Model Aliases
summary: A mutable named reference to a particular version of a registered model in Unity Catalog, used to indicate deployment status and decouple batch inference or serving from specific version numbers.
sources:
  - manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md
kind: concept
createdAt: "2026-07-07T22:00:00.000Z"
updatedAt: "2026-07-07T22:00:00.000Z"
tags:
  - databricks
  - unity-catalog
  - mlflow
  - model-registry
  - deployment
aliases:
  - model-alias
  - alias
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Model Aliases

**Model aliases** allow you to assign a mutable, named reference to a specific version of a [[Models in Unity Catalog|registered model in Unity Catalog]]. They are used to indicate the deployment status of a model version—for example, a "Champion" alias can point to the version currently in production. By targeting an alias in workloads, you can update the production model simply by reassigning the alias to a different version, decoupling model deployments from your batch inference or serving code. ^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Set and delete aliases

**Permissions required**: Owner of the registered model, plus `USE SCHEMA` and `USE CATALOG` privileges on the schema and catalog containing the model. ^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

You can set, update, and remove aliases using the [[Catalog Explorer|Databricks Catalog Explorer]] UI or the MLflow Client API. In the UI, hover over a model version row on the model details page, click **Add alias**, enter or select an alias, and save. To remove, click the pencil icon next to the alias, then the `X` for the alias to remove, and save. ^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

Using the API with the `MlflowClient`:

```python
from mlflow import MlflowClient
client = MlflowClient()

# create "Champion" alias for version 1
client.set_registered_model_alias("prod.ml_team.iris_model", "Champion", 1)

# reassign the alias to version 2
client.set_registered_model_alias("prod.ml_team.iris_model", "Champion", 2)

# get the model version currently pointed to by the alias
client.get_model_version_by_alias("prod.ml_team.iris_model", "Champion")

# delete the alias
client.delete_registered_model_alias("prod.ml_team.iris_model", "Champion")
```

^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Load a model version by alias for inference

**Permissions required**: `EXECUTE` privilege on the registered model, plus `USE SCHEMA` and `USE CATALOG` on the schema and catalog containing the model. ^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

Batch inference workloads can reference a model version by alias using the URI format `models:/<catalog>.<schema>.<model>@<alias>`. For example:

```python
import mlflow.pyfunc

model_version_uri = "models:/prod.ml_team.iris_model@Champion"
champion_version = mlflow.pyfunc.load_model(model_version_uri)
champion_version.predict(test_x)
```

If the "Champion" alias is later reassigned to a new model version, the batch workload automatically picks up the new version on its next execution. ^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

[[Model Serving Endpoint|Model serving endpoints]] can also reference a model version by alias. You can use the model serving REST API to update an endpoint to serve the version currently pointed to by an alias, as shown below:

```python
import mlflow
import requests

client = mlflow.tracking.MlflowClient()
champion_version = client.get_model_version_by_alias("prod.ml_team.iris_model", "Champion")

# Invoke the model serving REST API to update endpoint to serve the current "Champion" version
model_name = champion_version.name
model_version = champion_version.version
requests.request(...)
```

^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Relationship to stages

Stages (e.g., "Staging", "Production") are **not supported** for models in Unity Catalog. Databricks recommends using the three-level namespace to express the environment a model is in, and using aliases to promote models for deployment. Aliases provide the same semantic flexibility as stages but with a simpler, mutable reference model. ^[manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Related concepts

- [[Models in Unity Catalog|Registered model (Unity Catalog)]]
- [[MLflow Model Registry]]
- [[Unity Catalog]]
- [[Model Serving]]
- [[Batch Inference Pipelines|Batch inference]]
- Model deployment workflows

## Sources

- manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md
```

# Citations

1. [manage-model-lifecycle-in-unity-catalog-databricks-on-aws.md](/references/manage-model-lifecycle-in-unity-catalog-databricks-on-aws-5d1bac95.md)
