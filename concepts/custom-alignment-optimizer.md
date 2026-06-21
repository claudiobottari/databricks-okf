---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 397c5c1099986a5b97b9f8cd00e14cf412eae8d5e76d3273af358af6db4ac9fd
  pageDirectory: concepts
  sources:
    - align-judges-with-humans-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - custom-alignment-optimizer
    - CAO
    - Custom Alignment Optimizers
    - custom alignment optimizers
  citations:
    - file: align-judges-with-humans-databricks-on-aws.md
title: Custom Alignment Optimizer
description: An extensible framework allowing users to implement specialized alignment strategies by extending the AlignmentOptimizer base class with custom optimization logic.
tags:
  - optimizer
  - mlflow
  - customization
  - alignment
timestamp: "2026-06-19T17:32:24.858Z"
---

# Custom Alignment Optimizer

A **Custom Alignment Optimizer** is a user-defined implementation of the [`AlignmentOptimizer`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.judges.base.AlignmentOptimizer) base class that encapsulates a specialized strategy for aligning LLM judges with human feedback. Custom optimizers allow developers to go beyond the built-in optimizers (such as MemAlign) and tailor the alignment process to domain-specific quality criteria or unique optimization algorithms. ^[align-judges-with-humans-databricks-on-aws.md]

## Overview

Judge alignment transforms generic evaluators into domain-specific experts by using human feedback to adjust a judge’s behavior. The `align()` method on a judge accepts a traces list and an optional optimizer. By default, the MemAlign optimizer is used. When the default does not suffice, a custom optimizer can be supplied to implement arbitrary alignment logic. ^[align-judges-with-humans-databricks-on-aws.md]

Custom optimizers are part of the [`mlflow.genai.judges.optimizers`](https://mlflow.org/docs/latest/genai/eval-monitor/scorers/llm-judge/alignment/#alignment-optimizers) package and are supported in MLflow 3.4.0 and above. ^[align-judges-with-humans-databricks-on-aws.md]

## Creating a Custom Alignment Optimizer

To build a custom optimizer, subclass `AlignmentOptimizer` and implement the `align()` method. The `align()` method receives the judge to be optimized and a list of traces containing human feedback, and must return a new `Judge` instance with improved alignment. ^[align-judges-with-humans-databricks-on-aws.md]

The base class is imported from `mlflow.genai.judges.base`:

```python
from mlflow.genai.judges.base import AlignmentOptimizer, Judge
from mlflow.entities.trace import Trace

class MyCustomOptimizer(AlignmentOptimizer):
    """Custom optimizer implementation for judge alignment."""
    def __init__(self, model: str = None, **kwargs):
        """Initialize your optimizer with custom parameters."""
        self.model = model
        # Add any custom initialization logic

    def align(self, judge: Judge, traces: list[Trace]) -> Judge:
        """
        Implement your alignment algorithm.

        Args:
            judge: The judge to be optimized
            traces: List of traces containing human feedback

        Returns:
            A new Judge instance with improved alignment
        """
        # Your custom alignment logic here
        # 1. Extract feedback from traces
        # 2. Analyze disagreements between judge and human
        # 3. Generate improved instructions
        # 4. Return new judge with better alignment

        # Example: Return judge with modified instructions
        from mlflow.genai.judges import make_judge

        improved_instructions = self._optimize_instructions(judge.instructions, traces)
        return make_judge(
            name=judge.name,
            instructions=improved_instructions,
            model=judge.model,
        )

    def _optimize_instructions(self, instructions: str, traces: list[Trace]) -> str:
        """Your custom optimization logic."""
        # Implement your optimization strategy
        pass
```

^[align-judges-with-humans-databricks-on-aws.md]

The `align()` method is expected to:
1. Extract human feedback from the traces.
2. Analyze disagreements between the judge’s assessments and human ratings.
3. Generate improved instructions or criteria for the judge.
4. Return a new judge (typically created with [`make_judge()`](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/custom-judge/) or a built-in judge class) that reflects the optimized evaluation logic.

## Using a Custom Optimizer

Once a custom optimizer is instantiated, it can be passed to the judge’s `align()` method as the second argument:

```python
custom_optimizer = MyCustomOptimizer(model="your-model")
aligned_judge = initial_judge.align(traces_with_feedback, custom_optimizer)
```

^[align-judges-with-humans-databricks-on-aws.md]

The resulting `aligned_judge` can then be registered for production use via its `register()` method. ^[align-judges-with-humans-databricks-on-aws.md]

## Requirements

- MLflow 3.4.0 or above (the `align()` method and `AlignmentOptimizer` base class are available in this version). ^[align-judges-with-humans-databricks-on-aws.md]
- The judge to be aligned must be either a [built-in judge](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/judges/) (e.g., `RelevanceToQuery`, `Correctness`) or a [custom judge](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/custom-judge/) created with `make_judge()`. Session-level (multi-turn) judges such as `ConversationCompleteness` are not supported for alignment. ^[align-judges-with-humans-databricks-on-aws.md]

## Limitations

- Judge alignment (including custom optimizer–based alignment) does not support agent‑based or expectation‑based evaluation. ^[align-judges-with-humans-databricks-on-aws.md]

## Related Concepts

- [Judge Alignment](/concepts/judge-alignment.md) – The overall workflow of aligning LLM judges with human feedback.
- [Built-in Judges](/concepts/built-in-judges.md) – Pre‑defined judges that can be aligned.
- [Custom Judges](/concepts/custom-judges.md) – Judges created with `make_judge()` that are eligible for alignment.
- [AlignmentOptimizer Base Class](/concepts/alignmentoptimizer-base-class.md) – The abstract base class that custom optimizers must extend.
- make_judge()|make_judge – Function used to create a new judge with custom instructions.
- [Human Feedback Collection](/concepts/mlflow-human-feedback-collection.md) – Process for gathering human‑supplied ratings and rationales.

## Sources

- align-judges-with-humans-databricks-on-aws.md

# Citations

1. [align-judges-with-humans-databricks-on-aws.md](/references/align-judges-with-humans-databricks-on-aws-03f1583e.md)
