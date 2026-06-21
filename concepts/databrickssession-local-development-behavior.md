---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 76991183b18949611ddf372afd7faa9350743a6e17a734198f4570c387c1cfc0
  pageDirectory: concepts
  sources:
    - databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databrickssession-local-development-behavior
    - DLDB
  citations:
    - file: databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md
title: DatabricksSession local development behavior
description: In local IDE environments, getOrCreate() reuses existing sessions while create() always creates new sessions with connection params from code, env vars, or config files
tags:
  - local-development
  - session
  - databricks
timestamp: "2026-06-19T18:10:48.593Z"
---

# [DatabricksSession](/concepts/databrickssession.md) Local Development Behavior

The **DatabricksSession local development behavior** describes how `DatabricksSession` creates and manages Spark sessions when running code locally in an IDE outside of Databricks, as part of the [Databricks Connect](/concepts/databricks-connect.md) framework.

## Session Creation

When running code locally within an IDE outside of Databricks, `DatabricksSession.builder.getOrCreate()` checks for an existing Spark session for the provided configuration. If a session already exists, it returns that session; if no session exists, it creates a new one. In contrast, `DatabricksSession.builder.create()` always creates a new Spark session, regardless of whether an existing session is available. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

## Connection Parameters

Connection parameters such as `host`, `token`, and `cluster_id` are populated from one of three sources: the source code directly, environment variables, or the `.databrickscfg` configuration profiles file. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

## Key Difference from Workspace Behavior

A notable distinction exists between local development and Databricks workspace behavior. When running code locally via Databricks Connect, calling `DatabricksSession.builder.create()` twice creates two separate and distinct sessions. This differs from workspace behavior where `getOrCreate()` without additional configuration returns the pre-configured default Spark session. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — The framework enabling local development connections to Databricks compute
- [DatabricksSession workspace behavior](/concepts/databrickssession-workspace-behavior.md) — How sessions behave when running in notebooks and jobs
- Databricks Runtime 13.3 LTS and above — The runtime versions supporting this functionality
- .databrickscfg configuration file — The configuration profiles file used for connection settings

## Sources

- databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md

# Citations

1. [databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md](/references/databricks-connect-support-in-databricks-notebooks-databricks-on-aws-dd50e122.md)
