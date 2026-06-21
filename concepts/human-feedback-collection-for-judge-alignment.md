---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f649d2e362ac5d87c7b10a95c9d57b9b22cb71ba9aee0f262b8d5624ca479bcf
  pageDirectory: concepts
  sources:
    - align-judges-with-humans-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - human-feedback-collection-for-judge-alignment
    - HFCFJA
    - Human Feedback for GenAI
  citations:
    - file: align-judges-with-humans-databricks-on-aws.md
title: Human Feedback Collection for Judge Alignment
description: Best practices and methods for collecting domain expert feedback on judge assessments, including UI review and programmatic feedback, with guidance on diverse reviewers and balanced examples.
tags:
  - feedback
  - human-evaluation
  - mlflow
timestamp: "2026-06-19T22:05:23.840Z"
---

# Human Feedback Collection for Judge Alignment

**Human feedback collection** is the second step in the judge alignment workflow, where domain experts review and correct LLM judge assessments to teach generic evaluators domain-specific quality standards. This process transforms baseline judges into specialized evaluators that better match human evaluation criteria, improving agreement with human assessments by 30 to 50 percent. ^[align-judges-with-humans-databricks-on-aws.md]

## Overview

Judge alignment follows a three-step workflow: generate initial assessments using a built-in or custom judge, collect human feedback, then align and deploy the judge with the `align()` method. The same workflow applies to [Built-in Judges](/concepts/built-in-judges.md) (such as `RelevanceToQuery`, `Safety`, or `Correctness`) and [Custom Judges](/concepts/custom-judges.md) created with `make_judge()`. ^[align-judges-with-humans-databricks-on-aws.md]

Human feedback collection is the critical bridge between a generic judge and a domain-tuned evaluator. Without this step the judge would continue to apply its default criteria, which may not reflect your team's quality expectations.

## Requirements

To collect feedback for judge alignment you need:

- **MLflow 3.4.0 or above**. ^[align-judges-with-humans-databricks-on-aws.md]
- **A judge to align** – either a built-in judge or a custom judge created with `make_judge()`. ^[align-judges-with-humans-databricks-on-aws.md]
- The **human feedback assessment name must exactly match the judge's `name` attribute**. For built-in judges this is the default snake_case name (e.g., `relevance_to_query` for `RelevanceToQuery`) unless overridden; for custom judges it is the name passed to `make_judge()`. ^[align-judges-with-humans-databricks-on-aws.md]

Alignment is not supported for session-level (multi-turn) judges such as `ConversationCompleteness`. ^[align-judges-with-humans-databricks-on-aws.md]

## Step 1: Generate Initial Assessments (Prerequisite)

Before collecting human feedback, you must generate traces and have the judge produce baseline assessments. You can achieve reasonable alignment with at least 10 traces, but 50–100 traces yield better results. Use the judge's `name` attribute when logging feedback in the next step. ^[align-judges-with-humans-databricks-on-aws.md]

## Step 2: Collect Human Feedback

Collect human feedback to teach the judge your quality standards. There are two primary approaches:

- **Databricks UI review** – use the MLflow UI to manually review traces and provide feedback. This approach is recommended when domain experts need to examine outputs, when you want to iteratively refine feedback criteria, or when working with smaller datasets (under 100 examples). ^[align-judges-with-humans-databricks-on-aws.md]
- **Programmatic feedback** – use the MLflow API to log human feedback programmatically, suitable for automated pipelines or larger datasets. ^[align-judges-with-humans-databricks-on-aws.md]

### Using the Databricks UI for Manual Review

1. Navigate to your MLflow experiment in the Databricks workspace.
2. Click on the **Traces** tab to see traces.
3. Review each trace and its judge assessment.
4. Add human feedback using the UI's feedback interface.
5. Ensure the feedback name matches your judge's `name` attribute exactly (for example, `relevance_to_query` for a built-in `RelevanceToQuery` instance). ^[align-judges-with-humans-databricks-on-aws.md]

### Best Practices for Feedback Collection

- **Diverse reviewers**: Include multiple domain experts to capture varied perspectives.
- **Balanced examples**: Include at least 30% negative examples (poor/fair ratings).
- **Clear rationales**: Provide detailed explanations for ratings.
- **Representative samples**: Cover edge cases and common scenarios. ^[align-judges-with-humans-databricks-on-aws.md]

## Step 3: Align and Deploy

Once sufficient human feedback is collected, call the judge's `align()` method to create a new judge more aligned with human assessments. The system supports the optimizers available in the package `mlflow.genai.judges.optimizers`. When calling `align()` without specifying an optimizer, the MemAlign optimizer is used automatically. The aligned judge can then be registered for production use with a new name to distinguish it from the original judge. ^[align-judges-with-humans-databricks-on-aws.md]

## Validation

After alignment, compare the aligned judge's agreement with human ground truth against the original judge's agreement, typically on a held-out set of traces. This confirms that the human feedback collection improved judge performance. ^[align-judges-with-humans-databricks-on-aws.md]

## Limitations

- Judge alignment does not support agent-based or expectation-based evaluation.
- Multi-turn judges such as `ConversationCompleteness` cannot be aligned. ^[align-judges-with-humans-databricks-on-aws.md]

## Related Concepts

- [Judge Alignment](/concepts/judge-alignment.md) – The overall three-step workflow.
- [Built-in Judges](/concepts/built-in-judges.md) – Pre-configured LLM judges provided by MLflow.
- [Custom Judges](/concepts/custom-judges.md) – User-defined judges created with `make_judge()`.
- [MLflow](/concepts/mlflow.md) – The framework providing judge alignment capabilities.
- [Production Monitoring](/concepts/production-monitoring.md) – Deploying aligned judges at scale.
- [Custom Alignment Optimizers](/concepts/custom-alignment-optimizer.md) – Extending alignment strategies for specialized needs.

## Sources

- align-judges-with-humans-databricks-on-aws.md

# Citations

1. [align-judges-with-humans-databricks-on-aws.md](/references/align-judges-with-humans-databricks-on-aws-03f1583e.md)
