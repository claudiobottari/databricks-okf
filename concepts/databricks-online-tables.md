---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f807155549fc7deeb11667032cd398c1ee0d87d6632e0169c48ba951c0a4c6ad
  pageDirectory: concepts
  sources:
    - databricks-online-tables-legacy-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-online-tables
    - DOT
    - Databricks Tables
    - databricks-online-tables-legacy
    - DOT(
    - Databricks online table (legacy)
    - Online Table (legacy)
    - Online Tables (Legacy)
    - Online tables (legacy)
  citations:
    - file: databricks-online-tables-legacy-databricks-on-aws.md
title: Databricks Online Tables
description: Read-only, serverless copies of Delta Tables stored in row-oriented format, optimized for low-latency online access from Model Serving, Feature Serving, and RAG applications.
tags:
  - databricks
  - feature-store
  - serverless
timestamp: "2026-06-19T14:52:33.257Z"
---

---

title: Databricks Online Tables
summary: Read-only row-oriented copies of Delta Tables optimized for low-latency online access, used with Model Serving, Feature Serving, and RAG applications.
sources:
  - databricks-online-tables-legacy-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:40:07.241Z"
updatedAt: "2026-06-18T11:40:07.241Z"
tags:
  - databricks
  - feature-store
  - online-serving
aliases:
  - databricks-online-tables
  - DOT
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Databricks Online Tables

**Databricks Online Tables** are read-only copies of [Delta Table](/concepts/delta-lake-table.md)s stored in a row-oriented format optimized for low-latency, high-throughput online access. They are fully serverless and auto-scale with request load, making them suitable for powering [Model Serving](/concepts/model-serving.md), Feature Serving, and [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) applications. Online tables are in **Public Preview** in `us-east-1`, `us-west-2`, `eu-west-1`, `ap-southeast-1`, and `ap-southeast-2`. ^[databricks-online-tables-legacy-databricks-on-aws.md]

You can also query online tables via [Lakehouse Federation](/concepts/lakehouse-federation-data-sharing.md) using a Serverless SQL Warehouse, though only `SELECT` is supported. This capability is intended for interactive or debugging use only, not for production workloads. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Requirements

- The workspace must be enabled for [Unity Catalog](/concepts/unity-catalog.md).
- A model must be registered in Unity Catalog to access online tables directly from Model Serving.
- A Databricks admin must accept the Serverless Terms of Service in the account console. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Create an Online Table

### Using the UI (Catalog Explorer)

1. The source Delta table must have a primary key defined. If it does not, follow [the documentation to create one](https://docs.databricks.com/aws/en/machine-learning/feature-store/uc/feature-tables-uc#use-existing-uc-table).
2. In Catalog Explorer, navigate to the source table, open the **Create** menu, and select **Online table**.
3. Configure the online table:
   - **Name**: The Unity Catalog name for the online table.
   - **Primary Key**: One or more columns from the source table.
   - **Time series Key** (optional): If provided, only the row with the latest time series key value for each primary key is included.
   - **Sync mode**: Snapshot, Triggered, or Continuous. Note: Triggered and Continuous require the source table to have [Change data feed](https://docs.databricks.com/aws/en/tables/features/change-data-feed) enabled.
4. Click **Confirm**. The online table appears under the specified [Catalog and Schema](/concepts/catalog-and-schema.md), marked with a special icon. ^[databricks-online-tables-legacy-databricks-on-aws.md]

### Using the API or SDK

Use Python SDK version 0.20 or later, or the REST API. The example below creates a triggered online table with the SDK:

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

After creation, the online table automatically starts syncing. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Manage an Online Table

### Check Status and Trigger Updates

In the Catalog Explorer, open the online table to see its **Overview** tab. The **Data Ingest** section shows the latest update status. Click **Sync now** to trigger a manual update. The pipeline ID is also shown.

To schedule periodic updates (Snapshot or Triggered mode only), open the pipeline from the **Data Ingest** section, click **Schedule**, and configure the schedule. ^[databricks-online-tables-legacy-databricks-on-aws.md]

### Using APIs

Retrieve status and spec:

```python
pprint(w.online_tables.get('main.default.my_online_table'))
```

To trigger a refresh, call the pipeline API with the pipeline ID from the spec. Use `full_refresh=True` to discard existing data before refreshing (for example, if sync is stuck due to source table deletion and recreation). ^[databricks-online-tables-legacy-databricks-on-aws.md]

### Delete an Online Table

From the online table page in Catalog Explorer, select **Delete** from the kebab menu. Or with the SDK:

```python
w.online_tables.delete('main.default.my_online_table')
```

Deleting stops synchronization and releases all resources. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Serve Online Table Data Using a Feature Serving Endpoint

For models and applications hosted outside Databricks, you can create a [Feature Serving Endpoint](/concepts/feature-serving-endpoint.md) that provides low-latency REST API access to features backed by an online table.

1. Create a [feature spec](/concepts/featurespec.md) using `FeatureEngineeringClient`. The spec references the source Delta table; for online lookups, the serving endpoint automatically uses the associated online table.
   ```python
   from databricks.feature_engineering import FeatureEngineeringClient, FeatureLookup
   fe = FeatureEngineeringClient()
   fe.create_feature_spec(
       name="catalog.default.user_preferences_spec",
       features=[
           FeatureLookup(table_name="user_preferences", lookup_key="user_id")
       ]
   )
   ```
2. Create the serving endpoint:
   ```python
   from databricks.sdk import WorkspaceClient
   from databricks.sdk.service.serving import EndpointCoreConfigInput, ServedEntityInput

   workspace = WorkspaceClient()
   workspace.serving_endpoints.create_and_wait(
       name="fse-location",
       config=EndpointCoreConfigInput(
           served_entities=[
               ServedEntityInput(entity_name=feature_spec_name, scale_to_zero_enabled=True, workload_size="Small")
           ]
       )
   )
   ```
3. Query the endpoint with a POST request containing `dataframe_records`.

The user creating the endpoint must be the owner of both the offline table and the online table. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Use Online Tables with RAG Applications

In a RAG application, structured data from an online table is hosted on a feature serving endpoint. The application uses that endpoint (via a LangChain tool or similar) to look up relevant data. The typical steps are:

1. Create a feature serving endpoint.
2. Create a tool (e.g., LangChain) that calls the endpoint.
3. Build an agent that uses the tool.
4. Host the agent on a model serving endpoint.

See the [example notebook](https://docs.databricks.com/aws/en/machine-learning/feature-store/rag) for step-by-step instructions. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Use Online Tables with Model Serving

When you train a model using `FeatureLookup` from a feature table, and that feature table is synced to an online table, the model automatically looks up features from the online table during inference via Model Serving. No additional configuration beyond creating the online table is required. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## User Permissions

To create an online table, you need:

- `SELECT` privilege on the source table.
- `USE CATALOG` privilege on the destination catalog.
- `USE SCHEMA` and `CREATE TABLE` privilege on the destination schema.

To manage the data synchronization pipeline (e.g., trigger updates), you must be the owner of the online table or have the `REFRESH` privilege on it. Users without `USE CATALOG` and `USE SCHEMA` on the catalog will not see the online table in Catalog Explorer.

The Unity Catalog [Metastore](/concepts/metastore.md) must use Privilege Model Version 1.0. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Endpoint Permission Model

When a feature serving or model serving endpoint is created, a unique service principal is automatically provisioned with limited permissions to query data from online tables. This allows the endpoint to function independently of the creator, even if the creator leaves the workspace. The service principal exists for the lifetime of the endpoint. Audit logs may show system-generated records when the Unity Catalog owner grants privileges to this principal. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Limitations

- Only one online table is supported per source table.
- Maximum 1000 columns in source and online table.
- ARRAY, MAP, and STRUCT columns cannot be primary keys.
- Rows with `NULL` in primary key columns are ignored.
- Foreign, system, and internal tables are not supported as sources.
- Without Delta Change Data Feed, only the **Snapshot** sync mode is available.
- OpenSharing tables only support **Snapshot** mode.
- Online table names (catalog, schema, table) may contain only alphanumeric characters and underscores, and must not start with numbers. Hyphens are not allowed.
- String columns are limited to 64KB.
- Column names are limited to 64 characters.
- Maximum row size is 2MB.
- Combined uncompressed size of all online tables in a [Metastore](/concepts/metastore.md): 2 TB during Public Preview.
- Maximum read throughput per [Metastore](/concepts/metastore.md): approximately 750 MB/sec. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Troubleshooting

### I don't see the **Create online table** option

The source table may be of an unsupported type. Check the table's Securable Kind in Catalog Explorer. Supported types include `TABLE_EXTERNAL`, `TABLE_DELTA`, `TABLE_DELTA_EXTERNAL`, `TABLE_DELTASHARING`, `TABLE_DELTASHARING_MUTABLE`, `TABLE_STREAMING_LIVE_TABLE`, `TABLE_STANDARD`, `TABLE_FEATURE_STORE`, `TABLE_FEATURE_STORE_EXTERNAL`, `TABLE_VIEW`, `TABLE_VIEW_DELTASHARING`, and `TABLE_MATERIALIZED_VIEW`. ^[databricks-online-tables-legacy-databricks-on-aws.md]

### Cannot select Triggered or Continuous sync mode

The source table must have Delta Change Data Feed enabled and must not be a view or materialized view. ^[databricks-online-tables-legacy-databricks-on-aws.md]

### Online table update fails or status shows offline

Click the pipeline ID link in the online table's **Overview** tab. On the pipeline UI, click the failed entry (e.g., “Failed to resolve flow '__online_table'”) to see error details. Common causes:

- The source table was deleted or recreated while the online table was syncing.
- The source table is not accessible via Serverless Compute (firewall settings). The error may say “Failed to start the Lakeflow Spark Declarative Pipelines service…”
- The uncompressed size of the online table exceeds the 2 TB metastore-wide limit. To estimate the expanded row-oriented size of a Delta table, run from a Serverless SQL Warehouse:
  ```sql
  SELECT sum(length(to_csv(struct(*)))) FROM `source_table`;
  ``` ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md)
- [Delta Table](/concepts/delta-lake-table.md)
- [Model Serving](/concepts/model-serving.md)
- Feature Serving
- [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md)
- [Lakehouse Federation](/concepts/lakehouse-federation-data-sharing.md)
- Serverless SQL Warehouse
- [Feature Spec](/concepts/featurespec.md)
- [Feature Serving Endpoint](/concepts/feature-serving-endpoint.md)
- [Change Data Feed](/concepts/delta-change-data-feed-cdf.md)
- Databricks SDK

## Sources

- databricks-online-tables-legacy-databricks-on-aws.md

# Citations

1. [databricks-online-tables-legacy-databricks-on-aws.md](/references/databricks-online-tables-legacy-databricks-on-aws-a40fbf23.md)
