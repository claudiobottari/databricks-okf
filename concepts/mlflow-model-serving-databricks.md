---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 46a8b693d2056244aa708e7174ca9e8dba1db09992239fe02beead92025f7cf7
  pageDirectory: concepts
  sources:
    - deploy-python-code-with-model-serving-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-model-serving-databricks
    - MMS(
  citations:
    - file: deploy-python-code-with-model-serving-databricks-on-aws.md
    - file: configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
title: MLflow Model Serving (Databricks)
description: Databricks platform feature for deploying custom ML models as serving endpoints, with support for MLflow pyfunc models registered to Unity Catalog or Workspace Registry.
tags:
  - databricks
  - model-serving
  - deployment
timestamp: "2026-06-19T18:30:31.698Z"
---

# MLflow Model Serving (Databricks)

**MLflow Model Serving (Databricks)** is a managed inference platform on Databricks that enables deployment of machine learning models as REST API endpoints. It supports serving models logged with MLflow, including custom Python code packaged as MLflow Python functions (`pyfunc`). ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Overview

Model Serving on Databricks allows you to deploy registered models from [Unity Catalog](/concepts/unity-catalog.md) or [Workspace Registry](/concepts/workspace-model-registry.md) to production endpoints. The platform handles infrastructure management, scaling, and monitoring of deployed models. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Custom Python Code Deployment

MLflow's `pyfunc` (Python function) format provides flexibility to deploy any piece of Python code or any Python model. This is useful in scenarios where: ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

- Your model requires preprocessing before inputs can be passed to the model's predict function
- Your model framework is not natively supported by MLflow
- Your application requires post-processing of raw model outputs
- The model has per-request branching logic
- You need to deploy fully custom code as a model

## Constructing a Custom MLflow PyFunc Model

To package arbitrary Python code with MLflow, you must define two required functions: ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

- **`load_context`** – Defines anything that needs to be loaded just once for the model to operate. This minimizes the number of artifacts loaded during prediction, speeding up inference.
- **`predict`** – Houses all logic that runs every time an input request is made.

Prior to deployment, it is beneficial to verify the model is capable of being served using `mlflow.models.predict` to [validate models before deployment](/concepts/model-validation-before-deployment.md). ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

### Example Custom PyFunc Model

```python
class CustomModel(mlflow.pyfunc.PythonModel):
    def load_context(self, context):
        self.model = torch.load(context.artifacts["model-weights"])
        from preprocessing_utils.my_custom_tokenizer import CustomTokenizer
        self.tokenizer = CustomTokenizer(context.artifacts["tokenizer_cache"])

    def format_inputs(self, model_input):
        # insert some code that formats your inputs
        pass

    def format_outputs(self, outputs):
        predictions = (torch.sigmoid(outputs)).data.numpy()
        return predictions

    def predict(self, context, model_input):
        model_input = self.format_inputs(model_input)
        outputs = self.model.predict(model_input)
        return self.format_outputs(outputs)
```

## Logging a PyFunc Model

When logging a `pyfunc` model on [Databricks Runtime ML](/concepts/databricks-runtime-ml.md), you must explicitly specify `mlflow` (not `mlflow-skinny`) in the `pip_requirements` parameter. Databricks Runtime ML runtimes ship with `mlflow-skinny` by default rather than the full `mlflow` package. Without specifying `pip_requirements`, MLflow captures `mlflow-skinny` in the model's `conda.yaml`, which prevents Model Serving from building the container image. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

```python
mlflow.pyfunc.log_model(
    name="model",
    python_model=your_model,
    pip_requirements=["mlflow==3.8.1"],  # use mlflow, not mlflow-skinny
    registered_model_name="catalog.schema.model_name",
)
```

## Shared Code Modules

Custom pyfunc models can reference shared modules from your organization using the `code_path` parameter. This allows authors to log full code references that load into the path and are usable from other custom pyfunc models. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

For example, if a model is logged with:

```python
mlflow.pyfunc.log_model(CustomModel(), "model", code_path = ["preprocessing_utils/"])
```

Code from the `preprocessing_utils` directory becomes available in the loaded context of the model.

## Serving Your Model

After logging a custom `pyfunc` model, you can register it to [Unity Catalog](/concepts/unity-catalog.md) or [Workspace Registry](/concepts/workspace-model-registry.md) and serve the model to a [Model Serving Endpoint](/concepts/model-serving-endpoint.md). ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Serverless Budget Policies

When running serverless workloads — such as scheduled scorers, synthetic evaluation set generation, or agent evaluation — MLflow requires a serverless budget policy. If the workspace's default policy is disabled and no alternative policy is assigned, a 403 PERMISSION_DENIED Serverless Budget Policy Error occurs. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

To resolve this, set a serverless budget policy on the MLflow experiment either through the UI or via the API using `mlflow.set_experiment_tag()` with the `mlflow.workload_creation_policy_id` tag. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Related Concepts

- [MLflow Experiments](/concepts/mlflow-experiment.md) – The organizational unit for MLflow runs and evaluations
- [Model Serving Endpoint](/concepts/model-serving-endpoint.md) – The REST API endpoint for deployed models
- [Production Monitoring](/concepts/production-monitoring.md) – Scheduled scoring workflows
- [Agent evaluation](/concepts/mlflow-agent-evaluation.md) – Evaluation workflows affected by budget policies

## Sources

- deploy-python-code-with-model-serving-databricks-on-aws.md
- configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md

# Citations

1. [deploy-python-code-with-model-serving-databricks-on-aws.md](/references/deploy-python-code-with-model-serving-databricks-on-aws-84536f0c.md)
2. [configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md](/references/configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws-cb1d8a65.md)
