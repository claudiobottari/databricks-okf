---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0468a13a284b7072cdb95c9bc670df655af63790962ae3de7efd85b1c7c1f0d8
  pageDirectory: concepts
  sources:
    - pyspark-shell-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - stopping-the-pyspark-shell
    - STPS
    - PySpark Shell
  citations:
    - file: pyspark-shell-databricks-on-aws.md
title: Stopping the PySpark Shell
description: Multiple methods to terminate the Databricks Connect PySpark shell including Ctrl+D, Ctrl+Z, quit(), or exit().
tags:
  - databricks
  - pyspark
  - shell-commands
timestamp: "2026-06-19T20:00:15.976Z"
---

# Stopping the PySpark Shell

**Stopping the PySpark Shell** terminates the PySpark REPL (Read-Eval-Print Loop) that was started via Databricks Connect. This closes the interactive session and disconnects the local client from the remote cluster.

## Methods

The PySpark shell can be stopped using any of the following methods:

- Press `Ctrl + d` (end-of-file).
- Press `Ctrl + z` (suspend / terminate on Unix-like systems).
- Run the command `quit()`.
- Run the command `exit()`.

Each of these methods cleanly closes the shell session. ^[pyspark-shell-databricks-on-aws.md]

## Context

The PySpark shell is started by running the `pyspark` binary from an activated Python virtual environment configured for [Databricks Connect](/concepts/databricks-connect.md). Once started, the shell provides a `spark` object (a `SparkSession`) that sends DataFrame operations to the remote Databricks cluster. Stopping the shell disconnects the local client from that cluster. ^[pyspark-shell-databricks-on-aws.md]

## Related Concepts

- [PySpark Shell](/concepts/stopping-the-pyspark-shell.md) – The interactive REPL used with Databricks Connect.
- [Databricks Connect](/concepts/databricks-connect.md) – The library that enables remote execution of PySpark code on a Databricks cluster.
- SparkSession – The entry point for using Spark functionality in the shell.
- PySpark REPL – The interactive interpreter environment provided by the shell.

## Sources

- pyspark-shell-databricks-on-aws.md

# Citations

1. [pyspark-shell-databricks-on-aws.md](/references/pyspark-shell-databricks-on-aws-b2b40482.md)
