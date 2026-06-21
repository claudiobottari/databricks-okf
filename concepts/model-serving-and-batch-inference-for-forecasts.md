---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cd532905bb8f41e43c76dd74b197b964c7d949b5b83d579a845a3a321ee95f27
  pageDirectory: concepts
  sources:
    - forecasting-serverless-with-automl-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-serving-and-batch-inference-for-forecasts
    - Batch Inference for Forecasts and Model Serving
    - MSABIFF
  citations:
    - file: forecasting-serverless-with-automl-databricks-on-aws.md
title: Model Serving and Batch Inference for Forecasts
description: Post-training capabilities in Databricks Serverless Forecasting, including viewing predictions, generating batch inference notebooks, and deploying to Model Serving endpoints.
tags:
  - deployment
  - inference
  - databricks
  - mlops
timestamp: "2026-06-19T10:36:44.857Z"
---

# Model Serving and Batch Inference for Forecasts

**Model Serving and Batch Inference for Forecasts** refer to the two primary ways to use a trained forecasting model produced by Databricks AutoML: deploying it as a real-time endpoint for on-demand predictions, or running batch inference with an auto-generated notebook. Both options are available from the experiment results page after training completes.

## View Predictions

Before choosing an inference mode, you can directly inspect the forecast results. The prediction outputs are stored in a Delta table at the path you specified during experiment setup. From the experiment page, selecting **View predictions** opens this results table, allowing you to review the forecasted values alongside the historical data. ^[forecasting-serverless-with-automl-databricks-on-aws.md]

## Batch Inference

For scenarios where you need to generate forecasts for a large set of input data on a schedule or on-demand, select **Batch inference notebook** from the experiment page. This action opens an auto-generated notebook that contains code to perform batch inferencing using the best model from the experiment. The notebook includes the necessary logic to load the model, read input data, produce forecasts, and optionally write the results back to a Delta table. ^[forecasting-serverless-with-automl-databricks-on-aws.md]

## Model Serving

For real-time or interactive forecasting applications, select **Create serving endpoint** to deploy the best model to a [Model Serving](/concepts/model-serving.md) endpoint. This creates a REST API that can serve predictions with low latency, making the model available for integration into applications, dashboards, or downstream systems. The endpoint is managed and scaled by Databricks. ^[forecasting-serverless-with-automl-databricks-on-aws.md]

## Model Registration

Before either inference method can be used, the best model is automatically registered to [Unity Catalog](/concepts/unity-catalog.md) if a registration path was provided during experiment setup. The registered model is the one deployed to the serving endpoint or loaded in the batch inference notebook. ^[forecasting-serverless-with-automl-databricks-on-aws.md]

## Related Concepts

- [AutoML Forecasting](/concepts/automl-forecast.md) – The process of automatically training and tuning forecasting models.
- [Model Serving](/concepts/model-serving.md) – Real-time deployment of ML models as REST endpoints.
- [Unity Catalog](/concepts/unity-catalog.md) – Governance and registry for ML models.
- Batch Inference – Running predictions on a dataset rather than individual requests.
- [Serverless Forecasting](/concepts/databricks-serverless-forecasting.md) – The compute mode used in the experiment (serverless vs. classic).

## Sources

- forecasting-serverless-with-automl-databricks-on-aws.md

# Citations

1. [forecasting-serverless-with-automl-databricks-on-aws.md](/references/forecasting-serverless-with-automl-databricks-on-aws-8952bc49.md)
