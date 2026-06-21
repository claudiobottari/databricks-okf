---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d9bbda5b3e32dd5fdad89a53afe9e4bf4971af74a59b3aa4ef45a20eef73c6ca
  pageDirectory: concepts
  sources:
    - align-judges-with-humans-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - trace-based-feedback-loop
    - TFL
    - Trace Feedback
  citations:
    - file: align-judges-with-humans-databricks-on-aws.md
title: Trace-Based Feedback Loop
description: The mechanism of using MLflow Traces to store both judge assessments and human feedback, which are then retrieved and used as training data for judge alignment.
tags:
  - traces
  - feedback
  - mlflow
timestamp: "2026-06-19T22:05:27.069Z"
---

# Trace-Based Feedback Loop

A **Trace-Based Feedback Loop** is a systematic process in which [LLM-as-a-Judge](/concepts/llm-as-a-judge.md) evaluations are collected, reviewed by humans, and used to iteratively improve the judge's alignment with human quality standards. This approach transforms generic evaluators into domain-specific experts that better match human assessments. ^[align-judges-with-humans-databricks-on-aws.md]

## Overview

The trace-based feedback loop leverages [[MLflow Trace|MLflow Traces]] as the central data structure for capturing both automated judge assessments and human corrections. Each trace represents a single evaluation instance, containing the model's input, output, the judge's score and rationale, and any subsequent human feedback. By collecting these traces over time, practitioners can build a dataset that teaches judges to better align with human preferences. ^[align-judges-with-humans-databricks-on-aws.md]

This approach can improve agreement between judges and human assessments by 30 to 50 percent compared to baseline judges. ^[align-judges-with-humans-databricks-on-aws.md]

## Workflow

The trace-based feedback loop follows a three-step process:

### Step 1: Generate Initial Assessments

A built-in or custom judge evaluates traces to establish a baseline. At least 10 traces are recommended for reasonable alignment, with 50–100 traces yielding better results. The judge's assessment is logged to each trace using `mlflow.log_feedback()`, with the feedback name matching the judge's `name` attribute. ^[align-judges-with-humans-databricks-on-aws.md]

### Step 2: Collect Human Feedback

Domain experts review the judge's assessments and provide corrected ratings. Human feedback can be collected through:

- **Databricks UI review**: Experts manually review traces in the MLflow UI and provide feedback using the feedback interface.
- **Programmatic feedback**: Feedback is logged via the API for automated or batch correction workflows.

The feedback name must exactly match the judge's `name` attribute. For built-in judges, this is typically a snake_case string such as `relevance_to_query`; for custom judges, it is the name passed to `make_judge()`. ^[align-judges-with-humans-databricks-on-aws.md]

### Step 3: Align and Deploy

The judge's `align()` method is invoked with the collected traces to create a new judge instance that is more aligned with human feedback. The aligned judge can then be registered for production use. ^[align-judges-with-humans-databricks-on-aws.md]

## Supported Judge Types

The trace-based feedback loop works with both:

- **Built-in judges** (e.g., `RelevanceToQuery`, `Safety`, `Correctness`) — alignment adapts their generic criteria to a specific domain.
- **Custom judges** created with `make_judge()` — alignment refines specialized evaluation logic.

Alignment is not supported for session-level (multi-turn) judges such as `ConversationCompleteness`. ^[align-judges-with-humans-databricks-on-aws.md]

## Alignment Optimizers

The system supports optimizers available in the `mlflow.genai.judges.optimizers` package. The default optimizer is **MemAlign**, which is used automatically when no optimizer is specified. Custom optimizers can be created by extending the `AlignmentOptimizer` base class. ^[align-judges-with-humans-databricks-on-aws.md]

## Best Practices for Feedback Collection

- **Diverse reviewers**: Include multiple domain experts to capture varied perspectives.
- **Balanced examples**: Include at least 30% negative examples (poor/fair ratings).
- **Clear rationales**: Provide detailed explanations for ratings.
- **Representative samples**: Cover edge cases and common scenarios.

^[align-judges-with-humans-databricks-on-aws.md]

## Validation

After alignment, the improved judge should be validated against a held-out test set. Validation compares the original judge's accuracy against the aligned judge's accuracy, measuring the improvement in agreement with human ground truth. ^[align-judges-with-humans-databricks-on-aws.md]

## Limitations

- Judge alignment does not support agent-based or expectation-based evaluation.
- Session-level (multi-turn) judges cannot be aligned.

^[align-judges-with-humans-databricks-on-aws.md]

## Related Concepts

- [LLM-as-a-Judge](/concepts/llm-as-a-judge.md) — The evaluation paradigm that trace-based feedback loops improve.
- [Judge Alignment](/concepts/judge-alignment.md) — The broader process of teaching judges to match human standards.
- [[MLflow Trace|MLflow Traces]] — The data structure used to capture and store evaluation instances.
- [Production Monitoring](/concepts/production-monitoring.md) — Deploying aligned judges at scale for ongoing evaluation.
- [Custom Judges](/concepts/custom-judges.md) — Creating specialized judges with `make_judge()`.
- [Human Feedback Collection](/concepts/mlflow-human-feedback-collection.md) — Methods for gathering expert corrections.

## Sources

- align-judges-with-humans-databricks-on-aws.md

# Citations

1. [align-judges-with-humans-databricks-on-aws.md](/references/align-judges-with-humans-databricks-on-aws-03f1583e.md)
