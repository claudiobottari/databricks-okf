---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 86e779d27989e56a190296d0267a97a022b6305dbdf3b6019915648eff567d6f
  pageDirectory: concepts
  sources:
    - read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md
  confidence: 0.93
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - shared-views-in-databricks-to-databricks-sharing
    - SVIDS
    - views
  citations:
    - file: read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md
title: Shared Views in Databricks-to-Databricks Sharing
description: Shared views have specific restrictions including limited built-in function support, a 20-view query limit across at most 5 provider-shares, and a 5-minute query timeout for on-the-fly materialization without direct access.
tags:
  - delta-sharing
  - views
  - limitations
timestamp: "2026-06-19T20:07:33.898Z"
---

# Shared Views in Databricks‑to‑Databricks Sharing

**Shared Views** are read‑only logical tables that a provider makes available to a recipient using the [Databricks-to-Databricks OpenSharing](/concepts/databricks-to-databricks-sharing.md) protocol. Recipients query shared views just like shared tables, with a specific set of restrictions and behaviors that differ from table sharing. ^[read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md]

## Overview

When a provider shares a view, the recipient’s workspace must meet the same requirements as for any [Databricks-to-Databricks Sharing](/concepts/databricks-to-databricks-sharing.md)—the workspace must be enabled for [Unity Catalog](/concepts/unity-catalog.md). After a catalog is created from the share (or the share is mounted to an existing catalog), recipients with the appropriate privileges can query the view using Catalog Explorer, notebooks, SQL queries, the CLI, or REST APIs. ^[read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md]

The data in shared views is **read‑only** (`SELECT` privilege). Updates made by the provider are reflected in near real time, though column changes may take up to one minute to appear in Catalog Explorer. ^[read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md]

## Permissions Required

To query a shared view, a user must have the `SELECT` privilege on the view (inherited from the catalog or schema) and the `USE CATALOG` privilege on the catalog that contains the view. The catalog owner or a [Metastore](/concepts/metastore.md) admin can grant these privileges following the standard [Unity Catalog privilege hierarchy](/concepts/privileges-and-ownership.md). ^[read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md]

## How to Read a Shared View

Reading a shared view follows the same procedure as reading a shared table:

1. A privileged user creates a catalog from the provider’s share (via Catalog Explorer, SQL, or CLI).
2. That user or an admin grants you the `SELECT` privilege on the view.
3. You query the view using three‑level namespace: `catalog.schema.view`.

You can also use the view in transactions, subject to the transaction requirements and limitations of Databricks‑to‑Databricks sharing. ^[read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md]

## Limitations and Restrictions

Shared views in Databricks‑to‑Databricks sharing have several unique constraints:

### 1. Supported Functions and Operators

Shared views support only a subset of built‑in functions and operators in Databricks. See the official list of functions supported in Databricks-to-Databricks view sharing. ^[read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md]

### 2. Query Limits

- A single query can reference **no more than 20 shared views**.
- Those shared views must come from **no more than five different provider shares**. ^[read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md]

### 3. Dependent Views Restriction

When the provider is from the same account, or when you use **serverless compute** in a different account, you cannot query multiple dependent views from the same provider in a single query. For example, if `view1` depends on `view2` on the provider side and both are shared, a query that references both `view1` and `view2` will fail. ^[read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md]

### 4. Query Result Timeout

If the recipient does not have direct access to the underlying tables, Databricks performs **on‑the‑fly materialization** when the view is queried. If this materialization takes longer than **5 minutes**, the query times out. To avoid this limitation, switch to **serverless compute**. ^[read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md]

### 5. History and Streaming

- You **cannot** query history (time travel) on a shared view.
- You **cannot** use a shared view as a source for Spark Structured Streaming. ^[read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md]

## Naming Requirements

The catalog name you choose for the shared catalog that contains the view **must be different** from any catalog name in the provider’s [Metastore](/concepts/metastore.md) that holds a table referenced by the view. If the names collide, the query results in a namespace conflict error. For example, if the provider has a `test` catalog containing a table referenced in the view, and you also name your shared catalog `test`, the query will fail. ^[read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md]

## Cost

Sharing costs for queries on views are computed in the same way as for shared tables. See how OpenSharing costs are computed. ^[read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md]

## Related Concepts

- [Databricks-to-Databricks OpenSharing](/concepts/databricks-to-databricks-sharing.md)
- Shared Tables
- Shared Volumes
- [Unity Catalog](/concepts/unity-catalog.md)
- Serverless Compute
- Transaction requirements for OpenSharing
- Functions supported in Databricks-to-Databricks view sharing

## Sources

- read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md

# Citations

1. [read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md](/references/read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws-21150d4f.md)
