---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0a08ea889763afc1c3b8ccfea6f7f3c08260e2a46a9e7fe55cfb1179ed12e6ad
  pageDirectory: concepts
  sources:
    - databricks-connect-usage-requirements-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-cluster-access-modes
    - DCCAM
    - Cluster access modes
  citations:
    - file: databricks-connect-usage-requirements-databricks-on-aws.md
title: Databricks Connect Cluster Access Modes
description: Target clusters for Databricks Connect must use either Assigned or Shared cluster access mode.
tags:
  - databricks-connect
  - cluster-config
  - access-modes
timestamp: "2026-06-18T15:05:02.572Z"
---

# Databricks Connect Cluster Access Modes

**Databricks Connect Cluster Access Modes** refers to the required cluster configuration settings that allow Databricks Connect clients to connect to a Databricks cluster from their local development environment. The access mode determines how the cluster handles user isolation and shared computing resources.

## Requirements

When connecting to a cluster using Databricks Connect, the target cluster must use a cluster access mode of **Assigned** or **Shared**. These access modes are required for Databricks Connect to establish a connection and run code on the cluster. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

The specific access modes supported for Databricks Connect are:

- **Assigned**: A single-user access mode that provides dedicated cluster resources for one user.
- **Shared**: A multi-user access mode that allows multiple users to share cluster resources while maintaining isolation.

If a cluster is configured with a different access mode (such as Legacy single user or No isolation shared), Databricks Connect cannot connect to it. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

## Relationship with Compute Types

Databricks Connect supports two types of compute:

- **Cluster**: Standard Databricks clusters that support Assigned or Shared access modes.
- **Serverless compute**: A serverless compute option available starting with Databricks Connect version 15.1 that doesn't require manual cluster management.

For cluster connections, the access mode must be Assigned or Shared. Serverless compute has its own set of requirements and is supported on Databricks Connect versions 15.1 and above. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

## Version Compatibility

The Databricks Connect package version must be less than or equal to the Databricks Runtime version running on the target compute. Databricks recommends using the most recent Databricks Connect package that matches your Databricks Runtime version. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — The client library for running Spark code from local environments
- [Access Modes](/concepts/standard-access-mode.md) — Cluster configuration settings controlling user isolation and resource sharing
- Databricks Runtime Versions — Version compatibility requirements for Databricks Connect
- Serverless Compute — Serverless compute option for Databricks Connect connections
- Cluster Configuration — General cluster setup and configuration in Databricks

## Sources

- databricks-connect-usage-requirements-databricks-on-aws.md

# Citations

1. [databricks-connect-usage-requirements-databricks-on-aws.md](/references/databricks-connect-usage-requirements-databricks-on-aws-a56357da.md)
