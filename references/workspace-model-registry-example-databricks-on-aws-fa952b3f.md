---
title: Workspace Model Registry example | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow/workspace-model-registry-example
ingestedAt: "2026-06-18T08:14:22.432Z"
---

note

This documentation covers the Workspace Model Registry. Databricks recommends using [Models in Unity Catalog](https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/). Models in Unity Catalog provides centralized model governance, cross-workspace access, lineage, and deployment. Workspace Model Registry will be deprecated in the future.

This example illustrates how to use the Workspace Model Registry to build a machine learning application that forecasts the daily power output of a wind farm. The example shows how to:

*   Track and log models with MLflow
*   Register models with the Model Registry
*   Describe models and make model version stage transitions
*   Integrate registered models with production applications
*   Search and discover models in the Model Registry
*   Archive and delete models

The article describes how to perform these steps using the MLflow Tracking and MLflow Model Registry UIs and APIs.

For a notebook that performs all these steps using the MLflow Tracking and Registry APIs, see the [Model Registry example notebook](#notebook).

## Load dataset, train model, and track with MLflow Tracking[​](#load-dataset-train-model-and-track-with-mlflow-tracking "Direct link to Load dataset, train model, and track with MLflow Tracking")

Before you can register a model in the Model Registry, you must first train and log the [model](https://docs.databricks.com/aws/en/mlflow/models) during an [experiment run](https://docs.databricks.com/aws/en/mlflow/experiments). This section shows how to load the wind farm dataset, train a model, and log the training run to MLflow.

### Load dataset[​](#load-dataset "Direct link to Load dataset")

The following code loads a dataset containing weather data and power output information for a wind farm in the United States. The dataset contains `wind direction`, `wind speed`, and `air temperature` features sampled every six hours (once at `00:00`, once at `08:00`, and once at `16:00`), as well as daily aggregate power output (`power`), over several years.

Python

    import pandas as pdwind_farm_data = pd.read_csv("https://github.com/dbczumar/model-registry-demo-notebook/raw/master/dataset/windfarm_data.csv", index_col=0)def get_training_data():  training_data = pd.DataFrame(wind_farm_data["2014-01-01":"2018-01-01"])  X = training_data.drop(columns="power")  y = training_data["power"]  return X, ydef get_validation_data():  validation_data = pd.DataFrame(wind_farm_data["2018-01-01":"2019-01-01"])  X = validation_data.drop(columns="power")  y = validation_data["power"]  return X, ydef get_weather_and_forecast():  format_date = lambda pd_date : pd_date.date().strftime("%Y-%m-%d")  today = pd.Timestamp('today').normalize()  week_ago = today - pd.Timedelta(days=5)  week_later = today + pd.Timedelta(days=5)  past_power_output = pd.DataFrame(wind_farm_data)[format_date(week_ago):format_date(today)]  weather_and_forecast = pd.DataFrame(wind_farm_data)[format_date(week_ago):format_date(week_later)]  if len(weather_and_forecast) < 10:    past_power_output = pd.DataFrame(wind_farm_data).iloc[-10:-5]    weather_and_forecast = pd.DataFrame(wind_farm_data).iloc[-10:]  return weather_and_forecast.drop(columns="power"), past_power_output["power"]

### Train model[​](#train-model "Direct link to Train model")

The following code trains a neural network using TensorFlow Keras to predict power output based on the weather features in the dataset. MLflow is used to track the model's hyperparameters, performance metrics, source code, and artifacts.

Python

    def train_keras_model(X, y):  import tensorflow.keras  from tensorflow.keras.models import Sequential  from tensorflow.keras.layers import Dense  model = Sequential()  model.add(Dense(100, input_shape=(X_train.shape[-1],), activation="relu", name="hidden_layer"))  model.add(Dense(1))  model.compile(loss="mse", optimizer="adam")  model.fit(X_train, y_train, epochs=100, batch_size=64, validation_split=.2)  return modelimport mlflowX_train, y_train = get_training_data()with mlflow.start_run():  # Automatically capture the model's parameters, metrics, artifacts,  # and source code with the `autolog()` function  mlflow.tensorflow.autolog()  train_keras_model(X_train, y_train)  run_id = mlflow.active_run().info.run_id

## Register and manage the model using the MLflow UI[​](#register-and-manage-the-model-using-the-mlflow-ui "Direct link to Register and manage the model using the MLflow UI")

**In this section:**

*   [Create a new registered model](#create-a-new-registered-model)
*   [Explore the Model Registry UI](#explore-the-model-registry-ui)
*   [Add model descriptions](#add-model-descriptions)
*   [Transition a model version](#transition-a-model-version)

### Create a new registered model[​](#create-a-new-registered-model "Direct link to Create a new registered model")

1.  Navigate to the MLflow Experiment Runs sidebar by clicking the **Experiment** icon ![Experiment icon](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABUAAAAVCAYAAACpF6WWAAAAAXNSR0IArs4c6QAAAERlWElmTU0AKgAAAAgAAYdpAAQAAAABAAAAGgAAAAAAA6ABAAMAAAABAAEAAKACAAQAAAABAAAAFaADAAQAAAABAAAAFQAAAAAIGxIOAAABUUlEQVQ4EWP8DwQMVAZMVDYPbBxNDGUh5NL04jqGe4+eoChTkpNhmNnbhCKGzCFoKMhAYz0tBgMdDbC+C1duMJy9dA3ZDAw2QUNBOkAGRgT6wDUTMpQmYTpMDP0HzRdMjIzw8ISx8eUZvN4/eeYC2DBREWG4oTD2qfOX4GLoDEZc2XTf4RMMnVPmMPz7948hOtiXgYOdFaz3x49fDEvXbWFgYmJiqMhLYXC0tkA3kwHDUJCXFyxfx7B8/VYMxdgEQBbGhwcwMCIFEQPIpchgzaYd/11CEv9Pmr3o/9+/f5GlUNggud5pc8Fq123ZhSKHYWhoYv7/lr5pKIrwcRq7J/+PTC9GUYKRo8TFhRkePXnOsGL9Fmy+xRB78uwlg7iIEIo4RpjeuHWXoWvqXIbHz16gKMTFkZeWZCjNTWFQV1aEK8EwFC5DAQNvOiXX3KFjKAAbsvOWj3bmtQAAAABJRU5ErkJggg==) in the Databricks notebook's right sidebar.
    
    ![Runs sidebar](https://docs.databricks.com/aws/en/assets/images/notebook-toolbar-70a2fafa48b3a925099e836a4d5fb0ae.png)
    
2.  Locate the MLflow Run corresponding to the TensorFlow Keras model training session, and open it in the MLflow Run UI by clicking the **View Run Detail** icon.
    
3.  In the MLflow UI, scroll down to the **Artifacts** section and click the directory named **model**. Click the **Register Model** button that appears.
    
    ![Register model](https://docs.databricks.com/aws/en/assets/images/mlflow_ui_register_model-ff6251ef8dc151e0e8f918b2d5451af1.png)
    
4.  Select **Create New Model** from the drop-down menu, and input the following model name: `power-forecasting-model`.
    
5.  Click **Register**. This registers a new model called `power-forecasting-model` and creates a new model version: `Version 1`.
    
    ![New model version](https://docs.databricks.com/aws/en/assets/images/register_model_confirm-9a11ba1eb44abaecce5ac47a8db94205.png)
    
    After a few moments, the MLflow UI displays a link to the new registered model. Follow this link to open the new model version in the MLflow Model Registry UI.
    

### Explore the Model Registry UI[​](#explore-the-model-registry-ui "Direct link to Explore the Model Registry UI")

The model version page in the MLflow Model Registry UI provides information about `Version 1` of the registered forecasting model, including its author, creation time, and its current stage.

![Model version page](https://docs.databricks.com/aws/en/assets/images/registry_version_page-eca0d898dbb8c46bb5d6ee90804242ea.png)

The model version page also provides a **Source Run** link, which opens the MLflow Run that was used to create the model in the MLflow Run UI. From the MLflow Run UI, you can access the **Source** notebook link to view a snapshot of the Databricks notebook that was used to train the model.

![Source run](https://docs.databricks.com/aws/en/assets/images/source_run_link-c7765cd30cc6638696de200f2ce48e56.png)

![Source notebook](https://docs.databricks.com/aws/en/assets/images/source_notebook_link-8f1f1e871327adc72190e760086c50a1.png)

To navigate back to the MLflow Model Registry, click ![Models Icon](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAB4AAAAeCAYAAAA7MK6iAAAAAXNSR0IArs4c6QAAAERlWElmTU0AKgAAAAgAAYdpAAQAAAABAAAAGgAAAAAAA6ABAAMAAAABAAEAAKACAAQAAAABAAAAHqADAAQAAAABAAAAHgAAAADKQTcFAAADQ0lEQVRIDe1WWUhUURj+xlS0RYeEBHPcdw1NS8cUKwvbBKOMTMqiogehICJ8CCJ6sagsinoQyiQhLJU0MZWgtMClNMs1KcqyXkJTM9fR6f5H73TvnbkzdzLwoX4427995/znv/+5Kq/YRD3mgWzmAZNB/geec+TPnjiGtsflrNFcjhaoNd5n5ITW8glo384U2NvZsRYeEgQXtRpP6hqMXM35ju1t7aBdGY7MjHSkb09mACkHM0GNaMeWJDZKO1spg3bNK5c8qsbpS1dFKq4uLohcEcq1EESGzYwiBYULETAfKt6WwqZ2dkJ9U4sByNvDnRcbxtaubjS3dsDXU4P46CiU3rphkNHmTZFKWEAoKRYtdDSESeiANx4eGWEgza3taG7r5Fo7fnI8ni6cOonUbZuh1+tRUFJmFDFeT3Rinikd6cSVNc8YYOvbbqlYtL73sJIBt3R0yYKSgQiYwkLhlZ5UGxWBCZ0OHz59EYGYWni6uzF2T695XVFWUyLdKS7lQjeKyUkdBoaG2HroxzASYlYh/8o55F8+j4To1aYwGc/LfTkbP362ApgsCDxsYzKKK6qgdnJC3/cBaFN2Iyc3D4MKNuCpmQHu6f3KNiDXiU4sVKqqec6Wm9bGY3RsDNduFyBWwQb4E/f09grdGc1FWS2VNlWUYKnaGVszjqDz3XuD2NHBAYfTUnFozy44L1nM+LUNL7nrmcT6NTFQqVS4X16JrOyLBhvpxGzJ9ObuKywoAN/6+tHw6rXBVsclWmPLG+QXPcD4+ARCAvwQ6OMNHw8NAyXg0EB/2XJJjmRDTUJhuGktpd9XkIYJ7rRESsol6ZkFflrfiP6BQQT7+yLYz5f0/xqZBSaU6tkkS0qIMwKluz56YC/qSgvZa0QKVAP4OiBXLknPbHKRwjptNPJysjE9Pc1l9zjIWfb1XNnk0kZGkBnTkz4wTDDbiSqXUMDPE+O0bGpjY8PqOFW2DfGxcHNdxviUzTfvFqG28QVvomi0CMw/kfz7SmGkT+xPAfldWQTmFYXj1NQ09h/PErKsnlsENvVwmEsapTswW0DICf0v0X+Tn5cnezgKyyrMPndKgS1mtVJH1upZ/I6tdahU/98D/gXOKT9CrMPb5gAAAABJRU5ErkJggg==) **Models** in sidebar.

The resulting MLflow Model Registry home page displays a list of all the registered models in your Databricks workspace, including their versions and stages.

Click the **power-forecasting-model** link to open the registered model page, which displays all of the versions of the forecasting model.

### Add model descriptions[​](#add-model-descriptions "Direct link to Add model descriptions")

You can add descriptions to registered models and model versions. Registered model descriptions are useful for recording information that applies to multiple model versions (e.g., a general overview of the modeling problem and dataset). Model version descriptions are useful for detailing the unique attributes of a particular model version (e.g., the methodology and algorithm used to develop the model).

1.  Add a high-level description to the registered power forecasting model. Click the ![Edit Icon](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAAXlJREFUOBFj/A8ERx58ZsAFbBR4cUmBxVlAmu0W3sSp6F+9CVzu99//DElr7jFoi3MyVDhIQQyAyR6KV4cxsdJff/0Da+ZiZWKoOvgMrAZkCAuyalzO/fD9D0PS2vsMYtysDDMCFRgYVjMwXHv5A6yVCdkAbOzXX34zxKy6xyDDzwbWnL7uAcP3P/8Y5oYoEjbg6adfYM2aopwMk3zlGXI2PmR48/U3w9xgJQZWZkb8Bjx4/5MhZuVdBmNpboZuL1mGoq2PGB5++Am2mZsN4XAEC8n9t9/+ZIgGarZX5GNoc5dhqNjxhOHqy+8M84DOFuBECTYGrAYUbH7A4K0uwNDgIs1Qv+cpw8nHnxnmAzWLAgMRBEBRz9R4BkyjGofkCjtFXoa2/c8Y9tz5yLA0XJlBio8NSRbBxGqACBcrQ/sBSFwvCFVmUBBkR+hAY2E1YGGYEpoy3FysYYBbOaYMigvwZSpMrRARuAH4MhQuzSBxRkLZGZ9mUN4BACDdfCOqyNytAAAAAElFTkSuQmCC) icon and enter the following description:
    
        This model forecasts the power output of a wind farm based on weather data. The weather data consists of three features: wind speed, wind direction, and air temperature.
    
    ![Add model description](https://docs.databricks.com/aws/en/assets/images/model_description-8c2c48129bc35e794e245cfa30d442b8.png)
    
2.  Click **Save**.
    
3.  Click the **Version 1** link from the registered model page to navigate back to the model version page.
    
4.  Click the ![Edit Icon](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAAXlJREFUOBFj/A8ERx58ZsAFbBR4cUmBxVlAmu0W3sSp6F+9CVzu99//DElr7jFoi3MyVDhIQQyAyR6KV4cxsdJff/0Da+ZiZWKoOvgMrAZkCAuyalzO/fD9D0PS2vsMYtysDDMCFRgYVjMwXHv5A6yVCdkAbOzXX34zxKy6xyDDzwbWnL7uAcP3P/8Y5oYoEjbg6adfYM2aopwMk3zlGXI2PmR48/U3w9xgJQZWZkb8Bjx4/5MhZuVdBmNpboZuL1mGoq2PGB5++Am2mZsN4XAEC8n9t9/+ZIgGarZX5GNoc5dhqNjxhOHqy+8M84DOFuBECTYGrAYUbH7A4K0uwNDgIs1Qv+cpw8nHnxnmAzWLAgMRBEBRz9R4BkyjGofkCjtFXoa2/c8Y9tz5yLA0XJlBio8NSRbBxGqACBcrQ/sBSFwvCFVmUBBkR+hAY2E1YGGYEpoy3FysYYBbOaYMigvwZSpMrRARuAH4MhQuzSBxRkLZGZ9mUN4BACDdfCOqyNytAAAAAElFTkSuQmCC) icon and enter the following description:
    
        This model version was built using TensorFlow Keras. It is a feed-forward neural network with one hidden layer.
    
    ![Add model version description](https://docs.databricks.com/aws/en/assets/images/model_version_description-d2575a0ed7bf6ea6ac1a588e13412dbd.png)
    
5.  Click **Save**.
    

### Transition a model version[​](#transition-a-model-version "Direct link to Transition a model version")

The MLflow Model Registry defines several model stages: **None**, **Staging**, **Production**, and `Archived`. Each stage has a unique meaning. For example, **Staging** is meant for model testing, while **Production** is for models that have completed the testing or review processes and have been deployed to applications.

1.  Click the **Stage** button to display the list of available model stages and your available stage transition options.
    
2.  Select **Transition to -> Production** and press **OK** in the stage transition confirmation window to transition the model to **Production**.
    
    ![Transition to production](https://docs.databricks.com/aws/en/assets/images/stage_transition_prod-0029b892b3785e9cd8a28c6568191fe3.png)
    
    After the model version is transitioned to **Production**, the current stage is displayed in the UI, and an entry is added to the activity log to reflect the transition.
    
    ![Production stage](https://docs.databricks.com/aws/en/assets/images/stage_production-91bc1e2550c0ea587488537a72aa843b.png)
    
    ![Model version activity](https://docs.databricks.com/aws/en/assets/images/activity_production-380703119fe316167665a4ae41dc2d26.png)
    

The MLflow Model Registry allows multiple model versions to share the same stage. When referencing a model by stage, the Model Registry uses the latest model version (the model version with the largest version ID). The registered model page displays all of the versions of a particular model.

![Registered model page](https://docs.databricks.com/aws/en/assets/images/model_registry_versions-646f4801d1a54bd227e107f3894aa354.png)

## Register and manage the model using the MLflow API[​](#register-and-manage-the-model-using-the-mlflow-api "Direct link to Register and manage the model using the MLflow API")

**In this section:**

*   [Define the model's name programmatically](#define-the-models-name-programmatically)
*   [Register the model](#register-the-model)
*   [Add model and model version descriptions using the API](#add-model-and-model-version-descriptions-using-the-api)
*   [Transition a model version and retrieve details using the API](#transition-a-model-version-and-retrieve-details-using-the-api)

### Define the model's name programmatically[​](#define-the-models-name-programmatically "Direct link to Define the model's name programmatically")

Now that the model has been registered and transitioned to **Production**, you can reference it using MLflow programmatic APIs. Define the registered model's name as follows:

Python

    model_name = "power-forecasting-model"

### Register the model[​](#register-the-model "Direct link to Register the model")

Python

    model_name = get_model_name()import mlflow# The default path where the MLflow autologging function stores the TensorFlow Keras modelartifact_path = "model"model_uri = "runs:/{run_id}/{artifact_path}".format(run_id=run_id, artifact_path=artifact_path)model_details = mlflow.register_model(model_uri=model_uri, name=model_name)import timefrom mlflow.tracking.client import MlflowClientfrom mlflow.entities.model_registry.model_version_status import ModelVersionStatus# Wait until the model is readydef wait_until_ready(model_name, model_version):  client = MlflowClient()  for _ in range(10):    model_version_details = client.get_model_version(      name=model_name,      version=model_version,    )    status = ModelVersionStatus.from_string(model_version_details.status)    print("Model status: %s" % ModelVersionStatus.to_string(status))    if status == ModelVersionStatus.READY:      break    time.sleep(1)wait_until_ready(model_details.name, model_details.version)

### Add model and model version descriptions using the API[​](#add-model-and-model-version-descriptions-using-the-api "Direct link to Add model and model version descriptions using the API")

Python

    from mlflow.tracking.client import MlflowClientclient = MlflowClient()client.update_registered_model(  name=model_details.name,  description="This model forecasts the power output of a wind farm based on weather data. The weather data consists of three features: wind speed, wind direction, and air temperature.")client.update_model_version(  name=model_details.name,  version=model_details.version,  description="This model version was built using TensorFlow Keras. It is a feed-forward neural network with one hidden layer.")

### Transition a model version and retrieve details using the API[​](#transition-a-model-version-and-retrieve-details-using-the-api "Direct link to Transition a model version and retrieve details using the API")

Python

    client.transition_model_version_stage(  name=model_details.name,  version=model_details.version,  stage='production',)model_version_details = client.get_model_version(  name=model_details.name,  version=model_details.version,)print("The current model stage is: '{stage}'".format(stage=model_version_details.current_stage))latest_version_info = client.get_latest_versions(model_name, stages=["production"])latest_production_version = latest_version_info[0].versionprint("The latest production version of the model '%s' is '%s'." % (model_name, latest_production_version))

## Load versions of the registered model using the API[​](#load-versions-of-the-registered-model-using-the-api "Direct link to Load versions of the registered model using the API")

The MLflow Models component defines functions for loading models from several machine learning frameworks. For example, `mlflow.tensorflow.load_model()` is used to load TensorFlow models that were saved in MLflow format, and `mlflow.sklearn.load_model()` is used to load scikit-learn models that were saved in MLflow format.

These functions can load models from the MLflow Model Registry.

Python

    import mlflow.pyfuncmodel_version_uri = "models:/{model_name}/1".format(model_name=model_name)print("Loading registered model version from URI: '{model_uri}'".format(model_uri=model_version_uri))model_version_1 = mlflow.pyfunc.load_model(model_version_uri)model_production_uri = "models:/{model_name}/production".format(model_name=model_name)print("Loading registered model version from URI: '{model_uri}'".format(model_uri=model_production_uri))model_production = mlflow.pyfunc.load_model(model_production_uri)

## Forecast power output with the production model[​](#forecast-power-output-with-the-production-model "Direct link to Forecast power output with the production model")

In this section, the production model is used to evaluate weather forecast data for the wind farm. The `forecast_power()` application loads the latest version of the forecasting model from the specified stage and uses it to forecast power production over the next five days.

Python

    def plot(model_name, model_stage, model_version, power_predictions, past_power_output):  import pandas as pd  import matplotlib.dates as mdates  from matplotlib import pyplot as plt  index = power_predictions.index  fig = plt.figure(figsize=(11, 7))  ax = fig.add_subplot(111)  ax.set_xlabel("Date", size=20, labelpad=20)  ax.set_ylabel("Power\noutput\n(MW)", size=20, labelpad=60, rotation=0)  ax.tick_params(axis='both', which='major', labelsize=17)  ax.xaxis.set_major_formatter(mdates.DateFormatter('%m/%d'))  ax.plot(index[:len(past_power_output)], past_power_output, label="True", color="red", alpha=0.5, linewidth=4)  ax.plot(index, power_predictions.squeeze(), "--", label="Predicted by '%s'\nin stage '%s' (Version %d)" % (model_name, model_stage, model_version), color="blue", linewidth=3)  ax.set_ylim(ymin=0, ymax=max(3500, int(max(power_predictions.values) * 1.3)))  ax.legend(fontsize=14)  plt.title("Wind farm power output and projections", size=24, pad=20)  plt.tight_layout()  display(plt.show())def forecast_power(model_name, model_stage):  from mlflow.tracking.client import MlflowClient  client = MlflowClient()  model_version = client.get_latest_versions(model_name, stages=[model_stage])[0].version  model_uri = "models:/{model_name}/{model_stage}".format(model_name=model_name, model_stage=model_stage)  model = mlflow.pyfunc.load_model(model_uri)  weather_data, past_power_output = get_weather_and_forecast()  power_predictions = pd.DataFrame(model.predict(weather_data))  power_predictions.index = pd.to_datetime(weather_data.index)  print(power_predictions)  plot(model_name, model_stage, int(model_version), power_predictions, past_power_output)

## Create a new model version[​](#create-a-new-model-version "Direct link to Create a new model version")

Classical machine learning techniques are also effective for power forecasting. The following code trains a random forest model using scikit-learn and registers it with the MLflow Model Registry via the `mlflow.sklearn.log_model()` function.

Python

    import mlflow.sklearnfrom sklearn.ensemble import RandomForestRegressorfrom sklearn.metrics import mean_squared_errorwith mlflow.start_run():  n_estimators = 300  mlflow.log_param("n_estimators", n_estimators)  rand_forest = RandomForestRegressor(n_estimators=n_estimators)  rand_forest.fit(X_train, y_train)  val_x, val_y = get_validation_data()  mse = mean_squared_error(rand_forest.predict(val_x), val_y)  print("Validation MSE: %d" % mse)  mlflow.log_metric("mse", mse)  # Specify the `registered_model_name` parameter of the `mlflow.sklearn.log_model()`  # function to register the model with the MLflow Model Registry. This automatically  # creates a new model version  mlflow.sklearn.log_model(    sk_model=rand_forest,    artifact_path="sklearn-model",    registered_model_name=model_name,  )

### Fetch the new model version ID using MLflow Model Registry search[​](#fetch-the-new-model-version-id-using-mlflow-model-registry-search "Direct link to Fetch the new model version ID using MLflow Model Registry search")

Python

    from mlflow.tracking.client import MlflowClientclient = MlflowClient()model_version_infos = client.search_model_versions("name = '%s'" % model_name)new_model_version = max([model_version_info.version for model_version_info in model_version_infos])wait_until_ready(model_name, new_model_version)

### Add a description to the new model version[​](#add-a-description-to-the-new-model-version "Direct link to Add a description to the new model version")

Python

    client.update_model_version(  name=model_name,  version=new_model_version,  description="This model version is a random forest containing 100 decision trees that was trained in scikit-learn.")

### Transition the new model version to Staging and test the model[​](#transition-the-new-model-version-to-staging-and-test-the-model "Direct link to Transition the new model version to Staging and test the model")

Before deploying a model to a production application, it is often best practice to test it in a staging environment. The following code transitions the new model version to **Staging** and evaluates its performance.

Python

    client.transition_model_version_stage(  name=model_name,  version=new_model_version,  stage="Staging",)forecast_power(model_name, "Staging")

### Deploy the new model version to Production[​](#deploy-the-new-model-version-to-production "Direct link to Deploy the new model version to Production")

After verifying that the new model version performs well in staging, the following code transitions the model to **Production** and uses the exact same application code from the [Forecast power output with the production model](#forecast-power-output-with-the-production-model) section to produce a power forecast.

Python

    client.transition_model_version_stage(  name=model_name,  version=new_model_version,  stage="production",)forecast_power(model_name, "production")

There are now two model versions of the forecasting model in the **Production** stage: the model version trained in Keras model and the version trained in scikit-learn.

![Product model versions](https://docs.databricks.com/aws/en/assets/images/multiple_prod_stage-873765f4abc835464142f29521d63aaa.png)

note

When referencing a model by stage, the MLflow Model Model Registry automatically uses the latest production version. This enables you to update your production models without changing any application code.

## Archive and delete models[​](#archive-and-delete-models "Direct link to Archive and delete models")

When a model version is no longer being used, you can archive it or delete it. You can also delete an entire registered model; this removes all of its associated model versions.

### Archive `Version 1` of the power forecasting model[​](#archive-version-1-of-the-power-forecasting-model "Direct link to archive-version-1-of-the-power-forecasting-model")

Archive `Version 1` of the power forecasting model because it is no longer being used. You can archive models in the MLflow Model Registry UI or via the MLflow API.

### Archive `Version 1` in the MLflow UI[​](#archive-version-1-in-the-mlflow-ui "Direct link to archive-version-1-in-the-mlflow-ui")

To archive `Version 1` of the power forecasting model:

1.  Open its corresponding model version page in the MLflow Model Registry UI:
    
    ![Transition to archived](https://docs.databricks.com/aws/en/assets/images/stage_transition_archived-97506b2b3e4354089088f5e9e8f253c1.png)
    
2.  Click the **Stage** button, select **Transition To -> Archived**:
    
    ![Archived stage](https://docs.databricks.com/aws/en/assets/images/confirm_archived_transition-abbdb65373f81b1306baf31aae6d398f.png)
    
3.  Press **OK** in the stage transition confirmation window.
    
    ![Archived model version](https://docs.databricks.com/aws/en/assets/images/stage_archived-92cb223472643a9dee2c26623e881396.png)
    

#### Archive `Version 1` using the MLflow API[​](#archive-version-1-using-the-mlflow-api "Direct link to archive-version-1-using-the-mlflow-api")

The following code uses the `MlflowClient.update_model_version()` function to archive `Version 1` of the power forecasting model.

Python

    from mlflow.tracking.client import MlflowClientclient = MlflowClient()client.transition_model_version_stage(  name=model_name,  version=1,  stage="Archived",)

#### Delete `Version 1` of the power forecasting model[​](#delete-version-1-of-the-power-forecasting-model "Direct link to delete-version-1-of-the-power-forecasting-model")

You can also use the MLflow UI or MLflow API to delete model versions.

warning

Model version deletion is permanent and cannot be undone.

##### Delete `Version 1` in the MLflow UI[​](#delete-version-1-in-the-mlflow-ui "Direct link to delete-version-1-in-the-mlflow-ui")

To delete `Version 1` of the power forecasting model:

1.  Open its corresponding model version page in the MLflow Model Registry UI.
    
    ![Delete model version](https://docs.databricks.com/aws/en/assets/images/delete_version-840bfdf7ab7190e1554a1f85e4761e55.png)
    
2.  Select the drop-down arrow next to the version identifier and click **Delete**.
    

##### Delete `Version 1` using the MLflow API[​](#delete-version-1-using-the-mlflow-api "Direct link to delete-version-1-using-the-mlflow-api")

Python

    client.delete_model_version(   name=model_name,   version=1,)

##### Delete the model using the MLflow API[​](#delete-the-model-using-the-mlflow-api "Direct link to Delete the model using the MLflow API")

You must first transition all remaining model version stages to **None** or **Archived**.

Python

    from mlflow.tracking.client import MlflowClientclient = MlflowClient()client.transition_model_version_stage(  name=model_name,  version=2,  stage="Archived",)

Python

    client.delete_registered_model(name=model_name)

## Notebook[​](#notebook "Direct link to Notebook")

#### MLflow Model Registry example notebook
