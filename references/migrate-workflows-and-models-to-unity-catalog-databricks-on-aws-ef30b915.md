---
title: Migrate workflows and models to Unity Catalog | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/migrate-to-uc
ingestedAt: "2026-06-18T08:11:24.981Z"
---

Databricks recommends using Models in Unity Catalog for improved governance, easy sharing across workspaces and environments, and more flexible MLOps workflows. This page steps you through migrating models in the Workspace Model Registry to Unity Catalog.

## Introduction to models in Unity Catalog[​](#introduction-to-models-in-unity-catalog "Direct link to introduction-to-models-in-unity-catalog")

Models in Unity Catalog extends the benefits of Unity Catalog to ML models, including centralized access control, auditing, lineage, and model sharing and discovery across workspaces. Models in Unity Catalog also provides greater flexibility in managing the model lifecycle.

When you migrate models to Unity Catalog, some model lifecycle steps are done differently:

*   Workspace Model Registry permissions are replaced by account-level Unity Catalog permissions. See [Step 2. Assign Unity Catalog permissions to the model](#permissions).
*   Stages are replaced by custom aliases and tags. Instead of four fixed stages, you can create up to 10 custom and reassignable aliases. You can also set tags to label models. See [Step 4. Migrate model metadata](#stages-tags).
*   Deployment jobs are used to transition models through their lifecycle. See [Step 6. (Optional) Create a deployment job](#deployment-job).

## Step 1. Create a model in Unity Catalog[​](#step-1-create-a-model-in-unity-catalog "Direct link to step-1-create-a-model-in-unity-catalog")

See [Train and register Unity Catalog\-compatible models](https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/#train).

## Step 2. Assign Unity Catalog permissions to the model[​](#step-2-assign-unity-catalog-permissions-to-the-model "Direct link to step-2-assign-unity-catalog-permissions-to-the-model")

Unity Catalog has a [unified permission model](https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/privileges-reference). To learn how to assign permissions to models in Unity Catalog, see [Control access to models](https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/#control-access-to-models).

The following table shows the relationship between permissions in the workspace model registry and privileges in Unity Catalog. In addition to the privileges shown in the table, all actions also require `USE CATALOG` and `USE SCHEMA` privileges.

## Step 3. Copy model versions[​](#step-3-copy-model-versions "Direct link to Step 3. Copy model versions")

To copy model versions, use `copy_model_version()` with MLflow client >= `3.4.0`.

Python

    import mlflowfrom mlflow import MlflowClient# Registry must be set to workspace registrymlflow.set_registry_uri("databricks")client = MlflowClient(registry_uri="databricks")src_model_uri = f"models:/my_wmr_model/1"uc_migrated_copy = client.copy_model_version(   src_model_uri, "mycatalog.myschema.my_uc_model")

If the destination model does not exist in Unity Catalog, it is created by this API call.

Models in Unity Catalog require a signature. If the workspace model version doesn't have a signature, Databricks recommends that you create one by following the instructions in the [MLflow documentation](https://mlflow.org/docs/latest/ml/model/signatures/). Another alternative is to use the environment variable `MLFLOW_SKIP_SIGNATURE_CHECK_FOR_UC_REGISTRY_MIGRATION`. This environment variable is only available when you use `copy_model_version()` and requires MLflow version `3.4.0` or above. When this environment variable is set to `"true"`, a signature is not required.

For a script that you can use to migrate all of the model versions of a model in your workspace model registry to a destination Unity Catalog model, see [Migrate model versions from Workspace Model Registry to Unity Catalog](https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/migrate-models).

This section describes how to map workspace registry-level metadata to Unity Catalog model and model version metadata, such as stages, tags, and descriptions.

### Stages[​](#stages "Direct link to Stages")

The Workspace Model Registry used the concept of "stages", such as `Staging` and `Production`, to track the model lifecycle. You could search for or call models by stage. In Unity Catalog, stages have been replaced by [aliases](https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/#uc-model-aliases) for calling a model and by [tags](#tags) for labeling models.

For simple migration of Workspace Model Registry stages, you can directly use "Production" and "Staging" or any other alias names you prefer. In the Workspace Model Registry, multiple model versions could be in the same stage, and the latest version was called when you referenced a model version. In Unity Catalog, an alias is assigned to a unique model version.

For simple migration of stage labels, use tags to label model versions as "Production", "Staging", or "Archived". You can use any other label as well. For more info on tags, see [Tags](#tags).

In the Workspace Model Registry, the lifecycle of a model version was tracked by stage, and human approval was required for a transition request. In Unity Catalog, the lifecycle of a model version is managed by a [deployment job](https://docs.databricks.com/aws/en/mlflow/deployment-job). Each task in the deployment job corresponds to a "stage". Deployment jobs allow you to customize the model lifecycle and accommodate more complicated workflows than the Workspace Model Registry. Deployment jobs still accommodate human approvals. For details, see [MLflow 3 deployment jobs](https://docs.databricks.com/aws/en/mlflow/deployment-job).

### Tags[​](#tags "Direct link to Tags")

In Unity Catalog, you create [tags](https://docs.databricks.com/aws/en/admin/governed-tags/) on the model or model version.

![Add tags button in Unity Catalog model version UI.](data:image/png;base64,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)

To search for a model by tag in Catalog Explorer, type the key or value into the search box:

![Search for models by tag in the Unity Catalog model UI.](https://docs.databricks.com/aws/en/assets/images/search-by-tag-5d6bebceeb4926da8756b9b6d51dc2cd.png)

In Catalog Explorer, you can use tags only to search for models, not model versions. The MLflow client does not support searching for models by Unity Catalog tags. Unity Catalog allows at most 50 tags per object.

### Description and comments[​](#description-and-comments "Direct link to Description and comments")

You can add descriptions to the model and model version. Unity Catalog also provides the option of an [AI-generated description for the model](https://docs.databricks.com/aws/en/comments/ai-comments).

![Add model or model version description in Unity Catalog.](https://docs.databricks.com/aws/en/assets/images/uc-model-add-description-95c4ff96734b6d23a50cb32e177f5c67.png)

Models in Unity Catalog don't have a corresponding location for the information shown in the **Activities** section on the model version page in the workspace model registry. If there is information in that section that you want to transfer with the model version, copy it into the **Description** section of the model version page in Unity Catalog.

## Step 5. Update all workloads and endpoints[​](#step-5-update-all-workloads-and-endpoints "Direct link to Step 5. Update all workloads and endpoints")

After you migrate models and model versions to Unity Catalog, update all jobs, notebooks, and other workloads, including model serving endpoints, to use the versions in Unity Catalog.

## Step 6. (Optional) Create a deployment job[​](#step-6-optional-create-a-deployment-job "Direct link to step-6-optional-create-a-deployment-job")

A deployment job automatically triggers whenever a new model version is created and automates the evaluation, approval, and deployment workflow. For details, see [MLflow 3 deployment jobs](https://docs.databricks.com/aws/en/mlflow/deployment-job).

You can set notifications to trigger on events such as the creation or approval of a model version. See [Add notifications on a job](https://docs.databricks.com/aws/en/jobs/notifications).

If you had email notifications set up for events in the Workspace Model Registry, migrate them as follows:

*   New model version was created: Set up a deployment job that is triggered when a new model version is created, and an email notification when the job is triggered.
*   Stage transition request: Stage transition requests correspond to approval tasks. Set an email notification for the approval task's success or failure.
*   Stage transitions: Stage transitions correspond to job tasks. Set an email notification for the task's success or failure.
*   New comments: Comments are not supported in Unity Catalog.

If you had webhooks set up for events, you can implement them in Unity Catalog as model event job triggers. Model triggers allow you to [automate Lakeflow Jobs](https://docs.databricks.com/aws/en/jobs/triggers) based on the creation of new models, model versions, or model aliases in Unity Catalog. Model triggers are in [Private Preview](https://docs.databricks.com/aws/en/release-notes/release-types). Contact your Databricks representative for more information.

## More information[​](#more-information "Direct link to More information")

The pages linked below describe how to migrate workflows (model training and batch inference jobs) from the Workspace Model Registry to Unity Catalog.

*   [Upgrade ML workflows to target models in Unity Catalog](https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/upgrade-workflows)
*   [Migrate model versions from Workspace Model Registry to Unity Catalog](https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/migrate-models)
