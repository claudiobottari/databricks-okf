---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 25a60d67414cc7971384c76335f5e16df975bdcfddd2d26ee4c78b1649e56cd4
  pageDirectory: concepts
  sources:
    - forecasting-time-series-with-gluonts-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - rolling-window-backtesting-for-time-series
    - RWBFTS
    - Cross-Validation for Time Series
  citations:
    - file: forecasting-time-series-with-gluonts-databricks-on-aws.md
title: Rolling Window Backtesting for Time Series
description: A model evaluation technique that creates multiple train/test splits using rolling windows over a time series, allowing assessment of forecast performance across different time periods.
tags:
  - time-series
  - model-evaluation
  - backtesting
  - validation
timestamp: "2026-06-18T12:23:53.985Z"
---

# Rolling Window Backtesting for Time Series

**Rolling Window Backtesting** is a technique for evaluating time series forecasting models by repeatedly refitting the model on expanding or sliding training windows and evaluating on subsequent test periods. This approach simulates how a model would perform in a production environment where new data arrives sequentially.

## Overview

Time series backtesting differs from standard cross-validation because temporal order must be preserved—future data cannot be used to predict the past. Rolling window backtesting addresses this by creating multiple train/test splits that respect the temporal structure of the data. Each split uses an earlier window for training and a later window for testing, with the windows moving forward in time. ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

## Key Parameters

Rolling window backtesting is controlled by three parameters: ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

| Parameter | Description |
|-----------|-------------|
| `prediction_length` | The number of time steps to forecast in each test window |
| `NUM_WINDOWS` | The number of rolling windows (test periods) to evaluate |
| `DISTANCE` | The gap between successive windows. Controls overlap: less than `prediction_length` creates overlapping windows; equal to `prediction_length` creates adjacent, non-overlapping windows; greater than `prediction_length` leaves gaps between windows |

## Implementation with GluonTS

In [GluonTS](/concepts/gluonts.md), rolling window backtesting is implemented using the `DateSplitter` class. The following example creates 4 test windows for backtesting: ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

```python
from gluonts.dataset.split import DateSplitter

# Set backtest parameters
NUM_WINDOWS = 4                               # number of rolling windows
prediction_length = 168                        # 7 days × 24 hours
DISTANCE = prediction_length                   # adjacent, non-overlapping windows

# Calculate training end date
end_training_date = pd.Period(end_dataset_date, freq=freq) - NUM_WINDOWS * prediction_length

# Create train/test split
train_ds, test_template = DateSplitter(date=end_training_date).split(ts_dataset)
test_pairs = test_template.generate_instances(
    prediction_length=prediction_length,
    windows=NUM_WINDOWS,
    distance=DISTANCE,
)
```

After splitting, `test_pairs` contains multiple input/label pairs. The model is trained once on `train_ds`, then used to generate forecasts for each test window. ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

## Evaluation

After generating forecasts for each test window, the [GluonTS Evaluator](/concepts/gluonts-evaluator.md) computes metrics across all windows, including: ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

- **MASE** (Mean Absolute Scaled Error)
- **RMSE** (Root Mean Square Error)
- **Quantile losses** at specified probability levels (e.g., 0.1, 0.5, 0.9)

```python
from gluonts.evaluation import Evaluator

evaluator = Evaluator(quantiles=[0.1, 0.5, 0.9])
agg_metrics, item_metrics = evaluator(
    labels,
    predictor.predict(test_pairs.input, num_samples=20),
    num_series=len(test_pairs),
)
```

## Data Preparation

Before backtesting, time series data must be: ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

1. **Loaded and parsed** with correct datetime indexing and frequency
2. **Resampled** to a consistent interval (e.g., from 15-minute to 1-hour intervals)
3. **Converted to GluonTS format** using `PandasDataset` with a date range that covers both training and test periods

## Best Practices

- **Use sufficient windows.** Multiple windows provide a more robust estimate of model performance across different time periods. ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]
- **Match prediction length to business needs.** The forecast horizon should align with the actual decision-making timeframe. ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]
- **Avoid lookahead bias.** Ensure the training data for each window ends before the test data begins. ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]
- **Consider window overlap.** Overlapping windows (distance < prediction_length) provide more evaluation points but may introduce dependence between test periods. ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

## Related Concepts

- [GluonTS](/concepts/gluonts.md) — The Python library providing time series forecasting tools and backtesting utilities
- [DeepAR Model](/concepts/deepar-model.md) — A recurrent neural network model for probabilistic forecasting commonly evaluated with rolling window backtesting
- [Probabilistic Forecasting](/concepts/probabilistic-time-series-forecasting.md) — Forecasting approach that produces prediction intervals rather than point estimates
- [Time Series Cross-Validation](/concepts/time-series-cross-validation.md) — The broader class of techniques for evaluating temporal models
- Model Checkpointing — Saving model states to resume training or compare across backtesting iterations

## Sources

- forecasting-time-series-with-gluonts-databricks-on-aws.md

# Citations

1. [forecasting-time-series-with-gluonts-databricks-on-aws.md](/references/forecasting-time-series-with-gluonts-databricks-on-aws-26a285b9.md)
