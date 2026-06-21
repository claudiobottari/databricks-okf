---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 05a21f0239c98cab35d2b9c1c4e5f3840bd2fe3a81ddf911769d9bc1a100b5c5
  pageDirectory: concepts
  sources:
    - databricks-online-tables-legacy-databricks-on-aws.md
    - third-party-online-stores-databricks-on-aws.md
  confidence: 0.85
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - model-serving-with-automatic-feature-lookup
    - MSWAFL
    - Model Serving feature lookup
  citations:
    - file: databricks-online-tables-legacy-databricks-on-aws.md
    - file: third-party-online-stores-databricks-on-aws.md
title: Model Serving with Automatic Feature Lookup
description: Mechanism where models trained using FeatureLookup automatically retrieve feature values from online tables during inference without additional configuration.
tags:
  - databricks
  - model-serving
  - feature-store
timestamp: "2026-06-18T11:41:02.555Z"
---

# Model Serving with Automatic Feature Lookup

**Model Serving with automatic feature lookup** is a capability in [Databricks Feature Store](/concepts/databricks-feature-store.md) that allows a model deployed to Model Serving to automatically fetch feature values from an [online table](/concepts/online-tables.md) (or a third‑party online store) during inference. When a model is trained by referencing features through a `FeatureLookup`, and the underlying source table is synced to an online table, the deployed model retrieves the latest feature values without requiring any additional configuration. ^[databricks-online-tables-legacy-databricks-on-aws.md, third-party-online-stores-databricks-on-aws.md]

## How It Works

### With Databricks Online Tables

The recommended approach is to use [Databricks Online Feature Stores](/concepts/databricks-online-feature-store.md) (online tables). During model training, the user creates a training set by listing the feature lookups that describe which source Delta table and which lookup key to use. ^[databricks-online-tables-legacy-databricks-on-aws.md]

```python
training_set = fe.create_training_set(
    df=my_training_data,
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

After training, the model is registered in Unity Catalog and served with Model Serving. When the model receives an inference request, it automatically queries the online table that is synced from the source Delta table, using the primary key provided in the request payload. No extra configuration is needed on the serving endpoint. ^[databricks-online-tables-legacy-databricks-on-aws.md]

### With Third‑Party Online Stores

For real‑time serving of feature values, Databricks also supports third‑party online stores (such as Amazon DynamoDB or Redis). You publish feature tables to the third‑party database and deploy the model or feature spec to a REST endpoint. Automatic feature lookup works similarly: the input values provided by the client include values that are only available at the time of inference, and the model incorporates logic to automatically fetch the feature values it needs from the provided input values. ^[third-party-online-stores-databricks-on-aws.md]

The diagram below illustrates the relationship between [MLflow](/concepts/mlflow.md) and Feature Store components for real‑time serving:

![Feature Store workflow with online lookup](https://docs.databricks.com/aws/en/assets/images/fs-flow-online-lookup-3a850a7f3a04730d5911da59a10619af.png)

Databricks recommends using Databricks Online Feature Stores for new projects. ^[third-party-online-stores-databricks-on-aws.md]

## Requirements

- The workspace must be enabled for Unity Catalog. ^[databricks-online-tables-legacy-databricks-on-aws.md]
- A model must be registered in Unity Catalog to access online tables. ^[databricks-online-tables-legacy-databricks-on-aws.md]
- For Databricks online tables, the source Delta table must have a primary key, and an online table must be created from that source table (see [Online Tables (Legacy)](/concepts/databricks-online-tables.md)). ^[databricks-online-tables-legacy-databricks-on-aws.md]
- The user creating the feature spec and serving endpoint must be the owner of both the offline table and the online table. ^[databricks-online-tables-legacy-databricks-on-aws.md]
- For third‑party online stores, authentication must be configured as described in [Third‑Party Online Store Authentication](/concepts/third-party-online-store-authentication-for-feature-serving.md). ^[third-party-online-stores-databricks-on-aws.md]

## Workflow

1. **Create a feature spec** that references the source Delta table and the primary key. For example:
   ```python
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
2. **Create an online table** from the source Delta table (using Catalog Explorer or the API). The online table is a read‑only, row‑oriented copy that auto‑scales and serves low‑latency lookups. ^[databricks-online-tables-legacy-databricks-on-aws.md]
3. **Create a feature serving endpoint** that serves the feature spec. The endpoint uses the associated online table to perform fast lookups. ^[databricks-online-tables-legacy-databricks-on-aws.md]
4. **Deploy the model** using Model Serving. During inference, the model automatically fetches the required features from the online table (or third‑party store). ^[databricks-online-tables-legacy-databricks-on-aws.md]

For models hosted outside Databricks, you can create a [Feature Serving Endpoint](/concepts/feature-serving-endpoint.md) to serve features via REST API. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## User Permissions

To create an online table:
- `SELECT` privilege on the source table.
- `USE CATALOG` privilege on the destination catalog.
- `USE SCHEMA` and `CREATE TABLE` privilege on the destination schema. ^[databricks-online-tables-legacy-databricks-on-aws.md]

To manage the data synchronization pipeline of an online table, you must be the owner of the online table or be granted the `REFRESH` privilege on the online table. ^[databricks-online-tables-legacy-databricks-on-aws.md]

A unique service principal is automatically created for the feature serving or model serving endpoint with limited permissions required to query data from online tables. This allows endpoints to access data independently of the user who created the resource. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Limitations

- Only one online table is supported per source table. ^[databricks-online-tables-legacy-databricks-on-aws.md]
- The combined size of all online tables in a Unity Catalog [Metastore](/concepts/metastore.md) is 2 TB (uncompressed user data) during Public Preview. ^[databricks-online-tables-legacy-databricks-on-aws.md]
- Columns of data types `ARRAY`, `MAP`, or `STRUCT` cannot be used as primary keys. ^[databricks-online-tables-legacy-databricks-on-aws.md]
- If a primary‑key column contains null values, those rows are ignored in the online table. ^[databricks-online-tables-legacy-databricks-on-aws.md]
- Third‑party online stores are supported but Databricks recommends using Databricks Online Feature Stores. ^[third-party-online-stores-databricks-on-aws.md]

## Related Concepts

- [Feature Store](/concepts/feature-store.md)
- [Online Tables (Legacy)](/concepts/databricks-online-tables.md)
- [Feature Serving Endpoint](/concepts/feature-serving-endpoint.md)
- [Model Serving](/concepts/model-serving.md)
- [FeatureLookup](/concepts/featurelookup.md)
- [Third‑Party Online Store Authentication](/concepts/third-party-online-store-authentication-for-feature-serving.md)

## Sources

- databricks-online-tables-legacy-databricks-on-aws.md
- third-party-online-stores-databricks-on-aws.md

# Citations

1. [databricks-online-tables-legacy-databricks-on-aws.md](/references/databricks-online-tables-legacy-databricks-on-aws-a40fbf23.md)
2. [third-party-online-stores-databricks-on-aws.md](/references/third-party-online-stores-databricks-on-aws-33a2ab70.md)
