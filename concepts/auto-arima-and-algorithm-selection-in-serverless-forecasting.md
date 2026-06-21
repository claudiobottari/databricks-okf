---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bfcdadd11c0c057a5d8e24a750c2130a8d528eca002f93580dca03c5e686a524
  pageDirectory: concepts
  sources:
    - forecasting-serverless-with-automl-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - auto-arima-and-algorithm-selection-in-serverless-forecasting
    - Algorithm Selection in Serverless Forecasting and Auto-ARIMA
    - AAASISF
  citations:
    - file: forecasting-serverless-with-automl-databricks-on-aws.md
title: Auto-ARIMA and Algorithm Selection in Serverless Forecasting
description: The use of the Auto-ARIMA algorithm (via pmdarima) and the ability to choose training frameworks for AutoML to explore during model tuning.
tags:
  - algorithms
  - forecasting
  - arima
  - automl
timestamp: "2026-06-19T10:36:32.448Z"
---

Here is the wiki page for "Auto-ARIMA and Algorithm Selection in Serverless Forecasting", based solely on the provided source material.

---

## Auto-ARIMA and Algorithm Selection in Serverless Forecasting

**Auto-ARIMA and Algorithm Selection in Serverless Forecasting** refers to the automatic algorithm exploration and hyperparameter tuning process within Databricks Model Training's serverless forecasting capability. The service automatically selects the best algorithm and hyperparameters for a given forecasting problem, with Auto-ARIMA being one of the key algorithms available.^[forecasting-serverless-with-automl-databricks-on-aws.md]

### Auto-ARIMA Requirements

When using the Auto-ARIMA algorithm, the time series data must meet a strict requirement: the series must have a regular frequency where the interval between any two points is the same throughout the entire time series.^[forecasting-serverless-with-automl-databricks-on-aws.md]

To handle gaps in the data, the AutoML system automatically fills in missing time steps by imputing values with the previous value (forward fill). ^[forecasting-serverless-with-automl-databricks-on-aws.md]

### Training Framework Selection

During the experiment setup phase in the Databricks Model Training UI|Databricks Model Training UI, users can specify which training frameworks AutoML should explore. This is configured under the **Advanced options** section as the **Training framework** setting. The serverless system then uses this selection to guide which algorithms it tests during the tuning stage.^[forecasting-serverless-with-automl-databricks-on-aws.md]

### Algorithm Selection Process

The serverless forecasting experiment follows a staged process for algorithm selection:^[forecasting-serverless-with-automl-databricks-on-aws.md]

1.  **Preprocessing** — The system validates and prepares the input data. This includes imputing missing values, splitting data into training, validation, and test sets, and performing automatic feature generation such as one-hot encoding for categorical features.^[forecasting-serverless-with-automl-databricks-on-aws.md]
2.  **Tuning** — AutoML explores the different forecasting algorithms specified by the user (or all available) and tunes hyperparameters for each candidate.^[forecasting-serverless-with-automl-databricks-on-aws.md]
3.  **Training** — Using the best configuration identified during tuning, the system trains and evaluates the final selected model.^[forecasting-serverless-with-automl-databricks-on-aws.md]

### Primary Metric for Model Selection

Users can specify a **Primary metric** under **Advanced options** that serves as the criterion for evaluating and selecting the best model across all tested algorithms. This metric directly influences which algorithm and hyperparameter combination is ultimately chosen.^[forecasting-serverless-with-automl-databricks-on-aws.md]

### Related Concepts

- [Serverless Forecasting](/concepts/databricks-serverless-forecasting.md)
- AutoML
- [Time Series Forecasting](/concepts/multi-series-forecasting.md)
- [Hyperparameter Tuning](/concepts/hyperparameter-tuning.md)
- [Databricks Model Training](/concepts/databricks-model-training.md)

### Sources

- forecasting-serverless-with-automl-databricks-on-aws.md

# Citations

1. [forecasting-serverless-with-automl-databricks-on-aws.md](/references/forecasting-serverless-with-automl-databricks-on-aws-8952bc49.md)
