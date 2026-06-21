---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 58f5f7082bcb89e922bbf9a05f79b9be39e0fe179f5811035ad7f7f843c1c2ad
  pageDirectory: concepts
  sources:
    - databricks-online-tables-legacy-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature-serving-with-online-tables
    - FSWOT
    - Feature Serving with Online Stores
  citations:
    - file: databricks-online-tables-legacy-databricks-on-aws.md
title: Feature Serving with Online Tables
description: Architecture for serving online table data via REST API endpoints using a feature serving endpoint, enabling low-latency feature lookups for models and applications hosted outside Databricks.
tags:
  - databricks
  - feature-serving
  - rest-api
  - model-serving
timestamp: "2026-06-19T18:14:32.745Z"
---

# Feature Serving with Online Tables

**Feature Serving with Online Tables** is a Databricks capability that exposes features from [Online Tables](/concepts/online-tables.md) through a low-latency REST API, enabling models and applications hosted outside of Databricks to perform online feature lookups. A feature serving endpoint automatically reads from the associated online table, providing efficient, row-oriented access instead of querying the source Delta table directly. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## How Feature Serving with Online Tables Works

An [online table](/concepts/online-tables.md) is a read-only, row-oriented copy of a Delta Table that is optimized for online access. When you create a feature serving endpoint, you associate it with a [feature spec](/concepts/featurespec.md) that references a source Delta table. The endpoint automatically uses the online table (when present) for low-latency feature lookups, rather than querying the source Delta table directly. The source Delta table and the corresponding online table must share the same primary key. ^[databricks-online-tables-legacy-databricks-on-aws.md]

The feature spec is registered in Unity Catalog as a function and can be viewed under the **Function** tab in Catalog Explorer. The serving endpoint is a serverless endpoint that scales to zero and handles request load automatically. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Creating a Feature Serving Endpoint from an Online Table

### Prerequisites

- An online table must already exist and be synchronized from the source Delta table.
- The user performing the endpoint creation must be the owner of both the offline (source) table and the online table.
- The workspace must be enabled for Unity Catalog, and a Databricks admin must have accepted the Serverless Terms of Service. ^[databricks-online-tables-legacy-databricks-on-aws.md]

### Steps

1. **Create a feature spec** that defines the features to serve. Use the [FeatureEngineeringClient] to create a spec with one or more `FeatureLookup` objects referencing the source Delta table.

   ```python
   from databricks.feature_engineering import FeatureEngineeringClient, FeatureLookup

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

   ^[databricks-online-tables-legacy-databricks-on-aws.md]

2. **Create the serving endpoint** using the Databricks SDK or REST API. The endpoint configuration must reference the feature spec name and specify a workload size.

   ```python
   from databricks.sdk import WorkspaceClient
   from databricks.sdk.service.serving import EndpointCoreConfigInput, ServedEntityInput

   workspace = WorkspaceClient()

   endpoint_name = "fse-location"
   workspace.serving_endpoints.create_and_wait(
       name=endpoint_name,
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

   ^[databricks-online-tables-legacy-databricks-on-aws.md]

After creation, the endpoint is ready to accept requests.

## Querying a Feature Serving Endpoint

To retrieve features, send an HTTP POST request to the endpoint URL with the lookup keys in the request body.

```python
import json, requests

url = "https://{workspace_url}/serving-endpoints/user-preferences/invocations"
headers = {
    'Authorization': f'Bearer {DATABRICKS_TOKEN}',
    'Content-Type': 'application/json'
}
data = {"dataframe_records": [{"user_id": user_id}]}
data_json = json.dumps(data, allow_nan=True)

response = requests.request(method='POST', headers=headers, url=url, data=data_json)
if response.status_code != 200:
    raise Exception(f'Request failed with status {response.status_code}, {response.text}')
print(response.json()['outputs'][0]['hotel_preference'])
```

^[databricks-online-tables-legacy-databricks-on-aws.md]

The response contains the feature values for the requested keys.

## Permissions and Security

### Required Permissions for Endpoint Creation

- `SELECT` privilege on the source Delta table.
- `USE CATALOG` privilege on the destination catalog.
- `USE SCHEMA` and `CREATE TABLE` privilege on the destination schema (for the online table, if not already existing). ^[databricks-online-tables-legacy-databricks-on-aws.md]

### Service Principal for Endpoint

A unique service principal is automatically created for each feature serving endpoint. This service principal has limited permissions — only those required to read from the online table — so that the endpoint can function independently of the user who created it. The service principal lives as long as the endpoint exists. Audit logs may show system-generated records for the catalog owner granting necessary privileges to this service principal. ^[databricks-online-tables-legacy-databricks-on-aws.md]

### Managing the Pipeline

To manage the data synchronization pipeline of an online table (e.g., trigger a refresh), a user must be either the owner of the online table or have the `REFRESH` privilege on it. Users without `USE CATALOG` and `USE SCHEMA` on the parent catalog will not see the online table in Catalog Explorer. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Limitations

- Only one online table can be created per source Delta table.
- An online table and its source can have at most 1000 columns.
- Columns of data types `ARRAY`, `MAP`, or `STRUCT` cannot be used as primary keys.
- Rows with null primary key columns are ignored.
- Catalog, schema, and table names can only contain alphanumeric characters and underscores; dashes are not allowed.
- String columns are limited to 64 KB length; column names to 64 characters.
- Maximum row size is 2 MB.
- During Public Preview, the total uncompressed size of all online tables in a [Metastore](/concepts/metastore.md) is 2 TB.
- Maximum read throughput per [Metastore](/concepts/metastore.md) is approximately 750 MB/sec.
- Source tables without Delta Change Data Feed support only **Snapshot** sync mode. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Related Concepts

- [Online Tables](/concepts/online-tables.md) — The row-oriented, low-latency copies of Delta Tables
- [Feature Engineering Client](/concepts/featureengineeringclient-api.md) — The Python client for creating feature specs
- [Model Serving](/concepts/model-serving.md) — Serving models with automatic feature lookup from online tables
- [Feature Store](/concepts/feature-store.md) — The repository for storing and managing feature tables
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer that secures tables and endpoints
- Serverless Compute — The underlying compute for online table synchronization
- [Change Data Feed](/concepts/delta-change-data-feed-cdf.md) — Required for incremental sync modes

## Sources

- databricks-online-tables-legacy-databricks-on-aws.md

# Citations

1. [databricks-online-tables-legacy-databricks-on-aws.md](/references/databricks-online-tables-legacy-databricks-on-aws-a40fbf23.md)
