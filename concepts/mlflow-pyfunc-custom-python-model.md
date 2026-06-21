---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 290c894e0708b1825e8d3ed06e39c0dbd950e9c59558bbc35311e5157283f5c4
  pageDirectory: concepts
  sources:
    - deploy-python-code-with-model-serving-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-pyfunc-custom-python-model
    - MPCPM
    - MLflow pyfunc PythonModel
    - mlflow.pyfunc.PythonModel
    - MLflow Python Function (pyfunc) model
  citations:
    - file: deploy-python-code-with-model-serving-databricks-on-aws.md
title: MLflow pyfunc Custom Python Model
description: MLflow's Python function (pyfunc) format allows deploying arbitrary Python code as a model, including preprocessing, postprocessing, branching logic, or unsupported frameworks.
tags:
  - machine-learning
  - model-serving
  - mlflow
timestamp: "2026-06-18T15:26:46.620Z"
---

---

## MLflow pyfunc Custom Python Model

**MLflow pyfunc Custom Python Model** is a framework within [MLflow](/concepts/mlflow.md) that allows you to package and deploy any arbitrary Python code as a model. It uses MLflow’s **Python function (`pyfunc`) flavor** to provide a standardized interface for inference, enabling you to add preprocessing, postprocessing, or custom logic around a model.

### Overview

The `pyfunc` flavor is one of MLflow’s standard model flavors and gives you the flexibility to deploy any piece of Python code or any Python model that can be expressed as a Python function. This is useful when your model framework is not natively supported by MLflow, you need to add preprocessing or postprocessing, or you want to deploy fully custom code as a model. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

### Use Cases

You might want to use a custom `pyfunc` model in the following scenarios:

- **Preprocessing**: Your model requires transformations (e.g., tokenization, feature engineering) before inputs can be passed to its predict function.
- **Unsupported framework**: Your model is built with a framework that MLflow does not natively support.
- **Postprocessing**: The application needs the model’s raw outputs to be post-processed (e.g., converting logits to probabilities, formatting response strings).
- **Per-request branching**: The model itself has different logic paths depending on the request.
- **Fully custom code**: You want to deploy arbitrary Python code as a model without any underlying ML framework. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

### Structure of a Custom `pyfunc` Model

A custom `pyfunc` model requires implementing two functions:

1. **`load_context`** – Everything that needs to be loaded once for the model to operate (e.g., loading model weights, initializing a tokenizer) should be defined here. This is critical to minimize the number of artifacts loaded during each `predict` call, which speeds up inference. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]
2. **`predict`** – This function houses all the logic that runs every time an input request is made. It typically calls the underlying model and applies any pre- or post-processing. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

You can also share common modules of code across models using the `code_path` parameter. When logging a model with `code_path`, the specified code is loaded into the Python path and is usable from other custom `pyfunc` models. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

Example:

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

### Logging the Model

To log a custom `pyfunc` model, use `mlflow.pyfunc.log_model()`. You must specify the `python_model` argument (your custom model class instance) and the `pip_requirements` parameter. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

**Important**: Databricks Runtime ML runtimes include `mlflow-skinny` by default rather than the full `mlflow` package. When you log a `pyfunc` model on one of these runtimes without specifying `pip_requirements`, MLflow captures `mlflow-skinny` in the model’s `conda.yaml`. [Model Serving](/concepts/model-serving.md) requires `mlflow` (not `mlflow-skinny`) in `conda.yaml` and cannot build the container image otherwise. **Always specify `mlflow==<version>` in `pip_requirements` when you call `mlflow.pyfunc.log_model()` on a Databricks Runtime ML runtime.** ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

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

### Serving the Model

After you log a custom `pyfunc` model, you can register it to Unity Catalog or the Workspace Registry and serve it to a [Model Serving](/concepts/model-serving.md) endpoint. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

### Validation

Prior to deploying your custom code as a model, it is beneficial to verify that the model is capable of being served. See the MLflow documentation on how to use `mlflow.models.predict` to [validate models before deployment](/concepts/model-validation-before-deployment.md). ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

### Related Concepts

- [MLflow Model Flavors](/concepts/mlflow-model-flavors.md) – How different model types are handled in MLflow.
- [Model Serving on Databricks](/concepts/model-serving-on-databricks.md) – Endpoint-based serving for custom models.
- [Unity Catalog](/concepts/unity-catalog.md) – Where models can be registered for serving.
- [PythonModel](/concepts/custom-mlflow-pythonmodel.md) – The base class for custom `pyfunc` models.
- Preprocessing and Postprocessing – Common pipeline steps in ML models.
- code_path – Parameter for sharing Python modules across models.

### Sources

- deploy-python-code-with-model-serving-databricks-on-aws.md

---

# Citations

1. [deploy-python-code-with-model-serving-databricks-on-aws.md](/references/deploy-python-code-with-model-serving-databricks-on-aws-84536f0c.md)
