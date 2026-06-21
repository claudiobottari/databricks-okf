---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 751a556891e1091e9a95a5e67cfa283e54b9197c18d1bdbcc93784fd166e1fa4
  pageDirectory: concepts
  sources:
    - monitor-genai-apps-in-production-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - multi-turn-conversation-judges
    - MCJ
    - Multi-Turn Conversations
    - Multi-turn Conversations
    - Multi-turn conversation
    - Evaluate Conversations
    - Evaluate conversations
  citations:
    - file: monitor-genai-apps-in-production-databricks-on-aws.md
title: Multi-turn Conversation Judges
description: Scorers that evaluate entire conversations by grouping traces via session tags, assessing quality patterns like user frustration and conversation completeness across multiple interactions.
tags:
  - mlflow
  - multi-turn
  - conversations
  - evaluation
timestamp: "2026-06-19T19:46:26.880Z"
---

# Multi-turn Conversation Judges

**Multi-turn Conversation Judges** are a type of [LLM Judge (Scorer)](/concepts/llm-judges-and-scorers.md) designed to evaluate entire conversations — consisting of multiple user-assistant interactions — rather than individual traces or single-turn exchanges. These judges assess quality patterns that emerge across multiple turns, providing a holistic view of conversation performance. ^[monitor-genai-apps-in-production-databricks-on-aws.md]

## Overview

In production monitoring, multi-turn judges evaluate conversations as complete units. They are particularly useful for detecting interaction-level phenomena such as user frustration, conversation completeness, and other patterns that cannot be observed from isolated traces. ^[monitor-genai-apps-in-production-databricks-on-aws.md]

Multi-turn judges are registered and started the same way as single-turn judges, using the same `.register()` and `.start()` pattern. They can be combined with single-turn judges in the same experiment. ^[monitor-genai-apps-in-production-databricks-on-aws.md]

## Conversation Grouping and Completion

The monitoring job automatically groups traces into conversations based on the `mlflow.trace.session` tag. Multi-turn judges run after a conversation is considered complete. ^[monitor-genai-apps-in-production-databricks-on-aws.md]

By default, a conversation is considered complete when no new traces with that session ID are ingested for **5 minutes**. This buffer period can be adjusted by setting the `MLFLOW_ONLINE_SCORING_DEFAULT_SESSION_COMPLETION_BUFFER_SECONDS` environment variable on the monitoring job. ^[monitor-genai-apps-in-production-databricks-on-aws.md]

## Available Multi-turn Judges

The following multi-turn judges are available out-of-the-box:

- **ConversationCompleteness** — Evaluates whether a conversation reached a natural conclusion.
- **UserFrustration** — Detects signs of user frustration across multiple interactions.

^[monitor-genai-apps-in-production-databricks-on-aws.md]

## Usage

Multi-turn judges follow the same registration and starting procedure as single-turn judges. They can be used alongside single-turn judges in the same experiment. ^[monitor-genai-apps-in-production-databricks-on-aws.md]

```python
from mlflow.genai.scorers import (
    ConversationCompleteness,
    UserFrustration,
    ScorerSamplingConfig,
)

# Register and start multi-turn judges
completeness_scorer = ConversationCompleteness().register(name="conversation_completeness")
completeness_scorer = completeness_scorer.start(
    sampling_config=ScorerSamplingConfig(sample_rate=1.0),
)

frustration_scorer = UserFrustration().register(name="user_frustration")
frustration_scorer = frustration_scorer.start(
    sampling_config=ScorerSamplingConfig(sample_rate=1.0),
)
```

## Result Storage

For multi-turn judges, assessments are attached to the **first trace** in each session. This differs from single-turn judges, where assessments are attached to the individual trace being evaluated. ^[monitor-genai-apps-in-production-databricks-on-aws.md]

## Combining with Single-turn Judges

Single-turn and multi-turn judges can be combined in the same experiment. Each scorer is registered and started independently, allowing flexible monitoring configurations. ^[monitor-genai-apps-in-production-databricks-on-aws.md]

```python
from mlflow.genai.scorers import Safety, Guidelines, UserFrustration, ScorerSamplingConfig

# Single-turn judges
safety_judge = Safety().register(name="safety")
safety_judge = safety_judge.start(sampling_config=ScorerSamplingConfig(sample_rate=1.0))

# Multi-turn judge
frustration_judge = UserFrustration().register(name="frustration")
frustration_judge = frustration_judge.start(sampling_config=ScorerSamplingConfig(sample_rate=0.3))
```

## Related Concepts

- [LLM Judge (Scorer)](/concepts/llm-judges-and-scorers.md) — The general concept of automated evaluators for GenAI applications.
- [Production Monitoring](/concepts/production-monitoring.md) — The framework that schedules and runs judges on production traces.
- [ScorerSamplingConfig](/concepts/scorersamplingconfig.md) — Configuration for controlling which traces are evaluated and at what rate.
- [MLflow Tracing](/concepts/mlflow-tracing.md) — The mechanism for logging traces from GenAI applications.
- [Conversation Evaluation](/concepts/conversation-evaluation.md) — The broader methodology for assessing multi-turn interactions.

## Sources

- monitor-genai-apps-in-production-databricks-on-aws.md

# Citations

1. [monitor-genai-apps-in-production-databricks-on-aws.md](/references/monitor-genai-apps-in-production-databricks-on-aws-41428693.md)
