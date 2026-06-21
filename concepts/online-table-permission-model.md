---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d1f1a05f47fbd80043c14097c7c8816c8901b0b36ff959ea8a9f253e4cd9ea05
  pageDirectory: concepts
  sources:
    - databricks-online-tables-legacy-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - online-table-permission-model
    - OTPM
  citations:
    - file: databricks-online-tables-legacy-databricks-on-aws.md
title: Online Table Permission Model
description: Permission requirements for creating and managing online tables, including SELECT/USE_CATALOG/CREATE_TABLE privileges, REFRESH privilege, and an auto-created service principal for endpoints.
tags:
  - databricks
  - security
  - permissions
  - unity-catalog
timestamp: "2026-06-19T09:53:39.563Z"
---

## Online Table Permission Model

The **Online Table Permission Model** governs how access is controlled for [Online Tables](/concepts/online-tables.md) in Databricks, including the permissions required to create, manage, and consume them. Online tables are read-only, row-oriented copies of Delta tables that provide low-latency access for [Model Serving](/concepts/model-serving.md), Feature Serving, and [retrieval-augmented generation](/concepts/retrieval-augmented-generation-rag.md) (RAG) applications. ^[databricks-online-tables-legacy-databricks-on-aws.md]

### Required Permissions for Creating an Online Table

To create an online table, a user must have the following Unity Catalog privileges:

- `SELECT` privilege on the source Delta table. ^[databricks-online-tables-legacy-databricks-on-aws.md]
- `USE CATALOG` privilege on the destination catalog. ^[databricks-online-tables-legacy-databricks-on-aws.md]
- `USE SCHEMA` and `CREATE TABLE` privilege on the destination schema. ^[databricks-online-tables-legacy-databricks-on-aws.md]

The Unity Catalog [Metastore](/concepts/metastore.md) must have Privilege Model Version 1.0 (the current privilege model). ^[databricks-online-tables-legacy-databricks-on-aws.md]

### Managing the Online Table

To manage the data synchronization pipeline of an online table, a user must either be the owner of the online table or have the `REFRESH` privilege on it. Users without `USE CATALOG` and `USE SCHEMA` privileges on the catalog do not see the online table in Catalog Explorer. ^[databricks-online-tables-legacy-databricks-on-aws.md]

### Endpoint Permission Model

A unique service principal is automatically created for each [Feature Serving Endpoint](/concepts/feature-serving-endpoint.md) or [Model Serving Endpoint](/concepts/model-serving-endpoint.md) that consumes an online table. This service principal is granted the limited permissions needed to query data from online tables. It operates independently of the user who created the resource and is designed so that the endpoint continues to function even if the creator leaves the workspace. The lifetime of this service principal equals the lifetime of the endpoint. ^[databricks-online-tables-legacy-databricks-on-aws.md]

Audit logs may show system-generated records for the owner of the Unity Catalog catalog granting the necessary privileges to this service principal. ^[databricks-online-tables-legacy-databricks-on-aws.md]

### Federation and External Access

When using [Lakehouse Federation](/concepts/lakehouse-federation-data-sharing.md) to query online tables, only `SELECT` (read) operations are supported. Access requires a Serverless SQL warehouse. This capability is intended for interactive or debugging purposes only and must not be used for production or mission-critical workloads. ^[databricks-online-tables-legacy-databricks-on-aws.md]

### Related Concepts

- [Unity Catalog permissions](/concepts/unity-catalog-permissions-model.md) — The broader permission system for Unity Catalog objects.
- Online table creation — The process of creating an online table via the UI or APIs.
- Feature serving endpoint permissions — Permissions for serving features from online tables.
- Privilege Model Version — The Unity Catalog privilege model version required for online tables.

### Sources

- databricks-online-tables-legacy-databricks-on-aws.md

# Citations

1. [databricks-online-tables-legacy-databricks-on-aws.md](/references/databricks-online-tables-legacy-databricks-on-aws-a40fbf23.md)
