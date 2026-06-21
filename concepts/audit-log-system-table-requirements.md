---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ed077b9581686d7218d0a57ad3ec89b3291e4777a1bb27dba955c759d0212abf
  pageDirectory: concepts
  sources:
    - audit-and-monitor-data-sharing-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - audit-log-system-table-requirements
    - ALSTR
    - Audit Log System Table
    - Audit log system table
    - audit log system table
  citations:
    - file: audit-and-monitor-data-sharing-databricks-on-aws.md
title: Audit Log System Table Requirements
description: Prerequisites for accessing OpenSharing audit logs, including enabling the audit log system table and granting access to system.access.audit for non-admin users.
tags:
  - delta-sharing
  - system-tables
  - access-control
timestamp: "2026-06-19T09:04:59.476Z"
---

# Audit Log System Table Requirements

The **Audit Log System Table** (`system.access.audit`) provides a queryable interface for audit logs in Databricks. This page describes the requirements for accessing audit logs through the system table, which is the recommended method for monitoring platform activity including OpenSharing events and other security-related actions.

## Overview

When system tables are enabled for a Databricks account, audit logs are stored in `system.access.audit`. This table allows account admins, [Metastore](/concepts/metastore.md) admins, and authorized users to run SQL queries against historical audit events. An alternative path is the Audit Log Delivery setup, which delivers logs to a cloud storage bucket; however, the system table approach offers direct queryability within Databricks. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Requirements

### Account-Level Requirement

An account admin must **enable the audit log system table** for the Databricks account. This is a prerequisite before any user can read data from `system.access.audit`. For the procedure, see the documentation on Enabling System Tables. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

### Permission Requirement

- **Account admins and [Metastore](/concepts/metastore.md) admins** automatically have access to `system.access.audit`.
- **Other users** must be explicitly granted access to `system.access.audit` to read audit logs. Without this grant, queries against the table will fail. ^[audit-and-monitor-data-sharing-databricks-on-aws.md]

> **Note**: The `system.access.audit` table is separate from any audit log delivery configuration. If your account uses audit log delivery, the logs are also written to the configured bucket, but the system table provides a queryable SQL interface.

## How to Grant Access

To grant a non-admin user access to `system.access.audit`, a [Metastore](/concepts/metastore.md) admin or account admin can run a command similar to:

```sql
GRANT SELECT ON system.access.audit TO <user-or-group>;
```

After the grant is applied, the user can query the table using standard SQL, for example:

```sql
SELECT * FROM system.access.audit WHERE event_date >= '2025-01-01';
```

Refer to the Audit log system table reference for the full schema and available columns.

## Related Concepts

- Audit Log Delivery – Alternative method to receive audit logs in cloud storage.
- OpenSharing Events – Specific audit events related to Delta Sharing.
- System Tables – General documentation for system tables in Databricks.
- [Metastore Admin](/concepts/metastore-admin-role.md) – Role that has inherent access to the audit log system table.
- [Monitoring Data Sharing](/concepts/opensharing-delta-sharing.md) – Using audit logs to monitor data provider and recipient actions.

## Sources

- audit-and-monitor-data-sharing-databricks-on-aws.md

# Citations

1. [audit-and-monitor-data-sharing-databricks-on-aws.md](/references/audit-and-monitor-data-sharing-databricks-on-aws-b723cd40.md)
