---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f1ad796024552c429dbb505110bdd75eae7db8292ef8f634331a9133b15a2b12
  pageDirectory: concepts
  sources:
    - query-interruptions-with-databricks-connect-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-long-lived-sessions
    - DCLS
    - Long-lived sessions
  citations:
    - file: query-interruptions-with-databricks-connect-databricks-on-aws.md
title: Databricks Connect Long-lived Sessions
description: On serverless compute (DBR 16.4+), Databricks Connect best-effort preserves session state — including configs, temporary views, UDFs, temp variables, and uploaded files — across idle timeouts, so users don't need to re-run setup commands.
tags:
  - databricks
  - sessions
  - serverless
timestamp: "2026-06-19T20:02:26.619Z"
---

# Databricks Connect Long-lived Sessions

**Databricks Connect Long-lived Sessions** is a feature that preserves session state across periods of inactivity when using [Databricks Connect](/concepts/databricks-connect.md) with serverless compute. After the default idle timeout, a best-effort attempt is made to preserve the session, allowing users to reconnect without re-running setup commands.

## Overview

When you use Databricks Connect with serverless compute, after the default idle timeout a best effort is made to preserve your session. When you reconnect, Databricks attempts to automatically restore your session, including configurations, temporary views, UDFs, temporary variables, and uploaded files. ^[query-interruptions-with-databricks-connect-databricks-on-aws.md]

This is useful for sessions with commands that need state to survive periods of inactivity, such as setting configurations, registering UDFs, creating temporary views, or uploading files. Without this, an idle timeout would require you to re-run all of those setup commands before resuming work. ^[query-interruptions-with-databricks-connect-databricks-on-aws.md]

## Supported Compute Types

Long-lived sessions are only supported on serverless compute. They are not supported on standard or dedicated compute. ^[query-interruptions-with-databricks-connect-databricks-on-aws.md]

## Version Requirements

Long-lived sessions are supported in Databricks Connect version 16.4 and above on serverless compute. ^[query-interruptions-with-databricks-connect-databricks-on-aws.md]

## Preserved State

When a session is restored, the following state is preserved:

- Configurations
- Temporary views
- User-defined functions (UDFs)
- Temporary variables
- Uploaded files

^[query-interruptions-with-databricks-connect-databricks-on-aws.md]

## Limitations

- **Compute type restriction**: Long-lived sessions are only supported on serverless compute. They are not supported on standard or dedicated compute. ^[query-interruptions-with-databricks-connect-databricks-on-aws.md]
- **Best-effort recovery**: Session recovery after idle timeout is best-effort and not guaranteed. If your session cannot be restored, a new session is started. ^[query-interruptions-with-databricks-connect-databricks-on-aws.md]
- **State size limit**: Sessions that accumulate a large amount of state may exceed the size limit, after which state is no longer preserved. Reconnecting after this threshold starts a new session. ^[query-interruptions-with-databricks-connect-databricks-on-aws.md]
- **Inactivity expiration**: Preserved state expires after two days of inactivity. If your session is idle longer than this, reconnecting starts a new session. ^[query-interruptions-with-databricks-connect-databricks-on-aws.md]
- **Unsupported state types**: Streaming query state and SQL scripts that use `EXECUTE IMMEDIATE` are not preserved across reconnects. ^[query-interruptions-with-databricks-connect-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — The client library that enables connecting IDEs and custom applications to Databricks clusters
- Query Interruptions with Databricks Connect — Handling asynchronous queries and interruptions
- Serverless Compute — The compute type that supports long-lived sessions
- User-Defined Functions (UDFs) — Custom functions that can be preserved across session reconnects
- Temporary Views — Session-scoped views that persist across reconnects

## Sources

- query-interruptions-with-databricks-connect-databricks-on-aws.md

# Citations

1. [query-interruptions-with-databricks-connect-databricks-on-aws.md](/references/query-interruptions-with-databricks-connect-databricks-on-aws-c776ec46.md)
