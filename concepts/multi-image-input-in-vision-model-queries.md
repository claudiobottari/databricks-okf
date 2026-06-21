---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 588045095f9e2ddf065dabd66fb821eb6209a70c94ae938e92a0db3902d7981b
  pageDirectory: concepts
  sources:
    - query-vision-models-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - multi-image-input-in-vision-model-queries
    - MIIVMQ
    - Vision model queries
  citations:
    - file: query-vision-models-databricks-on-aws.md
title: Multi-Image Input in Vision Model Queries
description: The capability to send multiple images in a single Chat Completions API request, allowing vision models to analyze and compare images side by side.
tags:
  - vision
  - api
  - multi-modal
timestamp: "2026-06-19T20:05:30.090Z"
---

# Multi-Image Input in Vision Model Queries

**Multi-Image Input in Vision Model Queries** refers to the ability to pass multiple images in a single request to a vision-capable foundation model through the [Chat Completions API](/concepts/chat-completions-api.md) on Databricks Model Serving. This capability enables the model to analyze each image individually and synthesize information across all images to generate a cohesive response. ^[query-vision-models-databricks-on-aws.md]

## Overview

The Databricks Model Serving platform provides a unified API for understanding and analyzing images using a variety of foundation models. Multi-image input is supported by select Databricks-hosted foundation models as part of [Foundation Model APIs](/concepts/foundation-model-apis.md), and by serving endpoints that serve [External Models](/concepts/external-models.md). ^[query-vision-models-databricks-on-aws.md]

Users send a request containing a text prompt and multiple image attachments. The model processes each image, compares or contrasts them, and returns a combined analysis. For example, a user could ask "What are in these images? Is there any difference between them?" and include two images as input. ^[query-vision-models-databricks-on-aws.md]

## Requirements

- See the general requirements for querying foundation models, including cluster setup and package installation, in the [Query foundation models](https://docs.databricks.com/aws/en/machine-learning/model-serving/score-foundation-models) documentation. ^[query-vision-models-databricks-on-aws.md]
- The appropriate OpenAI client library (or SQL client) must be installed, depending on the chosen querying method. ^[query-vision-models-databricks-on-aws.md]

## Query Example

The following Python example uses the OpenAI client to send a multi-image request. Images are downloaded from URLs, base64-encoded, and included in the `image_url` field with a `data:` URI scheme. ^[query-vision-models-databricks-on-aws.md]

```python
from openai import OpenAI
import base64
import requests

# Get workspace API URL and token from notebook context
API_ROOT = dbutils.notebook.entry_point.getDbutils().notebook().getContext().apiUrl().get()
API_TOKEN = dbutils.notebook.entry_point.getDbutils().notebook().getContext().apiToken().get()

client = OpenAI(
    api_key=API_TOKEN,
    base_url=f"{API_ROOT}/serving-endpoints",
)

# Download and encode multiple images
image1_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"
resp1 = requests.get(image1_url)
resp1.raise_for_status()
image1_data = base64.b64encode(resp1.content).decode("utf-8")

image2_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"
resp2 = requests.get(image2_url)
resp2.raise_for_status()
image2_data = base64.b64encode(resp2.content).decode("utf-8")

# OpenAI request with multiple images
completion = client.chat.completions.create(
    model="databricks-claude-sonnet-4-5",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "What are in these images? Is there any difference between them?"},
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/jpeg;base64,{image1_data}"},
                },
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/jpeg;base64,{image2_data}"},
                },
            ],
        }
    ],
)
print(completion.choices[0].message.content)
```

The API supports any number of images in the `content` array, allowing the model to process each one and synthesize a response. ^[query-vision-models-databricks-on-aws.md]

## Supported Models

A list of supported vision models can be found in the [Foundation model types](https://docs.databricks.com/aws/en/machine-learning/model-serving/score-foundation-models#model-types) documentation. ^[query-vision-models-databricks-on-aws.md]

## Input Image Requirements

General input image requirements apply. For Databricks Foundation Model APIs, see the provider-specific documentation for image format, size limits, and encoding. External model endpoints follow their respective provider’s requirements. ^[query-vision-models-databricks-on-aws.md]

## Image to Token Conversion

For Foundation Model APIs, each image in a request is converted into tokens, which count toward your token usage. Use the [pricing calculator](https://www.databricks.com/product/pricing/genai-pricing-calculator) to estimate image pricing based on token consumption and the model being used. This conversion does not apply to external models; refer to the external provider’s documentation. ^[query-vision-models-databricks-on-aws.md]

## Limitations of Image Understanding

Databricks-hosted foundation models have certain image understanding limitations. For specific details, consult the provider’s documentation. External models are subject to their own limitations. ^[query-vision-models-databricks-on-aws.md]

## Related Concepts

- [Foundation Model APIs](/concepts/foundation-model-apis.md) – The managed endpoint offering for Databricks-hosted models.
- [Model Serving](/concepts/model-serving.md) – The underlying infrastructure that serves model endpoints.
- [Chat Completions API](/concepts/chat-completions-api.md) – The API format used for multi-image requests.
- [OpenAI client](/concepts/openai-client-compatibility.md) – The recommended Python client for querying.
- [External Models](/concepts/external-models.md) – Models served from third-party providers.
- Token Usage – How image inputs affect token-based billing.

## Sources

- query-vision-models-databricks-on-aws.md

# Citations

1. [query-vision-models-databricks-on-aws.md](/references/query-vision-models-databricks-on-aws-afa9c021.md)
