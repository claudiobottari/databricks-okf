---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ea914d7fba6752cc3695076022e9fa9789c6298dcf48b12519640eafa3403246
  pageDirectory: concepts
  sources:
    - migrate-from-legacy-and-third-party-online-tables-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - online-feature-store-databricks
    - OFS(
    - Feature Store on Databricks
    - Feature Store in Databricks
  citations:
    - file: migrate-from-legacy-and-third-party-online-tables-databricks-on-aws.md
title: Online Feature Store (Databricks)
description: A managed feature store that serves feature tables to model and feature serving endpoints, replacing legacy online tables for ML serving.
tags:
  - machine-learning
  - feature-store
  - serving
timestamp: "2026-06-19T19:33:32.984Z"
---

# Online Feature Store (Databricks)

**Online Feature Store** is a Databricks feature that provides low-latency serving of feature data for [Model Serving](/concepts/model-serving.md) and Feature Serving endpoints. It serves as a replacement for legacy online tables, offering improved performance and scalability for production machine learning workloads. ^[migrate-from-legacy-and-third-party-online-tables-databricks-on-aws.md]

## Overview

The Online Feature Store stores feature tables in a format optimized for real-time serving. When you publish feature tables to the online store, Databricks automatically synchronizes data from your offline feature tables, making it available for low-latency lookups during model inference. ^[migrate-from-legacy-and-third-party-online-tables-databricks-on-aws.md]

## Creating an Online Store

Databricks recommends creating a single online store per workspace for testing and proof of concept. For production use cases or isolation requirements, you can provision additional stores. ^[migrate-from-legacy-and-third-party-online-tables-databricks-on-aws.md]

```python
from databricks.feature_engineering import FeatureEngineeringClient

fe = FeatureEngineeringClient()

# Create a single online store that can support multiple feature tables
fe.create_online_store(
    name="online-feature-store",
    capacity="CU_2"
)
```

^[migrate-from-legacy-and-third-party-online-tables-databricks-on-aws.md]

## Migrating to Online Feature Store

When migrating from legacy online tables to the Online Feature Store, you must redeploy your serving endpoints with the `FEATURE_SOURCE` environment variable set to `DATABRICKS_ONLINE_STORE` on each served entity. This can be configured through the serving endpoint UI under **Advanced configuration > Environment variables**, or by using the REST API. ^[migrate-from-legacy-and-third-party-online-tables-databricks-on-aws.md]

After you publish your feature tables to the Online Feature Store, any subsequent change to your serving endpoints — including scaling operations — automatically switches them to use the Online Feature Store as the default source. Ensure your downstream systems are prepared for this change before publishing. ^[migrate-from-legacy-and-third-party-online-tables-databricks-on-aws.md]

## Verification

To verify a successful migration, check the endpoint events for messages containing `Linked to Online Feature Store table: "table name"`. This confirms that the serving endpoint is using the new online store. ^[migrate-from-legacy-and-third-party-online-tables-databricks-on-aws.md]

## Cleaning Up Legacy Resources

After migrating to the Online Feature Store and verifying that endpoints are functioning correctly, you can delete legacy online tables. This can be done through the UI by selecting **Delete** from the kebab menu on the online table page, or programmatically using the Databricks SDK: ^[migrate-from-legacy-and-third-party-online-tables-databricks-on-aws.md]

```python
w.online_tables.delete('main.default.my_online_table')
```

Deleting the online table stops any ongoing data synchronization and releases all its resources. ^[migrate-from-legacy-and-third-party-online-tables-databricks-on-aws.md]

## Related Concepts

- [Feature Engineering](/concepts/featureengineeringclient-api.md) — The process of creating and managing feature tables
- [Model Serving](/concepts/model-serving.md) — Endpoints that serve machine learning models with online features
- Feature Serving — Endpoints that serve feature data directly
- [Lakebase Synced Tables](/concepts/lakebase-synced-table.md) — Alternative migration target for OLTP workloads
- [Databricks Feature Store](/concepts/databricks-feature-store.md) — The overall feature management platform

## Sources

- migrate-from-legacy-and-third-party-online-tables-databricks-on-aws.md

# Citations

1. [migrate-from-legacy-and-third-party-online-tables-databricks-on-aws.md](/references/migrate-from-legacy-and-third-party-online-tables-databricks-on-aws-4e5cf207.md)
