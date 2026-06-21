---
title: What is Unity Catalog? | Databricks on AWS
source: https://docs.databricks.com/aws/en/data-governance/unity-catalog/
ingestedAt: "2026-06-18T08:03:12.890Z"
---

Unity Catalog is the unified governance layer built into Databricks. When enabled for a workspace, Unity Catalog operates beneath every data interaction in your workspaces automatically: enforcing access control when you query a table, tracking lineage as data moves, logging activity for auditing, and more. You work with the objects Unity Catalog governs through [Catalog Explorer](https://docs.databricks.com/aws/en/catalog-explorer/), SQL, the Databricks CLI, and REST APIs.

Unity Catalog is automatically enabled for all Databricks workspaces created after November 8, 2023.

*   To verify that Unity Catalog is enabled and set up properly for your workspace, see [Unity Catalog setup guide](https://docs.databricks.com/aws/en/data-governance/unity-catalog/setup-uc).
*   If your workspace was created before November 8, 2023, see [Upgrade a Databricks workspace to Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/upgrade/).

Unity Catalog is also available as an open-source implementation. See [the announcement blog](https://www.databricks.com/blog/open-sourcing-unity-catalog) and the public [Unity Catalog GitHub repo](https://github.com/unitycatalog/unitycatalog/blob/main/README.md).

## The Unity Catalog object model[​](#the-unity-catalog-object-model "Direct link to the-unity-catalog-object-model")

Every asset you govern in Unity Catalog is modeled as a **securable object**, an object on which you can grant permissions to users, service principals, or groups. Data assets such as tables, views, volumes, functions, and models follow a three-level namespace (`catalog.schema.object`). Tables and volumes can be **managed**, where Unity Catalog handles both governance and the underlying file storage lifecycle, or **external**, where Unity Catalog handles governance only. Other objects, such as storage credentials, external locations, connections, and shares, sit directly under the metastore.

![Unity Catalog object model diagram](https://docs.databricks.com/aws/en/assets/images/object-model-40d730065eefed283b936a8664f1b247.png)

The following pages explain core Unity Catalog concepts and workflows in more detail.

*   *   [Securable objects](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects)
    *   Learn about each object type in the Unity Catalog hierarchy and how permissions apply to them.
*   *   [Managed versus external assets](https://docs.databricks.com/aws/en/data-governance/unity-catalog/managed-versus-external)
    *   Understand the difference between managed and external tables and volumes, and when to use each.
*   *   [Requirements and limitations](https://docs.databricks.com/aws/en/data-governance/unity-catalog/requirements)
    *   Review compute requirements, supported file formats, naming constraints, and known limitations.

## Unity Catalog capabilities[​](#unity-catalog-capabilities "Direct link to unity-catalog-capabilities")

Unity Catalog provides built-in tools for governing every dimension of your data and AI environment. The following topics cover the major capability areas.

*   *   [Access control](https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/)
    *   Manage who can access what using privileges, attribute-based policies, row and column filters, and workspace bindings.
*   *   [Data discovery](https://docs.databricks.com/aws/en/catalog-explorer/)
    *   Interact with securable objects using Catalog Explorer, the Databricks UI for discovering and managing data and AI assets registered in Unity Catalog.
*   *   [Data lineage](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-lineage)
    *   Automatically track how data flows and transforms from source to final views and dashboards.
*   *   [Auditing](https://docs.databricks.com/aws/en/admin/system-tables/audit-logs)
    *   Maintain a complete record of all data access and system activity using the audit log system table.
*   *   [Data classification](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-classification)
    *   Automatically classify and tag sensitive data in your catalog.
*   *   [Data quality monitoring](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/)
    *   Proactively track data health with built-in profiling and alerts that catch anomalies before they reach downstream consumers.
*   *   [Data sharing](https://docs.databricks.com/aws/en/delta-sharing/)
    *   Securely share live data and AI assets across organizations and clouds using the open OpenSharing protocol.
*   *   [AI governance](https://docs.databricks.com/aws/en/data-governance/unity-catalog/ai-governance)
    *   Govern AI assets and AI traffic using Unity Catalog and AI Gateway.

## Get started[​](#get-started "Direct link to Get started")

The following resources help you get started with Unity Catalog. If your workspace was created after November 8, 2023, it is automatically enabled with Unity Catalog.

*   *   [Get started with Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/get-started)
    *   Check if Unity Catalog is already enabled for your workspace, and configure your first catalog, schema, and data access controls.
*   *   [Upgrade to Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/upgrade/)
    *   Learn how to upgrade a workspace that is not yet using Unity Catalog.

## Additional resources[​](#additional-resources "Direct link to Additional resources")

*   [Data governance with Databricks](https://docs.databricks.com/aws/en/data-governance/)
*   [Unity Catalog best practices](https://docs.databricks.com/aws/en/data-governance/unity-catalog/best-practices)
