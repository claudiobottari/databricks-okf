---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fe38a8b4528d30697d955aa1e0d170c06831ad71f50e55f1f05a4ab428b200b5
  pageDirectory: concepts
  sources:
    - evaluate-conversations-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - conversation-evaluation
    - Conversational AI
    - Conversational AI Evaluation
    - conversational AI
    - Conversation completeness
    - Conversational AI Evaluation|Conversational metrics
    - conversation-evaluation-multi-turn-evaluation
    - CE(E
    - evaluate-conversations|evaluating pre-generated conversations
  citations:
    - file: evaluate-conversations-databricks-on-aws.md
title: Conversation Evaluation
description: Assessing entire conversation sessions rather than individual turns to capture multi-interaction quality like user frustration, completeness, and coherence.
tags:
  - evaluation
  - conversational-ai
  - mlflow
timestamp: "2026-06-18T12:12:19.875Z"
---

# Conversation Evaluation

**Conversation evaluation** enables you to assess entire conversation sessions rather than individual turns. This is essential for evaluating conversational AI systems where quality emerges over multiple interactions, such as user frustration patterns, conversation completeness, or overall dialogue coherence. Multi-turn judges can be used both for offline evaluation during development and for continuous monitoring in production. ^[evaluate-conversations-databricks-on-aws.md]

## Prerequisites

- Install MLflow 3.10.0 or later: `pip install --upgrade 'mlflow[databricks]>=3.10'`
- Your agent must be instrumented to track [session IDs](/concepts/session-id-tracing.md) on traces. See [Track users and sessions](https://mlflow.org/docs/latest/genai/tracing/track-users-sessions/) for instructions. ^[evaluate-conversations-databricks-on-aws.md]

## Two Approaches

MLflow supports two approaches for evaluating conversations:

| Approach | Use case |
|----------|----------|
| **Evaluate pre-generated conversations** | When you have production data, pre-recorded test conversations, or conversations from a previous agent version for comparison. |
| **Simulate conversations during evaluation** | When you want to test a new agent version systematically, generate diverse test scenarios at scale, or stress-test with specific user behaviors. |

^[evaluate-conversations-databricks-on-aws.md]

### Evaluate Pre‑Generated Conversations

Evaluate conversations that have already been traced. This is useful for analyzing production data or pre-recorded test conversations.

1. **Tag traces with session IDs.** When building your agent, set session IDs on traces using `mlflow.update_current_trace(tags={"mlflow.trace.session": session_id})`.
2. **Retrieve and evaluate sessions.** Use `mlflow.search_traces` to get traces and pass them to `mlflow.genai.evaluate`. MLflow automatically groups traces by session ID. You can also retrieve complete sessions directly with `mlflow.search_sessions`. ^[evaluate-conversations-databricks-on-aws.md]

```python
import mlflow
from mlflow.genai.scorers import ConversationCompleteness, UserFrustration

traces = mlflow.search_traces(
    filter_string="attributes.status = 'OK'",
    return_type="list",
)
results = mlflow.genai.evaluate(
    data=traces,
    scorers=[ConversationCompleteness(), UserFrustration()],
)
```

### Simulate Conversations During Evaluation

Generate new conversations by simulating user interactions. This enables testing different agent versions with consistent goals and personas using a [ConversationSimulator](/concepts/conversationsimulator.md). ^[evaluate-conversations-databricks-on-aws.md]

```python
import mlflow
from mlflow.genai.simulators import ConversationSimulator
from mlflow.genai.scorers import ConversationCompleteness, Safety

simulator = ConversationSimulator(
    test_cases=[
        {"goal": "Successfully set up experiment tracking"},
        {"goal": "Identify the root cause of a deployment error"},
        {"goal": "Understand how to implement model versioning",
         "persona": "You are a beginner who needs detailed explanations"},
    ],
    max_turns=5,
)

def predict_fn(input: list[dict], **kwargs) -> str:
    response = your_agent.chat(input)
    return response

results = mlflow.genai.evaluate(
    data=simulator,
    predict_fn=predict_fn,
    scorers=[ConversationCompleteness(), Safety()],
)
```

## Multi‑Turn Judges

Multi-turn judges analyze the full conversation history rather than individual turns.

### Built‑In Judges

MLflow provides built-in multi-turn judges such as:
- `ConversationCompleteness()` – Did the agent answer all questions?
- `UserFrustration()` – Did the user become frustrated?
- `Safety()` – Evaluate conversation safety.

For the complete list, see the [MLflow predefined scorers documentation](https://mlflow.org/docs/latest/genai/eval-monitor/scorers/llm-judge/predefined/#multi-turn). ^[evaluate-conversations-databricks-on-aws.md]

### Custom Judges

Create custom multi-turn judges using make_judge()|`make_judge`. Use the `{{ conversation }}` template variable to access the full conversation history. ^[evaluate-conversations-databricks-on-aws.md]

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

results = mlflow.genai.evaluate(
    data=traces,
    scorers=[politeness_judge],
)
```

Note that `{{ conversation }}` can only be used with `{{ expectations }}`, not with `{{ inputs }}`, `{{ outputs }}`, or `{{ trace }}`. ^[evaluate-conversations-databricks-on-aws.md]

## How Assessments Are Stored

Multi-turn assessments are stored on the **first trace** (chronologically) in each session. This ensures assessments remain stable as new turns are added and enables efficient display of conversation metrics in the Sessions UI. Assessments include metadata identifying them as conversation-level, including `session_id`. ^[evaluate-conversations-databricks-on-aws.md]

## Working with Specific Sessions

To evaluate a specific session, filter traces by session ID: ^[evaluate-conversations-databricks-on-aws.md]

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

## Related Concepts

- [Multi-turn Judges](/concepts/multi-turn-judge.md) – The core scoring mechanism for conversation evaluation.
- [Conversation Simulation](/concepts/conversationsimulator.md) – Generating synthetic conversations for testing.
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) – Deploying multi-turn judges in production.
- [MLflow Tracing](/concepts/mlflow-tracing.md) – Instrumenting agents with session IDs and traces.
- [Custom Judges](/concepts/custom-judges.md) – Creating evaluators with `make_judge` for conversation-specific criteria.

## Sources

- evaluate-conversations-databricks-on-aws.md

# Citations

1. [evaluate-conversations-databricks-on-aws.md](/references/evaluate-conversations-databricks-on-aws-f530405b.md)
