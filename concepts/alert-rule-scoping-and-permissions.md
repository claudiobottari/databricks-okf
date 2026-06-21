---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 463bd673fe81697bd9340fcb88296da5d8907cb5489ee33b8e1dedde2b975cdc
  pageDirectory: concepts
  sources:
    - alerts-for-anomaly-detection-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - alert-rule-scoping-and-permissions
    - Permissions and Alert Rule Scoping
    - ARSAP
  citations:
    - file: alerts-for-anomaly-detection-databricks-on-aws.md
title: Alert Rule Scoping and Permissions
description: Alert rules in Databricks Data Quality Monitoring are scoped to a catalog or schema, with MANAGE privilege required on the scoped object to create or manage rules.
tags:
  - databricks
  - authorization
  - rbac
  - alerting
timestamp: "2026-06-19T13:59:05.383Z"
---

```markdown
---
title: Alert Rule Scoping and Permissions
summary: Alert rules in Databricks Data Quality Monitoring are scoped to a catalog or specific schema, and require the MANAGE privilege on the target catalog or schema to create or manage.
sources:
  - alerts-for-anomaly-detection-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T14:24:15.696Z"
updatedAt: "2026-06-19T08:57:30.655Z"
tags:
  - databricks
  - permissions
  - scoping
  - unity-catalog
aliases:
  - alert-rule-scoping-and-permissions
  - Permissions and Alert Rule Scoping
  - ARSAP
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Alert Rule Scoping and Permissions

**Alert Rule Scoping and Permissions** refers to how alert rules for [[anomaly detection]] in [[Unity Catalog]] are configured to monitor tables within a specific catalog or schema, and the [[MANAGE privilege]] required to create and manage those rules. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Scoping

Alert rules are scoped to a **catalog** or a **specific schema**. When a monitored table within the rule's scope becomes unhealthy, each recipient receives one email per important unhealthy table. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

- **Catalog-level alert**: covers every schema in the selected catalog.  
- **Schema-level alert**: covers only the selected schema.

Scoping determines which tables are monitored and which users can create or manage the rule. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Required Permissions

The privileges required to create or manage an alert rule depend on the rule's scope: ^[alerts-for-anomaly-detection-databricks-on-aws.md]

| Scope | Required Privilege |
|-------|-------------------|
| Schema | `MANAGE` on the schema |
| Catalog | `MANAGE` on the catalog |

Only workspace users with the corresponding `MANAGE` privilege can create, edit, or delete an alert rule at that scope. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Creating and Managing Alerts

### Data Quality Monitoring UI (Beta)

In the [[Data Quality Monitoring]] UI, alert rules are created and managed from the **Manage alerts** popover. Users with the appropriate `MANAGE` privilege can: ^[alerts-for-anomaly-detection-databricks-on-aws.md]

- Create a new alert by selecting a catalog, a specific schema (or "All Schemas"), and one or more workspace users to notify by email.  
- Edit an existing alert's scope and recipients.  
- Delete an alert.

The UI is accessible from a schema's **Details** tab in Catalog Explorer after data quality monitoring is enabled. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

### Databricks SQL Alerts

An alternative approach is to create an alert using [[Databricks SQL alerts]] by querying the system table `system.data_quality_monitoring.table_results`. By default, only account admins can access this table. Other users who need to configure SQL-based alerts must be granted appropriate access to the system table. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Related Concepts

- [[Anomaly detection]] – The underlying detection mechanism that triggers alerts
- [[Data Quality Monitoring]] – The UI and system for monitoring table health
- [[Unity Catalog]] – The governance framework where alerts are scoped
- System tables – The backend tables used for SQL-based alerts
- [[Databricks SQL alerts]] – The alerting framework used for SQL-based anomaly alerts

## Sources

- alerts-for-anomaly-detection-databricks-on-aws.md
```

# Citations

1. [alerts-for-anomaly-detection-databricks-on-aws.md](/references/alerts-for-anomaly-detection-databricks-on-aws-037caaff.md)
