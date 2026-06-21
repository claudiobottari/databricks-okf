---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1a8d03fb62055f63afb8c552629985b3238d820941382f46631913234542791a
  pageDirectory: concepts
  sources:
    - evaluate-conversations-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - session-id-tracking
    - SIT
  citations:
    - file: evaluate-conversations-databricks-on-aws.md
title: Session ID Tracking
description: The mechanism of tagging MLflow traces with session IDs to group individual turns into coherent conversation sessions for multi-turn evaluation.
tags:
  - mlflow
  - tracing
  - conversational-ai
timestamp: "2026-06-19T10:23:11.031Z"
---

# Session ID Tracking

**Session ID Tracking** is a mechanism for grouping individual [[MLflow Trace|MLflow Traces]] into coherent conversation sessions, enabling multi-turn evaluation of conversational AI systems. By assigning a unique session identifier to each trace, practitioners can assess conversation-level quality metrics such as user frustration, conversation completeness, knowledge retention, and dialogue coherence. ^[evaluate-conversations-databricks-on-aws.md]

## Overview

Traditional single-turn evaluation assesses each agent response independently. However, conversational agents require evaluation at the session level to capture emergent quality characteristics that span multiple interactions. Session ID tracking addresses this need by providing a way to group related traces into conversations that judges can analyze holistically. ^[evaluate-conversations-databricks-on-aws.md]

## Tagging Traces with Session IDs

Session IDs are set on traces using the `mlflow.update_current_trace()` function with a `mlflow.trace.session` tag. This tag is typically applied inside the traced function that handles each turn of the conversation: ^[evaluate-conversations-databricks-on-aws.md]

```python
import mlflow

@mlflow.trace
def my_chatbot(question, session_id):
    mlflow.update_current_trace(
        tags={"mlflow.trace.session": session_id}
    )
    # ... your chatbot logic
```

For complete documentation on tracking sessions, see [Track users and sessions](/concepts/mlflow-user-and-session-tracking.md). ^[evaluate-conversations-databricks-on-aws.md]

## Retrieving Sessions for Evaluation

### Using `mlflow.search_traces`

Traces can be filtered by session ID to retrieve all turns belonging to a specific conversation: ^[evaluate-conversations-databricks-on-aws.md]

```python
import mlflow

# Get traces for a specific session using filter
traces = mlflow.search_traces(
    filter_string="tags.`mlflow.trace.session` = '<your-session-id>'",
    return_type="list",
)
```

### Using `mlflow.search_sessions`

Complete sessions can be retrieved directly using `mlflow.search_sessions`, which returns each session as a list of traces: ^[evaluate-conversations-databricks-on-aws.md]

```python
import mlflow

# Get complete sessions (each session is a list of traces)
sessions = mlflow.search_sessions(
    locations=["<your-experiment-id>"],
    max_results=50,
)

# Flatten for evaluation
all_traces = [trace for session in sessions for trace in session]
```

## Evaluation with Session ID Tracking

When traces tagged with session IDs are passed to `mlflow.genai.evaluate()`, MLflow automatically groups them by the `mlflow.trace.session` tag. This enables the use of [Multi-turn Judges](/concepts/multi-turn-judge.md) that evaluate the entire conversation history using the `{{ conversation }}` template variable. ^[evaluate-conversations-databricks-on-aws.md]

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

## Assessment Storage

Multi-turn assessments generated through session ID tracking are stored on the **first trace** (chronologically) in each session. This design ensures: ^[evaluate-conversations-databricks-on-aws.md]

- Assessments remain stable even as new turns are added to a conversation
- Conversation-level assessments can be easily found by looking at session start traces
- The Sessions UI can efficiently display conversation metrics

Assessments include metadata identifying them as conversation-level, specifically the `session_id` that links the assessment to the full conversation. ^[evaluate-conversations-databricks-on-aws.md]

## Two Approaches to Conversation Evaluation

Session ID tracking supports two evaluation approaches: ^[evaluate-conversations-databricks-on-aws.md]

1. **Evaluate pre-generated conversations**: Analyze existing conversations that have already been traced with session IDs. This is useful for production data analysis, pre-recorded test conversations from QA or user studies, and comparing conversations from a previous agent version.

2. **Simulate conversations during evaluation**: Generate new conversations by simulating user interactions with [ConversationSimulator](/concepts/conversationsimulator.md). This enables testing different agent versions with consistent goals and personas.

## Related Concepts

- [Multi-turn Evaluation](/concepts/multi-turn-conversation-evaluation.md) — Evaluating entire conversation sessions rather than individual turns
- Conversation Completeness — A built-in judge for assessing whether all user questions were answered
- User Frustration — A built-in judge for detecting and resolving user frustration
- [Custom Judges](/concepts/custom-judges.md) — Creating custom multi-turn judges using `make_judge` with the `{{ conversation }}` variable
- [Production Monitoring](/concepts/production-monitoring.md) — Using multi-turn judges for continuous production monitoring
- [Conversation Simulation](/concepts/conversationsimulator.md) — Generating synthetic conversations for testing

## Sources

- evaluate-conversations-databricks-on-aws.md

# Citations

1. [evaluate-conversations-databricks-on-aws.md](/references/evaluate-conversations-databricks-on-aws-f530405b.md)
