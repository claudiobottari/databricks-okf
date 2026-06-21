---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: df694d10b3d91642b9a881dbe3fab5d2d5f795bcfd071058552f92b2b46e92fc
  pageDirectory: concepts
  sources:
    - forecasting-time-series-with-gluonts-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - gluonts-evaluator
    - gluonts-evaluation-metrics
    - GEM
    - Evaluation Metrics
    - Evaluation metrics
    - Time Series Evaluation Metrics
  citations:
    - file: forecasting-time-series-with-gluonts-databricks-on-aws.md
title: GluonTS Evaluator
description: A component of the GluonTS library that computes standard forecasting metrics including MASE, RMSE, and quantile losses across multiple time series.
tags:
  - time-series
  - evaluation
  - metrics
timestamp: "2026-06-19T18:53:06.209Z"
---

# GluonTS Evaluator

The **GluonTS Evaluator** is a component of the GluonTS library that calculates performance metrics for probabilistic time series forecasts. It provides a standardized way to assess forecast accuracy by comparing predicted values against ground truth data. ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

## Overview

The evaluator computes aggregate and per-item metrics for forecasted time series. It supports multiple evaluation metrics, including Mean Absolute Scaled Error (MASE), Root Mean Square Error (RMSE), and quantile losses at specified probability levels. ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

## Usage

To use the GluonTS Evaluator, instantiate it with the desired quantile levels, then call it with the ground truth labels and forecast predictions:

```python
from gluonts.evaluation import Evaluator

evaluator = Evaluator(quantiles=[0.1, 0.5, 0.9])
agg_metrics, item_metrics = evaluator(
    labels,
    deepar_predictor.predict(test_pairs.input, num_samples=20),
    num_series=len(test_pairs),
)
```

^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

### Parameters

- **quantiles**: A list of probability levels (e.g., `[0.1, 0.5, 0.9]`) for which quantile loss metrics are calculated. ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

### Return Values

- **agg_metrics**: A dictionary containing aggregated evaluation metrics across all time series, such as overall MASE and RMSE. ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]
- **item_metrics**: A DataFrame or similar structure containing per-time-series metrics, allowing for detailed inspection of individual forecast performance. ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

## Metrics

The evaluator calculates several metrics for probabilistic forecasting:

- **MASE (Mean Absolute Scaled Error)**: A scale-independent error metric that compares forecast errors to the in-sample naive forecast errors.
- **RMSE (Root Mean Square Error)**: A standard error metric that penalizes large errors more heavily.
- **Quantile Loss**: Measures forecast accuracy at specific probability levels, useful for evaluating prediction intervals.

These metrics are computed both at the aggregate level (averaged across all time series in the dataset) and at the individual item level. ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

## Related Concepts

- [GluonTS](/concepts/gluonts.md) — The parent library for probabilistic time series modeling and forecasting
- [DeepAR Estimator](/concepts/deepar.md) — A common model used with the evaluator for forecasting
- [Probabilistic Time-Series Forecasting](/concepts/probabilistic-time-series-forecasting.md) — The broader field of uncertainty-aware predictions
- [Time Series Evaluation Metrics](/concepts/gluonts-evaluator.md) — General concepts for assessing forecast quality
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) — The compute infrastructure where GluonTS runs on Databricks

## Sources

- forecasting-time-series-with-gluonts-databricks-on-aws.md

# Citations

1. [forecasting-time-series-with-gluonts-databricks-on-aws.md](/references/forecasting-time-series-with-gluonts-databricks-on-aws-26a285b9.md)
