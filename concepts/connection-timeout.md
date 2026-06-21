---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 51e89b90e95e2fce31c2f26ab75a48e4027d68ecb0a6a6491b75072ef96d9882
  pageDirectory: concepts
  sources:
    - debug-model-serving-timeouts-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - connection-timeout
    - Connection Timeouts
  citations:
    - file: debug-model-serving-timeouts-databricks-on-aws.md
title: Connection Timeout
description: Network-level timeout where a client waits to establish a connection with the server, commonly seen with JDBC/SQL endpoints.
tags:
  - networking
  - timeouts
  - connection
timestamp: "2026-06-19T14:56:36.910Z"
---

```yaml
---
title: Connection Timeout
summary: A client-side error that occurs when establishing a client-server connection (e.g., JDBC SocketTimeout) in model serving pipelines, distinguishable from server-side request processing timeouts.
sources:
  - debug-model-serving-timeouts-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T09:55:54.537Z"
updatedAt: "2026-06-19T09:55:54.537Z"
tags:
  - databricks
  - networking
  - timeouts
  - connection
aliases:
  - connection-timeout
confidence: 0.9
provenanceState: extracted
inferredParagraphs: 0
---

# Connection Timeout

**Connection timeout** is a client-side error that occurs when a client attempting to establish a network connection with a server does not receive a response within a predefined waiting period. When the timeout expires, the client cancels the connection attempt and typically raises an error. Connection timeouts are related to the time a client waits to establish a connection with the server. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Causes

Connection timeouts can occur if the server or network infrastructure is slow, overloaded, or unreachable. It is important to be aware of the clients used in your model pipeline—such as a custom PyFunc model that makes HTTP calls to external services—because their timeout configurations can influence whether a connection timeout is triggered. ^[debug-model-serving-timeouts-databricks-on-aws.md]

Connection timeouts are client-side errors, distinct from [[Server-Side Timeout|server-side timeouts]], which are triggered by the server after a request has been accepted but takes too long to process. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Detection

To diagnose a connection timeout:

1. **Check service logs and inference tables** of the [[Model Serving Endpoint|Model Serving Endpoints|Model Serving endpoint]] for messages containing the terms `"timed out"` or `"timeout"`. ^[debug-model-serving-timeouts-databricks-on-aws.md]
2. Understand that the specific error message varies by service. For example, a **SocketTimeout** for a JDBC connection to a SQL endpoint may appear as a parameter in the JDBC URL.

## Example: SocketTimeout for JDBC

When a model pipeline reads from or writes to a SQL endpoint over a JDBC connection, the default socket timeout can be configured in the JDBC URL. If the connection is not established within that time, a `SocketTimeout` exception is raised. The JDBC URL might look like:

```
jdbc:spark://<server-hostname>:443;HttpPath=<http-path>;TransportMode=http;SSL=1[;property=value[;property=value]];SocketTimeout=300
```

Adjusting the `SocketTimeout` parameter in the JDBC URL can resolve such timeouts. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Related Concepts

- [[Model Serving Endpoint Timeouts|Model Serving Timeouts]] – Overview of all timeout types for model serving endpoints.
- [[Server-Side Timeout]] – Timeout triggered by the server after a request is accepted.
- Client-Side Timeout – Timeout triggered by the client (e.g., MLflow or third-party clients).
- Model Serving Debugging – General debugging guidance for model serving endpoints.
- [[Inference Tables]] – Schema and logging of requests and responses.
- [[Ephemeral Service Logs|Service Logs]] – Logs that can contain timeout errors.

## Sources

- debug-model-serving-timeouts-databricks-on-aws.md
```

# Citations

1. [debug-model-serving-timeouts-databricks-on-aws.md](/references/debug-model-serving-timeouts-databricks-on-aws-7b1685db.md)
