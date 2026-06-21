---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9b82fae03cf04910c84969c207b8296df3c7453a0d7fcffcc15a5adfa43bb54a
  pageDirectory: concepts
  sources:
    - evaluate-conversations-databricks-on-aws.md
    - monitor-genai-apps-in-production-databricks-on-aws.md
  confidence: 1
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - multi-turn-conversation-evaluation
    - MCE
    - Multi-Turn Evaluation
    - Multi-turn Evaluation
    - Multi-turn evaluation
  citations:
    - file: evaluate-conversations-databricks-on-aws.md
    - file: monitor-genai-apps-in-production-databricks-on-aws.md
title: Multi-turn Conversation Evaluation
description: A paradigm for assessing conversational AI systems at the session level rather than individual turns, capturing user frustration, conversation completeness, knowledge retention, and dialogue coherence.
tags:
  - conversational-ai
  - evaluation
  - mlflow
timestamp: "2026-06-19T10:23:07.347Z"
---

# Multi-turn Conversation Evaluation

**Multi-turn Conversation Evaluation** is a technique for assessing conversational AI systems across entire conversation sessions, rather than evaluating individual turns in isolation. It captures quality patterns that emerge over multiple interactions, such as user frustration dynamics, conversation completeness, knowledge retention, and dialogue coherence. ^[evaluate-conversations-databricks-on-aws.md]

## Overview

Traditional single-turn evaluation assesses each agent response independently. However, conversational agents require evaluation at the session level to capture important quality dimensions that only become apparent across multiple exchanges. Multi-turn evaluation addresses these needs by grouping traces into conversation sessions and applying judges that analyze the entire conversation history. ^[evaluate-conversations-databricks-on-aws.md]

Multi-turn judges can be used both for offline evaluation during development and for continuous monitoring in production. ^[evaluate-conversations-databricks-on-aws.md, monitor-genai-apps-in-production-databricks-on-aws.md]

