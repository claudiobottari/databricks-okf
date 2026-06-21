---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 24ebcfc23d4fed8c0934ddc983acdd90a7533d15ed2060256b0fa6c114c741ad
  pageDirectory: concepts
  sources:
    - align-judges-with-humans-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - alignmentoptimizer-base-class
    - ABC
    - ABAC
  citations:
    - file: align-judges-with-humans-databricks-on-aws.md
title: AlignmentOptimizer Base Class
description: An extensible base class in mlflow.genai.judges.base for implementing custom alignment strategies, providing a template with an align() method for specialized optimization logic.
tags:
  - api-reference
  - llm-evaluation
  - mlflow
timestamp: "2026-06-19T08:58:08.711Z"
---

# AlignmentOptimizer Base Class

**AlignmentOptimizer** is a base class in `mlflow.genai.judges.base` that provides the interface for implementing custom alignment strategies for [LLM Judge](/concepts/llm-judges.md) alignment. By extending this class, developers can create specialized optimizers that transform a generic judge into one that is better aligned with human feedback on domain-specific quality criteria. ^[align-judges-with-humans-databricks-on-aws.md]

## Overview

The `AlignmentOptimizer` base class is used within the three-step judge alignment workflow: generating initial assessments, collecting human feedback, and then aligning the judge. When you call a judge’s `align()` method, you can optionally pass an optimizer instance. If no optimizer is specified, the `MemAlign` optimizer (the default) is used automatically. ^[align-judges-with-humans-databricks-on-aws.md]

Custom optimizers are useful when the built-in optimization strategies do not meet specialized requirements, such as domain-specific reward functions or multi-stage refinement. ^[align-judges-with-humans-databricks-on-aws.md]

## Class Definition

The `AlignmentOptimizer` class is defined in `mlflow.genai.judges.base`. It is an abstract base class that requires subclasses to implement the `align` method. The class also provides a standard `__init__` signature for accepting model and configuration parameters. ^[align-judges-with-humans-databricks-on-aws.md]

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
        pass
```

^[align-judges-with-humans-databricks-on-aws.md]

## Methods

### `__init__(self, model: str = None, **kwargs)`

Initializes the optimizer with optional model specification and additional keyword arguments. Subclasses can override this to accept custom parameters needed for their alignment strategy. ^[align-judges-with-humans-databricks-on-aws.md]

### `align(self, judge: Judge, traces: list[Trace]) -> Judge`

The core method that every optimizer must implement. It receives the original `judge` instance and a list of `traces` containing both the judge’s assessments and human feedback. The method should return a new `Judge` instance that is better aligned with the human evaluations. Common implementation steps include:

1. Extracting feedback from traces.
2. Analyzing disagreements between judge and human ratings.
3. Generating improved judge instructions based on the analysis.
4. Returning a new judge with those improved instructions. ^[align-judges-with-humans-databricks-on-aws.md]

## Usage Example

After creating a custom optimizer, you use it in the judge alignment step by passing it to the judge’s `align()` method:

```python
# Create your custom optimizer
custom_optimizer = MyCustomOptimizer(model="your-model")

# Use it for alignment
aligned_judge = initial_judge.align(traces_with_feedback, custom_optimizer)
```

^[align-judges-with-humans-databricks-on-aws.md]

## Available Optimizers

The package `mlflow.genai.judges.optimizers` contains all supported optimizers. The default optimizer used when none is specified is **MemAlign**. Developers can inspect this module to see the list of built-in optimizers and use them as reference for building custom ones. ^[align-judges-with-humans-databricks-on-aws.md]

## Related Concepts

- [Judge Alignment](/concepts/judge-alignment.md) – The overall workflow of aligning judges with human feedback
- [LLM Judge](/concepts/llm-judges.md) – The base concept of using LLMs as evaluators
- make_judge() – API for creating custom judges
- [Built-in Judges](/concepts/built-in-judges.md) – Predefined judges that can also be aligned
- [MLflow GenAI](/concepts/mlflow-3-for-genai.md) – The broader MLflow module for generative AI evaluation

## Sources

- align-judges-with-humans-databricks-on-aws.md

# Citations

1. [align-judges-with-humans-databricks-on-aws.md](/references/align-judges-with-humans-databricks-on-aws-03f1583e.md)
