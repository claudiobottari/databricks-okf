---
title: Get started with Unity Catalog | Databricks on AWS
source: https://docs.databricks.com/aws/en/data-governance/unity-catalog/get-started
ingestedAt: "2026-06-18T08:04:33.971Z"
---

Unity Catalog is the unified governance layer for data and AI in Databricks. It provides centralized access control, lineage, auditing, and data discovery across your workspaces. See [What is Unity Catalog?](https://docs.databricks.com/aws/en/data-governance/unity-catalog/).

Unity Catalog is automatically enabled for all Databricks workspaces created after November 8, 2023. If your workspace already has Unity Catalog enabled, follow the setup tutorial. If your workspace predates Unity Catalog or was not enabled at creation, follow the upgrade guide.

*   *   [Unity Catalog setup guide](https://docs.databricks.com/aws/en/data-governance/unity-catalog/setup-uc)
    *   For workspaces with Unity Catalog already enabled. Configure admin roles, users, compute, permissions, and catalogs.
*   *   [Upgrade to Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/upgrade/)
    *   For existing workspaces not yet on Unity Catalog. Enable Unity Catalog and migrate your data.

## Extend your Unity Catalog setup[​](#extend-your-unity-catalog-setup "Direct link to extend-your-unity-catalog-setup")

After your workspace is set up, you can apply more advanced governance capabilities to your data and AI workflows.

### Attribute-based access control[​](#attribute-based-access-control "Direct link to Attribute-based access control")

[Attribute-based access control (ABAC)](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/) lets you define dynamic, fine-grained access policies based on attributes of the data and the user accessing it. Instead of managing permissions table by table, you write policies that automatically enforce row-level filtering and column-level masking. For example, you can hide sensitive columns from users outside a specific region or mask PII for non-privileged roles.

![ABAC column masking in action](https://docs.databricks.com/aws/en/assets/images/abac-column-masking-results-8e6ab5cb50a4885c92a470a8e6dc77de.png)

### Data classification[​](#data-classification "Direct link to Data classification")

[Data classification](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-classification) uses an AI agent to automatically scan your catalog and tag sensitive data such as PII, financial information, and credentials. After classification, tags can integrate directly with ABAC policies, allowing you to apply governance controls based on what the data actually contains rather than managing access object by object.

![Data classification results](https://docs.databricks.com/aws/en/assets/images/data-classification-results-page-d72a16748a065ed0ac6a9a81ed84590c.png)

### Data quality monitoring[​](#data-quality-monitoring "Direct link to Data quality monitoring")

[Data quality monitoring](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/) provides anomaly detection across all tables in a schema and data profiling at the table level. Anomaly detection automatically monitors freshness and completeness using historical data patterns, surfacing issues without manual configuration. Data profiling captures statistical distributions over time, enabling you to track data integrity and set alerts for unexpected changes.

![Data quality monitoring dashboard](https://docs.databricks.com/aws/en/assets/images/metastore-data-quality-dashboard-9d194085ce5d7c9ccba7dff860d7988a.png)

### Data lineage[​](#data-lineage "Direct link to Data lineage")

[Data lineage](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-lineage) automatically captures how data flows across tables, notebooks, jobs, and pipelines — down to the column level. You can trace the origin of any column, see what downstream assets depend on it, and understand the full impact of a schema change before making it.

![Column-level data lineage](https://docs.databricks.com/aws/en/assets/images/uc-column-lineage-c8dfa626d400501fd428b1606ad74e7c.png)

### AI governance with Unity AI Gateway[​](#ai-governance-with-unity-ai-gateway "Direct link to ai-governance-with-unity-ai-gateway")

[Unity AI Gateway](https://docs.databricks.com/aws/en/ai-gateway/) extends Unity Catalog governance to AI. It provides enterprise governance for LLM endpoints, agents, and MCP servers, allowing you to implement access control, audit logging, and observability across all AI interactions in a unified UI.

For a complete overview of Unity Catalog capabilities, see [What is Unity Catalog?](https://docs.databricks.com/aws/en/data-governance/unity-catalog/). For governance best practices, see [Unity Catalog best practices](https://docs.databricks.com/aws/en/data-governance/unity-catalog/best-practices).
