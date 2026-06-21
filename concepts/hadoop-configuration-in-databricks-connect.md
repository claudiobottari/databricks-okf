---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bcf1f53b4e6955e24519a9c127210b934cbef95aa0168c02fbaa9183a8292b09
  pageDirectory: concepts
  sources:
    - migrate-to-databricks-connect-for-python-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - hadoop-configuration-in-databricks-connect
    - HCIDC
  citations:
    - file: migrate-to-databricks-connect-for-python-databricks-on-aws.md
title: Hadoop Configuration in Databricks Connect
description: How Hadoop configurations are managed in Databricks Connect, including the distinction between spark.conf.set (per-session) and sparkContext configurations (cluster-wide).
tags:
  - databricks
  - hadoop
  - configuration
timestamp: "2026-06-19T19:34:22.310Z"
---

## Hadoop Configuration in Databricks Connect

When working with [Databricks Connect](/concepts/databricks-connect.md), setting Hadoop Configuration requires careful consideration of where and how the configuration is applied. The client and the cluster treat configuration changes differently, depending on whether they are set via `spark.conf.set` or through `SparkContext`. ^[migrate-to-databricks-connect-for-python-databricks-on-aws.md]

### Using `spark.conf.set`

On the client, Hadoop configurations can be set using the `spark.conf.set` API. This approach applies the configuration to SQL and DataFrame operations only. It is session‑scoped and does not affect the entire cluster. ^[migrate-to-databricks-connect-for-python-databricks-on-aws.md]

### Using `SparkContext` (Cluster‑Level)

Hadoop configurations set on `SparkContext` are **not** tied to user sessions but apply to the entire cluster. Because of this, such configurations must be set in the cluster configuration or inside a notebook, not from the Databricks Connect client. Attempting to set them via `SparkContext` from the client will not work as expected. ^[migrate-to-databricks-connect-for-python-databricks-on-aws.md]

### Migration Implications

When migrating to Databricks Connect for Databricks Runtime 13.3 LTS and above, any existing code that previously set Hadoop configurations via `SparkContext` should be adjusted to either use `spark.conf.set` (if the configuration applies only to SQL/DataFrame operations) or be moved to the cluster’s Spark configuration (if cluster‑wide scope is required). ^[migrate-to-databricks-connect-for-python-databricks-on-aws.md]

### Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md)
- SparkSession
- PySpark
- Hadoop configuration properties
- Cluster configuration in Databricks

### Sources

- migrate-to-databricks-connect-for-python-databricks-on-aws.md

# Citations

1. [migrate-to-databricks-connect-for-python-databricks-on-aws.md](/references/migrate-to-databricks-connect-for-python-databricks-on-aws-5b63ea6f.md)
