---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c3ba52fe95780bc381edda6bc570e3a387765dda397ed1fa446000b54366ff84
  pageDirectory: concepts
  sources:
    - align-judges-with-humans-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - validation-of-judge-alignment
    - VOJA
  citations:
    - file: align-judges-with-humans-databricks-on-aws.md
title: Validation of Judge Alignment
description: A method to quantitatively compare original versus aligned judge performance against human ground truth, measuring accuracy improvement.
tags:
  - validation
  - evaluation
  - mlflow
timestamp: "2026-06-19T22:05:29.775Z"
---

# Validation of Judge Alignment

**Validation of Judge Alignment** refers to the process of quantitatively measuring whether an Aligned Judge produces assessments that better agree with human evaluators compared to the original unaligned judge. It is a critical step after applying the alignment workflow to ensure that the optimizations actually improved judge performance.

## Overview

Judge alignment uses human feedback to adjust an LLM judge’s evaluation criteria, but alignment alone does not guarantee improvement. Validation provides an objective measurement of the alignment’s effectiveness by comparing the decisions of the original judge and the aligned judge against human ground‑truth labels. ^[align-judges-with-humans-databricks-on-aws.md]

## Validation Method

The recommended validation approach is to run a comparison on a held‑out set of test traces that have human feedback. For each trace, both the original judge and the aligned judge produce a value, which is then compared against the human assessment. The system tracks two accuracy metrics:

- **Original accuracy** – fraction of test traces where the original judge agrees with the human.
- **Aligned accuracy** – fraction of test traces where the aligned judge agrees with the human.

The improvement is calculated as `(aligned_accuracy - original_accuracy)`. ^[align-judges-with-humans-databricks-on-aws.md]

A typical implementation, such as the `test_alignment_improvement` function shown in the alignment documentation, iterates over test traces, extracts the human feedback (identified by `source_type == "HUMAN"`), and then calls each judge on the trace to obtain their evaluations. The results are aggregated into a dictionary containing `original_accuracy`, `aligned_accuracy`, and `improvement`. ^[align-judges-with-humans-databricks-on-aws.md]

## Expected Improvement

The alignment workflow is designed to increase agreement with human assessments. When applied correctly, aligned judges typically show a 30 to 50 percent improvement in agreement compared to baseline judges. ^[align-judges-with-humans-databricks-on-aws.md]

## Related Concepts

- [Judge Alignment](/concepts/judge-alignment.md) – The full workflow for tuning judges to human standards.
- [LLM Judges](/concepts/llm-judges.md) – Generic evaluators that can be aligned for domain-specific tasks.
- [Human Feedback](/concepts/mlflow-human-feedback-collection.md) – The ground‑truth assessments used for training and validation.
- Aligned Judge – A judge that has been optimized through the alignment process.
- [AlignmentOptimizer](/concepts/alignment-optimizers.md) – Base class for custom alignment strategies.
- [Built‑in Judges](/concepts/built-in-judges.md) – Pre‑defined judges such as `RelevanceToQuery` and `Correctness`.

## Sources

- align-judges-with-humans-databricks-on-aws.md

# Citations

1. [align-judges-with-humans-databricks-on-aws.md](/references/align-judges-with-humans-databricks-on-aws-03f1583e.md)
