---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fb814c0126bf38d47a4e611486eb0c384580e1ff6bb50d5380a9831fef82476d
  pageDirectory: concepts
  sources:
    - databricks-connect-usage-requirements-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-requirement-for-databricks-connect
    - UCRFDC
  citations:
    - file: databricks-connect-usage-requirements-databricks-on-aws.md
title: Unity Catalog Requirement for Databricks Connect
description: To use Databricks Connect, the Databricks account and workspace must have Unity Catalog enabled.
tags:
  - databricks-connect
  - unity-catalog
  - prerequisites
timestamp: "2026-06-18T15:05:48.286Z"
---

# Unity Catalog Requirement for Databricks Connect

**Unity Catalog Requirement for Databricks Connect** refers to the mandatory condition that a Databricks workspace must have [Unity Catalog](/concepts/unity-catalog.md) enabled in order to use [Databricks Connect](/concepts/databricks-connect.md) for connecting client applications to the workspace. This requirement applies to all Databricks Connect usage for Databricks Runtime 13.3 LTS and above. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

## Overview

Databricks Connect enables developers to connect their local development environments to Databricks compute resources and run Spark code remotely. A prerequisite for this connection is that the target workspace must have Unity Catalog enabled at both the account and workspace levels. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

## Workspace Requirements

To use Databricks Connect, the following workspace conditions must be met: ^[databricks-connect-usage-requirements-databricks-on-aws.md]

- The Databricks account and workspace must have Unity Catalog enabled. For setup guidance, see the documentation on [getting started with Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/get-started) and [enabling a workspace for Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/enable-workspaces). ^[databricks-connect-usage-requirements-databricks-on-aws.md]
- The Databricks Runtime version of the target compute (cluster or serverless compute) must be greater than or equal to the Databricks Connect package version. Databricks recommends using the most recent Databricks Connect package that matches the Databricks Runtime version. ^[databricks-connect-usage-requirements-databricks-on-aws.md]
- For connecting to [serverless compute](/concepts/serverless-gpu-compute.md), the workspace must also meet the [requirements for serverless compute](https://docs.databricks.com/aws/en/compute/serverless/#requirements). Serverless compute is supported starting with Databricks Connect version 15.1. ^[databricks-connect-usage-requirements-databricks-on-aws.md]
- For connecting to a cluster, the target cluster must use a cluster access mode of **Assigned** or **Shared**. See the documentation on [access modes](https://docs.databricks.com/aws/en/compute/configure#access-mode). ^[databricks-connect-usage-requirements-databricks-on-aws.md]

## Feature Interdependence

The Unity Catalog requirement for Databricks Connect reflects the broader platform direction where Unity Catalog serves as the central governance layer for data and AI assets. This requirement ensures consistent access control, [Data Lineage](/concepts/data-lineage.md), and metadata management across both Databricks-native and external client connections.^[databricks-connect-usage-requirements-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — The client library for connecting local applications to Databricks clusters
- [Unity Catalog](/concepts/unity-catalog.md) — The unified governance solution for data and AI assets
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) — The runtime environment used with Databricks Connect
- OAuth Authentication for Databricks — Authentication methods supported by Databricks Connect
- Serverless Compute on Databricks — The serverless compute option for Databricks Connect

## Sources

- databricks-connect-usage-requirements-databricks-on-aws.md

# Citations

1. [databricks-connect-usage-requirements-databricks-on-aws.md](/references/databricks-connect-usage-requirements-databricks-on-aws-a56357da.md)
