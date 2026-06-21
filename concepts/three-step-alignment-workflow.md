---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 26f7441a70ac4745ccf64d6f8e98f20af636ba211c512c1333ab9e9202b429ab
  pageDirectory: concepts
  sources:
    - align-judges-with-humans-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - three-step-alignment-workflow
    - TAW
  citations:
    - file: align-judges-with-humans-databricks-on-aws.md
title: Three-Step Alignment Workflow
description: "The structured process for aligning judges: generate initial assessments, collect human feedback, then align and deploy using the align() method."
tags:
  - workflow
  - alignment
  - mlflow
timestamp: "2026-06-19T22:05:01.630Z"
---

```markdown
---
title: Three-Step Alignment Workflow
summary: "The standard process for judge alignment: (1) generate initial assessments, (2) collect human feedback, (3) align and deploy via the align() method."
sources:
  - align-judges-with-humans-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T14:24:14.217Z"
updatedAt: "2026-06-19T13:59:10.422Z"
tags:
  - workflow
  - llm-evaluation
  - mlflow
aliases:
  - three-step-alignment-workflow
  - TAW
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# Three-Step Alignment Workflow

**Three-Step Alignment Workflow** is a systematic process for teaching [[LLM judges]] to match human evaluation standards by collecting and incorporating human feedback. The workflow transforms generic evaluators into domain-specific experts that understand your unique quality criteria, improving agreement with human assessments by 30 to 50 percent compared to baseline judges. ^[align-judges-with-humans-databricks-on-aws.md]

## Overview

The same alignment workflow applies to both [[built-in judges]] (such as `RelevanceToQuery`, `Safety`, or `Correctness`) and [[custom judges]] created with `make_judge()`. Use alignment with built-in judges to adapt their generic criteria to your domain, or with custom judges to refine specialized evaluation logic. ^[align-judges-with-humans-databricks-on-aws.md]

Judge alignment follows a three-step workflow:

1. **Generate initial assessments**: Use a built-in or custom judge to evaluate traces and establish a baseline.
2. **Collect human feedback**: Domain experts review and correct judge assessments.
3. **Align and deploy**: Invoke the judge's `align()` method to create a new judge that is more aligned with human feedback.

The system supports optimizers available in the package `mlflow.genai.judges.optimizers`. ^[align-judges-with-humans-databricks-on-aws.md]

## Requirements

- **MLflow 3.4.0 or above** to use judge alignment features. ^[align-judges-with-humans-databricks-on-aws.md]
- **A judge to align** – either a built-in judge (for example, `RelevanceToQuery` or `Correctness`) or a custom judge created with `make_judge()`. ^[align-judges-with-humans-databricks-on-aws.md]
- **Matching assessment name** – the human feedback assessment name must exactly match the judge's `name` attribute. For built-in judges, this is the default snake_case name (for example, `relevance_to_query` for `RelevanceToQuery`) unless you override it by passing `name=` when instantiating the class. For custom judges, it's the `name` you passed to `make_judge()`. ^[align-judges-with-humans-databricks-on-aws.md]
- Alignment is **not** supported for session-level (multi-turn) judges such as `ConversationCompleteness`. ^[align-judges-with-humans-databricks-on-aws.md]

## Workflow Steps

### Step 1: Generate Initial Assessments

Set up your initial judge and generate traces with assessments. You can achieve reasonable alignment with at least 10 traces, but 50–100 traces yield better results. ^[align-judges-with-humans-databricks-on-aws.md]

After generating each trace, log the judge assessment to the trace using `mlflow.log_feedback()` with the judge's `name` as the feedback name. ^[align-judges-with-humans-databricks-on-aws.md]

### Step 2: Collect Human Feedback

Domain experts review and correct judge assessments. You can collect feedback using either the **Databricks UI** (navigate to the experiment's **Traces** tab and add feedback) or a **programmatic** approach. Collect human feedback when you need domain experts to review outputs, want to iteratively refine feedback criteria, or are working with a smaller dataset (fewer than 100 examples). ^[align-judges-with-humans-databricks-on-aws.md]

**Best practices for feedback collection** include:

- **Diverse reviewers**: Include multiple domain experts to capture varied perspectives.
- **Balanced examples**: Include at least 30% negative examples (poor/fair ratings).
- **Clear rationales**: Provide detailed explanations for ratings.
- **Representative samples**: Cover edge cases and common scenarios.

### Step 3: Align and Deploy

Once you have sufficient human feedback, call the judge's `align()` method. When you call `align()` without specifying an optimizer, the [[MemAlign optimizer]] is used automatically. ^[align-judges-with-humans-databricks-on-aws.md]

You can then register the aligned judge for production use using the `register()` method, giving it a new name to distinguish it from the original judge. ^[align-judges-with-humans-databricks-on-aws.md]

## Custom Alignment Optimizers

For specialized alignment strategies, extend the `AlignmentOptimizer` base class (available at `mlflow.genai.judges.base.AlignmentOptimizer`) to implement custom optimization logic. Then pass an instance of your optimizer to the `align()` method. ^[align-judges-with-humans-databricks-on-aws.md]

## Limitations

- Judge alignment does not support agent-based or expectation-based evaluation. ^[align-judges-with-humans-databricks-on-aws.md]

## Related Concepts

- [[Judge alignment]] — The broader concept of teaching judges to match human standards.
- [[LLM judges]] — AI-powered evaluators for assessing model outputs.
- [[Built-in judges]] — Pre-configured judges for common evaluation criteria.
- [[Custom judges]] — User-defined judges created with `make_judge()`.
- [[MemAlign optimizer]] — Default alignment optimizer used in the workflow.
- [[Production monitoring]] — Deploying aligned judges at scale.
- [[Code-based scorers]] — Complementary deterministic metrics for evaluation.

## Sources

- align-judges-with-humans-databricks-on-aws.md
```

# Citations

1. [align-judges-with-humans-databricks-on-aws.md](/references/align-judges-with-humans-databricks-on-aws-03f1583e.md)
