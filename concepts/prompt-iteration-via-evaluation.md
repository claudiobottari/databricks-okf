---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 645ee863b35c73f8f9c2611634e90a81c387f57f7a8fedebc62b5265164063c1
  pageDirectory: concepts
  sources:
    - 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - prompt-iteration-via-evaluation
    - PIVE
  citations:
    - file: 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md
title: Prompt Iteration via Evaluation
description: Iterative development workflow where GenAI prompts are refined based on quantitative evaluation results, with runs compared in the MLflow UI.
tags:
  - prompt-engineering
  - mlflow
  - iteration
timestamp: "2026-06-19T08:46:45.226Z"
---

# Prompt Iteration via Evaluation

**Prompt Iteration via Evaluation** is a systematic process for improving the performance of GenAI agents and [Large Language Models (LLMs)](/concepts/large-language-models-llms-on-databricks.md) by repeatedly refining prompts, running evaluations, and comparing results. This methodology forms the core of modern AI application development workflows.

## Overview

Prompt iteration via evaluation is a cyclical process that involves generating an initial response, evaluating it against predefined criteria, and then refining the prompt to produce better results. This approach enables developers to systematically improve their AI agents through data-driven decision making rather than guesswork.^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

## The Iteration Cycle

### Step 1: Initial Evaluation

The process begins with creating a baseline evaluation of the current prompt configuration. Using [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) tools like `mlflow.genai.evaluate()`, developers can assess how their AI system performs across multiple dimensions, including:

- Response quality and Safety evaluation
- [Guidelines adherence](/concepts/guidelines-scorer.md) and Template matching
- Creativity and Appropriateness for target audience^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

### Step 2: Analysis and Refinement

After reviewing evaluation results, developers identify specific areas for improvement. For example, an initial prompt might produce responses that are "not appropriate for children" or "lack creativity." The prompt is then refined with more specific instructions about:

- **Target audience**: Specifying age-appropriate content (e.g., "child appropriate for 1 to 6 year olds")
- **Desired qualities**: Requesting specific traits like "silly, unexpected, and absurd" responses
- **Output constraints**: Providing clear examples of desired and undesired outputs^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

### Step 3: Re-Evaluation

The refined prompt is then tested against the same [Evaluation Dataset](/concepts/evaluation-dataset.md) using identical evaluation criteria. This ensures that any changes in performance are directly attributable to the prompt modification rather than inconsistencies in the assessment process.^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

### Step 4: Comparison

Results from different prompt configurations are compared side-by-side using the [MLflow UI](/concepts/mlflow.md), allowing developers to see:

- Which version performs better across each evaluation criterion
- How specific changes to instructions affect output quality
- Whether the improvements are consistent across multiple test cases^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

## Evaluation Criteria

### Guidelines Scorers

[Guidelines scorers](/concepts/guidelines-scorer.md) are automated evaluation tools that assess how well outputs meet specific criteria. Common examples include:

- **Language consistency**: "Response must be in the same language as the input"
- **Creativity**: "Response must be funny or creative"
- **Safety**: "Response must be appropriate for children"
- **Structure**: "Response must follow the input template structure"^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

### Safety Scorers

[Safety scorers](/concepts/safety-scorer-in-mlflow.md) are built-in evaluation tools that automatically check for harmful or inappropriate content. These provide an essential baseline for any AI application, particularly those intended for broad or sensitive use cases.^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

## Best Practices

### Use Diverse Evaluation Data

The evaluation dataset should reflect the range of inputs the system will encounter in production. This ensures that prompt improvements are robust across different scenarios rather than optimized for a narrow set of test cases.^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

### Iterate on Specific Problems

Rather than making broad changes, each iteration should target specific weaknesses identified in the evaluation results. For example:

- If responses lack creativity, add specific examples of creative outputs
- If responses are too realistic, specify desired degrees of absurdity
- If responses are inappropriate, add explicit safety guidelines^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

### Track Changes Systematically

Using [MLflow Experiments](/concepts/mlflow-experiment.md) to track each iteration creates an auditable history of prompt development. This enables:

- Reproducibility of results
- Comparison between versions for validation
- Regression testing when making further changes^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

## Related Concepts

- Prompt engineering — The art and science of designing effective AI instructions
- [Evaluation Dataset](/concepts/evaluation-dataset.md) — Representative test cases for assessing AI performance
- Guidelines evaluation — Scoring AI outputs against defined criteria
- AI agent development — The broader context of building AI systems
- A/B comparison — Comparing different configurations of the same system
- [Production Monitoring](/concepts/production-monitoring.md) — Ongoing evaluation of deployed AI systems

## Sources

- 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md

# Citations

1. [10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md](/references/10-minute-demo-evaluate-a-genai-app-databricks-on-aws-c90f1438.md)
