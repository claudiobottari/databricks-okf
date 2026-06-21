---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e490a9b3501df1c89eb3d0d9e83b39807d1591e84a8caaba840d03215a9a4986
  pageDirectory: concepts
  sources:
    - get-started-with-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-enablement
    - UCE
    - UNITY_CATALOG_NOT_ENABLED
  citations:
    - file: get-started-with-unity-catalog-databricks-on-aws.md
title: Unity Catalog Enablement
description: The process of enabling Unity Catalog in Databricks workspaces, which is automatic for workspaces created after November 8, 2023, and requires manual upgrade for older workspaces.
tags:
  - databricks
  - setup
  - migration
timestamp: "2026-06-19T19:01:04.791Z"
---

# Unity Catalog Enablement

**Unity Catalog Enablement** refers to the process of activating and configuring [Unity Catalog](/concepts/unity-catalog.md)—the unified governance layer for data and AI in Databricks—within a workspace. It provides centralized access control, lineage, auditing, and data discovery across all workspaces in an organization. ^[get-started-with-unity-catalog-databricks-on-aws.md]

## Automatic Enablement

Unity Catalog is automatically enabled for all Databricks workspaces created after November 8, 2023. If your workspace was created after this date, Unity Catalog is ready to use and you can proceed with the setup tutorial. ^[get-started-with-unity-catalog-databricks-on-aws.md]

## Enabling Unity Catalog in Existing Workspaces

For workspaces that predate November 8, 2023, or that were not enabled at creation time, Unity Catalog must be manually enabled and configured. Databricks provides two different paths depending on the current state of the workspace: ^[get-started-with-unity-catalog-databricks-on-aws.md]

- **Unity Catalog setup guide** – Use this guide if your workspace already has Unity Catalog enabled. It walks through configuring admin roles, users, compute, permissions, and catalogs. ^[get-started-with-unity-catalog-databricks-on-aws.md]
- **Upgrade to Unity Catalog** – Use this guide for existing workspaces not yet on Unity Catalog. It covers enabling Unity Catalog and migrating your existing data. ^[get-started-with-unity-catalog-databricks-on-aws.md]

## Extending Governance After Enablement

Once Unity Catalog is active, administrators can apply advanced governance capabilities to data and AI workflows: ^[get-started-with-unity-catalog-databricks-on-aws.md]

- **[Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md)** – Define dynamic, fine-grained access policies based on attributes of the data and the user. ABAC supports row-level filtering and column-level masking without managing permissions table by table. ^[get-started-with-unity-catalog-databricks-on-aws.md]
- **[Data Classification](/concepts/data-classification.md)** – Use an AI agent to automatically scan your catalog and tag sensitive data such as PII, financial information, and credentials. Tags can integrate with ABAC policies to apply governance based on data content. ^[get-started-with-unity-catalog-databricks-on-aws.md]
- **[Data Quality Monitoring](/concepts/data-quality-monitoring.md)** – Provides anomaly detection for freshness and completeness across all tables in a schema, plus table-level data profiling that tracks statistical distributions over time. ^[get-started-with-unity-catalog-databricks-on-aws.md]
- **[Data Lineage](/concepts/data-lineage.md)** – Automatically captures how data flows across tables, notebooks, jobs, and pipelines down to the column level, enabling impact analysis before schema changes. ^[get-started-with-unity-catalog-databricks-on-aws.md]
- **[Unity AI Gateway](/concepts/unity-ai-gateway.md)** – Extends Unity Catalog governance to AI by providing enterprise governance for LLM endpoints, agents, and MCP servers with access control, audit logging, and observability. ^[get-started-with-unity-catalog-databricks-on-aws.md]

For a complete overview, see the page on [What is Unity Catalog?](/concepts/unity-catalog.md). For governance best practices, refer to Unity Catalog best practices. ^[get-started-with-unity-catalog-databricks-on-aws.md]

## Sources

- get-started-with-unity-catalog-databricks-on-aws.md

# Citations

1. [get-started-with-unity-catalog-databricks-on-aws.md](/references/get-started-with-unity-catalog-databricks-on-aws-3c48b4d4.md)
