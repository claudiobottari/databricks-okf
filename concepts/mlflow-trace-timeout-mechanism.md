---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 919fd4de65814456ca3172acc2667705ffb5518f791542f5708df8749b8d717e
  pageDirectory: concepts
  sources:
    - tracing-faq-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-trace-timeout-mechanism
    - MTTM
    - MLFLOW_TRACE_TIMEOUT_SECONDS
    - MLflow Trace Timeout
  citations:
    - file: tracing-faq-databricks-on-aws.md
title: MLflow Trace Timeout Mechanism
description: The MLFLOW_TRACE_TIMEOUT_SECONDS environment variable can halt stuck traces with ERROR status to prevent infinite 'in progress' traces.
tags:
  - mlflow
  - tracing
  - configuration
  - error-handling
timestamp: "2026-06-19T23:11:32.077Z"
---

```yaml
---
title: [[mlflow-trace|MLflow Trace]] Timeout Mechanism
summary: A mechanism to automatically halt an in-progress [[mlflow-trace|MLflow Trace]] after a configurable timeout, preventing stuck [[traces|Traces]] from remaining in "in progress" state indefinitely.
sources:
  - tracing-faq-databricks-on-aws.md
kind: concept
tags:
  - [[mlflow|MLflow]]
  - tracing
  - timeout
  - troubleshooting
aliases:
  - trace-timeout
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# [[mlflow-trace|MLflow Trace]] Timeout Mechanism

The **MLflow Trace Timeout Mechanism** allows users to set a maximum execution duration for an [[mlflow-trace|MLflow Trace]]. When a trace exceeds this limit, [[mlflow|MLflow]] automatically halts the trace, sets its status to `ERROR`, and exports it to the backend. This prevents [[traces|Traces]] from being stuck in a perpetual "in progress" state when a model or agent enters a long-running operation or infinite loop. ^[tracing-faq-databricks-on-aws.md]

## Configuration

The timeout is controlled by the `MLFLOW_TRACE_TIMEOUT_SECONDS` environment variable. By default, no timeout is set, meaning a trace can remain "in progress" indefinitely. Setting this variable to a positive integer (e.g., `"5"`) causes [[mlflow|MLflow]] to monitor the trace’s elapsed time and halt it if the duration exceeds the specified number of seconds. ^[tracing-faq-databricks-on-aws.md]

The timeout check is performed in a background thread. The interval between checks is controlled by the `MLFLOW_TRACE_TIMEOUT_CHECK_INTERVAL_SECONDS` environment variable, which defaults to every second. Resource consumption from this thread is negligible. ^[tracing-faq-databricks-on-aws.md]

## Behavior

- When a trace exceeds the timeout, [[mlflow|MLflow]] stops collecting new spans for that trace and marks it with `ERROR` status.
- The trace is then exported to the [[MLflow Tracking]] backend so that the spans can be analyzed to identify the cause of the hang.
- **Important**: The timeout applies only to the [[mlflow-trace|MLflow Trace]], not to the main program, model, or agent. The underlying code continues to run even after the trace is halted. This ensures that a stuck trace does not disrupt the actual workload. ^[tracing-faq-databricks-on-aws.md]

## Example

The following Python example sets a 5‑second timeout and simulates a long‑running operation that will be halted by the mechanism:

```python
import [MLflow](/concepts/mlflow.md)
import os
import time

# Set the timeout to 5 seconds for demonstration purposes
os.environ["MLFLOW_TRACE_TIMEOUT_SECONDS"] = "5"

# Simulate a long-running operation
@mlflow.trace
def long_running():
    for _ in range(10):
        child()

@mlflow.trace
def child():
    time.sleep(1)

long_running()
```

^[tracing-faq-databricks-on-aws.md]

## Use Cases

- Preventing "in progress" [[traces|Traces]] from accumulating when a model or agent gets stuck in an infinite loop.
- Debugging long-running agent chains or AI agent evaluations without waiting indefinitely for a trace to complete.
- Ensuring that production tracing systems can recover gracefully from unexpected delays without manual intervention.

## Related Concepts

- [[MLflow Tracing]] – Overview of the [[mlflow-tracing|MLflow Tracing]] system.
- MLflow Environment Variables – Reference for all [[mlflow|MLflow]] runtime configuration variables.
- Trace Search – Searching for [[traces|Traces]] after they have been exported with timeout.
- [[Production Monitoring]] – Using tracing in production with [[Scheduled Scorers (MLflow GenAI)|scheduled scorers]] and [[MLflow Agent Evaluation|agent evaluation]].
- AI Agents – Complex agent workflows that may trigger long-running [[traces|Traces]].

## Sources

- tracing-faq-databricks-on-aws.md
```

# Citations

1. [tracing-faq-databricks-on-aws.md](/references/tracing-faq-databricks-on-aws-83ee1878.md)
