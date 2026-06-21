---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 80bf97a38718f9823247915f3672c2d686f400565493b2090aef6f9a3d553c55
  pageDirectory: concepts
  sources:
    - align-judges-with-humans-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - alignment-optimizer-framework
    - AOF
  citations:
    - file: align-judges-with-humans-databricks-on-aws.md
title: Alignment Optimizer Framework
description: An extensible framework for judge alignment including the default MemAlign optimizer and the AlignmentOptimizer base class for custom optimization strategies.
tags:
  - optimization
  - llm-evaluation
  - mlflow
  - framework
timestamp: "2026-06-19T13:59:23.356Z"
---

# Alignment Optimizer Framework

The **Alignment Optimizer Framework** is a set of tools and base classes within [MLflow GenAI](/concepts/mlflow-3-for-genai.md) that allow developers to systematically improve [LLM Judges](/concepts/llm-judges.md) by aligning them with human feedback. The framework provides a standard three-step workflow — generate, collect, align — and supports multiple optimizers that transform generic evaluators into domain‑specific experts.^[align-judges-with-humans-databricks-on-aws.md]

## Overview

Judge alignment teaches an LLM judge to match human evaluation standards. A well‑aligned judge can improve agreement with human assessments by **30 to 50 percent** compared to baseline judges. The framework applies to both [Built-in Judges](/concepts/built-in-judges.md) (such as `RelevanceToQuery`, `Safety`, or `Correctness`) and [Custom Judges](/concepts/custom-judges.md) created with `make_judge()`.^[align-judges-with-humans-databricks-on-aws.md]

The system exposes the optimizers available in the package `mlflow.genai.judges.optimizers`.^[align-judges-with-humans-databricks-on-aws.md]

## Key Components

### Alignment Optimizer Base Class (`AlignmentOptimizer`)

The framework provides an abstract base class `AlignmentOptimizer` from `mlflow.genai.judges.base`. Developers can extend this class to implement custom alignment strategies. The base class defines the interface:

```python
class MyCustomOptimizer(AlignmentOptimizer):
    def __init__(self, model: str = None, **kwargs):
        """Initialize with custom parameters."""
        self.model = model

    def align(self, judge: Judge, traces: list[Trace]) -> Judge:
        """Implement alignment algorithm; return a new Judge instance."""
```

^[align-judges-with-humans-databricks-on-aws.md]

### MemAlign Optimizer (Default)

The **MemAlign** optimizer is the default optimizer used when `align()` is called without specifying an optimizer. It is recommended for most alignment tasks.^[align-judges-with-humans-databricks-on-aws.md]

## The Three‑Step Alignment Workflow

1. **Generate initial assessments** – Use a built‑in or custom judge to evaluate traces and establish a baseline. Judge results are logged to the trace using `mlflow.log_feedback()` with the judge’s name as the feedback name.^[align-judges-with-humans-databricks-on-aws.md]

2. **Collect human feedback** – Domain experts review and correct judge assessments. Feedback can be provided through the Databricks UI (manually) or programmatically. Best practices include:
   - Diverse reviewers with multiple domain experts
   - At least **30% negative examples** (poor/fair ratings)
   - Clear rationales for ratings
   - Representative samples covering edge cases and common scenarios^[align-judges-with-humans-databricks-on-aws.md]

3. **Align and deploy** – Call the judge’s `align()` method, passing the traces that contain both judge and human assessments. The method returns a new aligned judge. The aligned judge can then be registered for production use via `aligned_judge.register(...)`.^[align-judges-with-humans-databricks-on-aws.md]

### Requirements

- MLflow 3.4.0 or above
- A judge to align (built‑in or custom)
- The human feedback assessment name must exactly match the judge’s `name` attribute^[align-judges-with-humans-databricks-on-aws.md]

## Creating Custom Alignment Optimizers

For specialized alignment strategies, extend `AlignmentOptimizer`:

1. Define a subclass that implements an `__init__` method and an `align(self, judge, traces)` method.
2. Inside `align()`, extract feedback from traces, analyze disagreements, generate improved instructions, and return a new `Judge` instance (e.g., via `make_judge()`).
3. Use the custom optimizer by passing it to the judge’s `align()` method:

```python
custom_optimizer = MyCustomOptimizer(model="your-model")
aligned_judge = initial_judge.align(traces_with_feedback, custom_optimizer)
```

^[align-judges-with-humans-databricks-on-aws.md]

## Enabling Detailed Logging

To monitor the alignment process, enable debug logging for the optimizer (e.g., `mlflow.genai.judges.optimizers.memalign`). This is useful for debugging and understanding how the optimizer modifies the judge.^[align-judges-with-humans-databricks-on-aws.md]

## Limitations

- Judge alignment does **not** support agent‑based or expectation‑based evaluation.^[align-judges-with-humans-databricks-on-aws.md]
- Alignment is not supported for session‑level (multi‑turn) judges such as `ConversationCompleteness`.^[align-judges-with-humans-databricks-on-aws.md]

## Related Concepts

- [LLM Judges](/concepts/llm-judges.md) – The evaluators that the framework optimizes.
- [Built-in Judges](/concepts/built-in-judges.md) – Pre‑defined judges like `RelevanceToQuery`, `Safety`, `Correctness`.
- Custom Judges (make_judge) – User‑defined judges created with the `make_judge()` API.
- Human Feedback Alignment – The broader practice of improving judge accuracy with expert annotations.
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) – Deploying aligned judges for continuous quality monitoring.
- [Trace-Based Evaluation](/concepts/mlflow-trace-based-evaluation.md) – Using execution traces for deeper quality analysis.

## Sources

- align-judges-with-humans-databricks-on-aws.md

# Citations

1. [align-judges-with-humans-databricks-on-aws.md](/references/align-judges-with-humans-databricks-on-aws-03f1583e.md)
