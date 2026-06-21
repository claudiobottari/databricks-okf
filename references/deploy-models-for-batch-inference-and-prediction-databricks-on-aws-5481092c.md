---
title: Deploy models for batch inference and prediction | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/model-inference/
ingestedAt: "2026-06-18T08:11:38.678Z"
---

This article describes what Databricks recommends for batch inference.

For real-time model serving on Databricks, see [Deploy models using Model Serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/).

## AI Functions for batch inference[​](#-ai-functions-for-batch-inference "Direct link to -ai-functions-for-batch-inference")

AI Functions are built-in functions that you can use to apply AI on your data that is stored on Databricks. You can run batch inference using [task-specific AI functions](https://docs.databricks.com/aws/en/large-language-models/ai-functions#fmapi-functions) or the general purpose function, `ai_query`.

The following is an example of batch inference using the task-specific AI function, `ai_translate`. If you want perform batch inference on an entire table, you can remove the `limit 500` from your query.

SQL

    SELECTwriter_summary,  ai_translate(writer_summary, "cn") as cn_translationfrom user.batch.news_summarieslimit 500;

Alternatively, you can use the general purpose function, `ai_query` to perform batch inference.

*   See which [model types and the associated models](https://docs.databricks.com/aws/en/large-language-models/ai-query#supported-models) that `ai_query` supports.
*   See [Deploy batch inference pipelines](https://docs.databricks.com/aws/en/large-language-models/batch-inference-pipelines).
