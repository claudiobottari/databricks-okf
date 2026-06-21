---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: aa5cd8241e8fe9302b918ca83ac1201e9c5fda84d435c232d1e064df9a79a59b
  pageDirectory: concepts
  sources:
    - publish-features-to-a-third-party-online-store-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - drop-published-online-table
    - DPOT
  citations:
    - file: publish-features-to-a-third-party-online-store-databricks-on-aws.md
title: Drop Published Online Table
description: The drop_online_table() operation to delete a published table from an online store provider, along with irreversible warning about downstream dependencies and the suggested key-rotation safety practice.
tags:
  - feature-store
  - data-management
  - cleanup
timestamp: "2026-06-19T20:00:08.398Z"
---

# Drop Published Online Table

**Drop Published Online Table** refers to the operation of deleting a feature table that has been published from Databricks Feature Store to a third-party online store, such as Amazon DynamoDB, Amazon RDS, or other supported online stores. This operation is performed using the `drop_online_table()` method and removes both the table data from the online store provider and the associated metadata from Databricks. ^[publish-features-to-a-third-party-online-store-databricks-on-aws.md]

## Overview

The `drop_online_table()` function enables users to clean up published feature tables from online stores. This capability is available in Feature Store client v0.12.0 and above, for both the Feature Engineering in Unity Catalog client and the Workspace Feature Store client. ^[publish-features-to-a-third-party-online-store-databricks-on-aws.md]

## Operation Details

When you call `drop_online_table()`, the system performs two actions:

1. Deletes the published table from the online store provider (e.g., DynamoDB, MySQL, PostgreSQL)
2. Removes the online store metadata from Databricks

^[publish-features-to-a-third-party-online-store-databricks-on-aws.md]

### Syntax

The basic syntax for dropping a published online table is:

```python
fe.drop_online_table( # or fs.drop_online_table for Workspace Feature Store
  name='recommender_system.customer_features',
  online_store=online_store)
```

^[publish-features-to-a-third-party-online-store-databricks-on-aws.md]

## Important Considerations

### Scope of Deletion

The `drop_online_table()` operation **only deletes the published table from the online store**. It does **not** delete the original feature table stored in Databricks. The offline feature table in your Databricks catalog remains intact and available for future use. ^[publish-features-to-a-third-party-online-store-databricks-on-aws.md]

### Irreversibility

The deletion is permanent and cannot be undone. Once executed, the data is removed from the online store, and any downstream services that depend on this table for feature lookups will fail. ^[publish-features-to-a-third-party-online-store-databricks-on-aws.md]

### Dependency Check

Before deleting a published table, you should verify it has no downstream dependencies. Specifically, ensure that:

- The table is not used for [Model Serving](/concepts/model-serving.md) feature lookups
- The table is not referenced by any other production systems

^[publish-features-to-a-third-party-online-store-databricks-on-aws.md]

### Recommended Safe Deletion Practice

Databricks recommends a cautious approach before executing `drop_online_table()`:

> To check for any dependencies, consider rotating the keys for the published table you plan to delete for a day before you execute `drop_online_table`.

This practice helps identify any active consumers of the table by observing if any services fail after key rotation, before proceeding with the permanent deletion. ^[publish-features-to-a-third-party-online-store-databricks-on-aws.md]

## Related Operations

- Publish Features to a Third-Party Online Store — The operation to publish feature tables to online stores in the first place
- [Feature Engineering in Unity Catalog](/concepts/feature-engineering-in-unity-catalog.md) — The newer client for managing feature tables
- [Workspace Feature Store](/concepts/workspace-feature-store-ui.md) — The original workspace-scoped feature store client
- [Feature Lookup](/concepts/feature-lookup.md) — The mechanism by which models retrieve features from online stores during serving

## API Availability

The `drop_online_table()` method is available in both:

- `databricks.feature_engineering` (Feature Engineering in Unity Catalog) — `fe.drop_online_table()`
- `databricks.feature_store` (Workspace Feature Store) — `fs.drop_online_table()`

^[publish-features-to-a-third-party-online-store-databricks-on-aws.md]

## Sources

- publish-features-to-a-third-party-online-store-databricks-on-aws.md

# Citations

1. [publish-features-to-a-third-party-online-store-databricks-on-aws.md](/references/publish-features-to-a-third-party-online-store-databricks-on-aws-a5573cf3.md)
