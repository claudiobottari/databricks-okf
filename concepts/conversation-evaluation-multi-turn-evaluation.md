---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1d732da946c207d47a51fb600ece37519c971269f09a7d2d2380f6d165114221
  pageDirectory: concepts
  sources:
    - evaluate-conversations-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - conversation-evaluation-multi-turn-evaluation
    - CE(E
    - evaluate-conversations|evaluating pre-generated conversations
  citations:
    - file: evaluate-conversations-databricks-on-aws.md
title: Conversation Evaluation (Multi-turn Evaluation)
description: Assessment of entire conversation sessions rather than individual turns, capturing session-level quality like user frustration, conversation completeness, knowledge retention, and dialogue coherence.
tags:
  - mlflow
  - genai
  - evaluation
  - conversational-ai
timestamp: "2026-06-19T18:41:40.887Z"
---

# Conversation Evaluation (Multi-turn Evaluation)

**Conversation Evaluation** (also called **Multi-turn Evaluation**) is a method for assessing the quality of an entire conversational session, rather than evaluating each individual turn in isolation. It is essential for conversational AI systems where key quality attributes — such as user frustration patterns, conversation completeness, and overall dialogue coherence — only emerge over multiple interactions. ^[evaluate-conversations-databricks-on-aws.md]

Multi-turn judges can be used both for offline evaluation during development and for continuous monitoring in production. This feature is experimental and its API may change in future releases. ^[evaluate-conversations-databricks-on-aws.md]

## Prerequisites

To use multi-turn evaluation, you must install MLflow 3.10.0 or later (`pip install --upgrade 'mlflow[databricks]>=3.10'`). Your agent must also be instrumented to track session IDs on traces — see the documentation on [tracking users and sessions](/concepts/trace-grouping-by-users-and-sessions.md) for details on how to set session IDs. ^[evaluate-conversations-databricks-on-aws.md]

## Two Approaches

MLflow supports two distinct approaches for evaluating conversations: evaluating pre-generated conversations and simulating conversations during evaluation. ^[evaluate-conversations-databricks-on-aws.md]

### Evaluate Pre-Generated Conversations

Use this approach when you already have traced conversations, such as production data, pre-recorded test conversations from QA or user studies, or conversations from a previous agent version that you wish to compare. The workflow involves tagging traces with session IDs, then retrieving and evaluating those sessions. ^[evaluate-conversations-databricks-on-aws.md]

To tag traces, call `mlflow.update_current_trace` with the tag `"mlflow.trace.session"` set to the session ID. MLflow automatically groups traces by session ID when passed to `mlflow.genai.evaluate`. You can also retrieve complete sessions directly using `mlflow.search_sessions`. ^[evaluate-conversations-databricks-on-aws.md]

### Simulate Conversations During Evaluation

Generate new conversations by simulating user interactions with your agent. This is useful for testing a new agent version systematically with consistent scenarios, generating diverse test cases at scale, or stress-testing with specific user behaviors and edge cases. A `ConversationSimulator` is defined with test cases (each specifying a goal and optionally a persona), and the simulator is passed as the `data` parameter to `mlflow.genai.evaluate` alongside a `predict_fn`. ^[evaluate-conversations-databricks-on-aws.md]

## Multi-Turn Judges

MLflow provides built-in multi-turn judges (such as `ConversationCompleteness`, `UserFrustration`, and `Safety`) and also allows creation of custom judges. ^[evaluate-conversations-databricks-on-aws.md]

### Built-in Judges

Predefined multi-turn scorers are available for evaluating conversation quality. These include judges that assess whether the agent answered all questions, whether the user became frustrated, and other session-level criteria. For the complete list, see the MLflow [predefined scorers documentation](/concepts/mlflow-genai-predefined-scorers.md) and the [Scorers and LLM Judges](/concepts/scorers-and-llm-judges.md) page. ^[evaluate-conversations-databricks-on-aws.md]

### Custom Judges

Create custom multi-turn judges using `mlflow.genai.make_judge`. Use the `{{ conversation }}` template variable to inject the full conversation history into the judge’s instructions. The variable can only be used together with `{{ expectations }}`, not with `{{ inputs }}`, `{{ outputs }}`, or `{{ trace }}`. ^[evaluate-conversations-databricks-on-aws.md]

Example of a custom politeness judge:

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

## How Assessments are Stored

Multi-turn assessments are stored on the **first trace** (chronologically) in each session. This design ensures that assessments remain stable even as new turns are added, that conversation-level assessments can be easily found by looking at session start traces, and that the Sessions UI can efficiently display conversation metrics. Assessments include metadata (notably `session_id`) that identifies them as conversation-level. ^[evaluate-conversations-databricks-on-aws.md]

## Working with Specific Sessions

To evaluate a particular session, use `mlflow.search_traces` with a filter string that matches the session ID tag:

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

- [MLflow](/concepts/mlflow.md) — The platform providing multi-turn evaluation capabilities.
- [LLM Judges](/concepts/llm-judges.md) — Foundation for building both single-turn and multi-turn scorers.
- [Production Monitoring](/concepts/production-monitoring.md) — How to apply multi-turn judges to continuously monitor conversations in production.
- [Conversation Simulation](/concepts/conversation-simulation.md) — Detailed documentation on the `ConversationSimulator` and test case definition.
- [Predefined Scorers](/concepts/mlflow-genai-predefined-scorers.md) — Reference for all built-in scorers (single-turn and multi-turn).
- [Custom LLM Judges](/concepts/custom-llm-judges.md) — Build custom judges with `make_judge`.

## Sources

- evaluate-conversations-databricks-on-aws.md

# Citations

1. [evaluate-conversations-databricks-on-aws.md](/references/evaluate-conversations-databricks-on-aws-f530405b.md)
