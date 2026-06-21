---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 04429ed8c60ccb8f1fe978f6e3833c993939222ccba40ccd0d3ad8fc545430da
  pageDirectory: concepts
  sources:
    - combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-lake-integration-for-ray-via-third-party-libraries
    - DLIFRVTL
  citations:
    - file: combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md
title: Delta Lake Integration for Ray via Third-Party Libraries
description: Use the deltalake (delta-rs) and deltaray (Delta Incubator) libraries to write Ray Core data to Delta Lake tables, though deltalake currently works only with Hive metastore tables (not Unity Catalog) and is not officially supported by Databricks.
tags:
  - ray
  - delta-lake
  - third-party
  - databricks
timestamp: "2026-06-18T11:01:36.582Z"
---

# Delta Lake Integration for Ray via Third-Party Libraries

**Delta Lake Integration for Ray via Third-Party Libraries** refers to the use of external libraries — such as `deltalake` (from the delta-rs project) and `deltaray` (from the Delta Incubator project) — to write data from Ray Core tasks directly to [Delta Lake](/concepts/delta-lake.md) tables or Spark tables. This approach enables data exchange between Ray and Spark without requiring intermediate persistence or a Spark Connect connection. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

Databricks does not officially support these third-party libraries. Users should evaluate them for their own use cases and risk tolerance. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## The `deltalake` Library (delta-rs)

The `deltalake` library, available through the delta-rs project, allows Ray Core tasks to write data directly to Delta tables. A typical pattern uses `ray.remote` tasks that generate a Pandas DataFrame and append it to an existing Delta table using `write_deltalake`. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

```python
from deltalake import DeltaTable, write_deltalake
import pandas as pd
import numpy as np
import ray

@ray.remote
def write_test(table_name):
    random_df_id_vals = [int(np.random.randint(1000)),
                         int(np.random.randint(1000))]
    pdf = pd.DataFrame({"id": random_df_id_vals, "value": ["foo", "bar"]})
    write_deltalake(table_name, pdf, mode="append")

def main():
    table_name = "database.mytable"
    ray.get([write_test.remote(table_name) for _ in range(100)])
```

^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

### Limitation: Hive [Metastore](/concepts/metastore.md) Only

The `deltalake` library currently works only with [Hive metastore](/concepts/built-in-hive-metastore.md) tables. It does **not** support [Unity Catalog](/concepts/unity-catalog.md) tables. If you need to write to a Unity Catalog table, you must use one of the other integration patterns (persist to temporary location and read with Spark, or use Spark Connect). ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## The `deltaray` Library (Delta Incubator)

The `deltaray` library is a third-party library provided by the [Delta Incubator project](https://github.com/delta-incubator/deltaray). It provides a native Ray dataset interface for reading Delta tables, enabling Ray to consume Delta Lake data without going through Spark. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

```python
import pathlib
import deltaray
import deltalake as dl
import pandas as pd

# Creating a Delta Table
cwd = pathlib.Path().resolve()
table_uri = f'{cwd}/tmp/delta-table'
df = pd.DataFrame({'id': [0, 1, 2, 3, 4]})
dl.write_deltalake(table_uri, df)

# Reading our Delta Table
ds = deltaray.read_delta(table_uri)
ds.show()
```

^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

Like `deltalake`, `deltaray` is not officially supported by Databricks. Its capabilities are limited to reading Delta tables into Ray datasets; writing from Ray to Delta may rely on additional delta-rs primitives. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Comparison with Other Integration Patterns

Third-party libraries offer a more direct path for writing Ray data to Delta tables than the other two main patterns:

- **Pattern 1 (Persist output in a temporary location)** requires writing intermediate files (e.g., CSV or Parquet) to DBFS or Unity Catalog Volumes and then reading them with Spark. This adds latency and storage overhead. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]
- **Pattern 2 (Spark Connect)** allows Ray tasks to call Spark directly via `DatabricksSession`, but introduces a threading lock because all tasks share the same Spark driver, leading to sequential execution. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

Third-party libraries avoid these drawbacks but trade off Databricks support and Unity Catalog compatibility. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Best Practices

- Use third-party libraries only for workloads that can tolerate lack of official support and do not require Unity Catalog table writes.
- For Unity Catalog targets, consider using `ray.data.Dataset.write_databricks_table` (available in Databricks Runtime ML 15.0+) or the persist-then-read pattern.
- Always test library versions against your Databricks Runtime version to avoid compatibility issues.

## Related Concepts

- Ray — Distributed computing framework for AI and Python workloads
- [Delta Lake](/concepts/delta-lake.md) — Open-source storage layer for reliability and ACID transactions
- Spark — Unified analytics engine for large-scale data processing
- [Unity Catalog](/concepts/unity-catalog.md) — Data governance solution for Databricks workspaces
- [Hive metastore](/concepts/built-in-hive-metastore.md) — Legacy metadata store for tables in Databricks
- [Delta Sharing](/concepts/delta-sharing.md) — Open protocol for sharing Delta Lake data across platforms
- Ray data integration patterns — Summary of all methods for connecting Ray and Spark

## Sources

- combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md

# Citations

1. [combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md](/references/combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws-47bcb6c6.md)
