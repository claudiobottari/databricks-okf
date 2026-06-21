---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bf2440626ed5d8b0b7bfc2176707daf399a7c217f1def20d563a7de870d96a8f
  pageDirectory: concepts
  sources:
    - databricks-online-tables-legacy-databricks-on-aws.md
  confidence: 0.99
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - online-table-databricks
    - OT(
    - online-tables-databricks
  citations:
    - file: databricks-online-tables-legacy-databricks-on-aws.md
title: Online Table (Databricks)
description: Read-only, row-oriented, serverless copy of a Delta Table optimized for low-latency online access, used with Model Serving, Feature Serving, and RAG applications.
tags:
  - databricks
  - online-serving
  - feature-store
timestamp: "2026-06-19T09:53:26.498Z"
---

# Online Table (Databricks)

**Online Table** is a serverless, read-only copy of a [Delta Table](/concepts/delta-lake-table.md) stored in row-oriented format, optimized for low-latency, high-throughput access. It is designed for use with [Model Serving](/concepts/model-serving.md), Feature Serving, and [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) applications that require fast data lookups. Online tables auto-scale throughput capacity with request load and are fully managed by Databricks. ^[databricks-online-tables-legacy-databricks-on-aws.md]

Online tables are in **Public Preview** in AWS regions `us-east-1`, `us-west-2`, `eu-west-1`, `ap-southeast-1`, and `ap-southeast-2`. Pricing information is available on the [Databricks pricing page](https://www.databricks.com/product/pricing/online-tables). ^[databricks-online-tables-legacy-databricks-on-aws.md]

Online tables can also be queried read-only via [Lakehouse Federation](/concepts/lakehouse-federation-data-sharing.md) using a Serverless SQL warehouse. This capability is intended for interactive or debugging purposes and should not be used for production or mission-critical workloads. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Requirements

- The workspace must be enabled for [Unity Catalog](/concepts/unity-catalog.md) with a [Metastore](/concepts/metastore.md), and a catalog must exist. ^[databricks-online-tables-legacy-databricks-on-aws.md]
- A model must be registered in Unity Catalog to access online tables. ^[databricks-online-tables-legacy-databricks-on-aws.md]
- A Databricks admin must accept the Serverless Terms of Service in the account console. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Creating an Online Table

### Using the UI (Catalog Explorer)

1. The source Delta table must have a **primary key**. If it does not, create one by following the [instructions for using an existing Delta table as a feature table](https://docs.databricks.com/aws/en/machine-learning/feature-store/uc/feature-tables-uc#use-existing-uc-table). ^[databricks-online-tables-legacy-databricks-on-aws.md]
2. In Catalog Explorer, navigate to the source table and select **Create** > **Online table**. ^[databricks-online-tables-legacy-databricks-on-aws.md]
3. Configure:
   - **Name** – The Unity Catalog name for the online table.
   - **Primary Key** – Column(s) from the source table.
   - **Time Series Key** (optional) – When specified, only the row with the latest time series key value for each primary key is included.
   - **Sync Mode** – One of **Snapshot**, **Triggered**, or **Continuous**.
4. Click **Confirm**. The online table is created under the specified catalog/schema and is marked with a specific icon in Catalog Explorer. ^[databricks-online-tables-legacy-databricks-on-aws.md]

> **Note:** Triggered and Continuous sync modes require the source table to have [Change data feed](/concepts/delta-change-data-feed-cdf.md) enabled. ^[databricks-online-tables-legacy-databricks-on-aws.md]

### Using APIs

Use the Databricks SDK for Python (version 0.20 or above) or the [REST API](https://docs.databricks.com/api/workspace/onlinetables). ^[databricks-online-tables-legacy-databricks-on-aws.md]

**Python SDK example:**

```python
from pprint import pprint
from databricks.sdk import WorkspaceClient
from databricks.sdk.service.catalog import *

w = WorkspaceClient(host='https://xxx.databricks.com', token='xxx')

spec = OnlineTableSpec(
  primary_key_columns=["pk_col"],
  source_table_full_name="main.default.source_table",
  run_triggered=OnlineTableSpecTriggeredSchedulingPolicy.from_dict({'triggered': 'true'})
)
online_table = OnlineTable(
  name="main.default.my_online_table",
  spec=spec
)
w.online_tables.create_and_wait(table=online_table)
```

The online table automatically starts syncing after creation. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Sync Modes

| Sync Mode | Description |
|-----------|-------------|
| **Snapshot** | Full copy of the source table at creation time. No incremental updates. |
| **Triggered** | Updates on demand via manual trigger or scheduled refresh. Requires Change data feed. |
| **Continuous** | Continuously synchronizes changes from the source table. Requires Change data feed. |

To schedule periodic updates for Snapshot or Triggered tables, navigate to the online table’s pipeline in Catalog Explorer and add a schedule via the **Schedule** button. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Managing Online Tables

### Get Status and Trigger Refresh

In the UI, open the online table in Catalog Explorer. The **Data Ingest** section shows the latest update status and provides a **Sync now** button to trigger a manual refresh. The same section links to the underlying pipeline. ^[databricks-online-tables-legacy-databricks-on-aws.md]

Via the SDK:

```python
w.online_tables.get('main.default.my_online_table')
# Returns an OnlineTable object with status and spec

# To trigger a refresh:
w.pipelines.start_update(pipeline_id='some-pipeline-id', full_refresh=True)
```

The `full_refresh=True` parameter discards all existing data in the online table before refreshing. Use it if the sync is stuck (e.g., after source table recreation). ^[databricks-online-tables-legacy-databricks-on-aws.md]

### Delete an Online Table

UI: From the online table page, select **Delete** from the kebab menu. ^[databricks-online-tables-legacy-databricks-on-aws.md]

SDK:
```python
w.online_tables.delete('main.default.my_online_table')
```

Deleting stops ongoing synchronization and releases resources. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Serving Data from Online Tables

### Feature Serving Endpoint

For models and applications hosted outside Databricks, create a [Feature Serving Endpoint](/concepts/feature-serving-endpoint.md) that uses the online table for low-latency lookups via REST API.

1. **Create a feature spec** using `FeatureEngineeringClient`. The spec references the source Delta table and uses the same primary key as the online table. ^[databricks-online-tables-legacy-databricks-on-aws.md]
2. **Create a feature serving endpoint** with the SDK. The owner must own both the offline and online tables. ^[databricks-online-tables-legacy-databricks-on-aws.md]
3. **Query the endpoint** via HTTP POST with a bearer token. Example:
   ```python
   url = "https://{workspace_url}/serving-endpoints/user-preferences/invocations"
   headers = {'Authorization': f'Bearer {DATABRICKS_TOKEN}', 'Content-Type': 'application/json'}
   data = {"dataframe_records": [{"user_id": user_id}]}
   response = requests.post(url, headers=headers, json=data)
   ```

### Model Serving with Automatic Feature Lookup

When a model is trained using `FeatureLookup` from a feature table, and that feature table is synced to an online table, the model automatically retrieves feature values from the online table during inference via [Model Serving](/concepts/model-serving.md) — no additional configuration required. ^[databricks-online-tables-legacy-databricks-on-aws.md]

### RAG Applications

For [RAG](/concepts/retrieval-augmented-generation-rag.md) applications, create an online table for structured data, expose it via a feature serving endpoint, and use tools (e.g., LangChain) to query it from the agent. Step-by-step guidance and an example notebook are available in the [Databricks RAG documentation](https://docs.databricks.com/aws/en/machine-learning/feature-store/rag). ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Permissions

### User Permissions for Creating an Online Table

- `SELECT` privilege on the source table.
- `USE CATALOG` privilege on the destination catalog.
- `USE SCHEMA` and `CREATE TABLE` privileges on the destination schema. ^[databricks-online-tables-legacy-databricks-on-aws.md]

To manage the sync pipeline, users must be the owner of the online table or have `REFRESH` privilege on it. Users without `USE CATALOG` and `USE SCHEMA` on the catalog will not see the online table in Catalog Explorer. The [Metastore](/concepts/metastore.md) must use Privilege Model Version 1.0. ^[databricks-online-tables-legacy-databricks-on-aws.md]

### Endpoint Permission Model

When a feature serving or model serving endpoint is created, a unique service principal is automatically provisioned with the minimum permissions needed to query online tables. This ensures the endpoint continues to function independently of the creating user. The service principal lives as long as the endpoint exists. Audit logs may show system-generated records for the Unity Catalog owner granting necessary privileges to this principal. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Limitations

- Only **one online table** per source table.
- Online table and its source table can have at most **1000 columns**.
- Columns of type `ARRAY`, `MAP`, or `STRUCT` cannot be primary keys.
- Rows with `NULL` in a primary key column are ignored.
- Foreign, system, and internal tables are not supported as source tables.
- Source tables without Delta Change Data Feed support only **Snapshot** sync mode.
- OpenSharing tables are supported only in **Snapshot** mode.
- Catalog, schema, and table names can only contain alphanumeric characters and underscores; dashes (`-`) are not allowed; names must not start with a digit.
- `STRING` columns limited to **64 KB**.
- Column names limited to **64 characters**.
- Maximum row size: **2 MB**.
- Combined size of all online tables in a Unity Catalog [Metastore](/concepts/metastore.md) during Public Preview: **2 TB** uncompressed user data.
- Maximum read throughput per [Metastore](/concepts/metastore.md): approximately **750 MB/sec**. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Troubleshooting

### "Create online table" option not visible

The source table's Securable Kind (shown in Catalog Explorer's **Details** tab) must be one of: `TABLE_EXTERNAL`, `TABLE_DELTA`, `TABLE_DELTA_EXTERNAL`, `TABLE_DELTASHARING`, `TABLE_DELTASHARING_MUTABLE`, `TABLE_STREAMING_LIVE_TABLE`, `TABLE_STANDARD`, `TABLE_FEATURE_STORE`, `TABLE_FEATURE_STORE_EXTERNAL`, `TABLE_VIEW`, `TABLE_VIEW_DELTASHARING`, or `TABLE_MATERIALIZED_VIEW`. ^[databricks-online-tables-legacy-databricks-on-aws.md]

### Cannot select Triggered or Continuous sync mode

The source table likely lacks [Change data feed](/concepts/delta-change-data-feed-cdf.md) or is a View/Materialized view. Enable change data feed or use a non-view Delta table. ^[databricks-online-tables-legacy-databricks-on-aws.md]

### Online table update fails or shows offline

1. Click the **pipeline ID** link on the online table's **Overview** tab in Catalog Explorer. ^[databricks-online-tables-legacy-databricks-on-aws.md]
2. On the pipeline UI, click the entry that says “Failed to resolve flow '__online_table”. ^[databricks-online-tables-legacy-databricks-on-aws.md]
3. A popup shows detailed error information. ^[databricks-online-tables-legacy-databricks-on-aws.md]

Common causes:
- The source table was deleted or recreated while syncing (common with continuous sync).
- The source table is inaccessible via Serverless Compute due to firewall settings (error message may mention “Failed to start the Lakeflow Spark Declarative Pipelines service”).
- The aggregate online table size exceeds the 2 TB metastore-wide limit. Note that the uncompressed row-oriented size can be up to **100x larger** than the compressed columnar Delta table size shown in Catalog Explorer. To estimate the uncompressed size, run the following SQL from a Serverless SQL Warehouse:
  ```sql
  SELECT sum(length(to_csv(struct(*)))) FROM `source_table`;
  ``` ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Sources

- databricks-online-tables-legacy-databricks-on-aws.md

# Citations

1. [databricks-online-tables-legacy-databricks-on-aws.md](/references/databricks-online-tables-legacy-databricks-on-aws-a40fbf23.md)
