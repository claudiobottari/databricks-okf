---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 41e1e6260eb87e3d8637256c27ec465bb44e834043b1d7d2baae5d0682e1a2c8
  pageDirectory: concepts
  sources:
    - evaluate-conversations-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - conversation-simulation-for-evaluation
    - CSFE
  citations:
    - file: evaluate-conversations-databricks-on-aws.md
title: Conversation Simulation for Evaluation
description: Approach that generates new conversations by simulating user interactions with defined test cases, goals, and personas to test agent versions systematically.
tags:
  - mlflow
  - genai
  - simulation
  - evaluation
timestamp: "2026-06-19T18:42:01.520Z"
---

---
title: Conversation Simulation for Evaluation
summary: Generating new conversations by simulating user interactions to test agent versions with consistent goals and personas.
sources:
  - evaluate-conversations-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T12:12:30.033Z"
updatedAt: "2026-06-18T12:12:30.033Z"
tags:
  - simulation
  - testing
  - conversational-ai
  - mlflow
aliases:
  - conversation-simulation-for-evaluation
  - CSFE
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# Conversation Simulation for Evaluation

**Conversation Simulation for Evaluation** is an MLflow GenAI technique that generates synthetic, multi-turn conversations to assess how an agent performs under consistent, repeatable conditions. Instead of evaluating pre-recorded chat logs, the developer defines a set of scenarios (goals, personas, and turn limits) and lets a simulator drive those scenarios against the agent, producing a full trace of every interaction. Those traces are then scored by the same set of judges used in offline or production evaluation, making the comparison between configurations direct and fair. ^[evaluate-conversations-databricks-on-aws.md]

## Overview

Traditional single-turn evaluation scores each agent response independently. Conversational agents, however, need session-level assessment to capture qualities like user frustration, conversation completeness, knowledge retention across turns, and dialogue coherence. Conversation simulation addresses this need by generating new conversations from a fixed set of test scenarios, rather than relying on pre-existing production logs. ^[evaluate-conversations-databricks-on-aws.md]

## When to Use Simulation

Use conversation simulation when you want:

- To test a new agent version systematically with consistent scenarios.
- To generate diverse test scenarios at scale without waiting for production data.
- To stress-test your agent with specific user behaviors and edge cases.

Use pre-generated evaluation (evaluating traced production sessions) when you have existing conversation data to analyze, pre-recorded test conversations from QA or user studies, or conversations from a previous agent version for comparison. ^[evaluate-conversations-databricks-on-aws.md]

## How It Works

### Defining the Simulator

Create a [ConversationSimulator](/concepts/conversationsimulator.md) object to define the test scenarios:

```python
from mlflow.genai.simulators import ConversationSimulator

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
```

The simulator runs each scenario against your agent's predict function, generating conversations up to the specified turn limit. ^[evaluate-conversations-databricks-on-aws.md]

### Running the Evaluation

Pass the simulator to [mlflow.genai.evaluate()](/concepts/mlflowgenaievaluate.md) with the same predict function and set of [judges](/concepts/llm-judges.md) you want to compare across configurations:

```python
results = mlflow.genai.evaluate(
    data=simulator,
    predict_fn=predict_fn,
    scorers=[
        ConversationCompleteness(),
        Safety(),
    ],
)
```

### Using Multi-Turn Judges

The `{{ conversation }}` template variable in a [judge's](/concepts/llm-judges.md) instructions gives the judge access to the full conversation history. This variable can only be used with `{{ expectations }}`, not with `{{ inputs }}`, `{{ outputs }}`, or `{{ trace }}`. ^[evaluate-conversations-databricks-on-aws.md]

```python
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

## How Assessments Are Stored

Multi-turn assessments are stored on the first trace (chronologically) in each session. This design ensures:

- Assessments remain stable even as new turns are added to a conversation.
- You can easily find conversation-level assessments by looking at session start traces.
- The Sessions UI can efficiently display conversation metrics.

Each assessment includes `session_id` metadata that links it to the full conversation. ^[evaluate-conversations-databricks-on-aws.md]

## Prerequisites

- Install MLflow 3.10.0 or later: `pip install --upgrade 'mlflow[databricks]>=3.10'`
- Your agent must be instrumented to track session IDs on traces. See [Track users and sessions](/concepts/mlflow-user-and-session-tracking.md) for how to set session IDs. ^[evaluate-conversations-databricks-on-aws.md]

## Related Concepts

- [ConversationSimulator](/concepts/conversationsimulator.md) — The API for defining test scenarios
- [Multi-turn Judges](/concepts/multi-turn-judge.md) — Judges that analyze full conversation history
- [Pre-generated evaluation](/concepts/pre-generated-conversation-evaluation.md) — The alternative approach that uses traced production data
- make_judge()|Make Judge API — The `make_judge()` function for creating custom evaluators
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) — The `mlflow.genai.evaluate()` API for offline assessment
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Deploying multi-turn judges for continuous quality monitoring
- [Track users and sessions](/concepts/mlflow-user-and-session-tracking.md) — How to instrument your agent with session IDs

## Sources

- evaluate-conversations-databricks-on-aws.md

# Citations

1. [evaluate-conversations-databricks-on-aws.md](/references/evaluate-conversations-databricks-on-aws-f530405b.md)
