---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0fecb6164f604d6489a5bf8b8ef52ed16979fc7276a963242ee058b1991c5eef
  pageDirectory: concepts
  sources:
    - deploy-python-code-with-model-serving-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-serving-endpoint-deployment-for-custom-models
    - MSEDFCM
  citations:
    - file: deploy-python-code-with-model-serving-databricks-on-aws.md
title: Model Serving Endpoint Deployment for Custom Models
description: After logging a custom pyfunc model, it can be registered to Unity Catalog or Workspace Registry and served via a Databricks Model Serving endpoint.
tags:
  - databricks
  - model-serving
  - deployment
timestamp: "2026-06-18T15:27:06.395Z"
---

# Model Serving Endpoint Deployment for Custom Models

**Model Serving Endpoint Deployment for Custom Models** refers to the process of deploying arbitrary Python code as a model serving endpoint on Databricks using MLflow’s Python function (`pyfunc`) format. This approach provides flexibility when a model requires preprocessing, postprocessing, branching logic, or uses a framework not natively supported by MLflow. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Use Cases

You might deploy a custom model when:

- Your model requires preprocessing before inputs can be passed to the predict function.
- Your model framework is not natively supported by MLflow.
- Your application needs the raw model outputs to be post-processed for consumption.
- The model has per-request branching logic.
- You want to deploy fully custom code as a model. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Construct a Custom MLflow Python Function Model

MLflow’s custom Python models format requires two methods in a class that inherits from `mlflow.pyfunc.PythonModel`:

- `load_context(self, context)` – contains logic that runs once when the model is loaded (e.g., loading model weights, tokenizers). This minimizes work during inference.
- `predict(self, context, model_input)` – contains the logic run for every inference request. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

### Example

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

^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Log Your Python Function Model

To log a custom pyfunc model for serving, use `mlflow.pyfunc.log_model()`. There is a critical environment consideration on Databricks:

- Databricks Runtime ML ships with `mlflow-skinny` by default, not the full `mlflow` package. If you call `log_model` without specifying `pip_requirements`, MLflow captures `mlflow-skinny` in the model’s `conda.yaml`. Model Serving requires the full `mlflow` package and cannot build the container image otherwise. **Always specify `mlflow==<version>` in `pip_requirements`** when logging on a Databricks Runtime ML runtime. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

```python
# DBR ML ships with mlflow-skinny by default, so specify mlflow explicitly
# to ensure Model Serving compatibility.
mlflow.pyfunc.log_model(
    name="model",
    python_model=your_model,
    pip_requirements=["mlflow==3.8.1"],  # use mlflow, not mlflow-skinny
    registered_model_name="catalog.schema.model_name",
)
```

^[deploy-python-code-with-model-serving-databricks-on-aws.md]

### Shared Code Modules with `code_path`

You can include shared Python modules using the `code_path` parameter. This allows multiple custom pyfunc models to reuse code from a common location. For example:

```python
mlflow.pyfunc.log_model(CustomModel(), "model", code_path=["preprocessing_utils/"])
```

Code from `preprocessing_utils` is then available in the loaded context. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Serve Your Model

After logging a custom pyfunc model, register it in [Unity Catalog](/concepts/unity-catalog.md) or the Workspace Registry. You can then create a [Model Serving Endpoint](/concepts/model-serving-endpoint.md) from the Databricks UI or API to serve the model. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Validation Before Deployment

Before deploying, verify the model can be served by using `mlflow.models.predict()`. See the MLflow documentation on [validating models before deployment](https://www.mlflow.org/docs/latest/models.html#validate-models-before-deployment). ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Related Concepts

- [MLflow Python Function (pyfunc)](/concepts/mlflow-pyfunc-python-function.md) – foundational format for custom models.
- [Model Serving](/concepts/model-serving.md) – serving endpoints on Databricks.
- [Unity Catalog](/concepts/unity-catalog.md) – model registry for serving.
- Custom Model Inference Pipelines – preprocessing/postprocessing patterns.
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) – environment considerations.

## Sources

- deploy-python-code-with-model-serving-databricks-on-aws.md

# Citations

1. [deploy-python-code-with-model-serving-databricks-on-aws.md](/references/deploy-python-code-with-model-serving-databricks-on-aws-84536f0c.md)
