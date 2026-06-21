---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 136df26de7d8f2506f927c4e60dc4f2dd8bd1500d1de18411f5771e34c50f398
  pageDirectory: concepts
  sources:
    - databricks-feature-store-overview-and-glossary-databricks-on-aws.md
    - example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md
    - use-features-in-online-workflows-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - online-feature-store
    - OFS
    - Online Feature Stores
    - Online Store
    - Online Stores
    - Online store
    - online store
  citations:
    - file: databricks-feature-store-overview-and-glossary-databricks-on-aws.md
    - file: example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md
    - file: migrate-from-legacy-and-third-party-online-tables-databricks-on-aws.md
title: Online Feature Store
description: A high-performance, low-latency serving layer for real-time ML inference, powered by Databricks Lakebase, that syncs feature tables from the offline store.
tags:
  - feature-store
  - real-time
  - serving
timestamp: "2026-06-19T18:13:23.653Z"
---



# Online Feature Store

The **Online Feature Store** is a high-performance, scalable solution for serving feature data to real-time applications and machine learning models. Powered by Databricks Lakebase, it provides low-latency access to pre-computed features while maintaining governance, lineage, and consistency with offline feature tables. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

## Overview

In a typical machine learning workflow, features are computed and stored in offline feature tables backed by Delta tables in [Unity Catalog](/concepts/unity-catalog.md). For real-time serving scenarios — such as [Model Serving](/concepts/model-serving.md) endpoints — these features must be accessible with low latency (typically milliseconds). The Online Feature Store addresses this by providing a dedicated serving infrastructure that can be provisioned and scaled independently. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

At inference time, the model serving endpoint automatically uses entity IDs from the request data to look up pre-computed features from the online store. The endpoint uses Unity Catalog to resolve lineage from the served model to the features used to train the model, and tracks lineage to the online feature store for real-time access. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

## Architecture

The Online Feature Store is built on the serverless Lakebase platform. Key architectural components include:

- **Online Store instances**: Provisioned instances with configurable capacity (`CU_1`, `CU_2`, `CU_4`, `CU_8`) that serve feature data with low latency. ^[example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md]
- **Published tables**: Unity Catalog tables that are synchronized from offline feature tables to the online store, maintaining full lineage tracking to source tables. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]
- **Read-replicas**: Additional copies of online store data for scaling read capacity. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

## Workflow

### 1. Create an Online Store

You provision an online store instance with a specified capacity level. The instance transitions through states until it becomes `AVAILABLE` for use. ^[example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md]

```python
from databricks.feature_engineering import FeatureEngineeringClient

fe = FeatureEngineeringClient()

online_store = fe.create_online_store(
    name="my-online-store",
    capacity="CU_2"
)
```

### 2. Publish a Feature Table

After creating the online store, you publish a Unity Catalog feature table to it. The source table must have [Change Data Feed](/concepts/delta-change-data-feed-cdf.md) enabled to support continuous or triggered publish modes. ^[example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md]

```python
published_table = fe.publish_table(
    online_store=online_store,
    source_table_name="catalog.schema.feature_table",
    online_table_name="catalog.schema.online_feature_table"
)
```

### 3. Create a Feature Spec

A [FeatureSpec](/concepts/featurespec.md) defines the features to serve and any on-demand functions to apply at inference time. It combines [FeatureLookup](/concepts/featurelookup.md) references from feature tables and [FeatureFunction](/concepts/featurefunction.md) references for real-time computation. ^[example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md]

```python
from databricks.feature_engineering import FeatureLookup, FeatureFunction

features = [
    FeatureLookup(
        table_name="catalog.schema.feature_table",
        lookup_key="entity_id"
    ),
    FeatureFunction(
        udf_name="catalog.schema.distance_function",
        output_name="distance",
        input_bindings={
            "latitude": "latitude",
            "longitude": "longitude",
            "user_latitude": "user_latitude",
            "user_longitude": "user_longitude"
        }
    )
]

fe.create_feature_spec(name="catalog.schema.my_spec", features=features)
```

### 4. Deploy a Feature Serving Endpoint

