---
title: AutoML Python API reference | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/automl/automl-api-reference
ingestedAt: "2026-06-18T08:09:21.819Z"
---

This article describes the AutoML Python API, which provides methods to start classification, regression, and forecasting AutoML runs. Each method call trains a set of models and generates a trial notebook for each model.

For more information on AutoML, including a low-code UI option, see [What is AutoML?](https://docs.databricks.com/aws/en/machine-learning/automl/).

## Classify[​](#classify "Direct link to classify")

The `databricks.automl.classify` method configures an AutoML run to train a classification model.

note

The `max_trials` parameter is deprecated in Databricks Runtime 10.4 ML and is not supported in Databricks Runtime 11.0 ML and above. Use `timeout_minutes` to control the duration of an AutoML run.

Python

    databricks.automl.classify(  dataset: Union[pyspark.sql.DataFrame, pandas.DataFrame, pyspark.pandas.DataFrame, str],  *,  target_col: str,  primary_metric: str = "f1",  data_dir: Optional[str] = None,  experiment_dir: Optional[str] = None,                             # :re[DBR] 10.4 LTS ML and above  experiment_name: Optional[str] = None,                            # :re[DBR] 12.1 ML and above  exclude_cols: Optional[List[str]] = None,                         # :re[DBR] 10.3 ML and above  exclude_frameworks: Optional[List[str]] = None,                   # :re[DBR] 10.3 ML and above  feature_store_lookups: Optional[List[Dict]] = None,               # :re[DBR] 11.3 LTS ML and above  imputers: Optional[Dict[str, Union[str, Dict[str, Any]]]] = None, # :re[DBR] 10.4 LTS ML and above  pos_label: Optional[Union[int, bool, str]] = None,                 # :re[DBR] 11.1 ML and above  time_col: Optional[str] = None,  split_col: Optional[str] = None,                                  # :re[DBR] 15.3 ML and above  sample_weight_col: Optional[str] = None                           # :re[DBR] 15.4 ML and above  max_trials: Optional[int] = None,                                 # :re[DBR] 10.5 ML and below  timeout_minutes: Optional[int] = None,) -> AutoMLSummary

### Classify parameters[​](#classify-parameters "Direct link to classify-parameters")

## Regress[​](#regress "Direct link to regress")

The `databricks.automl.regress` method configures an AutoML run to train a regression model. This method returns an [AutoMLSummary](#automlsummary).

note

The `max_trials` parameter is deprecated in Databricks Runtime 10.4 ML and is not supported in Databricks Runtime 11.0 ML and above. Use `timeout_minutes` to control the duration of an AutoML run.

Python

    databricks.automl.regress(  dataset: Union[pyspark.sql.DataFrame, pandas.DataFrame, pyspark.pandas.DataFrame, str],  *,  target_col: str,  primary_metric: str = "r2",  data_dir: Optional[str] = None,  experiment_dir: Optional[str] = None,                             # :re[DBR] 10.4 LTS ML and above  experiment_name: Optional[str] = None,                            # :re[DBR] 12.1 ML and above  exclude_cols: Optional[List[str]] = None,                         # :re[DBR] 10.3 ML and above  exclude_frameworks: Optional[List[str]] = None,                   # :re[DBR] 10.3 ML and above  feature_store_lookups: Optional[List[Dict]] = None,               # :re[DBR] 11.3 LTS ML and above  imputers: Optional[Dict[str, Union[str, Dict[str, Any]]]] = None, # :re[DBR] 10.4 LTS ML and above  time_col: Optional[str] = None,  split_col: Optional[str] = None,                                  # :re[DBR] 15.3 ML and above  sample_weight_col: Optional[str] = None,                          # :re[DBR] 15.3 ML and above  max_trials: Optional[int] = None,                                 # :re[DBR] 10.5 ML and below  timeout_minutes: Optional[int] = None,) -> AutoMLSummary

### Regress parameters[​](#regress-parameters "Direct link to regress-parameters")

## Forecast[​](#forecast "Direct link to forecast")

The `databricks.automl.forecast` method configures an AutoML run for training a forecasting model. This method returns an [AutoMLSummary](#automlsummary). To use Auto-ARIMA, the time series must have a regular frequency (that is, the interval between any two points must be the same throughout the time series). The frequency must match the frequency unit specified in the API call. AutoML handles missing time steps by filling in those values with the previous value.

Python

    databricks.automl.forecast(  dataset: Union[pyspark.sql.DataFrame, pandas.DataFrame, pyspark.pandas.DataFrame, str],  *,  target_col: str,  time_col: str,  primary_metric: str = "smape",  country_code: str = "US",                                         # :re[DBR] 12.0 ML and above  frequency: str = "D",  horizon: int = 1,  data_dir: Optional[str] = None,  experiment_dir: Optional[str] = None,  experiment_name: Optional[str] = None,                            # :re[DBR] 12.1 ML and above  exclude_frameworks: Optional[List[str]] = None,  feature_store_lookups: Optional[List[Dict]] = None,               # :re[DBR] 12.2 LTS ML and above  identity_col: Optional[Union[str, List[str]]] = None,  sample_weight_col: Optional[str] = None,                          # :re[DBR] 16.0 ML and above  output_database: Optional[str] = None,                            # :re[DBR] 10.5 ML and above  timeout_minutes: Optional[int] = None,) -> AutoMLSummary

### Forecasting parameters[​](#forecasting-parameters "Direct link to forecasting-parameters")

## Import notebook[​](#import-notebook "Direct link to import-notebook")

The `databricks.automl.import_notebook` method imports a notebook that has been saved as an MLflow artifact. This method returns an [ImportNotebookResult](#importnotebookresult).

Python

    databricks.automl.import_notebook(  artifact_uri: str,  path: str,  overwrite: bool = False) -> ImportNotebookResult:

### Import notebook example[​](#import-notebook-example "Direct link to Import notebook example")

Python

    summary = databricks.automl.classify(...)result = databricks.automl.import_notebook(summary.trials[5].artifact_uri, "/Users/you@yourcompany.com/path/to/directory")print(result.path)print(result.url)

## `AutoMLSummary`[​](#automlsummary "Direct link to automlsummary")

Summary object for an AutoML run that describes the metrics, parameters, and other details for each of the trials. You also use this object to load the model trained by a specific trial.

## `TrialInfo`[​](#trialinfo "Direct link to trialinfo")

Summary object for each individual trial.

`TrialInfo` has a method to load the model generated for the trial.

## `ImportNotebookResult`[​](#importnotebookresult "Direct link to importnotebookresult")
