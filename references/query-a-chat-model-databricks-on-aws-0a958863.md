---
title: Query a chat model | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/model-serving/query-chat-models
ingestedAt: "2026-06-18T08:12:29.917Z"
---

In this article, you learn how to write query requests for foundation models that are optimized for chat and general purpose tasks and send them to your model serving endpoint.

The examples in this article apply to querying foundation models that are made available using either:

*   [Foundation Models APIs](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/) which are referred to as **Databricks-hosted foundation models**.
*   [External models](https://docs.databricks.com/aws/en/generative-ai/external-models/) which are referred to as **foundation models hosted outside of Databricks**.

## Requirements[​](#requirements "Direct link to Requirements")

*   See [Requirements](https://docs.databricks.com/aws/en/machine-learning/model-serving/score-foundation-models#required).
*   [Install the appropriate package](https://docs.databricks.com/aws/en/machine-learning/model-serving/score-foundation-models#install) to your cluster based on the [querying client option](https://docs.databricks.com/aws/en/machine-learning/model-serving/score-foundation-models#client-options) you choose.

## Query examples[​](#-query-examples "Direct link to -query-examples")

The examples in this section show how to query a Foundation Model API pay-per-token endpoint using the different [client options](https://docs.databricks.com/aws/en/machine-learning/model-serving/score-foundation-models#client-options).

For a batch inference example, see [Enrich data using AI Functions](https://docs.databricks.com/aws/en/large-language-models/ai-functions).

*   OpenAI Chat Completions
*   OpenAI Responses
*   SQL
*   REST API
*   MLflow Deployments SDK
*   Databricks Python SDK
*   LangChain

To use the OpenAI client, specify the model serving endpoint name as the `model` input.

Python

    from databricks_openai import DatabricksOpenAIclient = DatabricksOpenAI()response = client.chat.completions.create(    model="databricks-claude-sonnet-4-5",    messages=[      {        "role": "system",        "content": "You are a helpful assistant."      },      {        "role": "user",        "content": "What is a mixture of experts model?",      }    ],    max_tokens=256)

To query foundation models outside of your workspace, you must use the OpenAI client directly. You also need your Databricks workspace instance to connect the OpenAI client to Databricks. The following example assumes you have a Databricks API token and `openai` installed on your compute.

Python

    import osimport openaifrom openai import OpenAIclient = OpenAI(    api_key="dapi-your-databricks-token",    base_url="https://example.staging.cloud.databricks.com/serving-endpoints")response = client.chat.completions.create(    model="databricks-claude-sonnet-4-5",    messages=[      {        "role": "system",        "content": "You are a helpful assistant."      },      {        "role": "user",        "content": "What is a mixture of experts model?",      }    ],    max_tokens=256)

As an example, the following is the expected request format for a chat model when using the REST API. For external models, you can include additional parameters that are valid for a given provider and endpoint configuration. See [Additional query parameters](https://docs.databricks.com/aws/en/generative-ai/external-models/#extra-parameters).

Bash

    {  "messages": [    {      "role": "user",      "content": "What is a mixture of experts model?"    }  ],  "max_tokens": 100,  "temperature": 0.1}

The following is an expected response format for a request made using the REST API:

JSON

    {  "model": "databricks-claude-sonnet-4-5",  "choices": [    {      "message": {},      "index": 0,      "finish_reason": null    }  ],  "usage": {    "prompt_tokens": 7,    "completion_tokens": 74,    "total_tokens": 81  },  "object": "chat.completion",  "id": null,  "created": 1698824353}

## Supported models[​](#supported-models "Direct link to Supported models")

See [Foundation model types](https://docs.databricks.com/aws/en/machine-learning/model-serving/score-foundation-models#model-types) for supported chat models.

## Additional resources[​](#additional-resources "Direct link to Additional resources")

*   [Query an embedding model](https://docs.databricks.com/aws/en/machine-learning/model-serving/query-embedding-models).
*   [Query reasoning models](https://docs.databricks.com/aws/en/machine-learning/model-serving/query-reason-models).
*   [Query vision models](https://docs.databricks.com/aws/en/machine-learning/model-serving/query-vision-models).
