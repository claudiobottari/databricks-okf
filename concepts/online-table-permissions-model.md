---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fbee6c5530bd35f5f658dacba49eda61e5d7db1442ce4b5ab83e3d147827ea88
  pageDirectory: concepts
  sources:
    - databricks-online-tables-legacy-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - online-table-permissions-model
    - OTPM
  citations:
    - file: databricks-online-tables-legacy-databricks-on-aws.md
title: Online Table Permissions Model
description: Required Unity Catalog privileges (SELECT, USE CATALOG, USE SCHEMA, CREATE TABLE, REFRESH) and the automatic service principal created for endpoints.
tags:
  - databricks
  - permissions
  - unity-catalog
timestamp: "2026-06-18T15:09:05.357Z"
---

# Online Table Permissions Model

The **Online Table Permissions Model** defines the set of Unity Catalog privileges required to create, manage, and access online tables in Databricks, including the automatic service principal mechanism used by serving endpoints to query online table data independently of the user who created the resource. Delta tables must have a primary key to create an online table. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## User Permissions for Creating and Managing Online Tables

### Prerequisites

The Unity Catalog [Metastore](/concepts/metastore.md) must have Privilege Model Version 1.0 enabled for online table creation. ^[databricks-online-tables-legacy-databricks-on-aws.md]

### Required Privileges to Create an Online Table

To create an online table, a user must have the following permissions: ^[databricks-online-tables-legacy-databricks-on-aws.md]

| Permission | Scope | Purpose |
|------------|-------|---------|
| `SELECT` | Source table | Read data from the source Delta table to sync to the online table |
| `USE CATALOG` | Destination catalog | Access the catalog where the online table will be created |
| `USE SCHEMA` | Destination schema | Access the schema where the online table will be created |
| `CREATE TABLE` | Destination schema | Create the online table in the destination schema |

### Required Privileges to Manage the Synchronization Pipeline

To manage the data synchronization pipeline of an online table (including triggering updates or viewing pipeline status), a user must either be the owner of the online table or be granted the `REFRESH` privilege on the online table. ^[databricks-online-tables-legacy-databricks-on-aws.md]

### Visibility

Users who do not have `USE CATALOG` and `USE SCHEMA` privileges on the catalog will not see the online table in Catalog Explorer. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Endpoint Permission Model

### Automatic Service Principal Creation

When a [Feature Serving Endpoint](/concepts/feature-serving-endpoint.md) or [Model Serving Endpoint](/concepts/model-serving-endpoint.md) is created, Databricks automatically creates a unique service principal with limited permissions required to query data from online tables. ^[databricks-online-tables-legacy-databricks-on-aws.md]

This service principal allows the endpoint to access data independently of the user who created the resource. This design ensures that the endpoint can continue to function if the creator leaves the workspace. ^[databricks-online-tables-legacy-databricks-on-aws.md]

### Service Principal Lifecycle

The lifetime of the service principal is tied to the lifetime of the serving endpoint. When the endpoint is deleted, the corresponding service principal is also removed. ^[databricks-online-tables-legacy-databricks-on-aws.md]

### Audit Logging

Audit logs may indicate system-generated records for the owner of the Unity Catalog catalog granting necessary privileges to the serving endpoint's service principal. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Feature Serving Endpoint Owner Requirements

To create a feature serving endpoint that serves data from an online table, the user who creates the endpoint must be the owner of both the offline source table and the online table. ^[databricks-online-tables-legacy-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The data governance platform that provides the permission framework for online tables
- Feature Serving — Serving endpoints that use online tables for low-latency feature lookups
- [Model Serving](/concepts/model-serving.md) — Model serving endpoints that automatically look up features from online tables
- [Online Tables](/concepts/online-tables.md) — The read-only, row-oriented copies of Delta tables designed for online access
- [ABAC GRANT Policy](/concepts/abac-grant-policy.md) — Attribute-based access control policies that can grant privileges dynamically
- [Feature Engineering Client](/concepts/featureengineeringclient-api.md) — API client used to create feature specs that link to online tables

## Sources

- databricks-online-tables-legacy-databricks-on-aws.md

# Citations

1. [databricks-online-tables-legacy-databricks-on-aws.md](/references/databricks-online-tables-legacy-databricks-on-aws-a40fbf23.md)
