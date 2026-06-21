---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 96d7dc609d4b0c8fed61a058aabc6e22817b7e99bb317498b33faef78ffa5fff
  pageDirectory: concepts
  sources:
    - query-interruptions-with-databricks-connect-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-query-interruption-via-interrupttag-api
    - DCQIVIA
  citations:
    - file: query-interruptions-with-databricks-connect-databricks-on-aws.md
title: Databricks Connect Query Interruption via interruptTag API
description: Databricks Connect provides an interruptTag() API that allows users to tag DataFrames and then interrupt long-running queries by tag, useful for cost control.
tags:
  - databricks
  - api
  - query-interruption
timestamp: "2026-06-19T20:02:22.918Z"
---

# Databricks Connect Query Interruption via `interruptTag` API

**Databricks Connect Query Interruption via `interruptTag` API** refers to the ability to programmatically cancel a long-running query in [Databricks Connect](/concepts/databricks-connect.md) (for Databricks Runtime 14.0 and above) by using the `interruptTag()` method on a [DatabricksSession](/concepts/databrickssession.md). This capability gives users explicit control over query execution for purposes such as cost management or responding to changing conditions. ^[query-interruptions-with-databricks-connect-databricks-on-aws.md]

## Overview

Databricks Connect for Databricks Runtime 14.0 and above improves resilience to client-side network and operating system interruptions (for example, when a laptop lid is closed) for up to 5 minutes. In addition to this automatic reconnection, the client can now also *manually* interrupt a running query. The `interruptTag()` API provides a mechanism to stop all subsequent DataFrame queries that share a specified tag. ^[query-interruptions-with-databricks-connect-databricks-on-aws.md]

## Using the `interruptTag` API

The `interruptTag()` method is called on a `DatabricksSession` instance and accepts a string tag. When invoked, it interrupts any query that was created with the same tag via `session.addTag()`. The tag is applied to *all subsequent DataFrame queries* that use that session, not retroactively to queries already running before the tag was added. ^[query-interruptions-with-databricks-connect-databricks-on-aws.md]

### Python Example

The following example demonstrates a typical usage pattern: a query is started with a tag, and after a short delay a separate thread interrupts all queries carrying that tag.

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

^[query-interruptions-with-databricks-connect-databricks-on-aws.md]

### How It Works

1. **Add a tag** — `session.addTag("interrupt-me")` associates the tag with the session. From that point on, every DataFrame query executed through this session is implicitly tagged.
2. **Interrupt by tag** — Calling `session.interruptTag("interrupt-me")` cancels all running queries that have that tag. If a query has already completed, the call has no effect.
3. **Thread safety** — The interruption can be triggered from a separate thread, making it suitable for timeout or watchdog patterns.

The same API is also available in Scala (though a code example is not shown in the source). ^[query-interruptions-with-databricks-connect-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — Client library that connects IDEs and custom applications to Databricks clusters.
- [DatabricksSession](/concepts/databrickssession.md) — The main entry point for creating and managing connections with Databricks Connect.
- [Long-lived sessions](/concepts/databricks-connect-long-lived-sessions.md) — A feature (Databricks Connect 16.4+, serverless compute) that preserves session state across idle periods; complementary to interruption for managing query lifecycles.
- [Serverless compute](/concepts/serverless-gpu-compute.md) — Compute type that supports long-lived sessions but also works with interruption via `interruptTag`.
- Cost optimization on Databricks — Interrupting queries can help control cost by stopping unnecessary runs.

## Sources

- query-interruptions-with-databricks-connect-databricks-on-aws.md

# Citations

1. [query-interruptions-with-databricks-connect-databricks-on-aws.md](/references/query-interruptions-with-databricks-connect-databricks-on-aws-c776ec46.md)
