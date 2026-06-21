---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4d1422fb1b6a39102ee9307af5159b2c010c395c9c33954a192c33e7545fcb28
  pageDirectory: concepts
  sources:
    - audit-and-monitor-data-sharing-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - audit-log-access-requirements
    - ALAR
  citations:
    - file: audit-and-monitor-data-sharing-databricks-on-aws.md
title: Audit Log Access Requirements
description: Prerequisites for accessing OpenSharing audit logs, including enabling system tables, account admin privileges, and access to system.access.audit.
tags:
  - audit-logging
  - access-control
  - databricks
timestamp: "2026-06-18T10:49:31.228Z"
---

# Audit Log Access Requirements

To view audit logs for OpenSharing events (such as recipient queries and share management actions), both data providers and recipients must meet certain access prerequisites. These requirements ensure that only authorized principals can read log data, and that the underlying logging infrastructure is enabled.^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Prerequisites

- An **account admin** must enable the audit log system table for your Databricks account. This step activates the `system.access.audit` table where audit events are stored. See Enable system tables.^[audit-and-monitor-data-sharing-databricks-on-aws.md]
- If you are **not an account admin or a [Metastore](/concepts/metastore.md) admin**, you must be explicitly granted access to `system.access.audit` to read the audit logs.^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Alternative audit log delivery

If your account uses an audit log delivery setup instead of (or in addition to) the system table, you need to know the bucket and path where the logs are delivered in order to access them.^[audit-and-monitor-data-sharing-databricks-on-aws.md]

## Related concepts

- [Account Admin (Unity Catalog)](/concepts/account-admin-unity-catalog.md) – the role responsible for enabling system tables and managing metastores.
- [Metastore admin](/concepts/metastore-admin-role.md) – a role that can also grant access to `system.access.audit`.
- [Audit log system table](/concepts/audit-log-system-table-requirements.md) – the reference for the `system.access.audit` schema and querying patterns.
- System tables – the broader feature that provides system‑level data for audit, billing, and other purposes.

## Sources

- audit-and-monitor-data-sharing-databricks-on-aws.md

# Citations

1. [audit-and-monitor-data-sharing-databricks-on-aws.md](/references/audit-and-monitor-data-sharing-databricks-on-aws-b723cd40.md)
