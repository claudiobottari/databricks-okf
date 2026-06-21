---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1e7c737df97874191421627a37ae4c9e461bf0091cd8e63250dfaff7e62a6389
  pageDirectory: concepts
  sources:
    - forecasting-time-series-with-gluonts-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - gluonts-pandasdataset
  citations:
    - file: forecasting-time-series-with-gluonts-databricks-on-aws.md
title: GluonTS PandasDataset
description: A GluonTS dataset wrapper that converts Pandas DataFrames into the time series format required by GluonTS models, enabling seamless integration with standard data science workflows.
tags:
  - gluonts
  - data-preparation
  - pandas
  - time-series
timestamp: "2026-06-18T12:24:02.192Z"
---

# GluonTS PandasDataset

**GluonTS PandasDataset** is a dataset wrapper in the GluonTS library that converts a Pandas DataFrame or a dictionary of Pandas Series into a GluonTS-compatible dataset for probabilistic time series forecasting. It is imported from `gluonts.dataset.pandas` and serves as the primary entry point for ingesting tabular time series data into the GluonTS workflow.^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

## Usage

The `PandasDataset` constructor accepts a dictionary where each key is an item identifier and each value is a Pandas Series with a `DatetimeIndex`. Alternatively, a single Pandas DataFrame with a `DatetimeIndex` as row labels and each column representing a separate time series can be passed. The resulting dataset can be iterated over, visualised with `gluonts.dataset.util.to_pandas`, and split into training and test sets using utilities like `DateSplitter`.^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

### Example from the Notebook

In the forecasting time series with GluonTS notebook, a raw electricity consumption DataFrame (`data_kw`) is resampled to hourly intervals, a random subset of columns is selected, and the data is converted to GluonTS format:

```python
from gluonts.dataset.pandas import PandasDataset

ts_dataset = PandasDataset(
    dict(ts_sample[(ts_sample.index > start_training_date) &
                   (ts_sample.index <= end_dataset_date)].astype(np.float32))
)
```

After conversion, individual time series can be extracted and plotted using `to_pandas`:

```python
from gluonts.dataset.util import to_pandas
to_pandas(entry).plot(label=entry[FieldName.ITEM_ID])
```

^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

## Key Features

- **Direct integration with Pandas** – No intermediate file format required; any Pandas DataFrame or dictionary of Series with a datetime index can be used.
- **Item identification** – Each time series is assigned an `ITEM_ID` (accessible via `FieldName.ITEM_ID`) that labels the series during evaluation and visualisation.
- **Slicing and filtering** – The dataset supports subsetting by time range and by columns before conversion, as shown in the notebook example.

## Related Concepts

- [GluonTS](/concepts/gluonts.md) – The overarching library for probabilistic time series modeling
- [DeepAREstimator](/concepts/deepar.md) – A recurrent neural network model trained on a PandasDataset
- DateSplitter – GluonTS utility for creating train/test splits from a PandasDataset
- [Time Series Forecasting](/concepts/multi-series-forecasting.md) – The general task addressed by PandasDataset
- [Unity Catalog](/concepts/unity-catalog.md) – Used in the notebook for storing model checkpoints, not directly related to PandasDataset but part of the Databricks workflow

## Sources

- forecasting-time-series-with-gluonts-databricks-on-aws.md

# Citations

1. [forecasting-time-series-with-gluonts-databricks-on-aws.md](/references/forecasting-time-series-with-gluonts-databricks-on-aws-26a285b9.md)
