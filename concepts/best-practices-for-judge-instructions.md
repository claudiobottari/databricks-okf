---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0515ae6f0f3805cb0513df81bbd0a0ef8f9d59c4f1173f42497bedf5714c74cd
  pageDirectory: concepts
  sources:
    - custom-judges-databricks-on-aws.md
  confidence: 0.92
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - best-practices-for-judge-instructions
    - BPFJI
  citations:
    - file: custom-judges-databricks-on-aws.md
title: Best Practices for Judge Instructions
description: Guidelines for writing effective LLM judge prompts including specifying output format (categorical, boolean, or numeric) and breaking down complex evaluations into structured sections.
tags:
  - prompt-engineering
  - llm-evaluation
  - best-practices
timestamp: "2026-06-19T18:03:28.136Z"
---

# Best Practices for Judge Instructions

**Best Practices for Judge Instructions** refers to guidelines for writing effective evaluation criteria for [Custom LLM Judges](/concepts/custom-llm-judges.md) created using the `make_judge()` API in [MLflow GenAI](/concepts/mlflow-3-for-genai.md). Well-structured judge instructions produce reliable, consistent assessments of GenAI agents at scale. ^[custom-judges-databricks-on-aws.md]

## Overview

[Custom Judges](/concepts/custom-judges.md) are LLM-based scorers that evaluate agent outputs against natural language instructions. The instructions define how the judge should assess quality using template variables that access agent execution data. Following best practices when writing these instructions improves evaluation accuracy and reproducibility. ^[custom-judges-databricks-on-aws.md]

## Core Principles

### Be Specific About Expected Output Format

Instructions must clearly specify what format the judge should return. Use explicit language to define the output shape: ^[custom-judges-databricks-on-aws.md]

- **Categorical responses**: List specific values such as `'fully_resolved'`, `'partially_resolved'`, or `'needs_follow_up'`.
- **Boolean responses**: Explicitly state the judge should return `true` or `false`.
- **Numeric scores**: Specify the scoring range and what each score means.

### Structure Complex Evaluations

For complex evaluation tasks, break instructions into clear, logical sections. Each section should address a specific aspect of the evaluation: ^[custom-judges-databricks-on-aws.md]

1. **What to evaluate** – Define the specific aspect of agent behavior or output to assess.
2. **What information to examine** – Specify which template variables (`{{ inputs }}`, `{{ outputs }}`, `{{ expectations }}`, `{{ trace }}`) to analyze.
3. **How to make the judgment** – Provide clear reasoning steps or criteria.
4. **What format to return** – Define the exact output structure the judge should produce.

### Use Appropriate Template Variables

Instructions must include at least one [template variable](/concepts/prompt-template-variables.md) to access agent data. Allowed variables are: `{{ inputs }}`, `{{ outputs }}`, `{{ expectations }}`, and `{{ trace }}`. Custom variables like `{{ question }}` will throw validation errors to ensure consistent behavior and prevent template injection issues. ^[custom-judges-databricks-on-aws.md]

## Trace-Based Judge Instructions

[Trace-based Judges](/concepts/trace-based-judges.md) analyze execution traces to evaluate tool usage, identify bottlenecks, investigate failures, and verify multi-step workflows. These judges use Model Context Protocol (MCP) tools to autonomously explore traces. ^[custom-judges-databricks-on-aws.md]

### Model Requirements

Trace-based judges require a model capable of trace analysis, served by [Foundation Model APIs](/concepts/foundation-model-apis.md) (recommended), External Model Serving Endpoints, or [Custom Model Serving Endpoints](/concepts/custom-model-serving-endpoint-support.md). Recommended models include `databricks:/databricks-gpt-5-mini`, `databricks:/databricks-gpt-5`, `databricks:/databricks-gpt-oss-120b`, and `databricks:/databricks-claude-opus-4-5`. ^[custom-judges-databricks-on-aws.md]

### Including Trace in Instructions

For trace-based judges, include `{{ trace }}` in the instructions. The `model` argument must be specified in `make_judge()` to enable full trace analysis. ^[custom-judges-databricks-on-aws.md]

## Iterative Improvement

### Base Judges as Starting Points

Initial judge instructions serve as a starting point. As expert feedback is gathered on application outputs, the judge instructions can be refined to better align with human quality standards. See [Align judges with human experts](/concepts/aligning-judges-with-human-experts.md) for guidance on improving judge accuracy. ^[custom-judges-databricks-on-aws.md]

### Aligning with Human Feedback

After collecting expert annotations on agent outputs, update judge instructions to reflect human quality expectations. This iterative alignment process improves the reliability of automated evaluations and ensures they match domain-specific requirements. ^[custom-judges-databricks-on-aws.md]

## Common Pitfalls

- **Overly vague criteria** – Instructions like “assess quality” without specific definitions produce inconsistent results. ^[custom-judges-databricks-on-aws.md]
- **Missing output format** – Without specifying structure, judges may return unpredictable formats. ^[custom-judges-databricks-on-aws.md]
- **Custom template variables** – Using non-standard variables like `{{ question }}` instead of `{{ inputs }}` causes validation errors. ^[custom-judges-databricks-on-aws.md]
- **No trace model for trace judges** – Trace-based judges require a `model` argument; omitting it prevents trace analysis. ^[custom-judges-databricks-on-aws.md]

## Related Concepts

- [Custom Judges](/concepts/custom-judges.md) – LLM-based scorers using `make_judge()`
- make_judge()|Make Judge API – The `make_judge()` function for creating evaluators
- Template Variables – Variables for accessing agent execution data
- [Trace-Based Evaluation](/concepts/mlflow-trace-based-evaluation.md) – Using execution traces for deeper quality analysis
- [Foundation Model APIs](/concepts/foundation-model-apis.md) – Recommended model serving for trace judges
- [Align Judges with Human Experts](/concepts/aligning-judges-with-human-experts.md) – Improving judge accuracy with expert annotations

## Sources

- custom-judges-databricks-on-aws.md

# Citations

1. [custom-judges-databricks-on-aws.md](/references/custom-judges-databricks-on-aws-7a56fe4f.md)
