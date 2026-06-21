---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b38d664e3d86a4e41553b0f116f797b2a8ebaa4328021e16ce31405af2307d11
  pageDirectory: concepts
  sources:
    - databricks-online-tables-legacy-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - online-tables-databricks
    - OT(
  citations:
    - file: databricks-online-tables-legacy-databricks-on-aws.md
title: Online Tables (Databricks)
description: Read-only, row-oriented, serverless copies of Delta Tables optimized for low-latency online access, used with Model Serving, Feature Serving, and RAG applications.
tags:
  - databricks
  - online-tables
  - feature-serving
timestamp: "2026-06-18T15:09:16.515Z"
---

# Online Tables (Databricks)

**Online tables** are read-only copies of [Delta Table](/concepts/delta-lake-table.md)s stored in a row-oriented format optimized for low-latency, high-throughput online access. They are fully serverless and auto‑scale throughput with request load. Online tables are designed to work with [Model Serving](/concepts/model-serving.md), Feature Serving, and [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) applications for fast data lookups. ^[databricks-online-tables-legacy-databricks-on-aws.md]

Online tables can also be queried through [Lakehouse Federation](/concepts/lakehouse-federation-data-sharing.md) using a Serverless SQL warehouse, but only read operations (`SELECT`) are supported. This capability is intended for interactive or debugging purposes only and should not be used for production or mission‑critical workloads. ^[databricks-online-tables-legacy-databricks-on-aws.md]

Online tables are in **Public Preview** in the following AWS regions: `us-east-1`, `us-west-2`, `eu-west-1`, `ap-southeast-1`, `ap-southeast-2`. See the [pricing page](https://www.databricks.com/product/pricing/online-tables) for cost information. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Requirements

- The workspace must be enabled for [Unity Catalog](/concepts/unity-catalog.md) (a [Metastore](/concepts/metastore.md) must be created and enabled in the workspace).
- A model must be registered in Unity Catalog to access online tables.
- A Databricks admin must accept the Serverless Terms of Service in the account console. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Working with Online Tables via the UI

### Creating an Online Table

1.  The source Delta table must have a **primary key**. If it does not, you can create one by treating it as a feature table (see [Use an existing Delta table in Unity Catalog as a feature table](https://docs.databricks.com/aws/en/machine-learning/feature-store/uc/feature-tables-uc)).
2.  In Catalog Explorer, navigate to the source table and select **Create** → **Online table**.
3.  Configure the dialog:
    - **Name** – the full Unity Catalog name for the online table.
    - **Primary Key** – the column(s) from the source table to use as primary key(s).
    - **Time series Key** – (optional) a column to use as a time series key; when specified, only the row with the latest time series key value for each primary key is included.
    - **Sync mode** – choose **Snapshot**, **Triggered**, or **Continuous**. (Triggered and Continuous require the source table to have [Change Data Feed](/concepts/delta-change-data-feed-cdf.md) enabled.)
4.  Click **Confirm**. The online table appears in the catalog under the specified schema, with a dedicated icon.

^[databricks-online-tables-legacy-databricks-on-aws.md]

### Checking Status and Triggering Updates

Open the online table in Catalog Explorer. The **Data Ingest** section shows the status of the latest update. To trigger an immediate sync, click **Sync now**. This section also contains a link to the underlying pipeline that manages the table. ^[databricks-online-tables-legacy-databricks-on-aws.md]

### Scheduling Periodic Updates

For **Snapshot** or **Triggered** sync modes, you can schedule automatic updates via the pipeline. Navigate to the online table’s **Data Ingest** section, click the pipeline link, then click **Schedule** in the upper‑right corner of the pipeline page to add or update a schedule. ^[databricks-online-tables-legacy-databricks-on-aws.md]

### Deleting an Online Table

From the online table page, select **Delete** from the kebab menu. Deleting stops any ongoing data synchronization and releases all resources. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Working with Online Tables via APIs

You can use the Databricks SDK for Python (version 0.20 or above) or the REST API to create, get status, trigger refreshes, and delete online tables. ^[databricks-online-tables-legacy-databricks-on-aws.md]

### Creating an Online Table (SDK Example)

```python
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

^[databricks-online-tables-legacy-databricks-on-aws.md]

### Getting Status and Triggering a Refresh

```python
pprint(w.online_tables.get('main.default.my_online_table'))
# Returns the OnlineTable object with spec and status.
# To trigger a refresh, use the pipeline API:
w.pipelines.start_update(pipeline_id='some-pipeline-id', full_refresh=True)
```

^[databricks-online-tables-legacy-databricks-on-aws.md]

### Deleting

```python
w.online_tables.delete('main.default.my_online_table')
```

^[databricks-online-tables-legacy-databricks-on-aws.md]

## Serving Online Table Data via a Feature Serving Endpoint

For models and applications hosted outside Databricks, you can expose online table data through a Feature Serving endpoint.

1.  Create a **feature spec** using `FeatureEngineeringClient`. The spec references the source Delta table (the same one the online table syncs from). The source table and online table must share the same primary key.
    ```python
    fe = FeatureEngineeringClient()
    fe.create_feature_spec(
        name="catalog.default.user_preferences_spec",
        features=[
            FeatureLookup(
                table_name="user_preferences",
                lookup_key="user_id"
            )
        ]
    )
    ```
2.  Create a **feature serving endpoint** using the SDK. The user performing this operation must be the owner of both the offline and online tables.
    ```python
    workspace.serving_endpoints.create_and_wait(
        name="fse-location",
        config=EndpointCoreConfigInput(
            served_entities=[
                ServedEntityInput(
                    entity_name=feature_spec_name,
                    scale_to_zero_enabled=True,
                    workload_size="Small"
                )
            ]
        )
    )
    ```
3.  Query the endpoint via REST API (HTTP POST) with the DataFrame records format.

^[databricks-online-tables-legacy-databricks-on-aws.md]

## Using Online Tables with RAG Applications

RAG applications commonly use online tables for structured data lookups. The typical workflow:
1. Create a feature serving endpoint for the online table.
2. Build a tool (e.g., using LangChain) that calls the endpoint.
3. Use the tool in an agent to retrieve data.
4. Deploy the application on a [Model Serving](/concepts/model-serving.md) endpoint.

For step‑by‑step instructions and a sample notebook, see the Databricks documentation on [using features with structured RAG applications](https://docs.databricks.com/aws/en/machine-learning/feature-store/rag). ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Using Online Tables with Model Serving

When a model is trained using features from a Delta table (via `FeatureLookup`), serving that model on a [Model Serving](/concepts/model-serving.md) endpoint automatically causes the system to look up feature values from the corresponding online table – no extra configuration is needed. ^[databricks-online-tables-legacy-databricks-on-aws.md]

Example training step:
```python
training_set = fe.create_training_set(
    df=id_rt_feature_labels,
    label='quality',
    feature_lookups=[
        FeatureLookup(
            table_name="user_preferences",
            lookup_key="user_id"
        )
    ],
    exclude_columns=['user_id'],
)
```

^[databricks-online-tables-legacy-databricks-on-aws.md]

## User Permissions

To **create** an online table, a user needs:
- `SELECT` privilege on the source table.
- `USE CATALOG` privilege on the destination catalog.
- `USE SCHEMA` and `CREATE TABLE` privileges on the destination schema.

To **manage the synchronization pipeline**, the user must either be the owner of the online table or have the `REFRESH` privilege on it. Users without `USE CATALOG` and `USE SCHEMA` on the catalog will not see the online table in Catalog Explorer. The Unity Catalog [Metastore](/concepts/metastore.md) must have **Privilege Model Version 1.0**. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Endpoint Permission Model

A unique service principal is automatically created for each Feature Serving or [Model Serving](/concepts/model-serving.md) endpoint. This principal has limited permissions to query data from online tables, allowing the endpoint to continue functioning even if the original creator leaves the workspace. The service principal lives as long as the endpoint exists. Audit logs may show system‑generated records for the owner of the Unity Catalog catalog granting necessary privileges to this principal. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Limitations

- Only **one online table per source table** is supported.
- An online table and its source table can have at most **1000 columns**.
- Columns of types `ARRAY`, `MAP`, or `STRUCT` cannot be used as primary keys.
- Rows in the source table where a primary key column contains `NULL` are ignored.
- Foreign, system, and internal tables are **not supported** as source tables.
- Source tables without [Change Data Feed](/concepts/delta-change-data-feed-cdf.md) enabled support only **Snapshot** sync mode.
- [Delta Sharing](/concepts/delta-sharing.md) tables are supported only in **Snapshot** mode.
- Catalog, schema, and table names can contain only alphanumeric characters and underscores, and must not start with numbers. Dashes (`-`) are not allowed.
- String columns are limited to **64 KB** length; column names to **64 characters**.
- Maximum row size is **2 MB**.
- During Public Preview, the combined uncompressed size of all online tables in a Unity Catalog [Metastore](/concepts/metastore.md) is limited to **2 TB**.
- Maximum read throughput for a [Metastore](/concepts/metastore.md) is approximately **750 MB/sec**.

^[databricks-online-tables-legacy-databricks-on-aws.md]

## Troubleshooting

### “Create online table” option missing

The source table’s Securable Kind (shown in Catalog Explorer’s **Details** tab) must be one of the supported types, including: `TABLE_EXTERNAL`, `TABLE_DELTA`, `TABLE_DELTA_EXTERNAL`, `TABLE_DELTASHARING`, `TABLE_DELTASHARING_MUTABLE`, `TABLE_STREAMING_LIVE_TABLE`, `TABLE_STANDARD`, `TABLE_FEATURE_STORE`, `TABLE_FEATURE_STORE_EXTERNAL`, `TABLE_VIEW`, `TABLE_VIEW_DELTASHARING`, `TABLE_MATERIALIZED_VIEW`. ^[databricks-online-tables-legacy-databricks-on-aws.md]

### Cannot select Triggered or Continuous sync modes

This occurs if the source table does not have Delta change data feed enabled, or if it is a View or materialized view. Enable change data feed or switch to a non‑view source table. ^[databricks-online-tables-legacy-databricks-on-aws.md]

### Online table update fails or shows offline

1. Click the **pipeline ID** in the online table’s **Overview** tab.
2. On the pipeline UI, click the entry “Failed to resolve flow '\_\_online\_table”.
3. A popup shows **Error details**.

Common causes:
- The source table was deleted or recreated while the online table was syncing (especially common for continuous sync).
- The source table is inaccessible through Serverless Compute due to firewall settings (error: “Failed to start the Lakeflow Spark Declarative Pipelines service…”).
- The aggregate uncompressed size of all online tables in the [Metastore](/concepts/metastore.md) exceeds 2 TB. Note that the row‑oriented format can be significantly larger (up to 100×) than the compressed size shown in Catalog Explorer. To estimate the uncompressed size of a Delta table, run this query from a Serverless SQL Warehouse:
  ```sql
  SELECT sum(length(to_csv(struct(*)))) FROM `source_table`;
  ```
  Successfully executing this query also confirms that Serverless Compute can access the source table.

^[databricks-online-tables-legacy-databricks-on-aws.md]

## Related Concepts

- [Delta Table](/concepts/delta-lake-table.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Model Serving](/concepts/model-serving.md)
- Feature Serving
- [Feature Engineering Client](/concepts/featureengineeringclient-api.md)
- [Change Data Feed](/concepts/delta-change-data-feed-cdf.md)
- [Delta Sharing](/concepts/delta-sharing.md)
- [Lakehouse Federation](/concepts/lakehouse-federation-data-sharing.md)
- Serverless SQL Warehouse
- Databricks SDK for Python

## Sources

- databricks-online-tables-legacy-databricks-on-aws.md

# Citations

1. [databricks-online-tables-legacy-databricks-on-aws.md](/references/databricks-online-tables-legacy-databricks-on-aws-a40fbf23.md)
