---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a21871802be66fd124af762513dedb682d56b6850e684a14465c1f7b650ceabc
  pageDirectory: concepts
  sources:
    - databricks-online-feature-stores-databricks-on-aws.md
    - model-serving-with-automatic-feature-lookup-databricks-on-aws.md
    - third-party-online-stores-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - databricks-online-feature-store
    - DOFS
    - Databricks Online Feature Stores
  citations:
    - file: databricks-online-feature-stores-databricks-on-aws.md
    - file: model-serving-with-automatic-feature-lookup-databricks-on-aws.md
    - file: third-party-online-stores-databricks-on-aws.md
title: Databricks Online Feature Store
description: A high-performance, low-latency service for serving ML feature data to real-time applications, powered by Databricks Lakebase.
tags:
  - feature-store
  - machine-learning
  - real-time-inference
timestamp: "2026-06-19T18:14:05.252Z"
---

# Databricks Online Feature Store

**Databricks Online Feature Store** is a high-performance, scalable managed infrastructure for serving feature data to real-time machine learning models and online applications. It is powered by Databricks Lakebase and provides low-latency access to feature data at high scale while maintaining consistency with offline feature tables. ^[databricks-online-feature-stores-databricks-on-aws.md]

The primary use cases for Online Feature Stores include serving features to real-time applications (e.g., recommendation systems, fraud detection, personalization) using [Feature Serving Endpoints](/concepts/feature-serving-endpoint.md), and automatic feature lookup for real-time inference in [Model Serving](/concepts/model-serving.md) endpoints. ^[databricks-online-feature-stores-databricks-on-aws.md, model-serving-with-automatic-feature-lookup-databricks-on-aws.md]

New Online Feature Stores are created as Lakebase Autoscaling projects. For details on differences from previous implementations, see [Lakebase unification on Autoscaling](/concepts/lakebase-autoscaling.md). ^[databricks-online-feature-stores-databricks-on-aws.md]

## Requirements

Databricks Online Feature Stores require Databricks Runtime 16.4 LTS ML or above. You can also use [serverless compute](/concepts/serverless-gpu-compute.md). ^[databricks-online-feature-stores-databricks-on-aws.md]

To use the feature store, install the `databricks-feature-engineering` package. The following code must be executed each time a notebook is run:

```python
%pip install databricks-feature-engineering>=0.13.0
dbutils.library.restartPython()
```

^[databricks-online-feature-stores-databricks-on-aws.md]

## Creating an Online Store

When you create an online store, you provision a highly available managed infrastructure for real-time feature serving. The `create_online_store` API creates a Lakebase Autoscaling instance. ^[databricks-online-feature-stores-databricks-on-aws.md]

```python
from databricks.feature_engineering import FeatureEngineeringClient

fe = FeatureEngineeringClient()

fe.create_online_store(
    name="my-online-store",  # maximum of 63 bytes
    capacity="CU_2"  # Valid options: "CU_1", "CU_2", "CU_4", "CU_8"
)
```

The `capacity` setting controls how much compute your online store can use. Its value refers to the Lakebase Provisioned capacity. ^[databricks-online-feature-stores-databricks-on-aws.md]

### Encryption with Customer-Managed Keys

Online feature stores support encryption at rest with a customer-managed key (CMK) due to underlying support from Lakebase Autoscaling. No Lakebase or Feature Store configuration is required; CMK applies automatically for relevant workspaces when all of the following are true:

- The workspace has a customer-managed key configured for managed services.
- The online feature store is backed by a Lakebase Autoscaling project (all stores created with `fe.create_online_store` after March 23, 2026 use Lakebase Autoscaling).
- The backing Lakebase project was created after CMK support became available in your region.

^[databricks-online-feature-stores-databricks-on-aws.md]

## Managing Online Stores

You can retrieve information about existing online stores using the `list_online_stores` and `get_online_store` APIs:

```python
# List all accessible online stores
stores = fe.list_online_stores()
for store in stores:
    print(f"Store: {store.name}, State: {store.state}, Capacity: {store.capacity}")

# Get information about an existing online store
store = fe.get_online_store(name="my-online-store")
```

You can update an existing online store's capacity using `update_online_store`:

```python
updated_store = fe.update_online_store(
    name="my-online-store",
    capacity="CU_4"
)
```

^[databricks-online-feature-stores-databricks-on-aws.md]

### Adding Read Replicas

When creating or updating an online feature store, you can add read replicas by specifying the `read_replica_count` parameter. Read traffic is automatically distributed across read replicas, reducing latency and improving performance for high-concurrency workloads. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Publishing Feature Tables

After your online store is in the **AVAILABLE** state, you can publish feature tables using the `publish_table` API. This operation synchronizes data from your offline feature table to the online store. ^[databricks-online-feature-stores-databricks-on-aws.md]

### Prerequisites

All feature tables must meet these requirements before publishing:

1. **Primary key constraint**: Required for online store publishing.
2. **Non-nullable primary keys**: Primary key columns cannot contain NULL values.
3. **Change Data Feed enabled**: Required for `CONTINUOUS` and `TRIGGERED` publish modes.

^[databricks-online-feature-stores-databricks-on-aws.md]

### Publishing a Feature Table

```python
from databricks.ml_features.entities.online_store import DatabricksOnlineStore

online_store = fe.get_online_store(name="my-online-store")

fe.publish_table(
    online_store=online_store,
    source_table_name="catalog_name.schema_name.feature_table_name",
    online_table_name="catalog_name.schema_name.online_feature_table_name",
    publish_mode="TRIGGERED"  # Optional, defaults to "TRIGGERED"
)
```

The `publish_table` operation creates a table in the online store if it does not exist, syncs feature data, and sets up infrastructure for keeping the online store in sync. ^[databricks-online-feature-stores-databricks-on-aws.md]

