---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4ba8bc710fe494ef4b0d110717d1aa2f7c1c7a4f90eb1bcc2568fbbc1219a884
  pageDirectory: concepts
  sources:
    - align-judges-with-humans-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - built-in-judges
    - Built-in Judgers
    - Built‑in Judges
    - Built‑in judges
  citations:
    - file: align-judges-with-humans-databricks-on-aws.md
title: Built-in Judges
description: Pre-defined evaluation judges in MLflow/Databricks such as RelevanceToQuery, Safety, and Correctness, which can be used directly or aligned to a domain.
tags:
  - llm-evaluation
  - mlflow
  - judges
timestamp: "2026-06-19T13:59:14.638Z"
---

# Built-in Judges

**Built-in judges** are pre-configured LLM-based evaluators provided by MLflow that assess AI outputs on standard quality criteria such as relevance, safety, and correctness. They serve as ready-to-use scoring functions and can be aligned to domain-specific standards through human feedback. ^[align-judges-with-humans-databricks-on-aws.md]

## Available judges

Built-in judges include:

- `RelevanceToQuery` – evaluates how well the response addresses the user query.
- `Safety` – detects harmful or unsafe content.
- `Correctness` – checks factual accuracy of the output.
- `ConversationCompleteness` – a session-level (multi-turn) judge that assesses whether the conversation fully answers the user's needs. ^[align-judges-with-humans-databricks-on-aws.md]

> Alignment is **not supported** for `ConversationCompleteness` because it operates on multi-turn sessions rather than single-turn traces. ^[align-judges-with-humans-databricks-on-aws.md]

## Key characteristics

### Naming convention

Each built-in judge exposes a `name` attribute. By default the name is the snake_case version of the class name — for example, `relevance_to_query` for `RelevanceToQuery`. You can override this by passing a `name=` argument when instantiating the class. ^[align-judges-with-humans-databricks-on-aws.md]

### Instantiation

Built-in judges are instantiated directly without any configuration beyond an optional name override:

```python
from mlflow.genai.scorers import RelevanceToQuery

judge = RelevanceToQuery()
```

### Alignment compatibility

Built-in judges can be aligned to human evaluation standards using the same [Judge Alignment](/concepts/judge-alignment.md) workflow as [Custom Judges](/concepts/custom-judges.md). The alignment process requires a minimum of 10 traces (50–100 recommended) that contain both the judge's automated assessments and human feedback. ^[align-judges-with-humans-databricks-on-aws.md]

## Requirements

- **MLflow 3.4.0 or above** – the alignment and scoring features require this version.
- The Python package `mlflow[databricks]` with version ≥ 3.4.0. ^[align-judges-with-humans-databricks-on-aws.md]

## Related concepts

- [Custom Judges](/concepts/custom-judges.md) – user-defined evaluators created with `make_judge()`.
- [Judge Alignment](/concepts/judge-alignment.md) – the process of adapting judges to domain-specific human standards.
- [MLflow](/concepts/mlflow.md) – the platform that provides built-in judges as part of its GenAI evaluation toolkit.
- [LLM evaluation](/concepts/llm-as-a-judge-evaluation.md) – broader topic covering automated and human evaluation of AI systems.

## Sources

- align-judges-with-humans-databricks-on-aws.md

# Citations

1. [align-judges-with-humans-databricks-on-aws.md](/references/align-judges-with-humans-databricks-on-aws-03f1583e.md)
