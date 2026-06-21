---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8118f622e805b580664d0801cb79d0dbbdaf65e408612c73fda1cbd4cf162065
  pageDirectory: concepts
  sources:
    - custom-judges-databricks-on-aws.md
  confidence: 0.94
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - aligning-judges-with-human-experts
    - AJWHE
    - Align Judges with Human Experts
    - Align judges with human experts
    - Align Judges with Humans
    - Align judges with humans
    - align judges with human feedback
    - align judges with humans
    - align judges with humans|align the judge instructions
  citations:
    - file: custom-judges-databricks-on-aws.md
title: Aligning Judges with Human Experts
description: The process of improving LLM judge accuracy by iteratively aligning judge behavior with human expert feedback on application outputs.
tags:
  - llm-evaluation
  - human-feedback
  - mlflow
timestamp: "2026-06-19T14:39:41.518Z"
---

---
title: Aligning Judges with Human Experts
summary: A process of refining LLM-based judges by incorporating expert feedback on application outputs to improve evaluation accuracy.
sources:
  - custom-judges-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T15:30:00.000Z"
updatedAt: "2026-06-19T15:30:00.000Z"
tags:
  - mlflow
  - genai
  - evaluation
  - judges
  - human-feedback
aliases:
  - align-judges-with-human-experts
  - AHFE
confidence: 0.85
provenanceState: extracted
inferredParagraphs: 0
---

# Aligning Judges with Human Experts

**Aligning judges with human experts** is the practice of refining [LLM Judges](/concepts/llm-judges.md) by incorporating expert feedback on an application’s outputs, thereby improving the accuracy and reliability of automated evaluations.

## Overview

[Custom Judges](/concepts/custom-judges.md) created with `make_judge()` serve as a baseline for evaluating GenAI applications. While these base judges can capture general quality criteria, their alignment with human judgment can be further improved by collecting feedback from human experts on actual application outputs. ^[custom-judges-databricks-on-aws.md]

## Process

The alignment process begins once expert annotations or feedback have been gathered on the outputs produced by the GenAI application. This feedback is then used to adjust or fine-tune the LLM judge so that its scoring better reflects the nuanced assessments made by human evaluators. The goal is to incrementally increase the judge’s accuracy over time. ^[custom-judges-databricks-on-aws.md]

## Related Concepts

- [Custom Judges](/concepts/custom-judges.md) — The starting point for evaluation, created with `make_judge()`.
- [LLM Judges](/concepts/llm-judges.md) — The category of evaluators that can be aligned.
- [Human feedback](/concepts/mlflow-human-feedback-collection.md) — Expert annotations used to refine judges.
- [Model evaluation](/concepts/mlflow-evaluation-ui.md) — The broader context in which aligned judges are applied.
- [Align judges with humans](/concepts/aligning-judges-with-human-experts.md) — The dedicated topic covering the alignment workflow in detail.

## Sources

- custom-judges-databricks-on-aws.md

# Citations

1. [custom-judges-databricks-on-aws.md](/references/custom-judges-databricks-on-aws-7a56fe4f.md)
