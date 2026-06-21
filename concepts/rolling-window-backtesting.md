---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 00ed693e74bbacbf51608f0b3272156a639ec6973530c58df0c21cb61ad02430
  pageDirectory: concepts
  sources:
    - forecasting-time-series-with-gluonts-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - rolling-window-backtesting
    - RWB
    - Backtesting
    - Rolling Window
    - RollingWindow (declarative features)
    - rolling-window-backtesting-for-time-series
    - RWBFTS
    - Cross-Validation for Time Series
  citations:
    - file: forecasting-time-series-with-gluonts-databricks-on-aws.md
title: Rolling Window Backtesting
description: A time series evaluation technique using DateSplitter to create multiple train/test windows for robust model validation.
tags:
  - time-series
  - evaluation
  - validation
timestamp: "2026-06-19T18:53:14.858Z"
---

---

title: Rolling Window Backtesting
summary: A technique for evaluating time series forecast accuracy by creating multiple train/test splits across a historical dataset using overlapping or adjacent windows.
sources:
  - forecasting-time-series-with-gluonts-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T10:37:00.026Z"
updatedAt: "2026-06-19T10:37:00.026Z"
tags:
  - time-series
  - evaluation
  - validation
  - backtesting
aliases:
  - rolling-window-backtesting
  - RWB
confidence: 1
provenanceState: extracted
inferredParagraphs: 0

# Rolling Window Backtesting

**Rolling Window Backtesting** is a time series model evaluation technique that splits a dataset into multiple training and test windows that move forward in time. The model is trained once on a fixed training set and then evaluated on each successive test window, simulating periodic forecasting in production.^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

## Key Parameters

Rolling window backtesting is configured by three parameters:

- **Prediction length**: The forecast horizon for each test window (e.g., 168 hours for 7 days).
- **Number of windows**: How many test windows to generate (e.g., 4 windows).
- **Window distance**: The gap between consecutive test windows. This can be:
  - Smaller than prediction length for overlapping windows.
  - Equal to prediction length for adjacent windows.
  - Larger than prediction length for non‑overlapping, non‑adjacent windows.^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

## Implementation with GluonTS

In the [GluonTS](/concepts/gluonts.md) library, rolling window backtesting is implemented using the DateSplitter class and the generate_instances method. The typical workflow is:

1. **Define the training end date**: Calculated as the dataset end date minus the total span of all test windows (`NUM_WINDOWS * prediction_length`).
2. **Create the split**: Pass this date to `DateSplitter` to divide the dataset into training and test templates.
3. **Generate test instances**: Call `generate_instances()` with the prediction length, number of windows, and window distance.^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

```python
from gluonts.dataset.split import DateSplitter

# Define the training-testing split date
end_training_date = pd.Period(end_dataset_date, freq=freq) - NUM_WINDOWS * prediction_length

# Split into train and test datasets
train_ds, test_template = DateSplitter(date=end_training_date).split(ts_dataset)

# Generate test instances for backtesting
test_pairs = test_template.generate_instances(
    prediction_length=prediction_length,
    windows=NUM_WINDOWS,
    distance=DISTANCE,
)
```

## Evaluation

After generating forecasts for each test window, evaluation metrics are calculated by comparing predictions against ground truth labels. The [GluonTS Evaluator](/concepts/gluonts-evaluator.md) can compute metrics such as MASE, RMSE, and quantile losses across all test windows to produce both per‑time‑series and aggregated performance statistics.^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

## Benefits

- **Robustness**: Multiple test windows reduce the variance of performance estimates compared to a single fixed split.
- **Temporal consistency**: The model is evaluated on how it handles different seasonal patterns and trends across time.
- **Production realism**: Mimics the actual deployment scenario where forecasts are generated periodically.^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

## Related Concepts

- [Time Series Forecasting](/concepts/multi-series-forecasting.md)
- [GluonTS](/concepts/gluonts.md)
- [DeepAR](/concepts/deepar.md) – A probabilistic forecasting model commonly evaluated with rolling window backtesting.
- Train/Test Split
- [Cross-Validation for Time Series](/concepts/rolling-window-backtesting.md)
- Prediction Length
- [Probabilistic Forecasting](/concepts/probabilistic-time-series-forecasting.md)

## Sources

- forecasting-time-series-with-gluonts-databricks-on-aws.md

# Citations

1. [forecasting-time-series-with-gluonts-databricks-on-aws.md](/references/forecasting-time-series-with-gluonts-databricks-on-aws-26a285b9.md)
