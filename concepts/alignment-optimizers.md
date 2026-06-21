---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f6cfdc557cb7bed761d967ca404d16fcd64c0fd18055fe87f93905f330211ceb
  pageDirectory: concepts
  sources:
    - align-judges-with-humans-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - alignment-optimizers
    - AlignmentOptimizer
  citations:
    - file: align-judges-with-humans-databricks-on-aws.md
title: Alignment Optimizers
description: Optimization algorithms (e.g., MemAlign) and the AlignmentOptimizer base class used to align judges, supporting both default and custom optimizer implementations.
tags:
  - optimization
  - mlflow
  - genai
timestamp: "2026-06-19T22:05:13.933Z"
---

# Alignment Optimizers

**Alignment Optimizers** are components in the MLflow GenAI evaluation framework that transform generic LLM judges into domain-specific evaluators by teaching them to match human evaluation standards. They are available in the package `mlflow.genai.judges.optimizers` and are used through the `align()` method on judge objects.^[align-judges-with-humans-databricks-on-aws.md]

## Overview

Judge alignment teaches LLM judges to match human evaluation standards through systematic feedback. This process transforms generic evaluators into domain-specific experts that understand your unique quality criteria, improving agreement with human assessments by 30 to 50 percent compared to baseline judges.^[align-judges-with-humans-databricks-on-aws.md]

The same alignment workflow applies to both [Built-in Judges](/concepts/built-in-judges.md) (such as `RelevanceToQuery`, `Safety`, or `Correctness`) and [Custom Judges](/concepts/custom-judges.md) created with `make_judge()`. Use alignment with built-in judges to adapt their generic criteria to your domain, or with custom judges to refine specialized evaluation logic.^[align-judges-with-humans-databricks-on-aws.md]

## Available Optimizers

The system supports the optimizers that are available in the package `mlflow.genai.judges.optimizers`.^[align-judges-with-humans-databricks-on-aws.md]

### MemAlign (Default)

When you call `align()` without specifying an optimizer, the **MemAlign** optimizer is used automatically. This is the recommended default optimizer for most use cases.^[align-judges-with-humans-databricks-on-aws.md]

To enable detailed logging for the MemAlign optimizer during alignment:

```python
import logging
logging.getLogger("mlflow.genai.judges.optimizers.memalign").setLevel(logging.DEBUG)
```

^[align-judges-with-humans-databricks-on-aws.md]

## Alignment Workflow

Judge alignment follows a three-step workflow:^[align-judges-with-humans-databricks-on-aws.md]

1. **Generate initial assessments**: Use a built-in or custom judge to evaluate traces and establish a baseline.
2. **Collect human feedback**: Domain experts review and correct judge assessments.
3. **Align and deploy**: Invoke the judge's `align()` method to create a new judge that is more aligned with human feedback.

### Using the Default Optimizer

When you call `align()` without specifying an optimizer, the MemAlign optimizer is used automatically:^[align-judges-with-humans-databricks-on-aws.md]

```python
# Retrieve traces with both judge and human assessments
traces_for_alignment = mlflow.search_traces(
    experiment_ids=[experiment_id],
    max_results=100,
    return_type="list"
)

if len(traces_for_alignment) >= 10:
    # Align the judge based on human feedback using the default optimizer
    aligned_judge = initial_judge.align(traces_for_alignment)
    
    # Register the aligned judge for production use
    aligned_judge.register(
        experiment_id=experiment_id,
        name=f"{initial_judge.name}_aligned",
        tags={"alignment_date": "2025-10-23", "num_traces": str(len(traces_for_alignment))}
    )
```

### Using an Explicit Optimizer

You can also pass an explicit optimizer instance to the `align()` method:^[align-judges-with-humans-databricks-on-aws.md]

```python
# Create your custom optimizer
custom_optimizer = MyCustomOptimizer(model="your-model")

# Use it for alignment
aligned_judge = initial_judge.align(traces_with_feedback, custom_optimizer)
```

## Creating Custom Alignment Optimizers

For specialized alignment strategies, extend the `AlignmentOptimizer` base class from `mlflow.genai.judges.base`:^[align-judges-with-humans-databricks-on-aws.md]

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

## Requirements

- MLflow 3.4.0 or above to use judge alignment features.^[align-judges-with-humans-databricks-on-aws.md]
- A judge to align (built-in or custom).^[align-judges-with-humans-databricks-on-aws.md]
- The human feedback assessment name must exactly match the judge's `name` attribute.^[align-judges-with-humans-databricks-on-aws.md]
- Alignment is not supported for session-level (multi-turn) judges such as `ConversationCompleteness`.^[align-judges-with-humans-databricks-on-aws.md]

## Best Practices

- **Sufficient traces**: You can achieve reasonable alignment with at least 10 traces, but 50-100 traces yield better results.^[align-judges-with-humans-databricks-on-aws.md]
- **Diverse reviewers**: Include multiple domain experts to capture varied perspectives.^[align-judges-with-humans-databricks-on-aws.md]
- **Balanced examples**: Include at least 30% negative examples (poor/fair ratings).^[align-judges-with-humans-databricks-on-aws.md]
- **Clear rationales**: Provide detailed explanations for ratings.^[align-judges-with-humans-databricks-on-aws.md]
- **Representative samples**: Cover edge cases and common scenarios.^[align-judges-with-humans-databricks-on-aws.md]

## Limitations

- Judge alignment does not support agent-based or expectation-based evaluation.^[align-judges-with-humans-databricks-on-aws.md]

## Related Concepts

- [LLM Judges](/concepts/llm-judges.md) — The evaluators that alignment optimizers improve
- [Built-in Judges](/concepts/built-in-judges.md) — Pre-configured judges like `RelevanceToQuery`, `Safety`, and `Correctness`
- [Custom Judges](/concepts/custom-judges.md) — User-defined judges created with `make_judge()`
- [MLflow GenAI](/concepts/mlflow-3-for-genai.md) — The evaluation framework that provides alignment capabilities
- [Production Monitoring](/concepts/production-monitoring.md) — Deploying aligned judges at scale

## Sources

- align-judges-with-humans-databricks-on-aws.md

# Citations

1. [align-judges-with-humans-databricks-on-aws.md](/references/align-judges-with-humans-databricks-on-aws-03f1583e.md)
