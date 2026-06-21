---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4439071dbc3c03c6c977df9646a2cd5797a9c67f1420cd9b3257d0fc60879380
  pageDirectory: concepts
  sources:
    - forecasting-time-series-with-gluonts-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - gluonts-evaluation-metrics
    - GEM
    - Evaluation Metrics
    - Evaluation metrics
    - Time Series Evaluation Metrics
  citations:
    - file: forecasting-time-series-with-gluonts-databricks-on-aws.md
title: GluonTS Evaluation Metrics
description: Built-in evaluation toolkit in GluonTS that computes standard forecasting metrics including MASE, RMSE, and quantile losses across individual time series and aggregated results.
tags:
  - time-series
  - evaluation
  - metrics
  - forecasting
timestamp: "2026-06-19T10:36:52.349Z"
---

# GluonTS Evaluation Metrics

**GluonTS Evaluation Metrics** are the quantitative measures provided by the GluonTS library for assessing the accuracy of probabilistic time series forecasts. These metrics are calculated using the `Evaluator` class, which compares forecasted distributions against ground truth values across multiple time series.

## Overview

The GluonTS `Evaluator` computes a comprehensive set of metrics that evaluate both point forecast accuracy and probabilistic forecast quality. It supports configurable quantile levels and returns results both aggregated across all time series and per individual series. ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

## Using the Evaluator

The evaluator is instantiated with a list of quantile levels and then called with the ground truth labels and forecasted values:

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

### Return Values

The `Evaluator` returns two objects: ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

- **`agg_metrics`**: A dictionary of aggregated metrics computed across all time series in the evaluation set. These provide an overall assessment of model performance.
- **`item_metrics`**: A per-series breakdown of metrics, allowing inspection of performance on individual time series. This is typically a Pandas DataFrame.

## Common Metrics

The GluonTS evaluator calculates a range of standard time series forecasting metrics, including: ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

| Metric | Description |
|--------|-------------|
| **MASE** (Mean Absolute Scaled Error) | A scale-independent error metric that compares forecast errors to the in-sample naive forecast errors |
| **RMSE** (Root Mean Squared Error) | The square root of the mean squared differences between predicted and actual values |
| **Quantile Loss** | Measures the accuracy of probabilistic forecasts at specified quantile levels (e.g., 0.1, 0.5, 0.9) |

## Quantile Configuration

The `quantiles` parameter controls which probability levels are evaluated. Common choices include: ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

- `[0.1, 0.5, 0.9]` — Evaluates the 10th, 50th (median), and 90th percentiles
- The 0.5 quantile corresponds to the median forecast, often used as the point prediction
- Additional quantiles can be added for more granular assessment of prediction intervals

## Integration with Training Workflow

In a typical [GluonTS](/concepts/gluonts.md) workflow, evaluation follows model training and prediction generation. For example, after training a [DeepAR Model](/concepts/deepar-model.md) on a [PandasDataset](/concepts/pandasdataset.md), predictions are generated for test windows and then evaluated: ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

```python
# Generate predictions with confidence intervals
forecasts = deepar_predictor.predict(test_pairs.input, num_samples=20)

# Ground truth for comparison
labels = [to_pandas(l) for l in test_pairs.label]

# Calculate and display metrics
agg_metrics, item_metrics = evaluator(labels, forecasts, num_series=len(test_pairs))
item_metrics.display()
print(json.dumps(agg_metrics, indent=2))
```

## Related Concepts

- [GluonTS](/concepts/gluonts.md) — The Python library for probabilistic time series modeling
- [Probabilistic Forecasting](/concepts/probabilistic-time-series-forecasting.md) — Forecasting approach that produces probability distributions rather than point estimates
- [DeepAR](/concepts/deepar.md) — A recurrent neural network model for probabilistic forecasting supported by GluonTS
- Time Series Evaluation — Broader topic of assessing forecast accuracy
- [Backtesting](/concepts/rolling-window-backtesting.md) — The rolling window evaluation approach used with the `DateSplitter`

## Sources

- forecasting-time-series-with-gluonts-databricks-on-aws.md

# Citations

1. [forecasting-time-series-with-gluonts-databricks-on-aws.md](/references/forecasting-time-series-with-gluonts-databricks-on-aws-26a285b9.md)
