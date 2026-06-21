---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f5d5927b490117eb75d0b8880cd022940cc54f80d022433ae93253bb236a6d4a
  pageDirectory: concepts
  sources:
    - forecasting-serverless-with-automl-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - holiday-region-covariates
    - HRC
  citations:
    - file: forecasting-serverless-with-automl-databricks-on-aws.md
title: Holiday Region Covariates
description: A configurable option in Databricks forecasting that adds holiday region data as covariates (external features) during model training to improve forecast accuracy.
tags:
  - forecasting
  - covariates
  - features
  - holidays
timestamp: "2026-06-18T12:23:35.661Z"
---

---
title: Holiday Region Covariates
summary: An advanced option in Databricks serverless forecasting that enables holiday calendar effects from a selected region to be used as covariates during model training, improving forecast accuracy.
sources:
  - forecasting-serverless-with-automl-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T12:00:00.000Z"
updatedAt: "2026-06-18T12:00:00.000Z"
tags:
  - forecasting
  - automl
  - time-series
  - covariates
aliases:
  - holiday-region-covariates
  - HRC
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 1
---

# Holiday Region Covariates

**Holiday Region Covariates** is an optional feature in Databricks **Forecasting (serverless) with AutoML** that allows users to include holiday calendar effects for a specific geographic region as exogenous variables (covariates) in time‑series model training. By accounting for known holiday patterns, the model can better capture seasonal demand fluctuations, retail spikes, or other holiday‑driven behavior that a simple trend‑seasonality decomposition might miss.

## Usage in the Forecasting UI

Holiday Region Covariates are configured under **Advanced options** when creating a forecasting experiment via the Databricks Model Training UI. The user selects a **Holiday region** from a dropdown list of supported regions. ^[forecasting-serverless-with-automl-databricks-on-aws.md]

Once selected, the AutoML framework automatically generates holiday‑related features (e.g., binary indicators for public holidays, days before/after holidays, or rolling holiday windows) and includes them as covariates in all candidate models. The exact feature engineering strategy is determined by the AutoML pipeline and is not user‑configurable.

## How It Works

The holiday region acts as a source of calendar‑based signals that are independent of the time series’ own history. These signals are treated as exogenous covariates during training, meaning the model can learn the relationship between holiday events and the forecast target – such as higher sales on Black Friday or lower traffic on public holidays.

Because holidays vary by country, selecting the correct region is critical. For example, using US holidays for a European sales channel would introduce misleading patterns. The option therefore maps to a standard holiday calendar (e.g., from `holidays` Python library or a built‑in Databricks dataset) for the chosen region.

## Impact on Model Training

Including holiday covariates can improve forecast accuracy, especially for domains like retail, tourism, energy, or transportation where holiday effects are strong. It also helps the model generalize to future dates, as the holiday calendar is known in advance.

However, the feature adds complexity to the model and may increase training time. It is most beneficial when historical data shows clear holiday‑related patterns. For stable time series with little calendar influence, the option can be left at the default (no holiday region).

## Related Concepts

- [Time Series Forecasting](/concepts/multi-series-forecasting.md) with AutoML
- Exogenous Variables (Covariates) in forecasting
- Serverless Forecasting with AutoML
- Auto-ARIMA algorithm (which benefits from regular frequency and exogenous regressors)
- [Feature Engineering](/concepts/featureengineeringclient-api.md) in automated ML pipelines

## Sources

- forecasting-serverless-with-automl-databricks-on-aws.md

# Citations

1. [forecasting-serverless-with-automl-databricks-on-aws.md](/references/forecasting-serverless-with-automl-databricks-on-aws-8952bc49.md)
