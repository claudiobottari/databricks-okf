---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f8d2658ffef1a2c0fe8ab13f03153dd14cdff9f4b3902cd24acf7a35fb03abbd
  pageDirectory: concepts
  sources:
    - databricks-online-tables-legacy-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - online-table-permissions-and-security-model
    - Security Model and Online Table Permissions
    - OTPASM
  citations:
    - file: databricks-online-tables-legacy-databricks-on-aws.md
title: Online Table Permissions and Security Model
description: Permission requirements for creating and managing online tables, including Unity Catalog privileges and the automatic service principal model that enables endpoints to access data independently of the creating user.
tags:
  - databricks
  - permissions
  - security
  - unity-catalog
timestamp: "2026-06-19T18:14:29.423Z"
---

# Online Table Permissions and Security Model

The **Online Table Permissions and Security Model** defines the access control requirements and security mechanisms for creating, managing, and serving data from [Online Tables](/concepts/online-tables.md) on Databricks. Online tables are read-only, row-oriented copies of Delta Tables optimized for low-latency online access, and their security model spans user permissions, service principal management, and endpoint-level access controls.

## User Permissions for Creating Online Tables

To create an online table, a user must have the following Unity Catalog privileges:

- `SELECT` privilege on the source Delta table.
- `USE CATALOG` privilege on the destination catalog where the online table will be created.
- `USE SCHEMA` and `CREATE TABLE` privilege on the destination schema.

^[databricks-online-tables-legacy-databricks-on-aws.md]

The Unity Catalog [Metastore](/concepts/metastore.md) must be using Privilege Model Version 1.0 for online table permissions to function correctly. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Managing Online Table Permissions

To manage the data synchronization pipeline of an online table, a user must either be the **owner** of the online table or be granted the `REFRESH` privilege on the online table. Users who do not have `USE CATALOG` and `USE SCHEMA` privileges on the catalog will not see the online table in Catalog Explorer. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Endpoint Permission Model

When a [Feature Serving Endpoint](/concepts/feature-serving-endpoint.md) or [Model Serving Endpoint](/concepts/model-serving-endpoint.md) is created to serve data from online tables, a unique **service principal** is automatically created for that endpoint. This service principal has limited permissions — only those required to query data from the associated online tables. ^[databricks-online-tables-legacy-databricks-on-aws.md]

This design ensures that endpoints can access data independently of the user who created the resource. The endpoint continues to function even if the creator leaves the workspace. The lifetime of this service principal matches the lifetime of the endpoint — when the endpoint is deleted, the service principal is also removed. ^[databricks-online-tables-legacy-databricks-on-aws.md]

Audit logs may indicate system-generated records for the owner of the Unity Catalog catalog granting necessary privileges to this service principal. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Feature Serving Endpoint Requirements

When creating a feature serving endpoint that uses online tables, the user performing the operation must be the **owner** of both the offline Delta table and the online table. The feature spec used to create the endpoint references the source Delta table, and the serving endpoint automatically uses the online table for low-latency feature lookups during inference. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer that enforces online table permissions.
- [Feature Serving Endpoint](/concepts/feature-serving-endpoint.md) — REST API endpoint that serves features from online tables.
- [Model Serving](/concepts/model-serving.md) — Serving infrastructure that automatically looks up features from online tables.
- Service Principal — Automatically created identity for endpoint-to-online-table access.
- [Delta Change Data Feed](/concepts/delta-change-data-feed-cdf.md) — Required for triggered or continuous sync modes.

## Sources

- databricks-online-tables-legacy-databricks-on-aws.md

# Citations

1. [databricks-online-tables-legacy-databricks-on-aws.md](/references/databricks-online-tables-legacy-databricks-on-aws-a40fbf23.md)
