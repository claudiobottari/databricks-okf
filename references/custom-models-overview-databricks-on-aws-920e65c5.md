---
title: Custom models overview | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/model-serving/custom-models
ingestedAt: "2026-06-18T08:11:50.404Z"
---

This article describes support for **custom models** using [Model Serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/). It provides details about supported model logging options and compute types, how to package model dependencies for serving, and expectations for endpoint creation and scaling.

## What are custom models?[​](#what-are-custom-models "Direct link to What are custom models?")

Model Serving can deploy any Python model or [custom code](https://docs.databricks.com/aws/en/machine-learning/model-serving/deploy-custom-python-code) as a production-grade API using CPU or GPU compute resources. Databricks refers to such models as **custom models**. These ML models can be trained using standard ML libraries like scikit-learn, XGBoost, PyTorch, and HuggingFace transformers and can include any Python code.

To deploy a **custom model**,

1.  Log the model or code in the MLflow format, using either native [MLflow built-in flavors](https://mlflow.org/docs/latest/models.html#built-in-model-flavors) or [pyfunc](https://mlflow.org/docs/latest/python_api/mlflow.pyfunc.html#module-mlflow.pyfunc).
2.  After the model is logged, register it in the Unity Catalog (recommended) or the workspace registry.
3.  From here, you can create a model serving endpoint to deploy and query your model.
    1.  See [Create custom model serving endpoints](https://docs.databricks.com/aws/en/machine-learning/model-serving/create-manage-serving-endpoints)
    2.  See [Query serving endpoints for custom models](https://docs.databricks.com/aws/en/machine-learning/model-serving/score-custom-model-endpoints).

For a complete tutorial on how to serve custom models on Databricks, see [Model serving tutorial](https://docs.databricks.com/aws/en/machine-learning/model-serving/model-serving-intro).

Databricks also supports serving foundation models for generative AI applications, see [Foundation Model APIs](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/) and [External models](https://docs.databricks.com/aws/en/generative-ai/external-models/) for supported models and compute offerings.

## Log ML models[​](#log-ml-models "Direct link to Log ML models")

There are different methods to log your ML model for model serving. The following list summarizes the supported methods and examples.

*   **Autologging** This method is automatically enabled when using Databricks Runtime for ML.
    
    Python
    
        import mlflowfrom sklearn.ensemble import RandomForestRegressorfrom sklearn.datasets import load_irisiris = load_iris()model = RandomForestRegressor()model.fit(iris.data, iris.target)
    
*   **Log using MLflow's built-in flavors**. You can use this method if you want to manually log the model for more detailed control.
    
    Python
    
        import mlflowfrom sklearn.ensemble import RandomForestClassifierfrom sklearn.datasets import load_irisiris = load_iris()model = RandomForestClassifier()model.fit(iris.data, iris.target)with mlflow.start_run():    mlflow.sklearn.log_model(model, "random_forest_classifier")
    
*   **Custom logging with `pyfunc`**. You can use this method for deploying arbitrary python code models or deploying additional code alongside your model.
    
    Python
    
          import mlflow  import mlflow.pyfunc  class Model(mlflow.pyfunc.PythonModel):      def predict(self, context, model_input):          return model_input * 2  with mlflow.start_run():      mlflow.pyfunc.log_model("custom_model", python_model=Model())
    

### Signature and input examples[​](#signature-and-input-examples "Direct link to Signature and input examples")

Adding a signature and input example to MLflow is recommended. Signatures are necessary for logging models to the Unity Catalog.

The following is a signature example:

Python

    from mlflow.models.signature import infer_signaturesignature = infer_signature(training_data, model.predict(training_data))mlflow.sklearn.log_model(model, "model", signature=signature)

The following is an input example:

Python

    input_example = {"feature1": 0.5, "feature2": 3}mlflow.sklearn.log_model(model, "model", input_example=input_example)

## Compute type[​](#compute-type "Direct link to Compute type")

Model Serving provides a variety of CPU and GPU options for deploying your model. When deploying with a GPU, you must make sure that your code is set up so that predictions are run on the GPU, using the methods provided by your framework. MLflow does this automatically for models logged with the PyTorch or Transformers flavors.

The `CPU_MEDIUM` and `CPU_LARGE` workload types let you trade concurrency for more memory per worker on the same CPU hardware. Use them when your model needs more memory than standard `CPU` provides.

## Deployment container and dependencies[​](#deployment-container-and-dependencies "Direct link to Deployment container and dependencies")

During deployment, a production-grade container is built and deployed as the endpoint. This container includes libraries automatically captured or specified in the MLflow model. The base image may include some system-level dependencies, but application-level dependencies must be explicitly specified in your MLflow model.

If not all required dependencies are included in the model, you might encounter dependency errors during deployment. When running into model deployment issues, Databricks recommends you test the model locally.

### Package and code dependencies[​](#package-and-code-dependencies "Direct link to Package and code dependencies")

Custom or private libraries can be added to your deployment. See [Use custom Python libraries with Model Serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/private-libraries-model-serving).

For MLflow native flavor models, the necessary package dependencies are automatically captured.

For custom `pyfunc` models, dependencies can be explicitly added. For detailed information about logging requirements and best practices, see the [MLflow Models documentation](https://mlflow.org/docs/latest/models.html) and [MLflow Python API reference](https://mlflow.org/docs/latest/python_api/index.html).

You can add package dependencies using:

*   The `pip_requirements` parameter:
    
    Python
    
        mlflow.sklearn.log_model(model, "sklearn-model", pip_requirements = ["scikit-learn", "numpy"])
    
*   The `conda_env` parameter:
    
    Python
    
        conda_env = {    'channels': ['defaults'],    'dependencies': [        'python=3.7.0',        'scikit-learn=0.21.3'    ],    'name': 'mlflow-env'}mlflow.sklearn.log_model(model, "sklearn-model", conda_env = conda_env)
    
*   To include additional requirements beyond what is automatically captured, use `extra_pip_requirements`.
    
    Python
    
        mlflow.sklearn.log_model(model, "sklearn-model", extra_pip_requirements = ["sklearn_req"])
    

If you have code dependencies, these can be specified using `code_path`.

Python

      mlflow.sklearn.log_model(model, "sklearn-model", code_path=["path/to/helper_functions.py"],)

For information about validating and updating dependencies before deployment, see [Pre-deployment validation for Model Serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/model-serving-pre-deployment-validation).

## Expectations and limitations[​](#expectations-and-limitations "Direct link to Expectations and limitations")

note

The information in this section does not apply to endpoints that serve foundation models or external models.

The following sections describe known expectations and limitations for serving custom models using Model Serving.

### Endpoint creation and update expectations[​](#endpoint-creation-and-update-expectations "Direct link to Endpoint creation and update expectations")

*   **Deployment time**: Deploying a newly registered model version involves packaging the model and its model environment and provisioning the model endpoint itself. This process can take approximately 10 minutes, but may take longer depending on model complexity, size, and dependencies.
*   **Zero-downtime updates**: Databricks performs a zero-downtime update of endpoints by keeping the existing endpoint configuration up until the new one becomes ready. Doing so reduces risk of interruption for endpoints that are in use. During this update process, you are billed for both the old and new endpoint configurations until the transition is complete.
*   **Request timeout**: If model computation takes longer than 597 seconds, requests will time out.

important

Databricks performs occasional zero-downtime system updates and maintenance on existing Model Serving endpoints. During maintenance, Databricks reloads models. If a model fails to reload, the endpoint update is marked as failed and the existing endpoint configuration continues to serve requests. Make sure your customized models are robust and are able to reload at any time.

### Endpoint scaling expectations[​](#endpoint-scaling-expectations "Direct link to endpoint-scaling-expectations")

Serving endpoints automatically scale based on traffic and the capacity of provisioned concurrency units.

*   **Provisioned concurrency:** The maximum number of parallel requests the system can handle. Estimate the required concurrency using the formula: provisioned concurrency = queries per second (QPS) \* model execution time (s). To validate your concurrency configuration, see [Load testing for serving endpoints](https://docs.databricks.com/aws/en/machine-learning/model-serving/what-is-load-test).
*   **Scaling behavior:** Endpoints scale up almost immediately with increased traffic and scale down every five minutes to match reduced traffic. Nodes are ready to serve traffic after the model is downloaded and pass health checks; the model size and load time determine how long this takes.
*   **Scale to zero:** Scale to zero is an optional feature for endpoints that allows them to scale down to zero after 30 minutes of inactivity. The first request after scaling to zero experiences a "cold start," leading to higher latency. Scaling up from zero usually takes 10-20 seconds, but can sometimes take minutes. There is no SLA on scale from zero latency.
*   **Route optimization:** For high QPS and low latency use cases, [route optimization](https://docs.databricks.com/aws/en/machine-learning/model-serving/route-optimization) is the optimal and recommended option to improve performance.
*   **Express deployments:** For faster endpoint deployment speed, use [express deployments](https://docs.databricks.com/aws/en/machine-learning/model-serving/express-deployments).

warning

Scale to zero should not be used for production workloads that require consistent uptime or guaranteed response times. For latency-sensitive applications or endpoints requiring continuous availability, disable scale to zero.

### GPU workload limitations[​](#gpu-workload-limitations "Direct link to GPU workload limitations")

The following are limitations for serving endpoints with GPU workloads:

*   Container image creation for GPU serving takes longer than image creation for CPU serving due to model size and increased installation requirements for models served on GPU.
*   When deploying very large models, the deployment process might timeout if the container build and model deployment exceed a 60-minute duration, or the container build might fail with "No space left on device" error due to storage limitations. For large language models, use [Foundation Model APIs](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/) instead.
*   Autoscaling for GPU serving takes longer than for CPU serving.
*   GPU capacity is not guaranteed when scaling to zero. GPU endpoints might expect extra high latency for the first request after scaling to zero.

## Anaconda licensing notice for legacy models[​](#anaconda-licensing-notice-for-legacy-models "Direct link to anaconda-licensing-notice-for-legacy-models")

note

This section applies only to models logged with MLflow v1.17 or earlier (Databricks Runtime 8.3 ML or earlier). If you are using a newer version, you can skip this section.

The following notice is for customers relying on Anaconda with legacy models.

important

Anaconda Inc. updated their [terms of service](https://www.anaconda.com/terms-of-service) for anaconda.org channels. Based on the new terms of service you may require a commercial license if you rely on Anaconda's packaging and distribution. See [Anaconda Commercial Edition FAQ](https://www.anaconda.com/blog/anaconda-commercial-edition-faq) for more information. Your use of any Anaconda channels is governed by their terms of service.

MLflow models logged before [v1.18](https://mlflow.org/news/2021/06/18/1.18.0-release/index.html) (Databricks Runtime 8.3 ML or earlier) were by default logged with the conda `defaults` channel ([https://repo.anaconda.com/pkgs/](https://repo.anaconda.com/pkgs/)) as a dependency. Because of this license change, Databricks has stopped the use of the `defaults` channel for models logged using MLflow v1.18 and above. The default channel logged is now `conda-forge`, which points at the community managed [https://conda-forge.org/](https://conda-forge.org/).

If you logged a model before MLflow v1.18 without excluding the `defaults` channel from the conda environment for the model, that model may have a dependency on the `defaults` channel that you may not have intended. To manually confirm whether a model has this dependency, you can examine `channel` value in the `conda.yaml` file that is packaged with the logged model. For example, a model's `conda.yaml` with a `defaults` channel dependency may look like this:

YAML

    channels:- defaultsdependencies:- python=3.8.8- pip- pip:    - mlflow    - scikit-learn==0.23.2    - cloudpickle==1.6.0      name: mlflow-env

Because Databricks can not determine whether your use of the Anaconda repository to interact with your models is permitted under your relationship with Anaconda, Databricks is not forcing its customers to make any changes. If your use of the Anaconda.com repo through the use of Databricks is permitted under Anaconda's terms, you do not need to take any action.

If you would like to change the channel used in a model's environment, you can re-register the model to the model registry with a new `conda.yaml`. You can do this by specifying the channel in the `conda_env` parameter of `log_model()`.

For more information on the `log_model()` API, see the MLflow documentation for the model flavor you are working with, for example, [log\_model for scikit-learn](https://www.mlflow.org/docs/latest/python_api/mlflow.sklearn.html#mlflow.sklearn.log_model).

For more information on `conda.yaml` files, see the [MLflow documentation](https://www.mlflow.org/docs/latest/models.html#additional-logged-files).

## Additional resources[​](#additional-resources "Direct link to Additional resources")

*   [Create custom model serving endpoints](https://docs.databricks.com/aws/en/machine-learning/model-serving/create-manage-serving-endpoints)
*   [Query serving endpoints for custom models](https://docs.databricks.com/aws/en/machine-learning/model-serving/score-custom-model-endpoints)
*   [Debugging guide for Model Serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/model-serving-debug)
*   [Use custom Python libraries with Model Serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/private-libraries-model-serving)
*   [Package custom artifacts for Model Serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/model-serving-custom-artifacts)
*   [Deploy Python code with Model Serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/deploy-custom-python-code)
*   [Route optimization on serving endpoints](https://docs.databricks.com/aws/en/machine-learning/model-serving/route-optimization)
*   [Express deployments for model serving endpoints](https://docs.databricks.com/aws/en/machine-learning/model-serving/express-deployments)
*   [Configure access to resources from model serving endpoints](https://docs.databricks.com/aws/en/machine-learning/model-serving/store-env-variable-model-serving)
*   [Add an instance profile to a model serving endpoint](https://docs.databricks.com/aws/en/machine-learning/model-serving/add-model-serving-instance-profile)
