---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4814ce511cd6658dbe6714fe525454db448d17c089b5050e64d927cca1f2b9c0
  pageDirectory: concepts
  sources:
    - example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - publish-table-to-online-store
    - PTTOS
  citations:
    - file: example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md
title: Publish Table to Online Store
description: The process of synchronizing a Delta table from Unity Catalog to a Databricks Online Feature Store for low-latency feature serving.
tags:
  - feature-store
  - data-publishing
  - databricks
timestamp: "2026-06-19T10:25:24.002Z"
---

#Publish Table to Online Store

**Publish Table to Online Store** refers to the process of making a Delta table’s feature data available for low‑latency serving by publishing it to a [Databricks Online Feature Store](/concepts/databricks-online-feature-store.md). This enables real‑time inference workloads to retrieve features quickly without scanning the full source table. ^[example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md]

## Overview

The workflow involves three main phases: creating a source feature table in [Unity Catalog](/concepts/unity-catalog.md), creating an online store instance, and publishing the table to that online store. Once published, the features can be served through a [Feature Serving Endpoint](/concepts/feature-serving-endpoint.md) and used in online predictions. ^[example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md]

## Steps

### 1. Create the source feature table

First, use the [Feature Engineering Client](/concepts/featureengineeringclient-api.md) (`FeatureEngineeringClient`) to create a feature table in Unity Catalog. The table must have a primary key and contain precomputed feature values. ^[example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md]

```python
from databricks.feature_engineering import FeatureEngineeringClient

fe = FeatureEngineeringClient()
fe.create_table(
    name=feature_table_name,
    primary_keys="destination_id",
    df=destination_location_df,
    description="Destination location features."
)
```

### 2. Enable Change Data Feed

[Change Data Feed (CDF)](/concepts/delta-change-data-feed-cdf.md) must be enabled on the source table to support both `CONTINUOUS` and `TRIGGERED` publish modes. This allows the online store to stay synchronized with changes in the source table. ^[example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md]

```sql
ALTER TABLE feature_table_name SET TBLPROPERTIES (delta.enableChangeDataFeed = 'true')
```

### 3. Create an online store

Create an online store with a specified capacity. The capacity determines the throughput and cost of the store. Valid capacity options are `"CU_1"`, `"CU_2"`, `"CU_4"`, and `"CU_8"`. ^[example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md]

```python
online_store_name = f"{username}-online-store"
fe.create_online_store(
    name=online_store_name,
    capacity="CU_2"
)
```

Wait until the online store’s state becomes `AVAILABLE` before proceeding. ^[example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md]

```python
online_store = fe.get_online_store(name=online_store_name)
online_store.state
```

### 4. Publish the table

Publish the source table to the online store using `fe.publish_table()`. The method references the online store, the source table name, and the desired online table name. ^[example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md]

```python
published_table = fe.publish_table(
    online_store=online_store,
    source_table_name=feature_table_name,
    online_table_name=online_table_name
)
```

After publishing, the online store contains the feature data and can be used by a [Feature Spec](/concepts/featurespec.md) to serve features to endpoints.

## Next steps

Once the table is published, you typically create a [FeatureSpec](/concepts/featurespec.md) that combines feature lookups with on‑demand functions, then deploy a [Feature Serving Endpoint](/concepts/feature-serving-endpoint.md) for low‑latency inference. ^[example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md]

## Related concepts

- [Online Feature Store](/concepts/online-feature-store.md)
- [Feature Engineering Client](/concepts/featureengineeringclient-api.md)
- [Feature Serving Endpoint](/concepts/feature-serving-endpoint.md)
- [FeatureSpec](/concepts/featurespec.md)
- [Change Data Feed](/concepts/delta-change-data-feed-cdf.md)
- [Unity Catalog](/concepts/unity-catalog.md)

## Sources

- example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md

# Citations

1. [example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws.md](/references/example-deploy-and-query-a-feature-serving-endpoint-databricks-on-aws-69370e1c.md)
