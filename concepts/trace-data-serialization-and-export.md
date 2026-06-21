---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 03a2eba2f8518b0949bdc399c9e80e0ef754225e419148e7dba81ab010cb01d5
  pageDirectory: concepts
  sources:
    - access-trace-data-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - trace-data-serialization-and-export
    - Export and Trace Data Serialization
    - TDSAE
  citations:
    - file: access-trace-data-databricks-on-aws.md
title: Trace Data Serialization and Export
description: Methods for converting Trace objects to dictionaries, JSON strings, or Pandas DataFrame rows, and reconstructing them from serialized formats.
tags:
  - mlflow
  - tracing
  - serialization
  - data-export
timestamp: "2026-06-18T14:18:08.877Z"
---

# Trace Data Serialization and Export

**Trace Data Serialization and Export** refers to the methods provided by [MLflow](/concepts/mlflow.md) for converting a [Trace](/concepts/traces.md) object into portable formats such as Python dictionaries, JSON strings, and pandas DataFrame rows. These capabilities enable users to store, transmit, and analyze trace data outside of the MLflow environment, supporting integration with downstream tools, custom dashboards, and batch analysis pipelines.

The MLflow `Trace` object — made up of [`TraceInfo`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.TraceInfo) (metadata) and [`TraceData`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.TraceData) (execution data) — offers several built-in methods for serialization and export. ^[access-trace-data-databricks-on-aws.md]

## Dictionary Conversion

The [`Trace.to_dict`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.Trace.to_dict) method converts the entire trace (including its info and data) into a Python dictionary. Individual components such as `TraceInfo` and `TraceData` also expose `to_dict()` methods. A dictionary can be used to reconstruct a `Trace` object via `Trace.from_dict()`. ^[access-trace-data-databricks-on-aws.md]

```python
# Convert entire trace to dictionary
trace_dict = trace.to_dict()
print(f"Trace dict keys: {trace_dict.keys()}")
print(f"Info keys: {trace_dict['info'].keys()}")
print(f"Data keys: {trace_dict['data'].keys()}")

# Convert individual components
info_dict = trace.info.to_dict()
data_dict = trace.data.to_dict()

# Reconstruct trace from dictionary
from mlflow.entities import Trace
reconstructed_trace = Trace.from_dict(trace_dict)
print(f"Reconstructed trace ID: {reconstructed_trace.info.trace_id}")
```

## JSON Serialization

The [`Trace.to_json`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.Trace.to_json) method serializes the trace into a JSON string, optionally with pretty printing. The complementary [`Trace.from_json`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.Trace.from_json) static method reconstructs a `Trace` from a JSON string. This format is ideal for saving traces to files, sending over HTTP, or storing in document databases. ^[access-trace-data-databricks-on-aws.md]

```python
# Convert to JSON string
trace_json = trace.to_json()
print(f"JSON length: {len(trace_json)} characters")

# Pretty print JSON
trace_json_pretty = trace.to_json(pretty=True)
print("Pretty JSON (first 500 chars):")
print(trace_json_pretty[:500])

# Load trace from JSON
from mlflow.entities import Trace
loaded_trace = Trace.from_json(trace_json)
print(f"Loaded trace ID: {loaded_trace.info.trace_id}")
```

## Pandas DataFrame Conversion

The [`Trace.to_pandas_dataframe_row`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.Trace.to_pandas_dataframe_row) method converts a single trace into a dictionary that can be used as a row in a pandas DataFrame. This is useful for aggregating multiple traces (e.g., from `mlflow.search_traces()`) into a tabular structure for statistical analysis, visualization, or export to CSV. ^[access-trace-data-databricks-on-aws.md]

```python
# Convert trace to DataFrame row
row_data = trace.to_pandas_dataframe_row()
print(f"DataFrame row keys: {list(row_data.keys())}")

# Create DataFrame from multiple traces
import pandas as pd

# Get multiple traces
traces = mlflow.search_traces(max_results=5)

# If you have individual trace objects
trace_rows = [t.to_pandas_dataframe_row() for t in [trace]]
df = pd.DataFrame(trace_rows)
print(f"DataFrame shape: {df.shape}")
print(f"Columns: {df.columns.tolist()}")

# Access specific data from DataFrame
print(f"Trace IDs: {df['trace_id'].tolist()}")
print(f"States: {df['state'].tolist()}")
print(f"Durations: {df['execution_duration'].tolist()}")
```

## Span Serialization

Individual spans within a trace can be serialized and deserialized independently using the [`Span.to_dict`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.Span.to_dict) and [`Span.from_dict`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.Span.from_dict) methods. This enables selective export of specific execution segments. ^[access-trace-data-databricks-on-aws.md]

```python
# Convert span to dictionary
span_dict = span.to_dict()
print(f"Span dict keys: {span_dict.keys()}")

# Recreate span from dictionary
from mlflow.entities import Span
reconstructed_span = Span.from_dict(span_dict)
print(f"Reconstructed span: {reconstructed_span.name}")
```

## Use Cases

- **Archiving**: Store traces as JSON files for long-term retention and auditability.
- **Interoperability**: Pass trace data between systems via standard formats.
- **Custom Analysis**: Load traces into pandas or other analytics frameworks for custom metrics and dashboards.
- **Data Sharing**: Serialize traces for transfer across environments without requiring MLflow access.

## Related Concepts

- [Trace Object](/concepts/mlflow-trace-object.md) — The primary data structure for execution traces
- [TraceInfo](/concepts/traceinfo.md) — Metadata component of a trace
- [TraceData](/concepts/tracedata.md) — Execution data component of a trace
- Span Serialization — Converting individual spans
- Access Trace Data — Comprehensive guide to reading trace fields
- mlflow.search_traces()|Search Traces — Retrieving multiple traces for batch export
- mlflow.search_traces()|Collecting Traces — Creating traces that can later be serialized

## Sources

- access-trace-data-databricks-on-aws.md

# Citations

1. [access-trace-data-databricks-on-aws.md](/references/access-trace-data-databricks-on-aws-0c458734.md)
