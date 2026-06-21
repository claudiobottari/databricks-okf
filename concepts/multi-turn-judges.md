---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f9deaedfec1d95a7a2ea5550c60c8a7ca366f865a4b8d43080e7522ee47a17c0
  pageDirectory: concepts
  sources:
    - built-in-llm-judges-databricks-on-aws.md
    - evaluate-conversations-databricks-on-aws.md
    - scorers-and-llm-judges-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - multi-turn-judges
    - Multi‑Turn Judges
  citations:
    - file: built-in-llm-judges-databricks-on-aws.md
    - file: evaluate-conversations-databricks-on-aws.md
    - file: scorers-and-llm-judges-databricks-on-aws.md
title: Multi-turn Judges
description: LLM judges that evaluate entire conversations rather than individual turns, analyzing the complete conversation history for quality patterns over multiple interactions.
tags:
  - llm-evaluation
  - conversational-ai
  - mlflow
timestamp: "2026-06-19T17:42:26.839Z"
---

# Multi-turn Judges

**Multi-turn judges** are a type of [LLM judge](/concepts/llm-judges.md) that evaluate entire conversations rather than individual turns, assessing quality patterns that emerge over multiple interactions in conversational AI systems.^[built-in-llm-judges-databricks-on-aws.md] They analyze complete session history to capture dimensions such as user frustration, conversation completeness, knowledge retention, and dialogue coherence.^[evaluate-conversations-databricks-on-aws.md]

Multi-turn judges can be used both for offline evaluation during development and for continuous monitoring in production, ensuring consistent quality assessment throughout the application lifecycle.^[scorers-and-llm-judges-databricks-on-aws.md, evaluate-conversations-databricks-on-aws.md]

> **Note**: Multi-turn evaluation is an [experimental](https://docs.databricks.com/aws/en/release-notes/release-types) feature; the API and behavior may change in future releases.^[evaluate-conversations-databricks-on-aws.md]

## Available built-in multi-turn judges

MLflow provides built-in multi-turn judges for common conversation-level quality dimensions.^[built-in-llm-judges-databricks-on-aws.md] For the complete list and detailed documentation, see the [MLflow predefined scorers documentation](https://mlflow.org/docs/latest/genai/eval-monitor/scorers/llm-judge/predefined/#multi-turn).^[built-in-llm-judges-databricks-on-aws.md]

Examples include:

- **`ConversationCompleteness`** – Evaluates whether the agent answered all user questions by the end of the conversation.^[evaluate-conversations-databricks-on-aws.md]
- **`UserFrustration`** – Assesses whether the user became frustrated during the conversation.^[evaluate-conversations-databricks-on-aws.md]

These judges work with `mlflow.genai.evaluate()` and accept conversation traces as input.^[evaluate-conversations-databricks-on-aws.md]

## Custom multi-turn judges

When built-in judges do not cover a specific use case, you can create custom multi-turn judges using `make_judge`. The `{{ conversation }}` template variable injects the complete conversation history in a readable format for the judge to analyze.^[evaluate-conversations-databricks-on-aws.md]

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

> **Constraint**: The `{{ conversation }}` variable can only be combined with `{{ expectations }}`, not with `{{ inputs }}`, `{{ outputs }}`, or `{{ trace }}`.^[evaluate-conversations-databricks-on-aws.md]

## Usage context

Multi-turn judges are used in two main scenarios:

- **Pre-generated conversations**: Evaluate existing conversation traces that have been tagged with session IDs via `mlflow.update_current_trace(tags={"mlflow.trace.session": session_id})`.^[evaluate-conversations-databricks-on-aws.md]
- **Simulated conversations**: Generate new conversations during evaluation using a `ConversationSimulator` to test agent behavior with consistent scenarios.^[evaluate-conversations-databricks-on-aws.md]

Assessments from multi-turn judges are stored on the first trace (chronologically) in each session.^[evaluate-conversations-databricks-on-aws.md]

## Related concepts

- [LLM Judges](/concepts/llm-judges.md) – Overview of all judge types
- [Built-in LLM Judges](/concepts/built-in-llm-judges.md) – Predefined judges for common quality dimensions
- [Custom Judges](/concepts/custom-judges.md) – Creating judges with custom prompts
- [Conversation Evaluation](/concepts/conversation-evaluation.md) – Evaluating conversational AI systems
- [[Scorers]] – The scoring framework that multi-turn judges are part of
- [Code-based Scorers](/concepts/code-based-scorers.md) – Wrapping judges in custom scoring logic

## Sources

- built-in-llm-judges-databricks-on-aws.md
- evaluate-conversations-databricks-on-aws.md
- scorers-and-llm-judges-databricks-on-aws.md

# Citations

1. [built-in-llm-judges-databricks-on-aws.md](/references/built-in-llm-judges-databricks-on-aws-15825704.md)
2. [evaluate-conversations-databricks-on-aws.md](/references/evaluate-conversations-databricks-on-aws-f530405b.md)
3. [scorers-and-llm-judges-databricks-on-aws.md](/references/scorers-and-llm-judges-databricks-on-aws-b2df16f5.md)
