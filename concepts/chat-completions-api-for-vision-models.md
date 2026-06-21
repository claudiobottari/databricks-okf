---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 301e8caf82cf182f9bf606a25a5605990ff3191fb961c3ed9c54b888a7d0fb96
  pageDirectory: concepts
  sources:
    - query-vision-models-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - chat-completions-api-for-vision-models
    - CCAFVM
  citations:
    - file: query-vision-models-databricks-on-aws.md
title: Chat Completions API for Vision Models
description: The OpenAI-compatible Chat Completions API used to send text and image content to vision models hosted on Databricks, supporting multiple image inputs.
tags:
  - api
  - openai
  - vision
  - chat-completions
timestamp: "2026-06-19T20:07:12.807Z"
---

## Chat Completions API for Vision Models

The **Chat Completions API for Vision Models** is a unified interface provided by [Databricks Model Serving](/concepts/databricks-model-serving.md) that enables users to query foundation models optimized for vision tasks. This API follows the [OpenAI Chat Completions](/concepts/chat-completions-api.md) format and allows models to understand and analyze images using [multimodal capabilities](/concepts/multimodal-foundation-models.md), supporting tasks such as image recognition, comparison, and description generation. ^[query-vision-models-databricks-on-aws.md]

### Requirements

To use the Chat Completions API for vision models, you must meet the foundation model requirements and install the appropriate package for your chosen querying client option. The API works with both Databricks-hosted foundation models and external model serving endpoints. ^[query-vision-models-databricks-on-aws.md]

### Query Examples

#### Single Image Input

The API supports querying a model with a single image using the standard Chat Completions format. The request sends an image URL as a base64-encoded data URI and includes a text prompt for the model to process:

```python
from openai import OpenAI
import base64
import requests

# Get the workspace API URL and token from the notebook context
API_ROOT = dbutils.notebook.entry_point.getDbutils().notebook().getContext().apiUrl().get()
API_TOKEN = dbutils.notebook.entry_point.getDbutils().notebook().getContext().apiToken().get()

client = OpenAI(
    api_key=API_TOKEN,
    base_url=f"{API_ROOT}/serving-endpoints",
)

# Download and encode image
image_url = "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg"
resp = requests.get(image_url)
resp.raise_for_status()
image_data = base64.b64encode(resp.content).decode("utf-8")

# OpenAI request
completion = client.chat.completions.create(
    model="databricks-claude-sonnet-4-5",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "what's in this image?"},
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/jpeg;base64,{image_data}"},
                },
            ],
        }
    ],
)
print(completion.choices[0].message.content)
```

^[query-vision-models-databricks-on-aws.md]

#### Multiple

# Citations

1. [query-vision-models-databricks-on-aws.md](/references/query-vision-models-databricks-on-aws-afa9c021.md)
