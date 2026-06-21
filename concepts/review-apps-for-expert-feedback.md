---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: db8c22a01de9b7ea91381c829d457db1837a5654d252dfe3c3804be824cce71f
  pageDirectory: concepts
  sources:
    - mlflow-3-for-genai-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - review-apps-for-expert-feedback
    - RAFEF
    - Expert Feedback
    - expert feedback
    - expert feedback UI
  citations:
    - file: mlflow-3-for-genai-databricks-on-aws.md
title: Review Apps for Expert Feedback
description: Feature in MLflow 3 for collecting expert-labeled datasets to align automated judges and scorers with human judgement
tags:
  - feedback
  - human-in-the-loop
  - evaluation
timestamp: "2026-06-19T19:37:29.271Z"
---

# Review Apps for Expert Feedback

**Review Apps for Expert Feedback** is a feature within [MLflow 3 for GenAI](/concepts/mlflow-3-for-genai.md) that enables collection and evaluation of expert judgment on [Generative AI](/concepts/mlflow-tracing-for-generative-ai.md) applications and agents. It provides a structured interface where subject matter experts can review model outputs, provide ratings, and label datasets, helping to align automated [LLM Judges and Scorers](/concepts/llm-judges-and-scorers.md) with human expertise. ^[mlflow-3-for-genai-databricks-on-aws.md]

## Purpose

Evaluating [GenAI](/concepts/mlflow-genai-evaluate-api.md) applications is fundamentally different from evaluating traditional software. Inputs and outputs are often free-form text, and many different outputs can be considered correct. Quality depends not only on correctness but also on factors like precision, length, completeness, appropriateness, and other criteria specific to the use case. Because [Large Language Models (LLMs)](/concepts/large-language-models-llms-on-databricks.md) are inherently non-deterministic, and GenAI agents include additional components such as retrievers and tools, their responses can vary from run to run. ^[mlflow-3-for-genai-databricks-on-aws.md]

Review apps provide a mechanism to bridge the gap between automated evaluation and human judgment by allowing experts to:

- Review model outputs and provide feedback
- Rate responses based on quality criteria
- Create labeled datasets for evaluation
- Align automated scorers with expert judgment

^[mlflow-3-for-genai-databricks-on-aws.md]

## Integration with MLflow 3

Review apps for expert feedback are part of MLflow 3 for GenAI's evaluation and monitoring capabilities. They work alongside [built-in and custom LLM judges and scorers](/concepts/custom-llm-as-a-judge-in-scorers.md) to create a comprehensive quality assessment pipeline. Expert feedback collected through review apps can be used to:

- Validate automated evaluation metrics
- Improve model performance through iterative refinement
- Establish ground truth for evaluation datasets
- Track quality improvements over time

^[mlflow-3-for-genai-databricks-on-aws.md]

## Related Concepts

- [Tracing](/concepts/mlflow-tracing.md) – Provides the data foundation for evaluation and monitoring by automatically logging inputs, intermediate steps, and outputs
- [Automated evaluation](/concepts/automated-evaluation-and-monitoring.md) – Uses the same judges and scorers during development and production
- App and prompt versioning – Allows comparison of versions and tracking improvements over iterations
- [Human feedback](/concepts/mlflow-human-feedback-collection.md) – Incorporation of expert judgment into the evaluation pipeline
- [GenAI app lifecycle](/concepts/genai-app-lifecycle-management.md) – Enterprise-grade lifecycle management and governance tools

## Sources

- mlflow-3-for-genai-databricks-on-aws.md

# Citations

1. [mlflow-3-for-genai-databricks-on-aws.md](/references/mlflow-3-for-genai-databricks-on-aws-ac0de02b.md)
