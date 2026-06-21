---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3ec892f024d480bcfa5b99e358d23b1d9162ce57a2461bb8e1c15f69e990b117
  pageDirectory: concepts
  sources:
    - align-judges-with-humans-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - custom-judges
    - Custom Judge
    - custom judge
    - Create custom judges
    - create custom judges
  citations:
    - file: align-judges-with-humans-databricks-on-aws.md
title: Custom Judges
description: Domain-specific evaluation judges created with make_judge() that define specialized evaluation logic and can be aligned to human preferences.
tags:
  - llm-evaluation
  - mlflow
  - customization
timestamp: "2026-06-19T13:59:21.426Z"
---

# Custom Judges

**Custom judges** are user-defined LLM evaluators created with `make_judge()` that extend [Unity Catalog](/concepts/unity-catalog.md)'s AI governance capabilities by implementing domain-specific evaluation criteria. Custom judges can be aligned to match human evaluation standards through systematic feedback using the same alignment workflow as [Built-in Judges](/concepts/built-in-judges.md).^[align-judges-with-humans-databricks-on-aws.md]

## Creating a Custom Judge

Custom judges are created using the `make_judge()` function from the `mlflow.genai.judges` module. Each custom judge requires a name, evaluation instructions, and a model to use for evaluation. The instructions define the judge's evaluation criteria and can be refined through alignment.^[align-judges-with-humans-databricks-on-aws.md]

```python
from mlflow.genai.judges import make_judge

product_quality_judge = make_judge(
    name="product_quality",
    instructions="Evaluate whether product descriptions are accurate, "
                "concise, and match the requested specifications.",
    model="databricks-claude-sonnet-4"
)
```

^[align-judges-with-humans-databricks-on-aws.md]

## Alignment Workflow

Custom judges follow the same three-step alignment workflow as built-in judges, enabling them to match human evaluation standards more closely:^[align-judges-with-humans-databricks-on-aws.md]

1. **Generate initial assessments**: Use the custom judge to evaluate traces and establish a baseline.
2. **Collect human feedback**: Domain experts review and correct judge assessments through [MLflow](/concepts/mlflow.md)'s feedback interface.
3. **Align and deploy**: Invoke the judge's `align()` method to create a new judge aligned with human feedback.

The alignment process can improve agreement with human assessments by 30 to 50 percent compared to baseline judges.^[align-judges-with-humans-databricks-on-aws.md]

## Requirements

- [MLflow](/concepts/mlflow.md) 3.4.0 or above for judge alignment features.^[align-judges-with-humans-databricks-on-aws.md]
- The human feedback assessment name must exactly match the judge's `name` attribute. For custom judges, this is the `name` you passed to `make_judge()`.^[align-judges-with-humans-databricks-on-aws.md]
- Alignment requires at least 10 traces, with 50–100 traces yielding better results.^[align-judges-with-humans-databricks-on-aws.md]
- Alignment is not supported for session-level (multi-turn) judges such as `ConversationCompleteness`.^[align-judges-with-humans-databricks-on-aws.md]

## Alignment Optimizers

The system supports optimizers available in the package `mlflow.genai.judges.optimizers`. The default optimizer is `MemAlign`, which is used automatically when calling `align()` without specifying an optimizer.^[align-judges-with-humans-databricks-on-aws.md]

For specialized alignment strategies, you can extend the `AlignmentOptimizer` base class:^[align-judges-with-humans-databricks-on-aws.md]

```python
from mlflow.genai.judges.base import AlignmentOptimizer, Judge
from mlflow.entities.trace import Trace

class MyCustomOptimizer(AlignmentOptimizer):
    """Custom optimizer implementation for judge alignment."""
    
    def __init__(self, model: str = None, **kwargs):
        self.model = model
    
    def align(self, judge: Judge, traces: list[Trace]) -> Judge:
        # Implement custom alignment logic
        pass
```

^[align-judges-with-humans-databricks-on-aws.md]

## Best Practices for Feedback Collection

- **Diverse reviewers**: Include multiple domain experts to capture varied perspectives.^[align-judges-with-humans-databricks-on-aws.md]
- **Balanced examples**: Include at least 30 percent negative examples (poor/fair ratings).^[align-judges-with-humans-databricks-on-aws.md]
- **Clear rationales**: Provide detailed explanations for ratings.^[align-judges-with-humans-databricks-on-aws.md]
- **Representative samples**: Cover edge cases and common scenarios.^[align-judges-with-humans-databricks-on-aws.md]

## Validation

Validate alignment improvement by comparing judge performance before and after alignment against human ground truth from trace assessments:^[align-judges-with-humans-databricks-on-aws.md]

```python
def test_alignment_improvement(
    original_judge, aligned_judge, test_traces: list
) -> dict:
    """Compare judge performance before and after alignment."""
    original_correct = 0
    aligned_correct = 0
    for trace in test_traces:
        feedbacks = trace.search_assessments(type="feedback")
        human_feedback = next(
            (f for f in feedbacks if f.source.source_type == "HUMAN"), None
        )
        if not human_feedback:
            continue
        original_eval = original_judge(trace=trace)
        aligned_eval = aligned_judge(trace=trace)
        if original_eval.value == human_feedback.value:
            original_correct += 1
        if aligned_eval.value == human_feedback.value:
            aligned_correct += 1
    total = len(test_traces)
    return {
        "original_accuracy": original_correct / total,
        "aligned_accuracy": aligned_correct / total,
        "improvement": (aligned_correct - original_correct) / total,
    }
```

^[align-judges-with-humans-databricks-on-aws.md]

## Limitations

- Judge alignment does not support agent-based or expectation-based evaluation.^[align-judges-with-humans-databricks-on-aws.md]

## Related Concepts

- [Built-in Judges](/concepts/built-in-judges.md) — Predefined LLM evaluators like `RelevanceToQuery` and `Correctness`
- [Judge Alignment](/concepts/judge-alignment.md) — The process of aligning judges with human evaluation standards
- [AI Governance with Unity Catalog](/concepts/ai-governance-with-unity-catalog.md) — Unified governance for AI assets
- [MLflow](/concepts/mlflow.md) — Platform for tracking and managing ML experiments
- [Custom Alignment Optimizers](/concepts/custom-alignment-optimizer.md) — Specialized alignment strategies for custom judges

## Sources

- align-judges-with-humans-databricks-on-aws.md

# Citations

1. [align-judges-with-humans-databricks-on-aws.md](/references/align-judges-with-humans-databricks-on-aws-03f1583e.md)
