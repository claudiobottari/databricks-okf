---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8ce8c0ea4daa872a776e90cd1f01e6735a7864aef4540393de8fc5cbe946d825
  pageDirectory: concepts
  sources:
    - evaluate-conversations-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - pre-generated-conversation-evaluation
    - PCE
    - Pre-generated evaluation
  citations:
    - file: evaluate-conversations-databricks-on-aws.md
title: Pre-generated Conversation Evaluation
description: Approach for evaluating existing conversation traces (from production or pre-recorded test data) by retrieving traces grouped by session ID and passing them to mlflow.genai.evaluate.
tags:
  - mlflow
  - genai
  - evaluation
  - conversational-ai
timestamp: "2026-06-19T18:42:03.912Z"
---

# Pre-generated Conversation Evaluation

**Pre-generated Conversation Evaluation** is an approach in [MLflow GenAI](/concepts/mlflow-3-for-genai.md) that evaluates existing, pre-recorded conversation data — such as production logs, QA test sessions, or conversations from previous agent versions — by analyzing the full session history rather than individual turns. This technique is essential for assessing conversational AI systems where quality emerges over multiple interactions, including patterns of user frustration, conversation completeness, and dialogue coherence. ^[evaluate-conversations-databricks-on-aws.md]

## Overview

Traditional single-turn evaluation assesses each agent response independently. However, conversational agents require evaluation at the session level to capture key quality dimensions: ^[evaluate-conversations-databricks-on-aws.md]

- **User frustration**: Did the user become frustrated? Was it resolved?
- **Conversation completeness**: Were all user questions answered by the end of the conversation?
- **Knowledge retention**: Does the agent remember information from earlier in the conversation?
- **Dialogue coherence**: Does the conversation flow naturally?

Multi-turn evaluation addresses these needs by grouping traces into conversation sessions and applying judges that analyze the entire conversation history. ^[evaluate-conversations-databricks-on-aws.md]

## When to Use Pre-generated Evaluation

Use pre-generated conversation evaluation when you have: ^[evaluate-conversations-databricks-on-aws.md]

- Production conversation data to analyze
- Pre-recorded test conversations from QA or user studies
- Conversations from a previous agent version for comparison

This contrasts with [Conversation Simulation](/concepts/conversationsimulator.md), which generates new conversations during evaluation to test agent versions with consistent scenarios. ^[evaluate-conversations-databricks-on-aws.md]

## Prerequisites

- MLflow 3.10.0 or later installed (`pip install --upgrade 'mlflow[databricks]>=3.10'`)
- Your agent must be instrumented to track session IDs on traces ^[evaluate-conversations-databricks-on-aws.md]

## Workflow

### Step 1: Tag Traces with Session IDs

When building your agent, set session IDs on traces to group them into conversations: ^[evaluate-conversations-databricks-on-aws.md]

```python
import mlflow

@mlflow.trace
def my_chatbot(question, session_id):
    mlflow.update_current_trace(
        tags={"mlflow.trace.session": session_id}
    )
    # ... your chatbot logic
```

### Step 2: Retrieve and Evaluate Sessions

Get traces from your experiment and pass them to `mlflow.genai.evaluate`. MLflow automatically groups traces by session ID: ^[evaluate-conversations-databricks-on-aws.md]

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

You can also retrieve complete sessions directly using `mlflow.search_sessions`: ^[evaluate-conversations-databricks-on-aws.md]

```python
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

## Multi-turn Judges

### Built-in Judges

MLflow provides built-in multi-turn judges for evaluating conversation quality. For the complete list, see the [MLflow Predefined Scorers](/concepts/mlflow-genai-predefined-scorers.md) documentation. ^[evaluate-conversations-databricks-on-aws.md]

### Custom Judges

Create custom multi-turn judges using `make_judge`. Use the `{{ conversation }}` template variable to access the full conversation history: ^[evaluate-conversations-databricks-on-aws.md]

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

# Use in evaluation
results = mlflow.genai.evaluate(
    data=traces,
    scorers=[politeness_judge],
)
```

The `{{ conversation }}` variable injects the complete conversation history in a readable format for the judge to analyze. ^[evaluate-conversations-databricks-on-aws.md]

> **Note:** The `{{ conversation }}` variable can only be used with `{{ expectations }}`, not with `{{ inputs }}`, `{{ outputs }}`, or `{{ trace }}`. ^[evaluate-conversations-databricks-on-aws.md]

## How Assessments Are Stored

Multi-turn assessments are stored on the **first trace** (chronologically) in each session. This design ensures: ^[evaluate-conversations-databricks-on-aws.md]

- Assessments remain stable even as new turns are added to a conversation
- You can easily find conversation-level assessments by looking at session start traces
- The Sessions UI can efficiently display conversation metrics

Assessments include metadata identifying them as conversation-level, including a `session_id` field linking the assessment to the full conversation. ^[evaluate-conversations-databricks-on-aws.md]

## Working with Specific Sessions

To evaluate a specific session, use `mlflow.search_traces` with a filter string: ^[evaluate-conversations-databricks-on-aws.md]

```python
traces = mlflow.search_traces(
    filter_string="tags.`mlflow.trace.session` = '<your-session-id>'",
    return_type="list",
)

results = mlflow.genai.evaluate(
    data=traces,
    scorers=[ConversationCompleteness(), UserFrustration()],
)
```

## Production Monitoring

Multi-turn judges can also be used for continuous monitoring in production, not just offline evaluation during development. ^[evaluate-conversations-databricks-on-aws.md]

## Related Concepts

- [Conversation Simulation](/concepts/conversationsimulator.md) — Generating synthetic conversations during evaluation
- [Custom Judges](/concepts/custom-judges.md) — Building custom LLM judges using `make_judge`
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) — The `mlflow.genai.evaluate()` API for offline assessment
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Deploying judges for continuous quality monitoring
- [Track Users and Sessions](/concepts/mlflow-user-and-session-tracking.md) — Instrumenting agents with session IDs
- [MLflow Predefined Scorers](/concepts/mlflow-genai-predefined-scorers.md) — Complete reference for built-in scorers

## Sources

- evaluate-conversations-databricks-on-aws.md

# Citations

1. [evaluate-conversations-databricks-on-aws.md](/references/evaluate-conversations-databricks-on-aws-f530405b.md)
