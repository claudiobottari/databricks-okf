---
title: Create custom model serving endpoints | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/model-serving/create-manage-serving-endpoints
ingestedAt: "2026-06-18T08:11:48.804Z"
---

This article describes how to create model serving endpoints that serve [custom models](https://docs.databricks.com/aws/en/machine-learning/model-serving/custom-models) using Databricks [Model Serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/).

Model Serving provides the following options for serving endpoint creation:

*   The Serving UI
*   REST API
*   MLflow Deployments SDK

For creating endpoints that serve generative AI models, see [Create foundation model serving endpoints](https://docs.databricks.com/aws/en/machine-learning/model-serving/create-foundation-model-endpoints).

## Requirements[​](#requirements "Direct link to requirements")

*   Your workspace must be in a [supported region](https://docs.databricks.com/aws/en/machine-learning/model-serving/model-serving-limits#regions).
*   If you use custom libraries or libraries from a private mirror server with your model, see [Use custom Python libraries with Model Serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/private-libraries-model-serving) before you create the model endpoint.
*   For creating endpoints using the MLflow Deployments SDK, you must install the MLflow Deployment client. To install it, run:

Python

    import mlflow.deploymentsclient = mlflow.deployments.get_deploy_client("databricks")

## Identity and access[​](#identity-and-access "Direct link to identity-and-access")

To create or update a model serving endpoint, both the caller and the endpoint's recorded creator must:

*   Be a member of the workspace.
*   Hold the `workspace-access` entitlement.

### Creator identity[​](#creator-identity "Direct link to Creator identity")

When you create an endpoint, Databricks records the calling identity as the endpoint's **creator**. This identity — typically a service principal — is used to access Unity Catalog resources on behalf of the endpoint and cannot be changed after creation.

If the recorded creator lacks the required Unity Catalog grants or has been removed from the workspace, you must delete the endpoint and recreate it under a service principal that has the required permissions and is a current workspace member.

Configuration and served-entity updates re-evaluate the recorded creator's workspace membership and grants. Updates fail with `PERMISSION_DENIED` if the recorded creator is no longer a workspace member, even when the caller has valid permissions.

### Served entity grants[​](#served-entity-grants "Direct link to Served entity grants")

The recorded creator must hold the following grants on each served entity. Grants validated at endpoint creation or update cause the request to fail with `PERMISSION_DENIED` if missing. Grants required at query time are not validated upfront — missing grants cause runtime errors when the endpoint serves traffic.

note

If a Unity Catalog model declares transitive function dependencies, the recorded creator also needs `EXECUTE` on those upstream functions.

### Manage endpoint access[​](#manage-endpoint-access "Direct link to Manage endpoint access")

To understand access control options for model serving endpoints, see [Manage permissions on a model serving endpoint](https://docs.databricks.com/aws/en/machine-learning/model-serving/manage-serving-endpoints#permissions).

## Create an endpoint[​](#create-an-endpoint "Direct link to create-an-endpoint")

*   Serving UI
*   REST API
*   MLflow Deployments SDK
*   Workspace Client

You can create an endpoint for model serving with the **Serving** UI.

1.  Click **Serving** in the sidebar to display the Serving UI.
    
2.  Click **Create serving endpoint**.
    
    ![Model serving pane in Databricks UI](https://docs.databricks.com/aws/en/assets/images/serving-pane-ea28c77158ce07121e7c86bd9aa897ac.png)
    

For models registered in the Workspace model registry or models in Unity Catalog:

1.  In the **Name** field provide a name for your endpoint.
    
    *   Endpoint names cannot use the `databricks-` prefix. This prefix is reserved for Databricks preconfigured endpoints.
2.  In the **Served entities** section
    
    1.  Click into the **Entity** field to open the **Select served entity** form.
    2.  Select either **My models- Unity Catalog** or **My models- Model Registry** based on where your model is registered. The form dynamically updates based on your selection.
        *   Not all models are custom models. Models can be [foundation models](https://docs.databricks.com/aws/en/machine-learning/model-serving/create-foundation-model-endpoints) or features for [feature serving](https://docs.databricks.com/aws/en/machine-learning/feature-store/feature-function-serving).
    3.  Select which model and model version you want to serve.
    4.  Select the percentage of traffic to route to your served model.
    5.  Select what size compute to use. You can use CPU or GPU computes for your workloads. See [GPU workload types](#gpu) for more information on available GPU computes.
    6.  Under **Compute Scale-out**, select the size of the compute scale out that corresponds with the number of requests this served model can process at the same time. This number should be roughly equal to QPS x model run time. For customer-defined compute settings, see [model serving limits](https://docs.databricks.com/aws/en/machine-learning/model-serving/model-serving-limits).
        1.  Available sizes are **Small** for 0-4 requests, **Medium** 8-16 requests, and **Large** for 16-64 requests.
    7.  Specify if the endpoint should scale to zero when not in use. Scale to zero is not recommended for production endpoints, as capacity is not guaranteed when scaled to zero. When an endpoint scales to zero, there is additional latency, also referred to as a cold start, when the endpoint scales back up to serve requests.
    8.  Under Advanced configuration, you can:
        *   Rename the served entity to customize how it appears in the endpoint.
        *   [Add an instance profile](https://docs.databricks.com/aws/en/machine-learning/model-serving/add-model-serving-instance-profile) to connect to AWS resources from your endpoint.
        *   Add environment variables to [connect to resources](https://docs.databricks.com/aws/en/machine-learning/model-serving/store-env-variable-model-serving) from your endpoint or [log your feature lookup DataFrame to the endpoint's inference table](https://docs.databricks.com/aws/en/machine-learning/model-serving/store-env-variable-model-serving#features). Logging the feature lookup DataFrame requires MLflow 2.14.0 or above.
    9.  (Optional) To add additional served entities to your endpoint, click **Add served entity** and repeat the configuration steps above. You can serve multiple models or model versions from a single endpoint and control the traffic split between them. See [serve multiple models](https://docs.databricks.com/aws/en/machine-learning/model-serving/serve-multiple-models-to-serving-endpoint) for more information.
3.  In the **Route optimization** section, you can enable route optimization for your endpoint. Route optimization is recommended for endpoints with high QPS and throughput requirements. See [Route optimization on serving endpoints](https://docs.databricks.com/aws/en/machine-learning/model-serving/route-optimization).
    
4.  In the **AI Gateway** section, you can select which governance features to enable on your endpoint. See [Unity AI Gateway](https://docs.databricks.com/aws/en/ai-gateway/).
    
5.  Click **Create**. The **Serving endpoints** page appears with **Serving endpoint state** shown as Not Ready.
    
    ![Create a model serving endpoint](https://docs.databricks.com/aws/en/assets/images/create-endpoint-eb0a4ce61321f63be092b3e0359f1c07.png)
    

You can also:

*   [Enable inference tables](https://docs.databricks.com/aws/en/ai-gateway/inference-tables) to automatically capture incoming requests and outgoing responses to your model serving endpoints.
*   If you have inference tables enabled on your endpoint, you can [log your feature lookup DataFrame](https://docs.databricks.com/aws/en/machine-learning/model-serving/store-env-variable-model-serving#features) to the inference table.

You can also:

*   [Add an instance profile to a model serving endpoint](https://docs.databricks.com/aws/en/machine-learning/model-serving/add-model-serving-instance-profile)
*   [Configure access to resources from model serving endpoints](https://docs.databricks.com/aws/en/machine-learning/model-serving/store-env-variable-model-serving)

### GPU workload types[​](#gpu-workload-types "Direct link to gpu-workload-types")

GPU deployment is compatible with the following package versions:

*   PyTorch 1.13.0 - 2.0.1
*   TensorFlow 2.5.0 - 2.13.0
*   MLflow 2.4.0 and above

The following examples show how to create GPU endpoints using different methods.

*   Serving UI
*   REST API
*   MLflow Deployments SDK
*   Workspace Client

To configure your endpoint for GPU workloads with the **Serving** UI, select the desired GPU type from the **Compute Type** dropdown when creating your endpoint. Follow the same steps in [Create an endpoint](#create), but select a GPU workload type instead of CPU.

The available GPU workload types depend on your cloud provider, as summarized in the following table.

For GPU endpoints, the concurrency value determines the number of replicas allocated to serve your model. The number of replicas equals the concurrency value divided by 4. For example, setting `min_provisioned_concurrency` to 12 provisions 3 replicas.

## Modify a custom model endpoint[​](#modify-a-custom-model-endpoint "Direct link to modify-a-custom-model-endpoint")

After enabling a custom model endpoint, you can update the compute configuration as desired. This configuration is particularly helpful if you need additional resources for your model. Workload size and compute configuration play a key role in what resources are allocated for serving your model.

note

Configuration and served-entity updates re-validate the endpoint's recorded creator workspace membership and per-served-entity grants. Confirm both still hold before submitting an update; see [Identity and access](#permissions).

To avoid update failures:

*   Use a long-lived service principal owned by your team as the endpoint creator.
*   Do not use a personal user account that might be deactivated or removed from the workspace later.
*   The recorded creator must remain a workspace member for the lifetime of the endpoint.

note

Updates to the endpoint configuration can fail. When failures occur the existing active configuration stays effective as if the update didn’t happen.

Verify that the update was successfully applied by reviewing the [status of your endpoint](https://docs.databricks.com/aws/en/machine-learning/model-serving/manage-serving-endpoints#status).

Until the new configuration is ready, the old configuration keeps serving prediction traffic. While there is an update in progress, another update cannot be made. However, you can cancel an in progress update from the Serving UI.

*   Serving UI
*   REST API
*   MLflow Deployments SDK

After you enable a model endpoint, select **Edit endpoint** to modify the compute configuration of your endpoint.

![Edit endpoint button](https://docs.databricks.com/aws/en/assets/images/edit-endpoint-623573bccfaf350254453e9c68b44ebe.png)

You can change most aspects of the endpoint configuration, except for the endpoint name and certain immutable properties.

You can cancel an in progress configuration update by selecting **Cancel update** on the endpoint's details page.

## Scoring a model endpoint[​](#scoring-a-model-endpoint "Direct link to scoring-a-model-endpoint")

To score your model, send requests to the model serving endpoint.

*   See [Query serving endpoints for custom models](https://docs.databricks.com/aws/en/machine-learning/model-serving/score-custom-model-endpoints).
*   See [Use foundation models](https://docs.databricks.com/aws/en/machine-learning/model-serving/score-foundation-models).

## Additional resources[​](#additional-resources "Direct link to Additional resources")

*   [Manage model serving endpoints](https://docs.databricks.com/aws/en/machine-learning/model-serving/manage-serving-endpoints).
*   [External models in Model Serving](https://docs.databricks.com/aws/en/generative-ai/external-models/).
*   If you prefer to use Python, you can use the [Databricks real-time serving Python SDK](https://databricks-sdk-py.readthedocs.io/en/latest/dbdataclasses/serving.html#).

## Notebook examples[​](#notebook-examples "Direct link to notebook-examples")

The following notebooks include different Databricks registered models that you can use to get up and running with model serving endpoints. For additional examples, see [Tutorial: Deploy and query a custom model](https://docs.databricks.com/aws/en/machine-learning/model-serving/model-serving-intro).

The model examples can be imported into the workspace by following the directions in [Import a notebook](https://docs.databricks.com/aws/en/notebooks/notebook-export-import#import-notebook). After you choose and create a model from one of the examples, [register it in Unity Catalog](https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/), and then follow the [UI workflow](#create) steps for model serving.

#### Train and register a scikit-learn model for model serving notebook

#### Train and register a HuggingFace model for model serving notebook
