---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 58532eecea321134dd3508b7625782c8ec419c613ae40c694e02c0f26bdc7085
  pageDirectory: concepts
  sources:
    - forecasting-with-automl-classic-compute-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - forecast-horizon-and-frequency-configuration
    - Frequency Configuration and Forecast Horizon
    - FHAFC
  citations:
    - file: forecasting-with-automl-classic-compute-databricks-on-aws.md
title: Forecast Horizon and Frequency Configuration
description: Configuration parameters in AutoML forecasting that specify the number of future time periods to predict and the time units (e.g., days, weeks, months).
tags:
  - forecasting
  - configuration
  - databricks
timestamp: "2026-06-19T18:53:31.163Z"
---

# Forecast Horizon and Frequency Configuration

The **forecast horizon** is the number of future time periods for which an AutoML forecasting experiment should predict values. The **frequency** defines the time unit (e.g., days, weeks, months) of each period in the horizon. Together, these two parameters determine the length and granularity of the forecast output. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

## Configuring the Horizon and Frequency

When setting up a forecasting experiment using the AutoML UI (classic compute), you specify the horizon and frequency in the **Forecast horizon and frequency** fields: ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

- **Left box**: Enter an integer representing the number of periods to forecast (e.g., `7` for a 7‑day forecast).
- **Right box**: Select the time unit that matches the regular interval of your time series (e.g., `day`, `week`, `month`, `quarter`, `year`).

These parameters are also available in the [Forecasting API](https://docs.databricks.com/aws/en/machine-learning/automl/forecasting-train-api) (for example, the `horizon` and `frequency` arguments in `databricks.automl.forecast()`).

## Requirements for Auto-ARIMA

If you intend to use Auto-ARIMA, the time series must satisfy both of the following frequency‑related conditions: ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

1. **Regular frequency** – The interval between any two consecutive observations must be the same throughout the entire series.
2. **Matching frequency unit** – The frequency unit specified in the UI or API must exactly match the actual interval of the data.

AutoML handles missing time steps by forward‑filling them with the previous observed value. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

## Notes

- The forecast horizon and frequency apply to [Multi-Series Forecasting](/concepts/multi-series-forecasting.md) as well as single‑series experiments. When you define [time series identifiers](/concepts/time-series-identifier-columns.md), the same horizon and frequency are applied to every series independently.
- The frequency must match the time granularity of the column selected as the **Time column** in the experiment setup.
- This configuration is specific to the **classic compute** AutoML experience; serverless forecasting uses a different interface. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

## Related Concepts

- AutoML Experiment – The overall setup for machine learning experiments including forecasting.
- [Time Series Forecasting](/concepts/multi-series-forecasting.md) – General concept of predicting future values from historical data.
- [Multi-Series Forecasting](/concepts/multi-series-forecasting.md) – Forecasting multiple related time series within one experiment.
- Auto-ARIMA – A specific algorithm that enforces regular frequency requirements.
- Forecasting with AutoML – Overview of the forecasting capabilities in Databricks AutoML.

## Sources

- forecasting-with-automl-classic-compute-databricks-on-aws.md

# Citations

1. [forecasting-with-automl-classic-compute-databricks-on-aws.md](/references/forecasting-with-automl-classic-compute-databricks-on-aws-20de86d0.md)
