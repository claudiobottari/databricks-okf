---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cd9434f0d4e5ba66d4fd259a2eb00b6cc187bb3f1f7674a940683a231906d7a5
  pageDirectory: concepts
  sources:
    - align-judges-with-humans-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - built-in-judges-vs-custom-judges
    - BJVCJ
  citations:
    - file: align-judges-with-humans-databricks-on-aws.md
title: Built-in Judges vs Custom Judges
description: The distinction between predefined MLflow judges (like RelevanceToQuery, Safety, Correctness) and user-defined judges created with make_judge(), both of which support the alignment workflow.
tags:
  - judges
  - mlflow
  - genai
timestamp: "2026-06-19T22:05:11.243Z"
---

# Built-in Judges vs Custom Judges

**Built-in Judges** and **Custom Judges** are two categories of LLM-based evaluators in MLflow that assess the quality of AI-generated outputs. The choice between them depends on whether you need generic, pre-configured evaluation criteria or domain-specific, tailored assessment logic.

## Overview

Both built-in judges and custom judges can be aligned with human feedback to improve their evaluation accuracy. The same alignment workflow applies to both types, enabling you to adapt generic criteria to your domain or refine specialized evaluation logic. ^[align-judges-with-humans-databricks-on-aws.md]

## Built-in Judges

Built-in judges are pre-configured evaluators that come with MLflow, providing generic assessment criteria for common evaluation dimensions. Examples include `RelevanceToQuery`, `Safety`, and `Correctness`. ^[align-judges-with-humans-databricks-on-aws.md]

### Characteristics

- **Pre-defined criteria**: Built-in judges have default evaluation criteria that work well for general use cases.
- **Default naming**: Each built-in judge has a default snake_case name (e.g., `relevance_to_query` for `RelevanceToQuery`), which can be overridden by passing a `name=` parameter when instantiating the class.
- **Instantiation**: Built-in judges are instantiated directly from their class, such as `RelevanceToQuery()`.

### Use Cases

Use built-in judges when you need standard evaluation metrics without custom logic. They are suitable for:
- General-purpose quality assessment
- Quick evaluation setup
- Standard compliance checks (e.g., safety, relevance, correctness)

## Custom Judges

Custom judges are evaluators created with the `make_judge()` function, allowing you to define specialized evaluation logic tailored to your specific domain or application. ^[align-judges-with-humans-databricks-on-aws.md]

### Characteristics

- **Custom instructions**: You provide specific evaluation instructions that define the judge's criteria.
- **Custom naming**: The judge's name is set when calling `make_judge()`, such as `product_quality`.
- **Flexible creation**: Custom judges are created programmatically using the `make_judge()` API.

### Use Cases

Use custom judges when you need:
- Domain-specific evaluation criteria (e.g., product quality, medical accuracy, legal compliance)
- Specialized assessment logic not covered by built-in judges
- Fine-grained control over evaluation instructions

## Alignment

Both built-in and custom judges support alignment with human feedback through the same `align()` method. This process transforms generic evaluators into domain-specific experts, improving agreement with human assessments by 30 to 50 percent compared to baseline judges. ^[align-judges-with-humans-databricks-on-aws.md]

### Alignment Workflow

1. **Generate initial assessments**: Use a built-in or custom judge to evaluate traces and establish a baseline.
2. **Collect human feedback**: Domain experts review and correct judge assessments.
3. **Align and deploy**: Invoke the judge's `align()` method to create a new judge that is more aligned with human feedback.

### Key Requirements

- The human feedback assessment name must exactly match the judge's `name` attribute.
- For built-in judges, this is the default snake_case name unless overridden.
- For custom judges, this is the name passed to `make_judge()`.

## Comparison Table

| Feature | Built-in Judges | Custom Judges |
|---------|----------------|---------------|
| **Creation** | Instantiate class directly | Use `make_judge()` function |
| **Criteria** | Pre-defined, generic | User-defined, specialized |
| **Naming** | Default snake_case (overridable) | Set during creation |
| **Examples** | `RelevanceToQuery`, `Safety`, `Correctness` | `product_quality`, `medical_accuracy` |
| **Alignment** | Supported via `align()` | Supported via `align()` |
| **Best for** | Standard evaluation needs | Domain-specific evaluation |

## Limitations

- Judge alignment does not support agent-based or expectation-based evaluation.
- Alignment is not supported for session-level (multi-turn) judges such as `ConversationCompleteness`.

## Related Concepts

- [Judge Alignment](/concepts/judge-alignment.md) — The process of teaching judges to match human evaluation standards
- [LLM Judges](/concepts/llm-judges.md) — Overview of LLM-based evaluation in MLflow
- [Custom Scorers](/concepts/custom-scorers-mlflow-genai.md) — Complementary deterministic metrics for evaluation
- [Production Monitoring](/concepts/production-monitoring.md) — Deploying aligned judges at scale
- make_judge() — API for creating custom judges

## Sources

- align-judges-with-humans-databricks-on-aws.md

# Citations

1. [align-judges-with-humans-databricks-on-aws.md](/references/align-judges-with-humans-databricks-on-aws-03f1583e.md)
