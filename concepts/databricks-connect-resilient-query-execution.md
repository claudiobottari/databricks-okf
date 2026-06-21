---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d623ddc442b966bfa5bd2fe1632159da89155f40c5735ff50d9a9a3fbdc1b026
  pageDirectory: concepts
  sources:
    - query-interruptions-with-databricks-connect-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-resilient-query-execution
    - DCRQE
  citations:
    - file: query-interruptions-with-databricks-connect-databricks-on-aws.md
title: Databricks Connect Resilient Query Execution
description: Databricks Connect (DBR 14.0+) automatically reconnects to running queries after network interruptions or OS pauses (up to 5 min), and supports longer query execution beyond the previous 1-hour limit.
tags:
  - databricks
  - query-execution
  - resilience
timestamp: "2026-06-19T20:02:22.741Z"
---

# Databricks Connect Resilient Query Execution

**Databricks Connect Resilient Query Execution** refers to the enhanced fault‑tolerance and session management features introduced in [Databricks Connect](/concepts/databricks-connect.md) for Databricks Runtime 14.0 and above. These capabilities allow long‑running queries to survive network interruptions, operating‑system pauses (such as closing a laptop lid), and idle timeouts when using serverless compute. ^[query-interruptions-with-databricks-connect-databricks-on-aws.md]

## Query Execution Interruptions

When using Databricks Connect for Databricks Runtime 14.0 and above, query execution is more resilient to network and other interrupts while running long queries. If the client program receives an interruption or if the process is paused by the operating system for up to 5 minutes (for example, when the laptop lid is shut), the client automatically reconnects to the running query. This also allows queries to run for longer periods—previously limited to 1 hour—without being interrupted by a transient disconnection. ^[query-interruptions-with-databricks-connect-databricks-on-aws.md]

## Interrupting Running Queries

In addition to automatic reconnection, Databricks Connect provides the ability to manually interrupt a running query, which can be useful for cost‑saving or to stop a long‑running operation. The `interruptTag()` API allows a client to interrupt all queries that have been tagged with a specific identifier. ^[query-interruptions-with-databricks-connect-databricks-on-aws.md]

**Example (Python):**

```python
from databricks.connect import [[databrickssession|DatabricksSession]]
from time import sleep
import threading

session = [[databrickssession|DatabricksSession]].builder.getOrCreate()

def thread_fn():
    sleep(5)
    session.interruptTag("interrupt-me")

# All subsequent DataFrame queries that use session will have this tag.
session.addTag("interrupt-me")

t = threading.Thread(target=thread_fn).start()

df = <a long running DataFrame query>
df.show()

t.join()
```

In this example, a long‑running DataFrame query is started after the tag `"interrupt-me"` is added to the session. After 5 seconds, a separate thread calls `interruptTag("interrupt-me")`, which interrupts any active query that was submitted with that tag. ^[query-interruptions-with-databricks-connect-databricks-on-aws.md]

## Long‑Lived Sessions

Long‑lived sessions are supported in Databricks Connect version 16.4 and above when using [serverless compute](/concepts/serverless-gpu-compute.md). After the default idle timeout, Databricks makes a best‑effort attempt to preserve the session. When the client reconnects, the system automatically restores the session state, including:

- Configurations
- Temporary views
- UDFs (user‑defined functions)
- Temporary variables
- Uploaded files

This feature is especially valuable for sessions that require setup commands (such as registering UDFs or creating temporary views) before resuming work. Without long‑lived sessions, an idle timeout would force the user to re‑run all those setup commands. ^[query-interruptions-with-databricks-connect-databricks-on-aws.md]

### Limitations

Long‑lived sessions are subject to the following constraints:

- Supported **only on serverless compute**. Not available on standard or dedicated compute.
- Session recovery after idle timeout is **best‑effort and not guaranteed**. If the session cannot be restored, a new session is started.
- Sessions that accumulate a large amount of state may exceed the size limit; once the limit is reached, state is no longer preserved, and reconnecting starts a new session.
- Preserved state **expires after two days of inactivity**. If the session is idle longer than that, reconnecting starts a new session.
- Streaming queries|Streaming query state and SQL scripts that use `EXECUTE IMMEDIATE` are **not preserved** across reconnects. ^[query-interruptions-with-databricks-connect-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) – The client library for connecting IDEs and applications to Databricks clusters.
- Databricks Runtime 14.0 – The release that introduced resilient query execution.
- Serverless Compute – The compute type that supports long‑lived sessions.
- User‑Defined Functions (UDFs) – Stateful objects that are preserved during session restoration.
- Temporary Views – SQL views whose definitions are preserved across reconnects.
- Streaming Queries – A workload type whose state is not preserved by long‑lived sessions.

## Sources

- query-interruptions-with-databricks-connect-databricks-on-aws.md

# Citations

1. [query-interruptions-with-databricks-connect-databricks-on-aws.md](/references/query-interruptions-with-databricks-connect-databricks-on-aws-c776ec46.md)
