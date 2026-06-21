---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 647e85204cd0004253c188e8ee54aa8ea42af89806e2201becaa40e7ec5c7269
  pageDirectory: concepts
  sources:
    - query-interruptions-with-databricks-connect-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - limitations-of-databricks-connect-long-lived-sessions
    - LODCLS
  citations:
    - file: query-interruptions-with-databricks-connect-databricks-on-aws.md
title: Limitations of Databricks Connect Long-lived Sessions
description: Long-lived sessions are only available on serverless compute (not standard/dedicated), are best-effort (not guaranteed), have state size limits, expire after 2 days of inactivity, and do not preserve streaming query state or EXECUTE IMMEDIATE SQL scripts.
tags:
  - databricks
  - limitations
  - sessions
timestamp: "2026-06-19T20:02:28.497Z"
---

##Limitations of Databricks Connect Long-lived Sessions

Long-lived sessions in [Databricks Connect](/concepts/databricks-connect.md) allow sessions to survive idle timeouts on serverless compute, preserving state such as configurations, temporary views, UDFs, temporary variables, and uploaded files. However, this feature has several important limitations that users should understand before relying on it. ^[query-interruptions-with-databricks-connect-databricks-on-aws.md]

### List of Limitations

- **Serverless compute only**: Long-lived sessions are supported exclusively on serverless compute. They are not supported on standard or dedicated compute. ^[query-interruptions-with-databricks-connect-databricks-on-aws.md]

- **Best-effort recovery, not guaranteed**: Session recovery after idle timeout is best-effort and not guaranteed. If a session cannot be restored, a new session is started, requiring the user to re‑execute all setup commands. ^[query-interruptions-with-databricks-connect-databricks-on-aws.md]

- **State size limit**: Sessions that accumulate a large amount of state may exceed the size limit. Once the limit is reached, state is no longer preserved. Reconnecting after this threshold results in a fresh session. ^[query-interruptions-with-databricks-connect-databricks-on-aws.md]

- **Two‑day inactivity expiration**: Preserved state expires after two days of inactivity. If a session remains idle longer than this, reconnecting starts a new session. ^[query-interruptions-with-databricks-connect-databricks-on-aws.md]

- **Unpreserved state types**: Streaming query state and SQL scripts that use `EXECUTE IMMEDIATE` are **not** preserved across reconnects. Users must account for this when designing workflows that rely on long‑lived sessions. ^[query-interruptions-with-databricks-connect-databricks-on-aws.md]

### Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) – The client‑server library enabling connection to Databricks clusters.
- Serverless Compute – The compute type required for long‑lived session support.
- Query Interruption Handling – Related feature for resilient query execution.
- Temporary Views and UDFs – Types of state that are preserved (with limitations).

### Sources

- query-interruptions-with-databricks-connect-databricks-on-aws.md

# Citations

1. [query-interruptions-with-databricks-connect-databricks-on-aws.md](/references/query-interruptions-with-databricks-connect-databricks-on-aws-c776ec46.md)
