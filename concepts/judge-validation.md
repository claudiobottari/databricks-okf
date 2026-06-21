---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1713d5e6588da1bed5210c82afa1225ca04eb4b43f58b8e1dc487a59fc5b85ee
  pageDirectory: concepts
  sources:
    - align-judges-with-humans-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - judge-validation
  citations:
    - file: align-judges-with-humans-databricks-on-aws.md
title: Judge Validation
description: Methodology for comparing original and aligned judge performance against human ground truth to measure accuracy improvement.
tags:
  - validation
  - llm-evaluation
  - testing
timestamp: "2026-06-19T13:59:26.431Z"
---

# Judge Validation

**Judge Validation** refers to the process of measuring and improving the agreement between [LLM Judges](/concepts/llm-judges.md) and human evaluators. It ensures that automated quality assessments — whether from built-in or custom judges — reflect domain-specific standards and produce reliable, defensible scores for [GenAI](/concepts/mlflow-genai-evaluate-api.md) outputs.

## Why Validate Judges?

Generic LLM judges often fail to capture subtle, domain-specific quality criteria. Validation quantifies how well a judge matches human judgments and guides iterative refinement. Systematic alignment with human feedback can improve agreement by 30 to 50 percent compared to baseline judges. ^[align-judges-with-humans-databricks-on-aws.md]

Validation applies equally to built-in judges (such as `RelevanceToQuery`, `Safety`, or `Correctness`) and custom judges created with `make_judge()`. ^[align-judges-with-humans-databricks-on-aws.md]

## Validation Workflow

Judge validation follows a three-step workflow identical to [align judges with humans](/concepts/aligning-judges-with-human-experts.md):

1. **Generate initial assessments** – Use a judge to evaluate traces and establish a baseline.
2. **Collect human feedback** – Domain experts review and correct judge assessments.
3. **Align and deploy** – Invoke the judge’s `align()` method to create a new judge that is better aligned with human feedback. ^[align-judges-with-humans-databricks-on-aws.md]

The system supports the optimizers available in the package `mlflow.genai.judges.optimizers`. Alignment requires MLflow 3.4.0 or above, and the human feedback assessment name must exactly match the judge’s `name` attribute. ^[align-judges-with-humans-databricks-on-aws.md]

## Measuring Alignment

The standard way to validate alignment is to compare the judge’s ratings against human ground truth on a held-out set of traces. The following metrics are typical:

| Metric | Definition |
|--------|------------|
| Original accuracy | Fraction of test traces where the unaligned judge agrees with human feedback |
| Aligned accuracy | Fraction of test traces where the aligned judge agrees with human feedback |
| Improvement | Percentage-point increase after alignment |

A simple validation function can be implemented as shown below. It retrieves human feedback from trace assessments and compares both the original and aligned judge’s evaluations to that ground truth. ^[align-judges-with-humans-databricks-on-aws.md]

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

## Best Practices for Collecting Human Feedback

Effective validation depends on high-quality human annotations:

- **Diverse reviewers** – Include multiple domain experts to capture varied perspectives.
- **Balanced examples** – Include at least 30% negative examples (poor or fair ratings).
- **Clear rationales** – Provide detailed explanations for each rating.
- **Representative samples** – Cover edge cases and common scenarios.

^[align-judges-with-humans-databricks-on-aws.md]

A minimum of 10 traces is needed to begin alignment, but 50–100 traces yield substantially better results. ^[align-judges-with-humans-databricks-on-aws.md]

## Alignment Optimizers

Alignment uses optimizers to transform a judge’s instructions based on human feedback. The default optimizer is **MemAlign**; you can also implement [custom alignment optimizers](/concepts/custom-alignment-optimizer.md) by extending the `AlignmentOptimizer` base class. ^[align-judges-with-humans-databricks-on-aws.md]

## Limitations

- Judge alignment does not support agent-based or expectation-based evaluation.
- Session-level (multi-turn) judges such as `ConversationCompleteness` cannot be aligned.

^[align-judges-with-humans-databricks-on-aws.md]

## Related Concepts

- [Align judges with humans](/concepts/aligning-judges-with-human-experts.md) – The full workflow for judge alignment
- [Custom Judges](/concepts/custom-judges.md) – Creating judges with `make_judge()`
- [Built-in Judges](/concepts/built-in-judges.md) – Predefined judges like `RelevanceToQuery`
- Human Feedback Alignment – Broad topic of incorporating expert feedback
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) – The `mlflow.genai.evaluate()` API
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) – Deploying validated judges at scale

## Sources

- align-judges-with-humans-databricks-on-aws.md

# Citations

1. [align-judges-with-humans-databricks-on-aws.md](/references/align-judges-with-humans-databricks-on-aws-03f1583e.md)
