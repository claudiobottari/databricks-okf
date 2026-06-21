---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f397f4ca47ead61d5be3cfa4f950a17da2dbae719e37058fd718f389ab8a7192
  pageDirectory: concepts
  sources:
    - scorers-and-llm-judges-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - llm-judges
    - LLM Judge
    - LLM judge
    - AI judges
    - Judges
    - LLM Judge|LLM Judges
    - LLM Judge|LLM judges
    - judge's
    - judges
  citations:
    - file: scorers-and-llm-judges-databricks-on-aws.md
title: LLM Judges
description: A type of MLflow Scorer that uses Large Language Models to assess quality across dimensions like relevance, safety, and correctness.
tags:
  - mlflow
  - llm
  - evaluation
timestamp: "2026-06-19T20:19:39.408Z"
---

# LLM Judges

**LLM judges** are a type of MLflow `Scorer` that use large language models to perform quality assessment of GenAI applications, agents, and systems. They function as AI assistants specialized in evaluating inputs, outputs, and entire execution traces based on user-defined criteria. ^[scorers-and-llm-judges-databricks-on-aws.md]

## How LLM judges work

An LLM judge is an implementation of the broader [[Scorers]] concept. Like all scorers, a judge receives a [Trace](/concepts/traces.md) from either `evaluate()` or the production monitoring service. The judge parses the trace to extract relevant fields, runs its assessment, and returns the result as [Feedback](/concepts/feedback-object.md) that attaches to the trace. ^[scorers-and-llm-judges-databricks-on-aws.md]

Because judges use LLMs, they can understand semantic equivalence — for example, recognizing that “give me healthy food options” and “food to keep me fit” are similar queries. ^[scorers-and-llm-judges-databricks-on-aws.md]

## Types of LLM judges

### Built-in LLM judges

MLflow provides research-validated built-in judges covering common quality dimensions such as relevance, safety, groundedness, and correctness. For the complete list, see [Built-in LLM Judges](/concepts/built-in-llm-judges.md). ^[scorers-and-llm-judges-databricks-on-aws.md]

### Multi-turn judges

For conversational AI systems, MLflow also provides built-in judges that evaluate entire conversations rather than individual turns. These are documented under [Multi-turn Judges](/concepts/multi-turn-judges.md). ^[scorers-and-llm-judges-databricks-on-aws.md]

### Custom LLM judges

When built-in judges do not meet specific needs, users can create custom LLM judges by providing their own prompts and instructions. Custom judges allow full control over grades and scores (not just pass/fail) and are particularly useful for validating agent decisions and operations. [Judge Alignment](/concepts/judge-alignment.md) can be used to train custom judges to match human evaluation standards through systematic feedback. See [Custom LLM Judges](/concepts/custom-llm-judges.md). ^[scorers-and-llm-judges-databricks-on-aws.md]

## Selecting the LLM that powers the judge

By default, each judge uses a Databricks-hosted LLM designed for GenAI quality assessments. Users can change the judge model using the `model` argument in the judge definition, specifying the model in the format `<provider>:/<model-name>`. For example:

```python
from mlflow.genai.scorers import Correctness
Correctness(model="databricks:/databricks-gpt-5-mini")
```

^[scorers-and-llm-judges-databricks-on-aws.md]

## Model hosting and data handling

LLM judges may use third-party services — including Azure OpenAI operated by Microsoft — to evaluate GenAI applications. Databricks has opted out of Abuse Monitoring for Azure OpenAI, so no prompts or responses are stored. For European Union workspaces, judges use models hosted in the EU; all other regions use US‑hosted models. Disabling [Partner-powered AI features](/concepts/partner-powered-ai-features-on-databricks.md) prevents the judge from calling partner‑powered models, though users can still provide their own model. ^[scorers-and-llm-judges-databricks-on-aws.md]

## Judge accuracy

Databricks continuously improves judge quality through:
- Research validation against human expert judgment.
- Metrics tracking such as Cohen’s Kappa, accuracy, and F1 score.
- Diverse testing on academic and real‑world datasets.

^[scorers-and-llm-judges-databricks-on-aws.md]

## Usage guidance

Judges can be used directly with `mlflow.genai.evaluate()` or wrapped in [Custom code-based scorers](/concepts/code-based-scorers.md) for advanced scoring logic. Using the same judge for development evaluation and production monitoring keeps evaluation consistent throughout the application lifecycle. ^[scorers-and-llm-judges-databricks-on-aws.md]

## Related concepts

- [[Scorers]] – The parent abstraction that includes both LLM judges and code-based scorers
- [Built-in LLM Judges](/concepts/built-in-llm-judges.md) – Pre‑defined judges for common quality dimensions
- [Multi-turn Judges](/concepts/multi-turn-judges.md) – Judges for conversational AI evaluation
- [Custom LLM Judges](/concepts/custom-llm-judges.md) – User‑defined judges with custom prompts
- [Custom code-based scorers](/concepts/code-based-scorers.md) – Deterministic or heuristic scorers
- [Trace](/concepts/traces.md) – The execution data that scorers receive
- [Feedback](/concepts/feedback-object.md) – The scoring result attached to a trace
- [Judge Alignment](/concepts/judge-alignment.md) – Training custom judges to match human standards
- [Partner-powered AI features](/concepts/partner-powered-ai-features-on-databricks.md) – Controls for third‑party model usage

## Sources

- scorers-and-llm-judges-databricks-on-aws.md

# Citations

1. [scorers-and-llm-judges-databricks-on-aws.md](/references/scorers-and-llm-judges-databricks-on-aws-b2df16f5.md)
