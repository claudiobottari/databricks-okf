---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bffa57c267e31f9501de4c3bd100e6de5a88dcfc1fcb8332805b9f5c44ad330f
  pageDirectory: concepts
  sources:
    - get-started-with-unity-catalog-databricks-on-aws.md
    - what-is-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - unity-catalog
    - Unity Catalog ABAC
    - Unity Catalog CLI
    - Unity Catalog Tag
    - Unity Catalog Tags
    - Unity Catalog UDF
    - Unity Catalog UDFs
    - Unity Catalog tags
    - Catalog
    - Catalogs
    - Enable Unity Catalog
    - Unity Catalog function
    - Unity Catalog table
    - What is Unity Catalog?
    - catalogs
    - data catalog
    - unity-catalog-overview
    - UCO
    - Unity Catalog Views
    - Unity Catalog view
  citations:
    - file: what-is-unity-catalog-databricks-on-aws.md
    - file: get-started-with-unity-catalog-databricks-on-aws.md
title: Unity Catalog
description: The unified governance layer for data and AI in Databricks, providing centralized access control, lineage, auditing, and data discovery across workspaces.
tags:
  - data-governance
  - databricks
  - catalog
timestamp: "2026-06-19T19:00:46.224Z"
---

# Unity Catalog

**Unity Catalog** is the unified governance layer built into Databricks. It provides centralized access control, lineage, auditing, and data discovery across all workspaces, operating automatically beneath every data interaction. Unity Catalog is automatically enabled for all Databricks workspaces created after November 8, 2023, and is also available as an open-source implementation via the [Unity Catalog GitHub repository](https://github.com/unitycatalog/unitycatalog). ^[what-is-unity-catalog-databricks-on-aws.md]

Users interact with Unity Catalog–governed objects through [Catalog Explorer](/concepts/catalog-explorer.md), SQL, the Databricks CLI, and REST APIs. ^[what-is-unity-catalog-databricks-on-aws.md]

## Object model

Every asset governed in Unity Catalog is modeled as a **securable object** — an object on which permissions can be granted to users, service principals, or groups. Data assets such as tables, views, volumes, functions, and models follow a three‑level namespace: `catalog.schema.object`. ^[what-is-unity-catalog-databricks-on-aws.md]

Tables and volumes can be **managed**, where Unity Catalog handles both governance and the underlying file storage lifecycle, or **external**, where Unity Catalog handles governance only. Other objects — storage credentials, external locations, connections, and shares — sit directly under the [Metastore](/concepts/metastore.md). ^[what-is-unity-catalog-databricks-on-aws.md]

For more detail, see Securable objects and [Managed versus external assets](/concepts/managed-vs-external-assets-in-unity-catalog.md).

## Capabilities

Unity Catalog provides built‑in tools for governing every dimension of data and AI:

- **Access control** — Manage permissions using privileges, [attribute‑based access control (ABAC)](/concepts/attribute-based-access-control-abac.md), row and column filters, and workspace bindings. ABAC lets you define dynamic policies that automatically enforce row‑level filtering and column‑level masking. ^[get-started-with-unity-catalog-databricks-on-aws.md]
- **Data classification** — An AI agent automatically scans catalogs and tags sensitive data such as PII, financial information, and credentials. Tags can integrate directly with ABAC policies. ^[get-started-with-unity-catalog-databricks-on-aws.md]
- **Data quality monitoring** — Provides anomaly detection across all tables in a schema and data profiling at the table level. Anomaly detection monitors freshness and completeness using historical patterns; profiling captures statistical distributions over time. ^[get-started-with-unity-catalog-databricks-on-aws.md]
- **Data lineage** — Automatically captures how data flows across tables, notebooks, jobs, and pipelines, down to the column level. Users can trace column origins and understand downstream impact before making schema changes. ^[get-started-with-unity-catalog-databricks-on-aws.md]
- **Auditing** — Maintains a complete record of all data access and system activity using the audit log system table. ^[what-is-unity-catalog-databricks-on-aws.md]
- **Data sharing** — Securely shares live data and AI assets across organizations and clouds using the open OpenSharing protocol ([Delta Sharing](/concepts/delta-sharing.md)). ^[what-is-unity-catalog-databricks-on-aws.md]
- **AI governance** — [Unity AI Gateway](/concepts/unity-ai-gateway.md) extends Unity Catalog governance to AI, providing enterprise governance for LLM endpoints, agents, and MCP servers, including access control, audit logging, and observability. ^[get-started-with-unity-catalog-databricks-on-aws.md, what-is-unity-catalog-databricks-on-aws.md]

## Getting started

If your workspace was created after November 8, 2023, Unity Catalog is already enabled. Follow the Unity Catalog setup guide to configure admin roles, users, compute, permissions, and catalogs. For existing workspaces not yet using Unity Catalog, see the [Upgrade to Unity Catalog](/concepts/upgrading-jobs-to-unity-catalog.md) guide. ^[get-started-with-unity-catalog-databricks-on-aws.md]

For governance best practices, see Unity Catalog best practices.

## Sources

- what-is-unity-catalog-databricks-on-aws.md
- get-started-with-unity-catalog-databricks-on-aws.md

# Citations

1. [what-is-unity-catalog-databricks-on-aws.md](/references/what-is-unity-catalog-databricks-on-aws-ea58b0e9.md)
2. [get-started-with-unity-catalog-databricks-on-aws.md](/references/get-started-with-unity-catalog-databricks-on-aws-3c48b4d4.md)
