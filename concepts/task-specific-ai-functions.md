---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 86b3eea24edd1ebf30241c118c30f9d93819e46884115f2611c8c168da6ba125
  pageDirectory: concepts
  sources:
    - deploy-models-for-batch-inference-and-prediction-databricks-on-aws.md
  confidence: 0.8
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - task-specific-ai-functions
    - TAF
  citations:
    - file: deploy-models-for-batch-inference-and-prediction-databricks-on-aws.md
title: Task-Specific AI Functions
description: Specialized built-in SQL functions in Databricks for specific AI tasks like ai_translate, designed for targeted batch inference workloads
tags:
  - databricks
  - sql
  - ai-functions
  - natural-language-processing
timestamp: "2026-06-19T18:29:39.917Z"
---

---
title: Task-Specific AI Functions
summary: Specialized built-in AI functions in Databricks (such as ai_translate) designed for specific NLP tasks, enabling batch inference without writing custom ML code.
sources:
  - deploy-models-for-batch-inference-and-prediction-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:58:49.452Z"
updatedAt: "2026-06-19T10:11:36.440Z"
tags:
  - databricks
  - ai-functions
  - nlp
aliases:
  - task-specific-ai-functions
  - TAF
confidence: 0.9
provenanceState: extracted
inferredParagraphs: 0
---

# Task-Specific AI Functions

**Task-Specific AI Functions** are built-in SQL functions in Databricks designed for common natural language processing tasks such as translation, summarization, and classification. They allow you to apply AI to data stored in Databricks without writing custom prompts or managing model endpoints directly, enabling [batch inference](/concepts/batch-inference-on-databricks.md) with simple SQL queries. ^[deploy-models-for-batch-inference-and-prediction-databricks-on-aws.md]

## Batch Inference Example

The following SQL query uses the task-specific AI function `ai_translate` to translate a column of text into Chinese. The `LIMIT 500` clause can be removed to run batch inference on the entire table: ^[deploy-models-for-batch-inference-and-prediction-databricks-on-aws.md]

```sql
SELECT
  writer_summary,
  ai_translate(writer_summary, "cn") as cn_translation
FROM user.batch.news_summaries
LIMIT 500;
```

## Alternatives

For more general-purpose AI inference, Databricks provides the `ai_query()` function. See which model types and associated models `ai_query` supports, and refer to [Batch Inference Pipelines](/concepts/batch-inference-pipelines.md) for additional deployment guidance. ^[deploy-models-for-batch-inference-and-prediction-databricks-on-aws.md]

## Related Concepts

- ai_query — The general-purpose function for custom AI inference
- [Batch Inference Pipelines](/concepts/batch-inference-pipelines.md) — Pipelines for processing large-scale inference workloads
- [Model Serving](/concepts/model-serving.md) — Real-time inference infrastructure on Databricks

## Sources

- deploy-models-for-batch-inference-and-prediction-databricks-on-aws.md

# Citations

1. [deploy-models-for-batch-inference-and-prediction-databricks-on-aws.md](/references/deploy-models-for-batch-inference-and-prediction-databricks-on-aws-5481092c.md)
