---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4427cd9692cdc933a549aaa75a9b46478f1c727ce8205bfd3b11d740e0efcf98
  pageDirectory: concepts
  sources:
    - align-judges-with-humans-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - judge-alignment-validation
    - JAV
    - Java
  citations:
    - file: align-judges-with-humans-databricks-on-aws.md
title: Judge Alignment Validation
description: The process of comparing original and aligned judge performance against human ground truth to measure improvement in accuracy after alignment.
tags:
  - evaluation
  - validation
  - mlflow
timestamp: "2026-06-18T14:24:32.473Z"
---

# Judge Alignment Validation

**Judge alignment validation** is the process of evaluating whether a judge (an LLM-based evaluator) has improved its agreement with human assessments after undergoing an alignment workflow. Validation compares the original and aligned judges on a held-out set of traces to quantify the improvement in accuracy against human ground truth.

## Overview

Judge alignment teaches LLM judges to match human evaluation standards through systematic feedback.^[align-judges-with-humans-databricks-on-aws.md] After alignment, it is critical to validate that the judge has actually learned from human feedback and generalizes to unseen examples. Validation uses a test set of traces that were not used during alignment, each containing both a judge assessment and a human-provided assessment.^[align-judges-with-humans-databricks-on-aws.md]

## Validation Methodology

Validation follows a straightforward comparison approach:

1. **Prepare a test set** of traces that include both judge assessments and human feedback. These traces should be independent from the alignment traces.
2. **Run both the original judge and the aligned judge** on each trace in the test set.
3. **Compare each judge’s output** against the human ground truth (the human feedback stored on the trace).
4. **Compute accuracy** for each judge and the improvement.

The following Python function illustrates the validation logic:

```python
def test_alignment_improvement(
    original_judge, aligned_judge, test_traces: list
) -> dict:
    """Compare judge performance before and after alignment."""
    original_correct = 0
    aligned_correct = 0
    for trace in test_traces:
        # Get human ground truth from trace assessments
        feedbacks = trace.search_assessments(type="feedback")
        human_feedback = next(
            (f for f in feedbacks if f.source.source_type == "HUMAN"), None
        )
        if not human_feedback:
            continue
        # Get judge evaluations
        original_eval = original_judge(trace=trace)
        aligned_eval = aligned_judge(trace=trace)
        # Check agreement with human
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

### Key Points

- Judges can evaluate entire traces rather than individual inputs or outputs, so the validation step calls the judge with `trace=trace`.^[align-judges-with-humans-databricks-on-aws.md]
- Human feedback is identified by its source type (`"HUMAN"`). The function skips any trace without human assessment.
- The `value` attribute of the judge evaluation and the human feedback must exactly match the same assessment name used during alignment.

## Metrics

The validation function returns three metrics:

| Metric | Description |
|--------|-------------|
| `original_accuracy` | Fraction of test traces where the original judge’s output matches human feedback |
| `aligned_accuracy` | Fraction of test traces where the aligned judge’s output matches human feedback |
| `improvement` | Difference between aligned and original accuracy (can be positive or negative) |

A positive improvement confirms that alignment successfully moved the judge closer to human standards.

## Best Practices

- **Use a held-out test set.** Do not validate on the same traces used for alignment, to avoid overfitting.
- **Include diverse examples.** The test set should span the same variety of edge cases and scenarios as alignment data.
- **Ensure minimum test set size.** At least 10–20 traces are recommended for statistically meaningful validation.
- **Monitor for regression.** Compare improvement across multiple test sets to ensure the alignment generalizes.
- **Combine with other quality checks.** Human feedback alignment is only one aspect of judge quality; also consider inter‑rater reliability and consistency.

## Limitations

- Judge alignment validation does not support agent‑based or expectation‑based evaluation.^[align-judges-with-humans-databricks-on-aws.md]
- Validation accuracy depends on the quality and diversity of human feedback collected in the alignment step.

## Next Steps

After validation, deploy the aligned judge for production monitoring or use it in offline evaluation pipelines. See [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) and [Align judges with humans](/concepts/aligning-judges-with-human-experts.md).

## Related Concepts

- [Align judges with humans](/concepts/aligning-judges-with-human-experts.md) — The full workflow for teaching judges human quality standards
- [Human feedback alignment](/concepts/human-feedback-for-llm-judge-alignment.md) — Collecting and using human annotations
- [Custom Judges](/concepts/custom-judges.md) — Creating judges with `make_judge()`
- [Built-in Judges](/concepts/built-in-judges.md) — Pre‑defined judges like `RelevanceToQuery` and `Correctness`
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) — Using judges with `mlflow.genai.evaluate()`

## Sources

- align-judges-with-humans-databricks-on-aws.md

# Citations

1. [align-judges-with-humans-databricks-on-aws.md](/references/align-judges-with-humans-databricks-on-aws-03f1583e.md)
