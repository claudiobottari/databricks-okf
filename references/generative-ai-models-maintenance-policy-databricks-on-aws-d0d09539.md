---
title: Generative AI models maintenance policy | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/retired-models-policy
ingestedAt: "2026-06-18T08:13:15.210Z"
---

This article describes the model maintenance policy for the [Foundation Model APIs pay-per-token](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/#token-foundation-apis), [Foundation Model APIs provisioned throughput](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/#throughput), and [Foundation Model Fine-tuning](https://docs.databricks.com/aws/en/large-language-models/foundation-model-training/) offerings.

In order to continue supporting the most state-of-the-art models, Databricks might update supported models or retire older models for these offerings.

## Model retirement policy[​](#model-retirement-policy "Direct link to Model retirement policy")

The model retirement policy explains how Databricks notifies you when a supported model is set for retirement, what happens during the transition period, and what to expect on the retirement date. Timelines differ by offering and model category as summarized in the following sections.

For currently retired models and planned retirement dates, see [Retired models](#retired). For partner models, see [Partner model retirement policy](#partner-retire).

important

The retirement policies that apply to the Foundation Model APIs pay-per-token and Foundation Model Fine-tuning offerings only impact supported chat and completion models.

### Foundation Model APIs pay-per-token[​](#foundation-model-apis-pay-per-token "Direct link to Foundation Model APIs pay-per-token")

The following table summarizes the retirement policy for Foundation Model APIs pay-per-token.

### Foundation Model APIs provisioned throughput[​](#foundation-model-apis-provisioned-throughput "Direct link to Foundation Model APIs provisioned throughput")

The following table summarizes the retirement policy for Foundation Model APIs provisioned throughput.

### Partner model retirement policy[​](#-partner-model-retirement-policy "Direct link to -partner-model-retirement-policy")

Partner models are models provided by third-party partners, specifically OpenAI, Anthropic, and Google, that are available through Foundation Model APIs. For these partner models, Databricks generally follows the same deprecation timelines and policies as described for provisioned throughput and pay-per-token models.

However, retirement dates provided by partners might be shorter than the transition periods published by Databricks. In these cases, Databricks attempts to bridge the gap by temporarily redirecting models to a similar version, so customers receive the full transition time.

For example, if a pay-per-token model deprecation is announced with one month's lead time instead of three, Databricks redirects the model for an additional two months to prevent immediate breakage and allow time for migration. Queries fail at the end of the full three-month period.

note

This redirection can only occur if the replacement model has the same price and is backwards compatible. The replacement model is usually an incremental model version, like 3.0 versus 3.1.

### Foundation Model Fine-tuning[​](#foundation-model-fine-tuning "Direct link to Foundation Model Fine-tuning")

The following table summarizes the retirement policy for Foundation Model Fine-tuning.

## Model updates[​](#model-updates "Direct link to Model updates")

Databricks might ship incremental model updates to deliver optimizations. When a model is updated, the endpoint URL remains the same, but the model ID in the response object changes to reflect the date of the update. For example, if an update is shipped to `meta-llama/Meta-Llama-3.3-70B` on 3/4/2024, the model name in the response object updates to `meta-llama/Meta-Llama-3.3-70B-030424`. Databricks maintains a version history of the updates that you can refer to.

## Retired models[​](#retired-models "Direct link to retired-models")

The following sections summarize current and upcoming model retirements for the indicated feature offerings.

### Foundation Model APIs pay-per-token retirements[​](#foundation-model-apis-pay-per-token-retirements "Direct link to Foundation Model APIs pay-per-token retirements")

The following table shows model retirements, their retirement dates, and recommended replacement models to use for Foundation Model APIs pay-per-token serving workloads. Databricks recommends that you migrate your applications to use replacement models before the indicated retirement date.

If you require long-term support for a specific model version, Databricks recommends using Foundation Model APIs [provisioned throughput](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/#throughput) for your serving workloads.

### Foundation Model APIs provisioned throughput retirements[​](#foundation-model-apis-provisioned-throughput-retirements "Direct link to Foundation Model APIs provisioned throughput retirements")

The following table shows model family retirements, their retirement dates, and recommended replacement models to use for Foundation Model APIs provisioned throughput serving workloads. Databricks recommends that you migrate your applications to use replacement models before the indicated retirement date.

### Foundation Model Fine-tuning retirements[​](#foundation-model-fine-tuning-retirements "Direct link to foundation-model-fine-tuning-retirements")

The following table shows retired model families, their retirement dates, and recommended replacement model families to use for Foundation Model Fine-tuning workloads. Databricks recommends that you migrate your applications to use replacement models before the indicated retirement date.

## Find workloads that use retired models[​](#find-workloads-that-use-retired-models "Direct link to Find workloads that use retired models")

Use the following query to find workloads that are using deprecated models and identify their owners.

SQL

    SELECT   eu.requester,   se.endpoint_name,   se.entity_name,   COUNT(*) AS request_count,   SUM(eu.input_token_count) AS total_input_tokens,   SUM(eu.output_token_count) AS total_output_tokens,   MIN(eu.request_time) AS first_request,   MAX(eu.request_time) AS last_request FROM system.serving.endpoint_usage eu JOIN system.serving.served_entities se   ON eu.served_entity_id = se.served_entity_id WHERE LOWER(se.entity_name) LIKE '%<retired-model-name>%' GROUP BY eu.requester, se.endpoint_name, se.entity_name ORDER BY request_count DESC
