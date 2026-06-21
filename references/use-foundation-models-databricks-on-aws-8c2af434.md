---
title: Use foundation models | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/model-serving/score-foundation-models
ingestedAt: "2026-06-18T08:12:45.778Z"
---

In this article, you learn which options are available to write query requests for foundation models and how to send them to your model serving endpoint. You can query foundation models that are hosted by Databricks and foundation models hosted outside of Databricks.

For traditional ML or Python models query requests, see [Query serving endpoints for custom models](https://docs.databricks.com/aws/en/machine-learning/model-serving/score-custom-model-endpoints).

[Model Serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/) supports [Foundation Models APIs](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/) and [external models](https://docs.databricks.com/aws/en/generative-ai/external-models/) for accessing foundation models. Model Serving uses a unified OpenAI-compatible API and SDK for querying them. This makes it possible to experiment with and customize foundation models for production across supported clouds and providers.

## Query options[​](#-query-options "Direct link to -query-options")

Model Serving provides the following options for sending query requests to endpoints that serve foundation models:

## Requirements[​](#requirements "Direct link to requirements")

*   A [model serving endpoint](https://docs.databricks.com/aws/en/machine-learning/model-serving/create-foundation-model-endpoints).
*   A Databricks workspace in a supported region.
    *   [Foundation Model APIs regions](https://docs.databricks.com/aws/en/machine-learning/model-serving/model-serving-limits#regions)
    *   [External models regions](https://docs.databricks.com/aws/en/machine-learning/model-serving/model-serving-limits#regions)
*   To send a scoring request through the OpenAI client, REST API or MLflow Deployment SDK, you must have a Databricks API token.

## Install packages[​](#-install-packages "Direct link to -install-packages")

After you have selected a querying method, you must first install the appropriate package to your cluster.

*   OpenAI client
*   REST API
*   MLflow Deployments SDK
*   Databricks Python SDK

To use the OpenAI client, the `databricks-openai` package needs to be installed on your cluster. This package provides an OpenAI client with authorization automatically configured to query generative AI models. Run the following in your notebook or your local terminal:

    pip install -U databricks-openai

The following is only required when installing the package on a Databricks Notebook

Python

    dbutils.library.restartPython()

## Foundation model types[​](#-foundation-model-types "Direct link to -foundation-model-types")

The following table summarizes the supported foundation models based on task type.

important

Meta-Llama-3.1-405B-Instruct will be retired,

*   Starting February 15, 2026 for pay-per-token workloads.
*   Starting May 15, 2026 for provisioned throughput workloads.

See [Retired models](https://docs.databricks.com/aws/en/machine-learning/retired-models-policy#retired) for the recommended replacement model and guidance for how to migrate during deprecation.

## Function calling[​](#function-calling "Direct link to Function calling")

Databricks Function Calling is OpenAI-compatible and is only available during model serving as part of [Foundation Model APIs](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/) and serving endpoints that serve [external models](https://docs.databricks.com/aws/en/generative-ai/external-models/). For details, see [Function calling on Databricks](https://docs.databricks.com/aws/en/machine-learning/model-serving/function-calling).

## Structured outputs[​](#structured-outputs "Direct link to Structured outputs")

Structured outputs is OpenAI-compatible and is only available during model serving as part of [Foundation Model APIs](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/). For details, see [Structured outputs on Databricks](https://docs.databricks.com/aws/en/machine-learning/model-serving/structured-outputs).

## Prompt caching[​](#-prompt-caching "Direct link to -prompt-caching")

Prompt caching is supported for Databricks-hosted Claude models as part of [Foundation Model APIs](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/).

You can specify the `cache_control` parameter in your query requests to cache the following:

*   Text content messages in the `messages.content` array.
*   Thinking messages content in the `messages.content` array.
*   Images content blocks in the `messages.content` array.
*   Tool use, results and definitions in the `tools` array.

See [Foundation model REST API reference](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/api-reference).

*   TextContent
*   ReasonContent
*   ImageContent
*   ToolCallContent

JSON

    {  "messages": [    {      "role": "user",      "content": [        {          "type": "text",          "text": "What's the date today?",          "cache_control": { "type": "ephemeral" }        }      ]    }  ]}

note

The Databricks REST API is OpenAI-compatible and differs from the Anthropic API. These differences also impact response objects like the following:

*   Output is returned in the `choices` field.
*   Streaming chunk format. All chunks adhere to the same format where `choices` contains the response `delta` and usage is returned in every chunk.
*   Stop reason is returned in the `finish_reason` field.
    *   Anthropic uses: `end_turn`, `stop_sequence`, `max_tokens`, and `tool_use`
    *   Respectively, Databricks uses: `stop`, `stop`, `length`, and `tool_calls`

## Chat with supported LLMs using AI Playground[​](#chat-with-supported-llms-using-ai-playground "Direct link to chat-with-supported-llms-using-ai-playground")

You can interact with supported large language models using the [AI Playground](https://docs.databricks.com/aws/en/large-language-models/ai-playground). The AI Playground is a chat-like environment where you can test, prompt, and compare LLMs from your Databricks workspace.

![AI playground](https://docs.databricks.com/aws/en/assets/images/ai-playground-db12d6cfd71a5675ab6f4d8131466cea.png)

## Additional resources[​](#additional-resources "Direct link to Additional resources")

*   [Monitor served models using Unity AI Gateway\-enabled inference tables](https://docs.databricks.com/aws/en/ai-gateway/inference-tables)
*   [Deploy batch inference pipelines](https://docs.databricks.com/aws/en/large-language-models/batch-inference-pipelines)
*   [Databricks Foundation Model APIs](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/)
*   [External models in Model Serving](https://docs.databricks.com/aws/en/generative-ai/external-models/)
*   [Tutorial: Create external model endpoints to query OpenAI models](https://docs.databricks.com/aws/en/generative-ai/tutorials/external-models-tutorial)
*   [Databricks-hosted foundation models available in Foundation Model APIs](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/supported-models)
*   [Foundation model REST API reference](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/api-reference)
