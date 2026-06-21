---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 46cc1c49bbe32902dd63f95c7a1364278d993252257d094a9005351eee65e8c3
  pageDirectory: concepts
  sources:
    - forecasting-time-series-with-gluonts-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - pandasdataset
  citations:
    - file: forecasting-time-series-with-gluonts-databricks-on-aws.md
title: PandasDataset
description: A GluonTS utility that converts a Pandas DataFrame into the internal dataset format required for model training and prediction.
tags:
  - data-processing
  - time-series
  - gluonts
timestamp: "2026-06-19T18:53:22.202Z"
---

# PandasDataset

**PandasDataset** is a class in the GluonTS library that converts a Pandas DataFrame into a format suitable for time series forecasting with GluonTS models. It serves as the primary interface for loading and preparing tabular time series data for use with GluonTS estimators and predictors. ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

## Overview

PandasDataset wraps a dictionary of Pandas Series or a DataFrame where each column represents an individual time series and the index contains timestamps. The class handles the conversion of DataFrame columns into the dictionary-like format expected by GluonTS's internal dataset representation, enabling seamless integration with the library's training, evaluation, and prediction pipelines. ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

## Usage

To create a PandasDataset, pass a dictionary of columns from a Pandas DataFrame that has been filtered to the desired date range. The dictionary keys become item IDs for each time series. ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

```python
from gluonts.dataset.pandas import PandasDataset
import pandas as pd
import numpy as np

# Example: assuming df_raw is a DataFrame with datetime index and columns as time series
ts_dataset = PandasDataset(
    dict(df_raw[(df_raw.index > start_date) & (df_raw.index <= end_date)].astype(np.float32))
)
```

The resulting dataset can be iterated over to access individual time series entries, each containing fields like the item ID and the target values. ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

## Features

- **Direct DataFrame conversion**: Converts columns of a DataFrame directly into individual time series with their column names as identifiers.
- **Type handling**: Accepts data as `np.float32` for compatibility with PyTorch-based GluonTS models.
- **Integration with GluonTS ecosystem**: Works with DateSplitter for train/test splitting, [DeepAREstimator](/concepts/deepar.md) for model training, and Evaluator for performance metrics. ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

## Practical Example

In the GluonTS forecasting workflow, after loading and resampling electricity consumption data, PandasDataset is used to create the dataset that feeds into training:

1. Filter the DataFrame to the training period.
2. Convert to float32 for numerical precision.
3. Pass the dictionary of columns to PandasDataset.

The dataset can then be split using `DateSplitter.split(ts_dataset)` and used to train models like [DeepAR](/concepts/deepar.md). ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

## Related Concepts

- [GluonTS](/concepts/gluonts.md) — The library providing PandasDataset and other time series forecasting tools.
- DateSplitter — Utility for creating train/test splits from a PandasDataset.
- [DeepAREstimator](/concepts/deepar.md) — A probabilistic forecasting model that accepts PandasDataset as training data.
- [Time Series Forecasting](/concepts/multi-series-forecasting.md) — The broader task that PandasDataset supports.
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) — The Databricks compute environment used in the GluonTS tutorial.

## Sources

- forecasting-time-series-with-gluonts-databricks-on-aws.md

# Citations

1. [forecasting-time-series-with-gluonts-databricks-on-aws.md](/references/forecasting-time-series-with-gluonts-databricks-on-aws-26a285b9.md)
