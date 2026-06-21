---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8abdaeb767140189237972f769106a36d25a6228fdb7cc5db322da00b2fdeec2
  pageDirectory: concepts
  sources:
    - deploy-models-using-model-serving-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ai-functions
    - Function
    - Functions
    - functions
  citations:
    - file: deploy-models-using-model-serving-databricks-on-aws.md
title: AI Functions
description: SQL-based functions tightly integrated with Model Serving for batch inference, allowing users to call models directly from SQL analytics workflows without configuring endpoints for pre-provisioned models.
tags:
  - sql
  - batch-inference
  - ai-functions
  - databricks
timestamp: "2026-06-19T18:30:07.071Z"
---

```markdown
---
title: AI Functions
summary: Built-in SQL functions in Databricks that allow users to apply AI models to data using SQL queries for batch inference.
sources:
  - deploy-models-using-model-serving-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:59:17.651Z"
updatedAt: "2026-06-19T15:10:05.926Z"
tags:
  - databricks
  - sql
  - ai-functions
  - batch-inference
aliases:
  - ai-functions
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# AI Functions

**AI Functions** are built-in SQL-callable functions in Databricks that allow users to apply AI and machine learning models directly to data stored in the lakehouse. They provide a no-code interface for integrating AI inference into analytics workflows, enabling batch inference without writing Python or making REST API calls. ^[deploy-models-using-model-serving-databricks-on-aws.md]

## Overview

AI Functions bridge the gap between SQL analytics and AI/ML model serving. They are designed for batch inference scenarios where you need to process large datasets stored in Databricks tables. AI Functions include both task-specific functions and the general-purpose `ai_query()` function. ^[deploy-models-using-model-serving-databricks-on-aws.md]

Key characteristics:
- **SQL-native**: Callable directly in SQL statements for easy integration into analytics workflows.
- **Batch inference**: Designed for processing large datasets in batch pipelines without moving data out of the lakehouse.
- **Two categories**: Task-specific AI functions (e.g., `ai_translate`) and the general-purpose `ai_query()` function. ^[deploy-models-using-model-serving-databricks-on-aws.md]

## Integration with Model Serving

AI Functions and [[Model Serving]] are tightly integrated for batch inference scenarios. You can use either task-specific AI functions or `ai_query()` in your batch inference pipelines. If you choose to use a pre-provisioned model that is hosted and managed by Databricks (such as those available through [[Foundation Model APIs]]), you do not need to configure a model serving endpoint yourself. ^[deploy-models-using-model-serving-databricks-on-aws.md]

For an introductory guide on performing batch inference with AI Functions, see the documentation on enriching data using AI Functions. ^[deploy-models-using-model-serving-databricks-on-aws.md]

## Related Concepts

- ai_query – The general-purpose AI function for querying models.
- [[Model Serving]] – Real-time model serving infrastructure on Databricks.
- [[Foundation Model APIs]] – Pre-provisioned models accessible via AI Functions.
- [[External Models]] – Third-party models served through Databricks.

## Sources

- deploy-models-using-model-serving-databricks-on-aws.md
```

# Citations

1. [deploy-models-using-model-serving-databricks-on-aws.md](/references/deploy-models-using-model-serving-databricks-on-aws-7a559b74.md)
