---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 051f26ce2aaa7b05e2402e7da5927a2b3937e355bd43a842e77a4816b67ec712
  pageDirectory: concepts
  sources:
    - databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-remote-method
    - DCRM
  citations:
    - file: databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md
title: Databricks Connect remote() method
description: The remote() method allows connecting to Databricks compute not attached to the notebook or job using explicit configuration
tags:
  - remote-connection
  - api
  - databricks
timestamp: "2026-06-19T18:11:07.880Z"
---

# Databricks Connect `remote()` method

The `remote()` method in [Databricks Connect](/concepts/databricks-connect.md) provides a way to create a new Spark session that connects to a different Databricks compute resource than the one currently attached to a notebook or job. This allows you to work with multiple compute targets from within a single notebook session.

## Overview

`DatabricksSession.remote()` takes configuration keyword arguments or individual configuration methods (such as `host()` or `token()`) to specify the target compute. When invoked, it creates a new session for the referenced compute, similar to how Databricks Connect operates when used outside of a Databricks notebook or job. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

## Purpose

The primary use case for `remote()` is to connect to Databricks compute that is **not** attached to the current notebook or job. This enables you to develop, debug, and test code against one compute resource while running your analysis against another, all from within the same notebook. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

## Behavior

When running code in a Databricks notebook or job:

- `DatabricksSession.builder.getOrCreate()` returns the default Spark session (accessible through the `spark` variable) when used without additional configuration. This session is pre-configured to connect to the compute instance to which the notebook or job is attached.
- `remote()` takes a configuration _kwargs_ or individual configuration methods and creates a new session for the referenced compute. ^[databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md]

## Usage

Use `remote()` when you need to work with a Databricks compute resource that differs from the one currently attached to your notebook. For example, you might use it to connect to a larger cluster for production workloads while developing against a smaller test cluster.

## Related concepts

- [Databricks Connect](/concepts/databricks-connect.md) – The overall framework for connecting to Databricks compute from local development environments
- [DatabricksSession](/concepts/databrickssession.md) – The session object that manages connections to Databricks compute
- Databricks Runtime – The runtime environment for Databricks notebooks and jobs

## Sources

- databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md

# Citations

1. [databricks-connect-support-in-databricks-notebooks-databricks-on-aws.md](/references/databricks-connect-support-in-databricks-notebooks-databricks-on-aws-dd50e122.md)