> **Note:** Multi-turn evaluation is [experimental](https://docs.databricks.com/aws/en/release-notes/release-types). The API and behavior might change in future releases. ^[evaluate-conversations-databricks-on-aws.md]

## Prerequisites

- MLflow 3.10.0 or later
- Your agent must be instrumented to track session IDs on traces (see [Track users and sessions](/concepts/mlflow-user-and-session-tracking.md)) ^[evaluate-conversations-databricks-on-aws.md]

## Two Approaches

MLflow supports two approaches for evaluating conversations:

### Evaluate Pre-Generated Conversations

Evaluate existing conversations that have already been traced. Use this approach when you have:
- Production conversation data to analyze
- Pre-recorded test conversations from QA or user studies
- Conversations from a previous agent version for comparison ^[evaluate-conversations-databricks-on-aws.md]

**Step 1: Tag traces with session IDs**

When building your agent, set session IDs on traces to group them into conversations:

```python
import mlflow

@mlflow.trace
def my_chatbot(question, session_id):
    mlflow.update_current_trace(
        tags={"mlflow.trace.session": session_id}
    )
    # ... your chatbot logic
```

^[evaluate-conversations-databricks-on-aws.md]

**Step 2: Retrieve and evaluate sessions**

Get traces from your experiment and pass them to `mlflow.genai.evaluate`. MLflow automatically groups traces by session ID:

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

^[evaluate-conversations-databricks-on-aws.md]

You can also retrieve complete sessions directly using `mlflow.search_sessions`:

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

^[evaluate-conversations-databricks-on-aws.md]

### Simulate Conversations During Evaluation

Generate new conversations by simulating user interactions. This enables testing different agent versions with consistent goals and personas:

```python
import mlflow
from mlflow.genai.simulators import ConversationSimulator
from mlflow.genai.scorers import ConversationCompleteness, Safety

# Define test scenarios
simulator = ConversationSimulator(
    test_cases=[
        {"goal": "Successfully set up experiment tracking"},
        {"goal": "Identify the root cause of a deployment error"},
        {
            "goal": "Understand how to implement model versioning",
            "persona": "You are a beginner who needs detailed explanations",
        },
    ],
    max_turns=5,
)

# Your agent's predict function
def predict_fn(input: list[dict], **kwargs) -> str:
    # input is the conversation history
    response = your_agent.chat(input)
    return response

# Simulate conversations and evaluate
results = mlflow.genai.evaluate(
    data=simulator,
    predict_fn=predict_fn,
    scorers=[
        ConversationCompleteness(),
        Safety(),
    ],
)
```

^[evaluate-conversations-databricks-on-aws.md]

For complete documentation on conversation simulation, including test case definition, predict function interfaces, and configuration options, see [Conversation Simulation](/concepts/conversation-simulation.md). ^[evaluate-conversations-databricks-on-aws.md]

## Multi-Turn Judges

### Built-In Judges

MLflow provides built-in multi-turn judges for evaluating conversation quality. For the complete list and detailed documentation, see the [MLflow predefined scorers documentation](/concepts/mlflow-genai-predefined-scorers.md) and the [Scorers and LLM Judges](/concepts/scorers-and-llm-judges.md) page. ^[evaluate-conversations-databricks-on-aws.md]

### Custom Judges

Create custom multi-turn judges using `make_judge`. Use the `{{ conversation }}` template variable to access the full conversation history:

```python
from mlflow.genai.judges import make_judge
from typing import Literal

# Create a custom multi-turn judge
politeness_judge = make_judge(
    name="politeness",
    instructions=(
        "Evaluate whether the assistant maintained a polite and professional "
        "tone throughout this conversation:\n\n{{ conversation }}\n\n"
        "Rate as 'consistently_polite', 'mostly_polite', or 'impolite'."
    ),
    feedback_value_type=Literal["consistently_polite", "mostly_polite", "impolite"],
)

# Get traces from your experiment
traces = mlflow.search_traces(
    filter_string="attributes.status = 'OK'",
    return_type="list",
)

# Use in evaluation
results = mlflow.genai.evaluate(
    data=traces,
    scorers=[politeness_judge],
)
```

^[evaluate-conversations-databricks-on-aws.md]

The `{{ conversation }}` variable injects the complete conversation history in a readable format for the judge to analyze. ^[evaluate-conversations-databricks-on-aws.md]

> **Note:** The `{{ conversation }}` variable can only be used with `{{ expectations }}`, not with `{{ inputs }}`, `{{ outputs }}`, or `{{ trace }}`. ^[evaluate-conversations-databricks-on-aws.md]

## How Assessments Are Stored

Multi-turn assessments are stored on the **first trace** (chronologically) in each session. This design ensures:
- Assessments remain stable even as new turns are added to a conversation
- You can easily find conversation-level assessments by looking at session start traces
- The Sessions UI can efficiently display conversation metrics ^[evaluate-conversations-databricks-on-aws.md]

Assessments include metadata identifying them as conversation-level, including the `session_id` linking the assessment to the full conversation. ^[evaluate-conversations-databricks-on-aws.md]

## Production Monitoring with Multi-Turn Judges

Production monitoring supports multi-turn judges that evaluate entire conversations rather than individual traces. These judges assess quality patterns across multiple interactions, such as user frustration and conversation completeness. ^[monitor-genai-apps-in-production-databricks-on-aws.md]

The monitoring job automatically groups traces into conversations based on the `mlflow.trace.session` tag. Multi-turn judges run after a conversation is considered complete — by default, a conversation is complete when no new traces with that session ID are ingested for **5 minutes**. To configure this buffer, set the `MLFLOW_ONLINE_SCORING_DEFAULT_SESSION_COMPLETION_BUFFER_SECONDS` environment variable on the monitoring job. ^[monitor-genai-apps-in-production-databricks-on-aws.md]

Multi-turn judges are registered and started the same way as single-turn judges: ^[monitor-genai-apps-in-production-databricks-on-aws.md]

```python
from mlflow.genai.scorers import (
    ConversationCompleteness,
    UserFrustration,
    ScorerSamplingConfig,
)

# Register and start multi-turn judges just like single-turn judges
completeness_scorer = ConversationCompleteness().register(name="conversation_completeness")
completeness_scorer = completeness_scorer.start(
    sampling_config=ScorerSamplingConfig(sample_rate=1.0),
)

frustration_scorer = UserFrustration().register(name="user_frustration")
frustration_scorer = frustration_scorer.start(
    sampling_config=ScorerSamplingConfig(sample_rate=1.0),
)
```

^[monitor-genai-apps-in-production-databricks-on-aws.md]

## Working with Specific Sessions

To evaluate a specific session, use `mlflow.search_traces` with a filter string:

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

^[evaluate-conversations-databricks-on-aws.md]

## Related Concepts

- [Conversation Simulation](/concepts/conversation-simulation.md) — Generate synthetic conversations for testing
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Continuous quality assessment in production
- [Custom Judges](/concepts/custom-judges.md) — Build custom LLM judges using `make_judge`
- [Scorers and LLM Judges](/concepts/scorers-and-llm-judges.md) — Understand the metrics that power evaluation
- [Track users and sessions](/concepts/mlflow-user-and-session-tracking.md) — Instrument agents with session IDs
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) — The evaluation harness for offline assessment
- [Predefined scorers](/concepts/mlflow-genai-predefined-scorers.md) — Built-in single-turn and multi-turn scorers

## Sources

- evaluate-conversations-databricks-on-aws.md
- monitor-genai-apps-in-production-databricks-on-aws.md

# Citations

1. [evaluate-conversations-databricks-on-aws.md](/references/evaluate-conversations-databricks-on-aws-f530405b.md)
2. [monitor-genai-apps-in-production-databricks-on-aws.md](/references/monitor-genai-apps-in-production-databricks-on-aws-41428693.md)
