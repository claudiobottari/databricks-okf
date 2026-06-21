---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3e997032ff587a007aafca09793c8c69aaa5f0142a7c4f57baf35c61113d67c9
  pageDirectory: concepts
  sources:
    - deploy-python-code-with-model-serving-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - code-path-sharing-with-mlflow-pyfunc
    - CPSWMP
  citations:
    - file: deploy-python-code-with-model-serving-databricks-on-aws.md
title: Code Path Sharing with mlflow pyfunc
description: Using the code_path parameter in mlflow.pyfunc.log_model to share and re-use custom Python modules across logged pyfunc models
tags:
  - mlflow
  - code-organization
  - databricks
timestamp: "2026-06-19T10:12:52.317Z"
---

# Code Path Sharing with mlflow pyfunc

**Code Path Sharing with mlflow pyfunc** refers to the ability to share common Python modules and utility code across multiple custom MLflow Python function (pyfunc) models using the `code_path` parameter. This feature enables developers to reuse preprocessing utilities, tokenizers, and other shared code without duplicating it across individual model definitions.

## Overview

When constructing custom MLflow Python function models, developers can leverage shared modules of code from their organization. The `code_path` parameter in `mlflow.pyfunc.log_model()` allows authors to log full code references that load into the Python path, making them available for use from other custom pyfunc models. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## How It Works

When a model is logged with the `code_path` parameter, the specified directory or module is included in the model's artifact bundle. During inference, when the model's `load_context` or `predict` methods are called, the code from the shared path is automatically available in the Python environment. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

### Example

A shared module can be logged with a model using `code_path`:

```python
mlflow.pyfunc.log_model(
    CustomModel(), 
    "model", 
    code_path = ["preprocessing_utils/"]
)
```

The code from the `preprocessing_utils` directory is then available in the loaded context of any model that includes this path. A model using this shared code might look like:

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

## Benefits

- **Code Reusability**: Common preprocessing, tokenization, or transformation logic can be defined once and shared across multiple models. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]
- **Reduced Duplication**: Teams can maintain a single source of truth for utility functions rather than copying code into each model definition. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]
- **Consistency**: Shared code paths ensure that preprocessing and postprocessing logic remains consistent across different models in the organization. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]
- **Simplified Maintenance**: Updates to shared modules are automatically reflected in all models that reference the shared path when they are re-logged. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Best Practices

- **Use `load_context` for initialization**: Any shared resources (tokenizers, model weights, configuration files) that need to be loaded once for the model to operate should be defined in the `load_context` function to minimize per-request overhead. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]
- **Specify `pip_requirements` explicitly**: On Databricks Runtime ML, which ships with `mlflow-skinny` by default, always include `mlflow==<version>` in `pip_requirements` to ensure Model Serving compatibility:^[deploy-python-code-with-model-serving-databricks-on-aws.md]

```python
mlflow.pyfunc.log_model(
    name="model",
    python_model=your_model,
    pip_requirements=["mlflow==3.8.1"],
    registered_model_name="catalog.schema.model_name",
)
```

- **Validate before deployment**: Use `mlflow.models.predict` to validate models before deploying them to serve. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Use Cases

- **Shared Tokenizers**: A custom tokenizer class used across multiple NLP models can be defined once and shared via `code_path`. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]
- **Preprocessing Pipelines**: Common data transformation logic (scaling, encoding, feature engineering) can be centralized. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]
- **Postprocessing Logic**: Output formatting, result parsing, or response enrichment functions can be shared. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]
- **Utility Libraries**: Organizational utility functions for logging, validation, or error handling can be made available to all custom models. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Related Concepts

- [MLflow PyFunc Models](/concepts/custom-mlflow-pythonmodel.md) – The underlying framework for custom Python function models
- [Custom PyFunc Model Creation](/concepts/custom-mlflow-pythonmodel.md) – Creating custom MLflow Python function models
- Model Serving Deployment – Deploying custom models to production endpoints
- MLflow pyfunc load_context Pattern|PyFunc load_context – The initialization function for pyfunc models
- Shared Module Patterns in MLflow – Best practices for organizing shared code in MLflow projects

## Sources

- deploy-python-code-with-model-serving-databricks-on-aws.md

# Citations

1. [deploy-python-code-with-model-serving-databricks-on-aws.md](/references/deploy-python-code-with-model-serving-databricks-on-aws-84536f0c.md)
