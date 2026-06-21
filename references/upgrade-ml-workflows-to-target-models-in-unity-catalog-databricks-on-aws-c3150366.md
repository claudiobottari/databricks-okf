---
title: Upgrade ML workflows to target models in Unity Catalog | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/upgrade-workflows
ingestedAt: "2026-06-18T08:11:27.936Z"
---

This article explains how to migrate and upgrade existing [Databricks workflows](https://docs.databricks.com/aws/en/jobs/) to use models in Unity Catalog.

## Requirements[​](#requirements "Direct link to Requirements")

### Required privileges[​](#required-privileges "Direct link to Required privileges")

To execute a model training, deployment, or inference workflow in Unity Catalog, the principal running the workflow must have `USE CATALOG` and `USE SCHEMA` privileges on the catalog and schema that hold the model.

The following privileges are also required:

*   To create a model, the principal must have the `CREATE MODEL` privilege.
*   To load or deploy a model, the principal must have the `EXECUTE` privilege on the registered model.
*   To create a new model version, the principal must be the owner of the registered model, or have the [`CREATE MODEL VERSION`](https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/privileges-reference#create-model-version) privilege on it.
*   To set an alias on a registered model, the principal must be the owner of the registered model.

### Compute requirements[​](#compute-requirements "Direct link to Compute requirements")

The compute resource specified for the workflow must have access to Unity Catalog. See [Access modes](https://docs.databricks.com/aws/en/compute/configure#access-mode).

## Create parallel training, deployment, and inference workflows[​](#create-parallel-training-deployment-and-inference-workflows "Direct link to Create parallel training, deployment, and inference workflows")

To upgrade model training and inference workflows to Unity Catalog, Databricks recommends an incremental approach in which you create a parallel training, deployment, and inference pipeline that leverage models in Unity Catalog. When you're comfortable with the results using Unity Catalog, you can switch downstream consumers to read the batch inference output, or increase the traffic routed to models in Unity Catalog in serving endpoints.

## Model training workflow[​](#model-training-workflow "Direct link to model-training-workflow")

[Clone](https://docs.databricks.com/aws/en/jobs/configure-job#aux-job) your model training workflow. Confirm that the principal running the workflow and the compute specified for the workflow meet the [Requirements](#requirements).

Next, modify the model training code in the cloned workflow. You might need to clone the notebook run by the workflow, or create and target a new git branch in the cloned workflow. Follow [these steps](https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/#upgrade-training-workloads-for-uc) to install the necessary version of MLflow and configure the client to target Unity Catalog in your training code. Then, update the model training code to register models to Unity Catalog. See [Train and register Unity Catalog\-compatible models](https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/#train).

## Model deployment workflow[​](#model-deployment-workflow "Direct link to model-deployment-workflow")

[Clone](https://docs.databricks.com/aws/en/jobs/configure-job#aux-job) your model deployment workflow. Confirm that the principal running the workflow and the compute specified for the workflow meet the [Requirements](#requirements).

If you have model validation logic in your deployment workflow, update it to [load model versions from UC](https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/#load-models-for-inference). Use [aliases](https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/#uc-model-aliases) to manage production model rollouts.

## Model inference workflow[​](#model-inference-workflow "Direct link to model-inference-workflow")

### Batch inference workflow[​](#batch-inference-workflow "Direct link to Batch inference workflow")

[Clone](https://docs.databricks.com/aws/en/jobs/configure-job#aux-job) the batch inference workflow. Confirm that the principal running the workflow and the compute specified for the workflow meet the [Requirements](#requirements).

### Model serving workflow[​](#model-serving-workflow "Direct link to Model serving workflow")

If you are using [Model Serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/), you don't need to clone your existing endpoint. Instead, use the [traffic split](https://docs.databricks.com/aws/en/machine-learning/model-serving/serve-multiple-models-to-serving-endpoint) feature to start routing a small fraction of traffic to models in Unity Catalog. As you review the results using Unity Catalog, increase the amount of traffic until all of the traffic is rerouted.

Promoting a model across environments works differently with models in Unity Catalog. For details, see [Promote a model across environments](https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/#promote).

## Use job webhooks for manual approval for model deployment[​](#use-job-webhooks-for-manual-approval-for-model-deployment "Direct link to use-job-webhooks-for-manual-approval-for-model-deployment")

Databricks recommends that you automate model deployment if possible, using appropriate checks and tests during the model deployment process. However, if you do need to perform manual approvals to deploy production models, you can use [job notifications](https://docs.databricks.com/aws/en/jobs/notifications#configure-system-notifications) to call out to external CI/CD systems to request manual approval for deploying a model, after your model training job completes successfully. After manual approval is provided, your CI/CD system can then deploy the model version to serve traffic, for example by setting the “Champion” alias on it.
