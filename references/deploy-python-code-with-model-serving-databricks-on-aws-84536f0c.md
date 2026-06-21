---
title: Deploy Python code with Model Serving | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/model-serving/deploy-custom-python-code
ingestedAt: "2026-06-18T08:11:53.603Z"
---

This article describes how to deploy your customized Python code with [Model Serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/). The example in this article focuses on providing guidance for adding preprocessing and postprocessing logic to your model and deploying it.

MLflow's Python function, `pyfunc`, provides flexibility to deploy any piece of Python code or any Python model. The following are example scenarios where you might want to use the guide.

*   Your model requires preprocessing before inputs can be passed to the model's predict function.
*   Your model framework is not natively supported by MLflow.
*   Your application requires the model's raw outputs to be post-processed for consumption.
*   The model itself has per-request branching logic.
*   You are looking to deploy fully custom code as a model.

## Construct a custom MLflow Python function model[​](#construct-a-custom-mlflow-python-function-model "Direct link to Construct a custom MLflow Python function model")

MLflow offers the ability to log Python code with the [custom Python models format](https://mlflow.org/docs/latest/python_api/mlflow.pyfunc.html#creating-custom-pyfunc-models).

There are two required functions when packaging arbitrary python code with MLflow:

*   `load_context` - anything that needs to be loaded just one time for the model to operate should be defined in this function. This is critical so that the system minimize the number of artifacts loaded during the `predict` function, which speeds up inference.
*   `predict` - this function houses all the logic that is run every time an input request is made.

note

Prior to deploying your custom code as a model, it is beneficial to verify that the model is capable of being served. See the MLflow documentation for how you can use `mlflow.models.predict` to [validate models before deployment](https://www.mlflow.org/docs/latest/models.html#validate-models-before-deployment).

## Log your Python function model[​](#log-your-python-function-model "Direct link to Log your Python function model")

important

Databricks Runtime ML runtimes include `mlflow-skinny` by default rather than the full `mlflow` package. When you log a `pyfunc` model on one of these runtimes without specifying `pip_requirements`, MLflow captures `mlflow-skinny` in the model's `conda.yaml`. Model Serving requires `mlflow` (not `mlflow-skinny`) in `conda.yaml` and cannot build the container image otherwise. Always specify `mlflow==<version>` in `pip_requirements` when you call `mlflow.pyfunc.log_model()` on a Databricks Runtime ML runtime:

Python

    # DBR ML ships with mlflow-skinny by default, so specify mlflow explicitly# to ensure Model Serving compatibility.mlflow.pyfunc.log_model(    name="model",    python_model=your_model,    pip_requirements=["mlflow==3.8.1"],  # use mlflow, not mlflow-skinny    registered_model_name="catalog.schema.model_name",)

Even though you are writing your model with custom code, it is possible to use shared modules of code from your organization. With the `code_path` parameter, authors of models can log full code references that load into the path and are usable from other custom `pyfunc` models.

For example, if a model is logged with:

Python

    mlflow.pyfunc.log_model(CustomModel(), "model", code_path = ["preprocessing_utils/"])

Code from the `preprocessing_utils` is available in the loaded context of the model. The following is an example model that uses this code.

Python

    class CustomModel(mlflow.pyfunc.PythonModel):    def load_context(self, context):        self.model = torch.load(context.artifacts["model-weights"])        from preprocessing_utils.my_custom_tokenizer import CustomTokenizer        self.tokenizer = CustomTokenizer(context.artifacts["tokenizer_cache"])    def format_inputs(self, model_input):        # insert some code that formats your inputs        pass    def format_outputs(self, outputs):        predictions = (torch.sigmoid(outputs)).data.numpy()        return predictions    def predict(self, context, model_input):        model_input = self.format_inputs(model_input)        outputs = self.model.predict(model_input)        return self.format_outputs(outputs)

## Serve your model[​](#serve-your-model "Direct link to Serve your model")

After you log your custom `pyfunc` model, you can register it to Unity Catalog or Workspace Registry and serve your model to a [Model Serving endpoint](https://docs.databricks.com/aws/en/machine-learning/model-serving/create-manage-serving-endpoints).

## Notebook example[​](#notebook-example "Direct link to Notebook example")

The following notebook example demonstrates how to customize model output when the raw output of the queried model needs to be post-processed for consumption.

#### Customize model serving output with MLflow PyFunc notebook
