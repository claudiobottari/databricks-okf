---
title: Pre-deployment validation for Model Serving | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/model-serving/model-serving-pre-deployment-validation
ingestedAt: "2026-06-18T08:12:15.048Z"
---

The guidance in this article can help you catch issues with your model before waiting for the endpoint deployment process. Databricks recommends going through these validation steps to ensure a better development experience when using model serving.

## Test predictions before deployment[​](#test-predictions-before-deployment "Direct link to Test predictions before deployment")

Before deploying your model to the serving endpoint, test offline predictions with a virtual environment using `mlflow.models.predict` and input examples. MLflow provides validation APIs that simulate the deployment environment and allow testing of modified dependencies.

There are two pre-deployment validation options: the [MLflow Python API](https://mlflow.org/docs/latest/python_api/mlflow.models.html#mlflow.models.predict) and the [MLflow CLI](https://mlflow.org/docs/latest/cli.html#mlflow-models-predict). See [MLflow documentation for testing predictions](https://mlflow.org/docs/latest/model/dependencies.html#validating-environment-for-prediction) for more detailed guidance.

You can specify the following parameters:

*   The `model_uri` of the model that is deployed to model serving.
*   One of the following:
    *   The `input_data` in the expected format for the `mlflow.pyfunc.PyFuncModel.predict()` call of the model.
    *   The `input_path` that defines a file containing input data that will be loaded and used for the call to `predict`.
*   The `content_type` in `csv` or `json` format.
*   An optional `output_path` to write the predictions to a file. If you omit this parameter, the predictions are printed to `stdout`.
*   An environment manager, `env_manager`, that is used to build the environment for serving:
    *   The default is `virtualenv`. Recommended for serving validation.
    *   `local` is available, but potentially error prone for serving validation. Generally used only for rapid debugging.
*   Whether to install the current version of MLflow that is in your environment with the virtual environment using `install_mlflow`. This setting defaults to `False`.
*   Whether to update and test different versions of package dependencies for troubleshooting or debugging. You can specify this as a list of string dependency overrides or additions using the override argument, `pip_requirements_override`.

For example:

Python

    import mlflowrun_id = "..."model_uri = f"runs:/{run_id}/model"mlflow.models.predict(  model_uri=model_uri,  input_data={"col1": 34.2, "col2": 11.2, "col3": "green"},  content_type="json",  env_manager="virtualenv",  install_mlflow=False,  pip_requirements_override=["pillow==10.3.0", "scipy==1.13.0"],)

## Update model dependencies[​](#update-model-dependencies "Direct link to Update model dependencies")

If there are any issues with the dependencies specified with a logged model, you can update the requirements by using the [MLflow CLI](https://mlflow.org/docs/latest/cli.html#mlflow-models-update-pip-requirements) or `mlflow.models.model.update_model_requirements()` in the MLflow Python API without having to log another model.

The following example shows how to update the `pip_requirements.txt` of a logged model in-place.

You can update existing definitions with specified package versions or add non-existent requirements to the `pip_requirements.txt` file. This file is within the MLflow model artifact at the specified `model_uri` location.

Python

    from mlflow.models.model import update_model_requirementsupdate_model_requirements(  model_uri=model_uri,  operation="add",  requirement_list=["pillow==10.2.0", "scipy==1.12.0"],)

## Validate the model input before deployment[​](#validate-the-model-input-before-deployment "Direct link to validate-the-model-input-before-deployment")

Model serving endpoints expect a special format of JSON input. You can validate that your model input works on a serving endpoint before deployment using `validate_serving_input` in MLflow.

The following is an example of the auto-generated code in the run's artifacts tab if your model is logged with a valid input example.

Python

    from mlflow.models import validate_serving_inputmodel_uri = 'runs:/<run_id>/<artifact_path>'serving_payload = """{ "messages": [   {     "content": "How many product categories are there?",     "role": "user"   } ]}"""# Validate the serving payload works on the modelvalidate_serving_input(model_uri, serving_payload)

You can also test any input examples against the logged model by using the `convert_input_example_to_serving_input` API to generate a valid JSON serving input.

Python

    from mlflow.models import validate_serving_inputfrom mlflow.models import convert_input_example_to_serving_inputmodel_uri = 'runs:/<run_id>/<artifact_path>'# Define INPUT_EXAMPLE with your own input example to the model# A valid input example is a data instance suitable for pyfunc predictionserving_payload = convert_input_example_to_serving_input(INPUT_EXAMPLE)# Validate the serving payload works on the modelvalidate_serving_input(model_uri, serving_payload)

## Manually test serving the model[​](#manually-test-serving-the-model "Direct link to Manually test serving the model")

You can manually test the serving behavior of the model using the following steps:

1.  Open a notebook and attach to an All-Purpose cluster that uses a Databricks Runtime version, not Databricks Runtime for Machine Learning.
2.  Load the model using MLflow and try debugging from there.

You can also load the model locally on your PC and debug from there. Load your model locally using the following:

Python

    import osimport mlflowos.environ["MLFLOW_TRACKING_URI"] = "databricks://PROFILE"ARTIFACT_URI = "model_uri"if '.' in ARTIFACT_URI:    mlflow.set_registry_uri('databricks-uc')local_path = mlflow.artifacts.download_artifacts(ARTIFACT_URI)print(local_path)conda env create -f local_path/artifact_path/conda.yamlconda activate mlflow-envmlflow.pyfunc.load_model(local_path/artifact_path)
