---
title: Debugging guide for Model Serving | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/model-serving/model-serving-debug
ingestedAt: "2026-06-18T08:12:08.590Z"
---

This article demonstrates debugging steps for common issues that users might encounter when working with model serving endpoints. Common issues could include errors users encounter when the endpoint fails to initialize or start, build failures related to the container, or problems during the operation or running of the model on the endpoint.

Validate before debugging

Having deployment issues? Start with [pre-deployment validation](https://docs.databricks.com/aws/en/machine-learning/model-serving/model-serving-pre-deployment-validation) to catch common problems before they occur.

## Debug your container build[​](#debug-your-container-build "Direct link to Debug your container build")

Databricks recommends reviewing logs for debugging and troubleshooting errors in your model serving workloads. See [Monitor model quality and endpoint health](https://docs.databricks.com/aws/en/machine-learning/model-serving/monitor-diagnose-endpoints) for information about logs and how to view them.

The event logs (click the **Events** tab) in the workspace UI contain information about the progress of a container build. A successful container build is highlighted by a `SERVED_ENTITY_CONTAINER_EVENT` event type along with a message `Container image creation finished successfully`. If you do not see any build event or message after an hour of creating the endpoint, reach out to Databricks support for assistance.

If your build is successful, but you encounter other errors see [Debug after container build succeeds](#build-success). If your build fails, see [Debug after container build failure](#build-fail).

## Debug after container build succeeds[​](#debug-after-container-build-succeeds "Direct link to debug-after-container-build-succeeds")

Even if the container builds successfully, there might be issues when you run the model or during the operation of the endpoint itself. The following subsections detail common issues and how to troubleshoot them.

note

If your model code returns `MlflowException` errors, expect the response code to be mapped to a `4xx` response. Databricks considers these model code errors to be customer-caused errors, since they can be resolved based on the resulting error message. `5xx` error codes are reserved to communicate errors where Databricks is at fault.

### Missing dependency[​](#missing-dependency "Direct link to Missing dependency")

You might get an error like `An error occurred while loading the model. No module named <module-name>.`, which might indicate that a dependency is missing from the container. Verify that you properly denoted all the dependencies that should be included in the build of the container. Pay special attention to custom libraries and ensure that the `.whl` files are included as artifacts.

### Model fails or times out when requests are sent to the endpoint[​](#model-fails-or-times-out-when-requests-are-sent-to-the-endpoint "Direct link to Model fails or times out when requests are sent to the endpoint")

You might receive an error like `Encountered an unexpected error while evaluating the model. Verify that the input is compatible with the model for inference.` when `predict()` is called on your model.

This error can indicate a code issue in the `predict()` function. Databricks recommends that you load the model from MLflow in a notebook and call it. Doing so highlights the issues in the `predict()` function, and you can see where the failure is happening within the method.

### Root cause analysis of failed requests[​](#root-cause-analysis-of-failed-requests "Direct link to Root cause analysis of failed requests")

If a request to an endpoint fails, you can perform root cause analysis by using inference tables. If enabled, inference tables automatically log all requests and responses to your endpoint in a Unity Catalog table for you to query.

*   See [Monitor served models using Unity AI Gateway\-enabled inference tables](https://docs.databricks.com/aws/en/ai-gateway/inference-tables).

To query inference tables:

1.  In your workspace, go to the **Serving** tab and select your endpoint name.
2.  In the **Inference tables** section, find the inference table's fully-qualified name. For example, `my-catalog.my-schema.my-table`.
3.  Run the following in a Databricks notebook:
    
    Python
    
        %sqlSELECT * FROM my-catalog.my-schema.my-table
    
4.  View and filter on columns such as `request`, `response`, `request_time` and `status_code` to understand the requests and narrow down results.
    
    Python
    
        %sqlSELECT * FROM my-catalog.my-schema.my-tableWHERE status_code != 200
    
5.  If you enabled agent tracing for AI agents, see the **Response** column to view detailed traces. See [Enable inference tables for AI agents](https://docs.databricks.com/aws/en/ai-gateway/inference-tables#enable-agent-tracing).

### Workspace exceeds provisioned concurrency[​](#workspace-exceeds-provisioned-concurrency "Direct link to Workspace exceeds provisioned concurrency")

You might receive a `Workspace exceeded provisioned concurrency quota` error. This indicates that you have reached your workspace quota for provisioned concurrency. See [Model Serving limits and regions](https://docs.databricks.com/aws/en/machine-learning/model-serving/model-serving-limits) for more information about concurrency limits.

You can free up this quota by [deleting](https://docs.databricks.com/aws/en/machine-learning/model-serving/manage-serving-endpoints#delete-endpoint) or [stopping](https://docs.databricks.com/aws/en/machine-learning/model-serving/manage-serving-endpoints#stop-start-endpoint) unused endpoints.

This limit can be increased depending on region availability. Reach out to your Databricks account team and provide your workspace ID to request a concurrency increase.

### Workspace exceeds parallel requests limit[​](#workspace-exceeds-parallel-requests-limit "Direct link to Workspace exceeds parallel requests limit")

You might receive the following 429 error: `Exceeded max number of parallel requests. Please contact your Databricks representative to increase the limit`. This limit indicates that you have reached the workspace limit on the maximum number of requests that can be sent in parallel. See [Model Serving limits and regions](https://docs.databricks.com/aws/en/machine-learning/model-serving/model-serving-limits) for more information about this limit.

Databricks recommends moving to [route optimized endpoints](https://docs.databricks.com/aws/en/machine-learning/model-serving/route-optimization), where this limit has been removed. If you cannot move to route optimized endpoints, you can either reduce the number of clients sending inference requests or contact your Databricks representative for a quota increase.

### Too many concurrent requests[​](#too-many-concurrent-requests "Direct link to Too many concurrent requests")

You might receive the following 429 error: `Too many concurrent requests. Consider increasing the provisioned concurrency of the served entity.` This error indicates that your endpoint's current provisioned concurrency cannot handle the incoming traffic volume. If you have enabled autoscaling for your endpoint, the system will automatically provision additional concurrency up to the endpoint's configured limit to handle the increased load. If autoscaling is not enabled, consider manually increasing the provisioned concurrency or enabling autoscaling to handle traffic spikes.

## Debug after container build failure[​](#debug-after-container-build-failure "Direct link to debug-after-container-build-failure")

This section details issues that might occur when your build fails.

### `OSError: [Errno 28] No space left on device`[​](#oserror-errno-28-no-space-left-on-device "Direct link to oserror-errno-28-no-space-left-on-device")

The `No space left` error can be due to too many large artifacts being logged alongside the model unnecessarily. Check in MLflow that extraneous artifacts are not logged alongside the model and try to redeploy the slimmed down package.

### Build failure due to lack of GPU availability[​](#build-failure-due-to-lack-of-gpu-availability "Direct link to Build failure due to lack of GPU availability")

Due to restrictions in GPU supply and availability, your GPU build may fail with this error: `Build could not start due to an internal error - please contact your Databricks representative.`.

Reach out to your Databricks account team to help resolve. Depending on region availability, the team can provision more GPU resources.

### Installed library package versions[​](#installed-library-package-versions "Direct link to Installed library package versions")

Databricks recommends that you define all important libraries as model dependencies to ensure consistent and reproducible model behavior across environments. In the build logs you can confirm the package versions that are installed correctly.

*   For MLflow versions, if you do not have a version specified, Model Serving uses the latest version.
*   For custom GPU serving, Model Serving installs the recommended versions of `cuda` and `cuDNN` according to public PyTorch and Tensorflow documentation.

### Log models that require `flash-attn`[​](#log-models-that-require-flash-attn "Direct link to log-models-that-require-flash-attn")

If you are logging a model that requires `flash-attn`, Databricks recommends using a custom wheel version of `flash-attn`. Otherwise, build errors such as `ModuleNotFoundError: No module named 'torch'` can result.

To use a custom wheel version of `flash-attn`, specify all pip requirements as a list and pass it as a parameter into your `mlflow.transformers.log_model` function. You must also specify the pytorch, torch, and torchvision versions that are compatible with the CUDA version specified in your `flash attn` wheel.

For example, Databricks recommends using the following versions and wheels for CUDA 11.8:

*   [Pytorch](https://download.pytorch.org/whl/cu118)
*   Torch 2.0.1+cu118
*   Torchvision 0.15.2+cu118
*   [Flash-Attn](https://github.com/Dao-AILab/flash-attention/releases/download/v2.5.8/flash_attn-2.5.8+cu118torch2.0cxx11abiFALSE-cp311-cp311-linux_x86_64.whl)

Python

    logged_model=mlflow.transformers.log_model(transformers_model=test_pipeline,       artifact_path="artifact_path",       pip_requirements=["--extra-index-url https://download.pytorch.org/whl/cu118", "mlflow==2.13.1", "setuptools<70.0.0", "torch==2.0.1+cu118", "accelerate==0.31.0", "astunparse==1.6.3", "bcrypt==3.2.0", "boto3==1.34.39", "configparser==5.2.0", "defusedxml==0.7.1", "dill==0.3.6", "google-cloud-storage==2.10.0", "ipython==8.15.0", "lz4==4.3.2", "nvidia-ml-py==12.555.43", "optree==0.12.1", "pandas==1.5.3", "pyopenssl==23.2.0", "pytesseract==0.3.10", "scikit-learn==1.3.0", "sentencepiece==0.1.99", "torchvision==0.15.2+cu118", "transformers==4.41.2", "https://github.com/Dao-AILab/flash-attention/releases/download/v2.5.8/flash_attn-2.5.8+cu118torch2.0cxx11abiFALSE-cp311-cp311-linux_x86_64.whl"],       input_example=input_example,       registered_model_name=registered_model_name)
