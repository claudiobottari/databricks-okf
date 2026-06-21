---
title: Query with the Anthropic Messages API | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/model-serving/query-anthropic-messages
ingestedAt: "2026-06-18T08:12:26.503Z"
---

important

The Anthropic Messages API is only compatible with Anthropic pay per token foundation models and external models. For a unified API that works across all providers, use the [Chat Completions API](https://docs.databricks.com/aws/en/machine-learning/model-serving/query-chat-models).

The Anthropic Messages API provides native Anthropic SDK compatibility for Claude models on Databricks. Use this API when you need Anthropic-specific features or are migrating existing Anthropic SDK code.

## Requirements[​](#requirements "Direct link to Requirements")

*   See [Requirements](https://docs.databricks.com/aws/en/machine-learning/model-serving/score-foundation-models#required).
*   Install the `anthropic` package on your compute.

## Query examples[​](#query-examples "Direct link to Query examples")

The following examples show how to query a Foundation Model API pay-per-token endpoint using the Anthropic Messages API.

*   Python
*   REST API

Python

    import anthropicimport osDATABRICKS_TOKEN = os.environ.get('DATABRICKS_TOKEN')client = anthropic.Anthropic(    api_key="unused",    base_url="https://example.staging.cloud.databricks.com/serving-endpoints/anthropic",    default_headers={        "Authorization": f"Bearer {DATABRICKS_TOKEN}",    },)message = client.messages.create(    model="databricks-claude-sonnet-4-5",    max_tokens=256,    messages=[        {"role": "user", "content": "What is a mixture of experts model?"},    ],)print(message.content[0].text)

## Supported models[​](#supported-models "Direct link to Supported models")

### Databricks-hosted foundation models[​](#databricks-hosted-foundation-models "Direct link to Databricks-hosted foundation models")

important

Anthropic Claude 3.7 Sonnet will be retired on April 12, 2026. See [Retired models](https://docs.databricks.com/aws/en/machine-learning/retired-models-policy#retired) for the recommended replacement model and guidance for how to migrate during deprecation.

*   `databricks-claude-opus-4-7`
*   `databricks-claude-opus-4-6`
*   `databricks-claude-sonnet-4-6`
*   `databricks-claude-sonnet-4-5`
*   `databricks-claude-haiku-4-5`
*   `databricks-claude-opus-4-5`
*   `databricks-claude-opus-4-1`
*   `databricks-claude-sonnet-4`

### External models[​](#external-models "Direct link to External models")

*   Anthropic model provider
*   Bedrock Anthropic model provider

## Supported input types[​](#supported-input-types "Direct link to Supported input types")

Anthropic Claude models on Databricks accept text and image inputs. See [Query vision models](https://docs.databricks.com/aws/en/machine-learning/model-serving/query-vision-models) for image format and size requirements. For per-model input types, see [Databricks-hosted foundation models available in Foundation Model APIs](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/supported-models).

## Additional resources[​](#additional-resources "Direct link to Additional resources")

*   [Query a chat model](https://docs.databricks.com/aws/en/machine-learning/model-serving/query-chat-models).
*   [Databricks-hosted foundation models available in Foundation Model APIs](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/supported-models).
