---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 104d50da85440f1e7f52cfd90fd30764f1e5cef9f209e171cf14e8ba23b952b0
  pageDirectory: concepts
  sources:
    - evaluate-conversations-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - session-id-tracing
    - SIT
    - Session ID Tagging
    - session IDs
  citations:
    - file: evaluate-conversations-databricks-on-aws.md
title: Session ID Tracing
description: Tagging MLflow traces with session IDs via mlflow.update_current_trace to group individual turns into coherent conversations.
tags:
  - tracing
  - mlflow
  - telemetry
timestamp: "2026-06-18T12:12:58.522Z"
---

# Session ID Tracing

**Session ID Tracing** is the practice of tagging individual [[MLflow Trace|MLflow Traces]] with a session identifier so that they can be grouped into multi-turn conversations for evaluation and monitoring. By assigning a session ID to each trace, MLflow can reconstruct complete conversation sessions from individual trace records, enabling [Conversation Evaluation](/concepts/conversation-evaluation.md) at the session level rather than the turn level. ^[evaluate-conversations-databricks-on-aws.md]

## Overview

Conversational AI systems require evaluation at the session level to capture quality dimensions that emerge over multiple interactions — such as user frustration patterns, conversation completeness, knowledge retention, and dialogue coherence. Session ID tracing provides the foundation for this by linking individual turns into coherent sessions. ^[evaluate-conversations-databricks-on-aws.md]

## Setting Session IDs on Traces

When building an agent, you set session IDs on traces using `mlflow.update_current_trace()` with the `mlflow.trace.session` tag. This tag groups traces into conversation sessions for later retrieval and evaluation. ^[evaluate-conversations-databricks-on-aws.md]

```python
import mlflow

@mlflow.trace
def my_chatbot(question, session_id):
    mlflow.update_current_trace(
        tags={"mlflow.trace.session": session_id}
    )
    # ... your chatbot logic
```

For complete documentation on tracking sessions, see [Track Users and Sessions](/concepts/mlflow-user-and-session-tracking.md). ^[evaluate-conversations-databricks-on-aws.md]

## Retrieving Sessions for Evaluation

### Using `mlflow.search_traces`

You can retrieve traces from an experiment and pass them to `mlflow.genai.evaluate`. MLflow automatically groups traces by session ID when evaluating. ^[evaluate-conversations-databricks-on-aws.md]

```python
from mlflow.genai.scorers import ConversationCompleteness, UserFrustration

# Get traces from your experiment
traces = mlflow.search_traces(
    filter_string="attributes.status = 'OK'",
    return_type="list",
)

# Evaluate the conversations
# MLflow automatically groups traces by their session ID tag
results = mlflow.genai.evaluate(
    data=traces,
    scorers=[
        ConversationCompleteness(),  # Did the agent answer all questions?
        UserFrustration(),           # Did the user become frustrated?
    ],
)
```

### Using `mlflow.search_sessions`

You can also retrieve complete sessions directly using `mlflow.search_sessions`, which returns each session as a list of traces. ^[evaluate-conversations-databricks-on-aws.md]

```python
import mlflow

# Get complete sessions (each session is a list of traces)
sessions = mlflow.search_sessions(
    locations=["<your-experiment-id>"],
    max_results=50,
)

# Flatten for evaluation
all_traces = [trace for session in sessions for trace in session]

results = mlflow.genai.evaluate(
    data=all_traces,
    scorers=[ConversationCompleteness(), UserFrustration()],
)
```

### Evaluating a Specific Session

To evaluate a specific session, use `mlflow.search_traces` with a filter string targeting the session ID tag. ^[evaluate-conversations-databricks-on-aws.md]

```python
import mlflow
from mlflow.genai.scorers import ConversationCompleteness, UserFrustration

# Get traces for a specific session using filter
traces = mlflow.search_traces(
    filter_string="tags.`mlflow.trace.session` = '<your-session-id>'",
    return_type="list",
)

# Evaluate the session
results = mlflow.genai.evaluate(
    data=traces,
    scorers=[ConversationCompleteness(), UserFrustration()],
)
```

## How Assessments Are Stored

Multi-turn assessments generated from session-level evaluation are stored on the **first trace** (chronologically) in each session. This design ensures: ^[evaluate-conversations-databricks-on-aws.md]

- Assessments remain stable even as new turns are added to a conversation
- You can easily find conversation-level assessments by looking at session start traces
- The Sessions UI can efficiently display conversation metrics

Assessments include metadata identifying them as conversation-level, including the `session_id` linking the assessment to the full conversation. ^[evaluate-conversations-databricks-on-aws.md]

## Use Cases

Session ID tracing supports two primary evaluation approaches: ^[evaluate-conversations-databricks-on-aws.md]

### Evaluate Pre-Generated Conversations

Evaluate existing conversations that have already been traced. Use this approach when you have:
- Production conversation data to analyze
- Pre-recorded test conversations from QA or user studies
- Conversations from a previous agent version for comparison

### Simulate Conversations During Evaluation

Generate new conversations by simulating user interactions with your agent. Use this approach when you want to:
- Test a new agent version systematically with consistent scenarios
- Generate diverse test scenarios at scale
- Stress-test your agent with specific user behaviors and edge cases

## Requirements

- MLflow 3.10.0 or later is required for multi-turn evaluation. ^[evaluate-conversations-databricks-on-aws.md]
- Your agent must be instrumented to track session IDs on traces. ^[evaluate-conversations-databricks-on-aws.md]

## Related Concepts

- [Conversation Evaluation](/concepts/conversation-evaluation.md) — Evaluating entire conversation sessions rather than individual turns
- [Multi-turn Judges](/concepts/multi-turn-judge.md) — LLM-based judges that analyze complete conversation histories
- [Conversation Simulation](/concepts/conversationsimulator.md) — Generating synthetic conversations for testing
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Using multi-turn judges for continuous production monitoring
- [[MLflow Trace|MLflow Traces]] — The underlying trace records that session IDs group into conversations
- [Track Users and Sessions](/concepts/mlflow-user-and-session-tracking.md) — Complete documentation for instrumenting agents with session IDs

## Sources

- evaluate-conversations-databricks-on-aws.md

# Citations

1. [evaluate-conversations-databricks-on-aws.md](/references/evaluate-conversations-databricks-on-aws-f530405b.md)
