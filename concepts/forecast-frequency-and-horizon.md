---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 32745181b814826ea76bafd6006e8559b63c0658d33917578400b1ee407e8d19
  pageDirectory: concepts
  sources:
    - forecasting-serverless-with-automl-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - forecast-frequency-and-horizon
    - Horizon and Forecast Frequency
    - FFAH
    - Forecast Horizon
  citations:
    - file: forecasting-serverless-with-automl-databricks-on-aws.md
title: Forecast Frequency and Horizon
description: Two key parameters that define the granularity (frequency) and duration (horizon) of a time series forecast in Databricks AutoML.
tags:
  - forecasting
  - time-series
  - parameters
timestamp: "2026-06-19T10:36:30.593Z"
---

# Forecast Frequency and Horizon

**Forecast Frequency** and **Forecast Horizon** are two core parameters that define the temporal scope and granularity of a time series forecasting experiment. In serverless forecasting on Databricks, these parameters are configured together to specify both the time unit of the input data and how many of those units to predict into the future. ^[forecasting-serverless-with-automl-databricks-on-aws.md]

## Definition

**Forecast Frequency** selects the time unit that represents the input data's frequency. Options include minutes, hours, days, months, and other time units. This parameter determines the granularity of the time series – for example, if data has one observation per day, the frequency should be set to “days”. ^[forecasting-serverless-with-automl-databricks-on-aws.md]

**Forecast Horizon** specifies how many units of the selected frequency to forecast into the future. Together with the forecast frequency, this defines both the time units and the number of time units to forecast. For instance, a horizon of 10 with a frequency of “days” means predicting 10 days ahead. ^[forecasting-serverless-with-automl-databricks-on-aws.md]

## Relationship Between Frequency and Horizon

Frequency and horizon work together to define the complete forecasting window:

- **Frequency** establishes the base time unit (e.g., hourly, daily, monthly).
- **Horizon** specifies the number of those units to predict.

This means that for the same absolute time period (e.g., one month), a higher frequency (daily) would require a larger horizon value (30 days) than a lower frequency (weekly, with a horizon of 4 weeks). ^[forecasting-serverless-with-automl-databricks-on-aws.md]

## Configuration in the UI

When creating a forecasting experiment through the Databricks Model Training UI, users set these parameters under the **Training data** section:

1. **Time column** – Select the column containing the time periods for the time series (must be of type `timestamp` or `date`).
2. **Forecast frequency** – Choose the time unit representing the input data's frequency.
3. **Forecast horizon** – Specify the number of frequency units to forecast forward.

These settings appear in the “Time series” configuration section of the UI. ^[forecasting-serverless-with-automl-databricks-on-aws.md]

## Impact on Auto-ARIMA

When using the Auto-ARIMA algorithm, the time series must have a **regular frequency** – the interval between any two consecutive points must be constant throughout the series. AutoML handles missing time steps by filling in those values with the previous value. Therefore, ensuring the chosen frequency matches the actual data pattern is critical for Auto-ARIMA to work correctly. ^[forecasting-serverless-with-automl-databricks-on-aws.md]

## Best Practices

- Choose a frequency that aligns with the natural rhythm of the data (e.g., hourly for real-time operations, daily for sales forecasting, monthly for financial planning).
- Set the horizon to a meaningful prediction window that supports decision-making timelines.
- Ensure the time series has consistent intervals between observations to support regular frequency patterns, especially when using algorithms like Auto-ARIMA.

## Related Concepts

- Time series forecasting
- Auto-ARIMA
- [Serverless forecasting](/concepts/databricks-serverless-forecasting.md)
- [Time Series Identifier Columns](/concepts/time-series-identifier-columns.md)
- Forecast experiment configuration

## Sources

- forecasting-serverless-with-automl-databricks-on-aws.md

# Citations

1. [forecasting-serverless-with-automl-databricks-on-aws.md](/references/forecasting-serverless-with-automl-databricks-on-aws-8952bc49.md)
