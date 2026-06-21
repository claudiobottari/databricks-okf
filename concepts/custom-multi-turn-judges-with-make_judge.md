---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9c4e43a6724a9e8e7fa38893a18a5e620ec7da1f14c77e613fec64e04d604057
  pageDirectory: concepts
  sources:
    - evaluate-conversations-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - custom-multi-turn-judges-with-make_judge
    - CMJWM
  citations:
    - file: evaluate-conversations-databricks-on-aws.md
title: Custom Multi-turn Judges with make_judge
description: The ability to create custom multi-turn evaluation judges using MLflow's make_judge API, leveraging the {{ conversation }} template variable to inject full conversation history.
tags:
  - llm-judges
  - custom-evaluation
  - mlflow
timestamp: "2026-06-19T10:23:49.622Z"
---

# Custom Multi-turn Judges with make_judge

**Custom Multi-turn Judges with `make_judge`** allow you to create LLM-based evaluators that assess entire conversation sessions rather than individual turns. These judges analyze the full conversation history to evaluate criteria such as user frustration, conversation completeness, knowledge retention, and dialogue coherence. ^[evaluate-conversations-databricks-on-aws.md]

## Overview

Traditional single-turn evaluation assesses each agent response independently. However, conversational agents require evaluation at the session level to capture quality dimensions that emerge over multiple interactions. Multi-turn judges address this need by grouping traces into conversation sessions and applying evaluation criteria that analyze the entire conversation history. ^[evaluate-conversations-databricks-on-aws.md]

Multi-turn judges can be used both for offline evaluation during development and for [Production Monitoring for GenAI|continuous monitoring in production](/concepts/production-monitoring-for-genai-applications.md). ^[evaluate-conversations-databricks-on-aws.md]

## Prerequisites

- Install MLflow 3.10.0 or later: `pip install --upgrade 'mlflow[databricks]>=3.10'`
- Your agent must be instrumented to track session IDs on traces. See [Track users and sessions](/concepts/mlflow-user-and-session-tracking.md) for how to set session IDs on your traces. ^[evaluate-conversations-databricks-on-aws.md]

## Creating a Custom Multi-turn Judge

Use `make_judge` from `mlflow.genai.judges` to create custom multi-turn judges. The key difference from single-turn judges is the use of the `{{ conversation }}` template variable, which injects the complete conversation history in a readable format for the judge to analyze. ^[evaluate-conversations-databricks-on-aws.md]

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
```

### Template Variables

The `{{ conversation }}` variable is the primary template variable for multi-turn judges. It provides the full conversation history to the LLM judge for analysis. ^[evaluate-conversations-databricks-on-aws.md]

**Important:** The `{{ conversation }}` variable can only be used with `{{ expectations }}`, not with `{{ inputs }}`, `{{ outputs }}`, or `{{ trace }}`. ^[evaluate-conversations-databricks-on-aws.md]

## Using Multi-turn Judges in Evaluation

### Evaluating Pre-generated Conversations

To evaluate existing conversations that have already been traced, retrieve traces from your experiment and pass them to `mlflow.genai.evaluate`. MLflow automatically groups traces by session ID: ^[evaluate-conversations-databricks-on-aws.md]

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

### Evaluating Specific Sessions

To evaluate a specific session, use `mlflow.search_traces` with a filter string: ^[evaluate-conversations-databricks-on-aws.md]

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

### Simulating Conversations During Evaluation

You can also generate new conversations by simulating user interactions with your agent. This enables testing different agent versions with consistent goals and personas: ^[evaluate-conversations-databricks-on-aws.md]

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

## Built-in Multi-turn Judges

MLflow provides built-in multi-turn judges for evaluating conversation quality. For the complete list and detailed documentation, see the MLflow predefined scorers documentation and the [Scorers and LLM Judges](/concepts/scorers-and-llm-judges.md) page. ^[evaluate-conversations-databricks-on-aws.md]

## How Assessments Are Stored

Multi-turn assessments are stored on the **first trace** (chronologically) in each session. This design ensures: ^[evaluate-conversations-databricks-on-aws.md]

- Assessments remain stable even as new turns are added to a conversation
- You can easily find conversation-level assessments by looking at session start traces
- The Sessions UI can efficiently display conversation metrics

Assessments include metadata identifying them as conversation-level, including a `session_id` that links the assessment to the full conversation. ^[evaluate-conversations-databricks-on-aws.md]

## Best Practices

- **Tag traces with session IDs** when building your agent to enable multi-turn evaluation. Use `mlflow.update_current_trace(tags={"mlflow.trace.session": session_id})` within your traced functions. ^[evaluate-conversations-databricks-on-aws.md]
- **Use representative test scenarios** when simulating conversations to cover a range of user behaviors and edge cases.
- **Combine custom and built-in judges** to evaluate both domain-specific criteria and general conversation quality metrics.
- **Align judges with human feedback** by iteratively refining judge instructions based on expert annotations.

## Related Concepts

- make_judge()|Make Judge API — The `make_judge()` function for creating custom evaluators
- [Conversation Evaluation](/concepts/conversation-evaluation.md) — The broader framework for evaluating multi-turn conversations
- [Conversation Simulation](/concepts/conversation-simulation.md) — Generating synthetic conversations for testing
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Deploying multi-turn judges for continuous monitoring
- [Track users and sessions](/concepts/mlflow-user-and-session-tracking.md) — Instrumenting agents with session IDs
- MLflow predefined scorers — Built-in single-turn and multi-turn scorers
- [Scorers and LLM Judges](/concepts/scorers-and-llm-judges.md) — Reference for all scorer types

## Sources

- evaluate-conversations-databricks-on-aws.md

# Citations

1. [evaluate-conversations-databricks-on-aws.md](/references/evaluate-conversations-databricks-on-aws-f530405b.md)
