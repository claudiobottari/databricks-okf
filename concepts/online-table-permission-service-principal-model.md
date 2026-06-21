---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1af5ef5628bce312d08e94e2acd86a25183567b1e97ef517e23d2386163d78bb
  pageDirectory: concepts
  sources:
    - databricks-online-tables-legacy-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - online-table-permission-service-principal-model
    - OTP&SPM
  citations:
    - file: databricks-online-tables-legacy-databricks-on-aws.md
title: Online Table Permission & Service Principal Model
description: A unique auto-generated service principal for each serving endpoint that allows autonomous data access from online tables, independent of the user who created the resource, with the principal lifetime tied to the endpoint lifetime.
tags:
  - databricks
  - security
  - permissions
  - service-principal
timestamp: "2026-06-19T14:52:19.901Z"
---

## Online Table Permission & Service Principal Model

The **Online Table Permission & Service Principal Model** defines the access control rules and automated identity management used when creating, managing, and serving online tables on Databricks. Online tables are read‑only, row‑oriented copies of Delta tables designed for low‑latency lookups from Model Serving, Feature Serving, or RAG applications. Understanding the permission model is essential for administrators and developers who set up real‑time feature or model endpoints.

### User Permissions for Online Tables

To create an online table, a user must hold the following Unity Catalog privileges:

- `SELECT` privilege on the source table.
- `USE CATALOG` privilege on the destination catalog.
- `USE SCHEMA` and `CREATE TABLE` privileges on the destination schema. ^[databricks-online-tables-legacy-databricks-on-aws.md]

In addition, the Unity Catalog [Metastore](/concepts/metastore.md) must use [Privilege Model Version 1.0](https://docs.databricks.com/aws/en/archive/unity-catalog/upgrade-privilege-model). ^[databricks-online-tables-legacy-databricks-on-aws.md]

### Management Permissions

Once an online table exists, managing its data synchronization pipeline (e.g., triggering updates or viewing status) requires either:

- Ownership of the online table, or
- The `REFRESH` privilege granted on the online table.

Users who do not possess `USE CATALOG` and `USE SCHEMA` privileges on the catalog will not be able to see the online table in Catalog Explorer. ^[databricks-online-tables-legacy-databricks-on-aws.md]

### Endpoint Permission Model

When a [Feature Serving Endpoint](/concepts/feature-serving-endpoint.md) or [Model Serving Endpoint](/concepts/model-serving-endpoint.md) is created to serve data from online tables, Databricks automatically provisions a unique service principal for that endpoint. This service principal has limited permissions — only those required to query data from the associated online tables. ^[databricks-online-tables-legacy-databricks-on-aws.md]

**Key characteristics:**

- **Autonomy:** The service principal allows the endpoint to access data independently of the user who created the resource. This ensures the endpoint continues to function even if the creator leaves the workspace. ^[databricks-online-tables-legacy-databricks-on-aws.md]
- **Lifetime:** The service principal lives as long as the endpoint exists. When the endpoint is deleted, the service principal is also removed. ^[databricks-online-tables-legacy-databricks-on-aws.md]
- **Auditability:** Audit logs may record system‑generated entries showing the Unity Catalog owner granting necessary privileges to this service principal. ^[databricks-online-tables-legacy-databricks-on-aws.md]

**Additional constraint:** The user who creates a feature serving endpoint must be the owner of both the offline Delta table and the online table. ^[databricks-online-tables-legacy-databricks-on-aws.md]

### Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) – The underlying governance system for permissions.
- [Feature Serving Endpoint](/concepts/feature-serving-endpoint.md) – REST API for low‑latency feature lookups.
- [Model Serving](/concepts/model-serving.md) – Real‑time inference with automatic feature lookup.
- Service Principal – Automated identity used by endpoints.
- REFRESH Privilege – Permission to trigger online table updates.

### Sources

- databricks-online-tables-legacy-databricks-on-aws.md

# Citations

1. [databricks-online-tables-legacy-databricks-on-aws.md](/references/databricks-online-tables-legacy-databricks-on-aws-a40fbf23.md)
