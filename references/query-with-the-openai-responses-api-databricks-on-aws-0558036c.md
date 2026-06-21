---
title: Query with the OpenAI Responses API | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/model-serving/query-openai-responses
ingestedAt: "2026-06-18T08:12:34.998Z"
---

important

The Responses API is only compatible with OpenAI pay per token foundation models and external models. For a unified API that works across all providers, use the [Chat Completions API](https://docs.databricks.com/aws/en/machine-learning/model-serving/query-chat-models).

The OpenAI Responses API is an alternative to the Chat Completions API that provides additional features for OpenAI models, including custom tools and multi-step workflows.

## Requirements[​](#requirements "Direct link to Requirements")

*   See [Requirements](https://docs.databricks.com/aws/en/machine-learning/model-serving/score-foundation-models#required).
*   [Install the appropriate package](https://docs.databricks.com/aws/en/machine-learning/model-serving/score-foundation-models#install) to your cluster based on the [querying client option](https://docs.databricks.com/aws/en/machine-learning/model-serving/score-foundation-models#client-options) you choose.

## Query examples[​](#query-examples "Direct link to Query examples")

The examples in this section show how to query a Foundation Model API pay-per-token endpoint using the OpenAI Responses API.

*   Python (DatabricksOpenAI)
*   Python (OpenAI)
*   REST API

To use the OpenAI Responses API, specify the model serving endpoint name as the `model` input.

Python

    from databricks_openai import DatabricksOpenAIclient = DatabricksOpenAI()response = client.responses.create(    model="databricks-gpt-5",    input=[      {        "role": "system",        "content": "You are a helpful assistant."      },      {        "role": "user",        "content": "What is a mixture of experts model?",      }    ],    max_output_tokens=256)

Custom tools allow the model to return arbitrary string output instead of JSON-formatted function arguments. This is useful for code generation, applying patches, or other use cases where structured JSON is not required.

note

Custom tools are only supported with GPT-5 series models (`databricks-gpt-5`, `databricks-gpt-5-1`, `databricks-gpt-5-2`, `databricks-gpt-5-4`, `databricks-gpt-5-5`, `databricks-gpt-5-5-pro`) through the Responses API.

Python

    from databricks_openai import DatabricksOpenAIclient = DatabricksOpenAI()response = client.responses.create(    model="databricks-gpt-5",    input=[{"role": "user", "content": "Write a Python function to calculate factorial"}],    tools=[        {            "type": "custom",            "name": "code_exec",            "description": "Executes arbitrary Python code. Return only valid Python code."        }    ],    max_output_tokens=1024)

Built-in tools allow the model to call platform-provided capabilities without requiring you to implement the tool backend yourself. These tools return structured outputs and are fully managed by the platform.

Python

    from databricks_openai import DatabricksOpenAIclient = DatabricksOpenAI()response = client.responses.create(    model="databricks-gpt-5",    input=[{        "role": "user",        "content": "Add input validation to the factorial function in main.py."    }],    tools=[        {            "type": "apply_patch"        }    ],    max_output_tokens=1024)print(response.output_text)

## Supported models[​](#supported-models "Direct link to Supported models")

### Databricks-hosted foundation models[​](#databricks-hosted-foundation-models "Direct link to Databricks-hosted foundation models")

*   `databricks-gpt-5-5-pro`
*   `databricks-gpt-5-5`
*   `databricks-gpt-5-4`
*   `databricks-gpt-5-4-mini`
*   `databricks-gpt-5-4-nano`
*   `databricks-gpt-5-3-codex`
*   `databricks-gpt-5-2`
*   `databricks-gpt-5-2-codex`
*   `databricks-gpt-5-1`
*   `databricks-gpt-5-1-codex-max`
*   `databricks-gpt-5-1-codex-mini`
*   `databricks-gpt-5`
*   `databricks-gpt-5-mini`
*   `databricks-gpt-5-nano`

### External models[​](#external-models "Direct link to External models")

*   OpenAI model provider
*   Azure OpenAI model provider

## Supported input types[​](#supported-input-types "Direct link to Supported input types")

OpenAI GPT models on Databricks accept text and image inputs. See [Query vision models](https://docs.databricks.com/aws/en/machine-learning/model-serving/query-vision-models) for image format and size requirements. For per-model input types, see [Databricks-hosted foundation models available in Foundation Model APIs](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/supported-models).

## Limitations[​](#limitations "Direct link to Limitations")

The following limitations apply to [pay-per-token foundation models](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/#token-foundation-apis) only. External models support all Responses API parameters and tools.

The following parameters are not supported and return a 400 error if specified:

*   `background` — Background processing is not supported.
*   `store` — Stored responses is not supported.
*   `previous_response_id` — Stored responses is not supported.
*   `service_tier` — Service tier selection is managed by Databricks.

The following tool types are supported for pay-per-token foundation models:

*   `function` — Traditional structured function calling
*   `custom` — Custom user-defined tools
*   `apply_patch` — Code patching operations
*   `shell` — Shell command execution
*   `image_generation` — Image generation
*   `mcp` — Model Context Protocol tools
*   `web_search` — Web search

## Additional resources[​](#additional-resources "Direct link to Additional resources")

*   [Query a chat model](https://docs.databricks.com/aws/en/machine-learning/model-serving/query-chat-models).
*   [Function calling on Databricks](https://docs.databricks.com/aws/en/machine-learning/model-serving/function-calling).
*   [Structured outputs on Databricks](https://docs.databricks.com/aws/en/machine-learning/model-serving/structured-outputs).
