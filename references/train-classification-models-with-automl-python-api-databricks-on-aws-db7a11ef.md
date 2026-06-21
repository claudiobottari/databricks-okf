---
title: Train classification models with AutoML Python API | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/automl/classification-train-api
ingestedAt: "2026-06-18T08:09:28.607Z"
---

This example notebook shows how to train a classification model on Databricks using the AutoML Python API. Using the UCI Census Income dataset, you call `automl.classify()` to predict whether an individual earns more than $50K per year, then use the best trial to run inference on both pandas and Spark DataFrames.

## Requirements[​](#requirements "Direct link to Requirements")

Databricks Runtime for Machine Learning.

## Census income dataset[​](#census-income-dataset "Direct link to Census income dataset")

This dataset contains census data from the 1994 census database. Each row represents a group of individuals. The goal is to determine whether a group has an income of over 50k a year or not. This classification is represented as a string in the **income** column with values `<=50K` or `>50k`.

Python

    from pyspark.sql.types import DoubleType, StringType, StructType, StructFieldschema = StructType([  StructField("age", DoubleType(), False),  StructField("workclass", StringType(), False),  StructField("fnlwgt", DoubleType(), False),  StructField("education", StringType(), False),  StructField("education_num", DoubleType(), False),  StructField("marital_status", StringType(), False),  StructField("occupation", StringType(), False),  StructField("relationship", StringType(), False),  StructField("race", StringType(), False),  StructField("sex", StringType(), False),  StructField("capital_gain", DoubleType(), False),  StructField("capital_loss", DoubleType(), False),  StructField("hours_per_week", DoubleType(), False),  StructField("native_country", StringType(), False),  StructField("income", StringType(), False)])input_df = spark.read.format("csv").schema(schema).load("/databricks-datasets/adult/adult.data")

## Train/test split[​](#traintest-split "Direct link to Train/test split")

Python

    train_df, test_df = input_df.randomSplit([0.99, 0.01], seed=42)display(train_df)

## Training[​](#training "Direct link to Training")

The following command starts an AutoML run. You must provide the column that the model should predict in the `target_col` argument.  
When the run completes, you can follow the link to the best trial notebook to examine the training code. This notebook also includes a feature importance plot.

Python

    from databricks import automlsummary = automl.classify(train_df, target_col="income", timeout_minutes=30)

The following command displays information about the AutoML output.

## Inference[​](#inference "Direct link to Inference")

You can use the model trained by AutoML to make predictions on new data. The examples below demonstrate how to make predictions on data in pandas DataFrames, or register the model as a Spark UDF for prediction on Spark DataFrames.

Python

    model_uri = summary.best_trial.model_path# model_uri = "<model-uri-from-generated-notebook>"

### pandas DataFrame[​](#pandas-dataframe "Direct link to pandas DataFrame")

Python

    import mlflow# Prepare test datasettest_pdf = test_df.toPandas()y_test = test_pdf["income"]X_test = test_pdf.drop("income", axis=1)# Run inference using the best modelmodel = mlflow.pyfunc.load_model(model_uri)predictions = model.predict(X_test)test_pdf["income_predicted"] = predictionsdisplay(test_pdf)

### Spark DataFrame[​](#spark-dataframe "Direct link to Spark DataFrame")

Python

    predict_udf = mlflow.pyfunc.spark_udf(spark, model_uri=model_uri, result_type="string")display(test_df.withColumn("income_predicted", predict_udf()))

### Test[​](#test "Direct link to Test")

Use the final model to make predictions on the holdout test set to estimate how the model would perform in a production setting. The diagram shows the breakdown between correct and incorrect predictions.

Python

    import sklearn.metricsmodel = mlflow.sklearn.load_model(model_uri)sklearn.metrics.plot_confusion_matrix(model, X_test, y_test)

## Register and deploy the model[​](#register-and-deploy-the-model "Direct link to Register and deploy the model")

You can register and deploy a model trained by AutoML like any other model in the MLflow Model Registry. See [Log, load, and register MLflow models](https://docs.databricks.com/aws/en/mlflow/models).

### Troubleshooting: `No module named pandas.core.indexes.numeric`[​](#troubleshooting-no-module-named-pandascoreindexesnumeric "Direct link to troubleshooting-no-module-named-pandascoreindexesnumeric")

When serving an AutoML\-trained model with Model Serving, you may see the error `No module named pandas.core.indexes.numeric`. This happens when the `pandas` version used by AutoML differs from the one in the model serving endpoint environment. To resolve:

1.  Download the [add-pandas-dependency.py script](https://docs.databricks.com/aws/en/assets/files/add-pandas-dependency-4808dc9dcdfb035bdca6ebce6b86d719.py). The script edits `requirements.txt` and `conda.yaml` for the logged model to pin `pandas==1.5.3`.
2.  Edit the script to include the `run_id` of the MLflow run where the model was logged.
3.  Re-register the model.
4.  Serve the new model version.

## Example notebook[​](#example-notebook "Direct link to Example notebook")

#### Train classification models with AutoML Python API

## Next steps[​](#next-steps "Direct link to Next steps")

[AutoML Python API reference](https://docs.databricks.com/aws/en/machine-learning/automl/automl-api-reference).
