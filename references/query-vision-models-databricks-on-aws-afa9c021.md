---
title: Query vision models | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/model-serving/query-vision-models
ingestedAt: "2026-06-18T08:12:40.478Z"
---

In this article, you learn how to write query requests for foundation models optimized for vision tasks, and send them to your model serving endpoint.

Model Serving provides a unified API to understand and analyze images using a variety of foundation models, unlocking powerful multimodal capabilities. This functionality is available through select Databricks-hosted models as part of [Foundation Model APIs](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/) and serving endpoints that serve [external models](https://docs.databricks.com/aws/en/generative-ai/external-models/).

## Requirements[​](#requirements "Direct link to Requirements")

*   See [Requirements](https://docs.databricks.com/aws/en/machine-learning/model-serving/score-foundation-models#required).
*   [Install the appropriate package](https://docs.databricks.com/aws/en/machine-learning/model-serving/score-foundation-models#install) to your cluster based on the [querying client option](https://docs.databricks.com/aws/en/machine-learning/model-serving/score-foundation-models#client-options) you choose.

## Query examples[​](#query-examples "Direct link to Query examples")

*   OpenAI client
*   SQL

To use the OpenAI client, specify the model serving endpoint name as the `model` input.

Python

    from openai import OpenAIimport base64import requests# Get the workspace API URL and token from the notebook contextAPI_ROOT = dbutils.notebook.entry_point.getDbutils().notebook().getContext().apiUrl().get()API_TOKEN = dbutils.notebook.entry_point.getDbutils().notebook().getContext().apiToken().get()client = OpenAI(    api_key=API_TOKEN,    base_url=f"{API_ROOT}/serving-endpoints",)# Download and encode imageimage_url = "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg"resp = requests.get(image_url)resp.raise_for_status()image_data = base64.b64encode(resp.content).decode("utf-8")# OpenAI requestcompletion = client.chat.completions.create(    model="databricks-claude-sonnet-4-5",    messages=[        {            "role": "user",            "content": [                {"type": "text", "text": "what's in this image?"},                {                    "type": "image_url",                    "image_url": {"url": f"data:image/jpeg;base64,{image_data}"},                },            ],        }    ],)print(completion.choices[0].message.content)

The Chat Completions API supports multiple image inputs, allowing the model to analyze each image and synthesize information from all inputs to generate a response to the prompt.

Python

    from openai import OpenAIimport base64import requests# Get the workspace API URL and token from the notebook contextAPI_ROOT = dbutils.notebook.entry_point.getDbutils().notebook().getContext().apiUrl().get()API_TOKEN = dbutils.notebook.entry_point.getDbutils().notebook().getContext().apiToken().get()client = OpenAI(    api_key=API_TOKEN,    base_url=f"{API_ROOT}/serving-endpoints",)# Download and encode multiple imagesimage1_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"resp1 = requests.get(image1_url)resp1.raise_for_status()image1_data = base64.b64encode(resp1.content).decode("utf-8")image2_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"resp2 = requests.get(image2_url)resp2.raise_for_status()image2_data = base64.b64encode(resp2.content).decode("utf-8")# OpenAI requestcompletion = client.chat.completions.create(    model="databricks-claude-sonnet-4-5",    messages=[        {            "role": "user",            "content": [                {"type": "text", "text": "What are in these images? Is there any difference between them?"},                {                    "type": "image_url",                    "image_url": {"url": f"data:image/jpeg;base64,{image1_data}"},                },                {                    "type": "image_url",                    "image_url": {"url": f"data:image/jpeg;base64,{image2_data}"},                },            ],        }    ],)print(completion.choices[0].message.content)

## Supported models[​](#supported-models "Direct link to Supported models")

See [Foundation model types](https://docs.databricks.com/aws/en/machine-learning/model-serving/score-foundation-models#model-types) for supported vision models.

## Input image requirements[​](#input-image-requirements "Direct link to Input image requirements")

## Image to token conversion[​](#image-to-token-conversion "Direct link to Image to token conversion")

This section applies only to Foundation Model APIs. For external models, refer to the provider's documentation.

Each image in a request to a foundation model adds to your token usage. See the [pricing calculator](https://www.databricks.com/product/pricing/genai-pricing-calculator) to estimate image pricing based on the token usage and model you are using.

## Limitations of image understanding[​](#limitations-of-image-understanding "Direct link to Limitations of image understanding")

This section applies only to Foundation Model APIs. For external models, refer to the provider's documentation.

The following are image understanding limitations for the supported Databricks-hosted foundation models:

## Additional resources[​](#additional-resources "Direct link to Additional resources")

*   [Query an embedding model](https://docs.databricks.com/aws/en/machine-learning/model-serving/query-embedding-models).
*   [Query reasoning models](https://docs.databricks.com/aws/en/machine-learning/model-serving/query-reason-models).
*   [Query a chat model](https://docs.databricks.com/aws/en/machine-learning/model-serving/query-chat-models).
