---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bb6a0157a9876a4c68a4f79f1235fbfcff84147817568920f58da84f2c72d594
  pageDirectory: concepts
  sources:
    - evaluate-conversations-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - multi-turn-llm-judges
    - MLJ
  citations:
    - file: evaluate-conversations-databricks-on-aws.md
title: Multi-turn LLM Judges
description: LLM-based evaluators that analyze full conversation history using built-in scorers like ConversationCompleteness and UserFrustration, or custom judges via make_judge with the {{ conversation }} template variable.
tags:
  - llm-judges
  - evaluation
  - mlflow
timestamp: "2026-06-19T10:23:24.845Z"
---

# Multi-turn LLM Judges

**Multi-turn LLM Judges** are evaluation components that assess entire conversation sessions rather than individual turns. They are essential for evaluating conversational AI systems where quality emerges over multiple interactions, such as user frustration patterns, conversation completeness, or overall dialogue coherence. ^[evaluate-conversations-databricks-on-aws.md]

## Overview

Traditional single-turn evaluation assesses each agent response independently. However, conversational agents require evaluation at the session level to capture aspects that span multiple interactions. Multi-turn evaluation addresses this need by grouping traces into conversation sessions and applying judges that analyze the entire conversation history. ^[evaluate-conversations-databricks-on-aws.md]

Key capabilities that multi-turn judges evaluate include:

- **User frustration**: Did the user become frustrated? Was it resolved?
- **Conversation completeness**: Were all user questions answered by the end of the conversation?
- **Knowledge retention**: Does the agent remember information from earlier in the conversation?
- **Dialogue coherence**: Does the conversation flow naturally?

^[evaluate-conversations-databricks-on-aws.md]

## Prerequisites

Multi-turn evaluation requires MLflow 3.10.0 or later, installed with Databricks support. The agent must also be instrumented to track [session IDs](/concepts/session-id-tracing.md) on traces, using the `mlflow.trace.session` tag. ^[evaluate-conversations-databricks-on-aws.md]

## Approaches

MLflow supports two approaches for evaluating conversations:

1. **Evaluate pre-generated conversations**: Assess existing conversations that have already been traced. Use this when you have production conversation data to analyze, pre-recorded test conversations from QA or user studies, or conversations from a previous agent version for comparison.

2. **Simulate conversations during evaluation**: Generate new conversations by simulating user interactions with your agent. Use this to test a new agent version systematically with consistent scenarios, generate diverse test scenarios at scale, or stress-test your agent with specific user behaviors and edge cases.

^[evaluate-conversations-databricks-on-aws.md]

## Built-in Multi-turn Judges

MLflow provides built-in multi-turn judges for evaluating conversation quality. These predefined scorers include:

| Judge | Purpose |
|-------|---------|
| `ConversationCompleteness()` | Assesses whether the agent answered all user questions |
| `UserFrustration()` | Evaluates whether the user became frustrated during the conversation |
| `Safety()` | Checks conversation content for safety violations |

For the complete list, see the [MLflow predefined scorers documentation](/concepts/mlflow-genai-predefined-scorers.md) and the [Scorers and LLM Judges](/concepts/scorers-and-llm-judges.md) page. ^[evaluate-conversations-databricks-on-aws.md]

## Custom Multi-turn Judges

Create custom multi-turn judges using make_judge()|make_judge, the `make_judge()` function. Use the `{{ conversation }}` template variable to access the full conversation history in the judge's instructions: ^[evaluate-conversations-databricks-on-aws.md]

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

The `{{ conversation }}` variable injects the complete conversation history in a readable format for the judge to analyze. ^[evaluate-conversations-databricks-on-aws.md]

### Limitations

The `{{ conversation }}` variable can only be used with `{{ expectations }}`. It cannot be combined with `{{ inputs }}`, `{{ outputs }}`, or `{{ trace }}`. ^[evaluate-conversations-databricks-on-aws.md]

## How Assessments Are Stored

Multi-turn assessments are stored on the **first trace** (chronologically) in each session. This design ensures:

- Assessments remain stable even as new turns are added to a conversation
- You can easily find conversation-level assessments by looking at session start traces
- The Sessions UI can efficiently display conversation metrics

Assessments include `session_id` metadata identifying them as conversation-level assessments. ^[evaluate-conversations-databricks-on-aws.md]

## Usage

### Evaluating Pre-generated Conversations

Retrieve traces from your experiment and pass them to `mlflow.genai.evaluate()`. MLflow automatically groups traces by session ID: ^[evaluate-conversations-databricks-on-aws.md]

```python
from mlflow.genai.scorers import ConversationCompleteness, UserFrustration

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

### Simulating Conversations During Evaluation

Use [ConversationSimulator](/concepts/conversationsimulator.md) to generate new conversations with consistent goals and personas: ^[evaluate-conversations-databricks-on-aws.md]

```python
from mlflow.genai.simulators import ConversationSimulator
from mlflow.genai.scorers import ConversationCompleteness, Safety

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

def predict_fn(input: list[dict], **kwargs) -> str:
    response = your_agent.chat(input)
    return response

results = mlflow.genai.evaluate(
    data=simulator,
    predict_fn=predict_fn,
    scorers=[ConversationCompleteness(), Safety()],
)
```

### Evaluating a Specific Session

Use `mlflow.search_traces` with a filter string targeting the session ID: ^[evaluate-conversations-databricks-on-aws.md]

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

## Usage Contexts

Multi-turn judges can be used both for offline evaluation during development and for continuous monitoring in production. ^[evaluate-conversations-databricks-on-aws.md]

## Related Concepts

- Single-turn LLM Judges – Traditional judges that evaluate individual turns independently
- [ConversationSimulator](/concepts/conversationsimulator.md) – Tool for generating synthetic test conversations
- [Session ID Tracking](/concepts/session-id-tracking.md) – Instrumentation required for grouping traces into sessions
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) – Deploying multi-turn judges for continuous quality monitoring
- make_judge()|Make Judge API – The `make_judge()` function for creating custom evaluators
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) – The `mlflow.genai.evaluate()` API for offline assessment

## Sources

- evaluate-conversations-databricks-on-aws.md

# Citations

1. [evaluate-conversations-databricks-on-aws.md](/references/evaluate-conversations-databricks-on-aws-f530405b.md)