### Publishing Modes

The `publish_mode` parameter determines how the online table is updated with changes from the offline feature table:

- **TRIGGERED**: Updates are triggered manually.
- **CONTINUOUS**: Changes are streamed continuously.

The supported modes are summarized in Sync modes explained. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Deleting an Online Table

To delete an online table, use the Databricks SDK:

```python
from databricks.sdk import WorkspaceClient

w = WorkspaceClient()
w.feature_store.delete_online_table(
    online_table_name="catalog_name.schema_name.online_feature_table_name"
)
```

This is the only recommended method for deleting an online table, as it removes the table from both Unity Catalog and the underlying database. Other methods like `DROP TABLE` or the Python SDK delete command do not remove the table from database storage. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Exploring and Querying Online Features

After publishing, you can explore and query feature data through the **Unity Catalog UI** or the **SQL Editor** for running PostgreSQL queries against online feature tables. For detailed instructions, see Query from Lakebase SQL Editor. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Using Online Features in Real-Time Applications

To serve features to real-time applications, create a feature serving endpoint. Models trained using features from Databricks automatically track lineage to those features. When deployed as endpoints, these models use [Unity Catalog](/concepts/unity-catalog.md) to find appropriate features in online stores. ^[databricks-online-feature-stores-databricks-on-aws.md]

### Automatic Feature Lookup

When you train a model using Databricks Feature Store and serve it with [Model Serving](/concepts/model-serving.md), the model automatically looks up feature values from an online store. This happens automatically with no setup required. When a scoring request comes in, Model Serving automatically retrieves the published feature values needed by the model. ^[model-serving-with-automatic-feature-lookup-databricks-on-aws.md]

Automatic feature lookup is supported for the following data types: `IntegerType`, `FloatType`, `BooleanType`, `StringType`, `DoubleType`, `LongType`, `TimestampType`, `DateType`, `ShortType`, `ArrayType`, `MapType`. ^[model-serving-with-automatic-feature-lookup-databricks-on-aws.md]

### Overriding Feature Values

To override feature values when scoring a model using a REST API, include the feature values as part of the API payload. The new feature values must conform to the feature's data type as expected by the underlying model. ^[model-serving-with-automatic-feature-lookup-databricks-on-aws.md]

### Logging Augmented DataFrames

For endpoints created starting February 2025, you can configure a model serving endpoint to log the augmented DataFrame containing looked-up feature values and function return values to the inference table. See Log feature lookup DataFrames to inference tables. ^[model-serving-with-automatic-feature-lookup-databricks-on-aws.md]

## Third-Party Online Stores

Databricks Feature Store also supports publishing to third-party online stores like Amazon DynamoDB (v0.3.8 and above). When using third-party stores, you publish feature tables to a low-latency database and deploy the model or feature spec to a REST endpoint for real-time serving. ^[model-serving-with-automatic-feature-lookup-databricks-on-aws.md, third-party-online-stores-databricks-on-aws.md]

## Cost Optimization Best Practices

- **Reuse online stores**: You can publish multiple feature tables to a single online store. For development, testing, and training scenarios, share one online store across multiple projects.
- **Right-size capacity**: Start with `CU_2` for testing and only scale up or down based on performance and cost.
- **Delete online stores not in use**: Online stores continuously incur costs. Delete stores that are no longer needed.

^[databricks-online-feature-stores-databricks-on-aws.md]

## Limitations

- Specifying a specific online table is not supported; when a feature table is published to multiple online tables, model serving resolves to the oldest one by creation timestamp.
- Up to 3 read replicas are supported (4 compute instances total, including the primary).
- Parameters `filter_condition`, `checkpoint_location`, `mode`, `trigger`, and `features` are not supported.
- Only feature tables in Unity Catalog are supported.
- Only "merge" publish mode is supported.
- Lakebase scale-to-zero is not supported.
- Feature Serving and Model Serving endpoints that look up features from multiple online stores cannot use Lakebase Autoscaling instances.
- Autoscaling instances created using the projects API or the UI do not use the `creator`, `read_replica_count`, and `capacity` fields and cannot be updated.

^[databricks-online-feature-stores-databricks-on-aws.md]

## Troubleshooting

**Error**: `Skipping publishing to online table '...' because the feature sync pipeline is already running.`

This occurs if multiple notebooks or jobs try to publish to an online table simultaneously. Only a single sync operation is allowed per online table at a time. Use `get_status()` to wait until other publish commands have finished before triggering a new publish. ^[databricks-online-feature-stores-databricks-on-aws.md]

## Related Concepts

- [Feature Engineering in Databricks](/concepts/feature-engineering-on-databricks.md)
- [Feature Serving Endpoints](/concepts/feature-serving-endpoint.md)
- Feature Function Serving
- [Feature Serving with Online Stores](/concepts/feature-serving-with-online-tables.md)
- Lakebase
- [Unity Catalog](/concepts/unity-catalog.md)
- [Model Serving](/concepts/model-serving.md)
- [MLflow](/concepts/mlflow.md)
- Online Workflows

## Sources

- databricks-online-feature-stores-databricks-on-aws.md
- model-serving-with-automatic-feature-lookup-databricks-on-aws.md
- third-party-online-stores-databricks-on-aws.md

# Citations

1. [databricks-online-feature-stores-databricks-on-aws.md](/references/databricks-online-feature-stores-databricks-on-aws-50356663.md)
2. [model-serving-with-automatic-feature-lookup-databricks-on-aws.md](/references/model-serving-with-automatic-feature-lookup-databricks-on-aws-7e249d4a.md)
3. [third-party-online-stores-databricks-on-aws.md](/references/third-party-online-stores-databricks-on-aws-33a2ab70.md)