The feature serving endpoint serves the feature spec, making features available for real-time queries. You can create endpoints using the UI, REST API, or Databricks SDK. ^[example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md]

```python
from databricks.sdk import WorkspaceClient
from databricks.sdk.service.serving import EndpointCoreConfigInput, ServedEntityInput

workspace = WorkspaceClient()

endpoint = workspace.serving_endpoints.create_and_wait(
    name="my-feature-endpoint",
    config=EndpointCoreConfigInput(
        served_entities=[
            ServedEntityInput(
                entity_name="catalog.schema.my_spec",
                scale_to_zero_enabled=True,
                workload_size="Small"
            )
        ]
    )
)
```

### 5. Query the Endpoint

When querying the endpoint, you provide the primary key values and any context data required by on-demand functions. The endpoint returns the requested feature values with low latency. ^[example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md]

```python
import mlflow.deployments

client = mlflow.deployments.get_deploy_client("databricks")

response = client.predict(
    endpoint="my-feature-endpoint",
    inputs={
        "dataframe_records": [
            {"entity_id": 1, "user_latitude": 37, "user_longitude": -122},
            {"entity_id": 2, "user_latitude": 37, "user_longitude": -122},
        ]
    }
)
```

## On-Demand Feature Computation

The Online Feature Store supports on-demand feature computation through [FeatureFunction](/concepts/featurefunction.md)s. This is useful when a feature depends on information only available at inference time — such as a user's current location or the current timestamp. The function is registered in Unity Catalog and applied to the retrieved features at query time. ^[example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md]

## Streaming

In addition to batch publishing, the Online Feature Store supports streaming feature tables from the offline store to the online store. This enables near-real-time updates to feature values as new data arrives. You can write feature values to a feature table from a streaming source, and feature computation code can utilize [Structured Streaming](/concepts/structured-streaming-on-shared-tables.md) to transform raw data streams into features. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

## Governance and Lineage

Online feature tables are Unity Catalog entities that natively track lineage to their source offline tables. This ensures that governance policies apply consistently across both offline and online serving. The lineage information is visible in Catalog Explorer and can be used for auditing and compliance. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

## Best Practices

- **Enable Change Data Feed** on source tables to support continuous and triggered publish modes. ^[example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md]
- **Choose appropriate capacity** based on expected query volume and latency requirements. Start with a lower capacity and scale up as needed. ^[example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md]
- **Use [FeatureSpec](/concepts/featurespec.md)s** to define reusable feature sets that can be shared across multiple models and endpoints. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]
- **Create a single online store per workspace** for testing and proof of concept; provision additional stores for production or isolation requirements. ^[migrate-from-legacy-and-third-party-online-tables-databricks-on-aws.md]

## Related Concepts

- [Feature Store](/concepts/feature-store.md) — The centralized repository for feature management
- [Feature Tables](/concepts/feature-tables.md) — Delta tables with primary keys that store feature data
- [FeatureSpec](/concepts/featurespec.md) — A Unity Catalog entity defining a reusable set of features for serving
- [FeatureLookup](/concepts/featurelookup.md) — Specifies which features to use from a feature table
- [FeatureFunction](/concepts/featurefunction.md) — On-demand computation for features requiring real-time inputs
- Feature Serving — Deploying feature specs as serving endpoints
- [Model Serving](/concepts/model-serving.md) — Real-time model inference using online features
- [Unity Catalog](/concepts/unity-catalog.md) — Governance layer providing lineage and access control
- Third-Party Online Stores — Alternative online serving infrastructure

## Sources

- databricks-feature-store-overview-and-glossary-databricks-on-aws.md
- example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md
- migrate-from-legacy-and-third-party-online-tables-databricks-on-aws.md

# Citations

1. [databricks-feature-store-overview-and-glossary-databricks-on-aws.md](/references/databricks-feature-store-overview-and-glossary-databricks-on-aws-368c726e.md)
2. [example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md](/references/example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws-69370e1c.md)
3. [migrate-from-legacy-and-third-party-online-tables-databricks-on-aws.md](/references/migrate-from-legacy-and-third-party-online-tables-databricks-on-aws-4e5cf207.md)
