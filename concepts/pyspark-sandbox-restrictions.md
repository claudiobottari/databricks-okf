---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 116865334121fe504e6fd59d14800bcd592a5b6190dbe425954490d4b4ff6eff
  pageDirectory: concepts
  sources:
    - enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - pyspark-sandbox-restrictions
    - PSR
  citations:
    - file: enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md
title: PySpark Sandbox Restrictions
description: Security restrictions applied to user code when Python and SQL table access control is enabled, including low-privilege users, filesystem restrictions, and network port limitations.
tags:
  - databricks
  - security
  - pyspark
  - sandbox
timestamp: "2026-06-19T10:21:00.447Z"
---

# PySpark Sandbox Restrictions

**PySpark Sandbox Restrictions** are security constraints enforced on clusters with Python and SQL table access control enabled in the legacy Hive [Metastore](/concepts/metastore.md). These restrictions limit user capabilities to prevent unauthorized data access through the cluster.

## Overview

When Python and SQL table access control is enabled on a cluster, users are restricted to using only the Spark SQL API or DataFrame API. All commands must run on cluster nodes as a low-privilege user who is forbidden from accessing sensitive parts of the filesystem or creating network connections to unauthorized ports. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

## Key Restrictions

### API Limitations

Users can only access Spark using the Spark SQL API or DataFrame API. In both cases, access to tables and views is restricted by administrators according to the Databricks privileges granted on Hive [Metastore](/concepts/metastore.md) objects. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

### Network Restrictions

Users are forbidden from creating network connections to ports other than 80 and 443. Only built-in Spark functions can create network connections on these restricted ports. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

### JDBC Connector Restrictions

Only workspace admin users or users with the `ANY FILE` privilege can read data from external databases through the PySpark JDBC connector. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

### Outbound Port Configuration

If Python processes need access to additional outbound ports, administrators can set the Spark configuration `spark.databricks.pyspark.iptable.outbound.whitelisted.ports` to specify allowed ports. The supported format is `[port[:port][,port[:port]]...]`, for example: `21,22,9000:9999`. Ports must be within the valid range of 0-65535. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

## Enforcement

Attempts to bypass these restrictions will fail with an exception. These restrictions are in place to ensure that users can never access unprivileged data through the cluster. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

## Related Concepts

- [Hive Metastore Table Access Control](/concepts/hive-metastore-table-access-control.md) — The parent security framework that enables these restrictions
- [Hive Metastore Privileges and Securable Objects](/concepts/hive-metastore-privileges-and-securable-objects.md) — The privilege system that governs data access
- [Table Access Control Cluster Configuration](/concepts/table-access-control-cluster-configuration.md) — How to enable table access control on clusters
- [SQL-only Table Access Control](/concepts/sql-only-table-access-control.md) — A stricter variant that restricts users to SQL commands only
- [ANY FILE Privilege](/concepts/any-file-securable.md) — A special privilege that bypasses certain sandbox restrictions

## Sources

- enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md

# Citations

1. [enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md](/references/enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws-9c6f8fe1.md)
