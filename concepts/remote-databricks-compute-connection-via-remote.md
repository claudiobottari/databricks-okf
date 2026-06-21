---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ce1524a6a311e0ede69d0a2970ef602281441cb20358eab3268bbd8b9cdc3fb3
  pageDirectory: concepts
  sources:
    - databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - remote-databricks-compute-connection-via-remote
    - RDCCVR
    - Remote Databricks compute
  citations:
    - file: databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md
title: Remote Databricks compute connection via remote()
description: DatabricksSession.builder.remote() allows connecting to Databricks compute that is not attached to the current notebook or job, using keyword arguments or configuration methods like host(), token(), etc.
tags:
  - databricks
  - connectivity
  - remote
timestamp: "2026-06-19T14:47:22.120Z"
---

# Remote Databricks compute connection via remote()

**Remote Databricks compute connection via `remote()`** is a method provided by [Databricks Connect](/concepts/databricks-connect.md) that allows code running inside a Databricks notebook or job to connect to a separate Databricks compute resource that is not attached to the current notebook or job. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

## Overview

When using Databricks Connect within a Databricks notebook or job, the `remote()` function enables connections to external compute resources. This is particularly useful for scenarios where code needs to access a different cluster or serverless compute than the one to which the notebook is currently attached. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

## Usage

The `remote()` function accepts configuration parameters as keyword arguments (*kwargs*) or through individual configuration methods such as `host()` or `token()`. When `remote()` is called, a new [DatabricksSession](/concepts/databrickssession.md) is created for the referenced compute, similar to how Databricks Connect behaves when used outside of a notebook or job environment. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

## Behavior

When `remote()` is used inside a Databricks notebook or job, it does not use the default Spark session (accessible through the `spark` variable). Instead, it creates a completely new session that connects to the specified remote compute resource. This is distinct from the standard behavior where `DatabricksSession.builder.getOrCreate()` returns the default Spark session. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — The framework that enables connecting to Databricks compute from local and remote environments.
- [DatabricksSession](/concepts/databrickssession.md) — The session object used to interact with Databricks compute resources.
- [Remote Databricks compute](/concepts/remote-databricks-compute-connection-via-remote.md) — Compute resources that are not directly attached to the current notebook or job.
- [DatabricksSession.builder](/concepts/databrickssession-builder-api.md) — The builder pattern used to configure and create [DatabricksSession](/concepts/databrickssession.md) instances.

## Sources

- databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md

# Citations

1. [databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md](/references/databricks-connect-support-in-databricks-notebooks-databricks-on-aws-dd50e122.md)
