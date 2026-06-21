---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 64c7bf8bd74ae963d423cbfd3ef7948119d2521caa10f61df687fabb6cc267a0
  pageDirectory: concepts
  sources:
    - use-apache-spark-mllib-on-databricks-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - gradient-boosted-trees-regression-with-mllib
    - GBTRWM
    - Gradient Boosted Trees
    - Gradient Boosted Trees (GBT)
  citations:
    - file: use-apache-spark-mllib-on-databricks-databricks-on-aws.md
title: Gradient Boosted Trees Regression with MLlib
description: Using MLlib pipelines to perform regression with gradient boosted trees, demonstrated with bike rental count prediction.
tags:
  - machine-learning
  - mllib
  - regression
  - gradient-boosting
timestamp: "2026-06-19T23:21:05.146Z"
---

## Gradient Boosted Trees Regression with MLlib

**Gradient Boosted Trees (GBT) Regression** is a machine learning algorithm implemented in [Apache Spark MLlib](/concepts/apache-spark-mllib.md) that builds an ensemble of decision trees sequentially, where each new tree corrects the errors of the previous ones. GBT regression is used for predicting a continuous target variable and is well-suited for datasets with mixed feature types (numeric and categorical) and non-linear relationships. MLlib provides GBT regression through the `GBTRegressor` class in the `pyspark.ml` package, which is supported on serverless, standard, and dedicated compute on Databricks. ^[use-apache-spark-mllib-on-databricks-databricks-on-aws.md]

### MLlib Pipelines for GBT Regression

MLlib’s [Pipelines API](/concepts/mllib-pipelines-api.md) provides a uniform interface for building and tuning GBT regression workflows. A typical pipeline involves:
- **Feature transformers** (e.g., `VectorAssembler`, `StringIndexer`) to prepare the raw data.
- **A `GBTRegressor`** as the estimator.
- **An evaluator** (e.g., `RegressionEvaluator`) to assess performance using metrics like RMSE, MSE, or R².

The pipeline can then be fit to a training dataset and used to generate predictions on new data. Grid search and cross-validation can be applied via ParamGridBuilder and [CrossValidator](/concepts/crossvalidator.md) to optimise hyperparameters such as the number of trees, max depth, and learning rate. ^[use-apache-spark-mllib-on-databricks-databricks-on-aws.md]

### Bike Sharing Regression Notebook

A practical example of GBT regression using MLlib pipelines is provided in the *Bike sharing regression notebook*, which predicts hourly bike rental counts. The notebook uses historical data containing features such as day of the week, weather conditions, season, temperature, and humidity. The pipeline applies StringIndexer to categorical columns, VectorAssembler to combine all features into a single vector, and `GBTRegressor` to model the rental count. The resulting model can be used for demand forecasting and resource planning. ^[use-apache-spark-mllib-on-databricks-databricks-on-aws.md]

### Comparison with Other MLlib Models

GBT regression often delivers higher predictive accuracy than single Decision Tree Regression by reducing overfitting through boosting. Compared to Random Forest Regression (another ensemble method), GBT typically produces lower bias but may be more sensitive to noisy data and requires more careful [Hyperparameter Tuning](/concepts/hyperparameter-tuning.md). MLlib also offers Linear Regression and Generalized Linear Regression for problems where a linear relationship is appropriate. ^[use-apache-spark-mllib-on-databricks-databricks-on-aws.md]

### Related Concepts

- [Apache Spark MLlib](/concepts/apache-spark-mllib.md)
- [Gradient Boosted Trees](/concepts/gradient-boosted-trees-regression-with-mllib.md)
- Decision Tree Regression
- Random Forest Regression
- [MLlib Pipelines](/concepts/mllib-pipelines-api.md)
- Bike Sharing Dataset
- [CrossValidator](/concepts/crossvalidator.md)
- Feature Engineering with Spark MLlib

## Sources

- use-apache-spark-mllib-on-databricks-databricks-on-aws.md

# Citations

1. [use-apache-spark-mllib-on-databricks-databricks-on-aws.md](/references/use-apache-spark-mllib-on-databricks-databricks-on-aws-545482f3.md)
