---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cef497215b7149775883dbb4f358b6e463e678a93d5dba87f6afb76dca1cc640
  pageDirectory: concepts
  sources:
    - evaluate-conversations-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - session-tracking-with-trace-tags
    - STWTT
  citations:
    - file: evaluate-conversations-databricks-on-aws.md
title: Session Tracking with Trace Tags
description: Mechanism for instrumenting agents with session IDs on traces (mlflow.trace.session tag) to group individual turns into conversation sessions for evaluation.
tags:
  - mlflow
  - tracing
  - sessions
  - instrumentation
timestamp: "2026-06-19T18:41:52.692Z"
---

# Session Tracking with Trace Tags

**Session Tracking with Trace Tags** is a mechanism in [MLflow](/concepts/mlflow.md) for grouping individual [Traces](/concepts/traces.md) into coherent conversation sessions, enabling multi-turn evaluation of conversational AI systems. By tagging traces with a session identifier, MLflow can automatically associate multiple turns of a conversation, allowing [LLM Judges](/concepts/llm-judges.md) to evaluate session-level qualities such as user frustration, conversation completeness, and dialogue coherence. ^[evaluate-conversations-databricks-on-aws.md]

## Overview

Conversational AI systems require evaluation at the session level rather than at the individual turn level. Traditional single-turn evaluation assesses each agent response independently, but session-level evaluation captures emergent qualities such as whether the user became frustrated and whether that frustration was resolved, whether all user questions were answered by the end of the conversation, whether the agent remembers information from earlier turns, and whether the conversation flows naturally. Session tracking with trace tags provides the infrastructure to group individual traces into sessions for this purpose. ^[evaluate-conversations-databricks-on-aws.md]

## Instrumenting Traces with Session IDs

To enable session tracking, agents must set a session ID on each trace using the `mlflow.trace.session` tag. This is done inside a traced function by calling `mlflow.update_current_trace()` and setting the appropriate tag: ^[evaluate-conversations-databricks-on-aws.md]

```python
import mlflow

@mlflow.trace
def my_chatbot(question, session_id):
    mlflow.update_current_trace(
        tags={"mlflow.trace.session": session_id}
    )
    # ... your chatbot logic
```

When the session ID tag is present, MLflow can group all traces with the same session ID into a single conversation session. For complete documentation on tracking sessions, see [Track users and sessions](/concepts/mlflow-user-and-session-tracking.md). ^[evaluate-conversations-databricks-on-aws.md]

## Retrieving Sessions

### Searching Traces by Session ID

To evaluate a specific session, use `mlflow.search_traces` with a filter string that targets the session tag: ^[evaluate-conversations-databricks-on-aws.md]

```python
import mlflow
from mlflow.genai.scorers import ConversationCompleteness, UserFrustration

traces = mlflow.search_traces(
    filter_string="tags.`mlflow.trace.session` = '<your-session-id>'",
    return_type="list",
)

results = mlflow.genai.evaluate(
    data=traces,
    scorers=[ConversationCompleteness(), UserFrustration()],
)
```

### Using `mlflow.search_sessions`

MLflow also provides `mlflow.search_sessions` to retrieve complete sessions directly. Each session is returned as a list of traces: ^[evaluate-conversations-databricks-on-aws.md]

```python
sessions = mlflow.search_sessions(
    locations=["<your-experiment-id>"],
    max_results=50,
)

all_traces = [trace for session in sessions for trace in session]
```

### Evaluating Pre-Generated Conversations

For production conversation data or pre-recorded test conversations, pass traces to `mlflow.genai.evaluate`. MLflow automatically groups traces by their session ID tag: ^[evaluate-conversations-databricks-on-aws.md]

```python
traces = mlflow.search_traces(
    filter_string="attributes.status = 'OK'",
    return_type="list",
)

results = mlflow.genai.evaluate(
    data=traces,
    scorers=[
        ConversationCompleteness(),
        UserFrustration(),
    ],
)
```

## How Assessments Are Stored

Multi-turn assessments generated from session tracking are stored on the **first trace** (chronologically) in each session. This design ensures that assessments remain stable even as new turns are added to a conversation, that conversation-level assessments can be easily found by looking at session start traces, and that the Sessions UI can efficiently display conversation metrics. Assessments include metadata identifying them as conversation-level, including the `session_id` that links the assessment to the full conversation. ^[evaluate-conversations-databricks-on-aws.md]

## Multi-Turn Judges

Session tracking enables the use of [Multi-turn Judges](/concepts/multi-turn-judge.md), which analyze the entire conversation history rather than individual responses. MLflow provides built-in multi-turn judges such as `ConversationCompleteness`, which evaluates whether the agent answered all user questions, and `UserFrustration`, which evaluates whether the user became frustrated during the conversation. ^[evaluate-conversations-databricks-on-aws.md]

### Custom Multi-Turn Judges

Custom multi-turn judges can be created using `make_judge` with the `{{ conversation }}` template variable, which injects the complete conversation history in a readable format: ^[evaluate-conversations-databricks-on-aws.md]

```python
from mlflow.genai.judges import make_judge
from typing import Literal

politeness_judge = make_judge(
    name="politeness",
    instructions=(
        "Evaluate whether the assistant maintained a polite and professional "
        "tone throughout this conversation:\n\n{{ conversation }}\n\n"
        "Rate as 'consistently_polite', 'mostly_polite', or 'impolite'."
    ),
    feedback_value_type=Literal["consistently_polite", "mostly_polite", "impolite"],
)
```

The `{{ conversation }}` variable can only be used with `{{ expectations }}`, not with `{{ inputs }}`, `{{ outputs }}`, or `{{ trace }}`. ^[evaluate-conversations-databricks-on-aws.md]

## Related Concepts

- [Multi-turn Judges](/concepts/multi-turn-judge.md)
- [[MLflow Trace|MLflow Traces]]
- [Conversation Simulation](/concepts/conversationsimulator.md)
- [Production monitoring with multi-turn judges](/concepts/genai-production-monitoring-with-llm-judges.md)
- [LLM evaluation](/concepts/llm-as-a-judge-evaluation.md)
- [Track users and sessions](/concepts/mlflow-user-and-session-tracking.md)

## Sources

- evaluate-conversations-databricks-on-aws.md

# Citations

1. [evaluate-conversations-databricks-on-aws.md](/references/evaluate-conversations-databricks-on-aws-f530405b.md)
