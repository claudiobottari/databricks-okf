---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 70c1749126dcbe9bb47b3d824885a45f2b1aad9c9b13c321c82fb550e4757747
  pageDirectory: concepts
  sources:
    - query-vision-models-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - querying-vision-models-on-databricks-model-serving
    - QVMODMS
    - Query Vision Models|vision models
    - Query vision models on Databricks
  citations:
    - file: query-vision-models-databricks-on-aws.md
title: Querying Vision Models on Databricks Model Serving
description: How to send query requests to foundation models optimized for vision tasks via Databricks Model Serving endpoints using a unified API.
tags:
  - databricks
  - machine-learning
  - vision
  - model-serving
timestamp: "2026-06-19T20:04:57.070Z"
---

## Querying Vision Models on Databricks Model Serving

**Querying Vision Models on Databricks Model Serving** describes how to send inference requests to foundation models optimized for vision tasks using Databricks Model Serving. The service provides a unified API to understand and analyze images through a variety of foundation models, unlocking multimodal capabilities such as image captioning, object recognition, and visual question answering. This functionality is available through select Databricks-hosted models as part of [Foundation Model APIs](/concepts/foundation-model-apis.md) and through serving endpoints that serve [External Models](/concepts/external-models.md). ^[query-vision-models-databricks-on-aws.md]

### Requirements

Before querying vision models, review the general requirements for scoring foundation models and install the appropriate package for your chosen querying client (e.g., OpenAI client). See the [Requirements](https://docs.databricks.com/aws/en/machine-learning/model-serving/score-foundation-models#required) and [client installation](https://docs.databricks.com/aws/en/machine-learning/model-serving/score-foundation-models#install) documentation for details. ^[query-vision-models-databricks-on-aws.md]

### Query Examples

Model Serving supports both the OpenAI‑compatible client and SQL for submitting vision queries. The examples below use the OpenAI client with the **Chat Completions API**. The model serving endpoint is specified as the `model` parameter (e.g., `databricks-claude-sonnet-4-5`). Images are base64‑encoded and passed in the `content` array using the `image_url` type. ^[query-vision-models-databricks-on-aws.md]

#### Single Image Query

```python
from openai import OpenAI
import base64
import requests

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

#### Multiple Image Query

The Chat Completions API supports multiple image inputs. You can include several `image_url` entries in the same message content to have the model analyze all images and synthesize information from all inputs. ^[query-vision-models-databricks-on-aws.md]

```python
# ... (client setup as above) ...

image1_data = base64.b64encode(requests.get(image1_url).content).decode("utf-8")
image2_data = base64.b64encode(requests.get(image2_url).content).decode("utf-8")

completion = client.chat.completions.create(
    model="databricks-claude-sonnet-4-5",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "What are in these images? Is there any difference between them?"},
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image1_data}"}},
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image2_data}"}},
            ],
        }
    ],
)
print(completion.choices[0].message.content)
```

^[query-vision-models-databricks-on-aws.md]

### Supported Models

For the current list of foundation models optimized for vision tasks, see the [Foundation model types](https://docs.databricks.com/aws/en/machine-learning/model-serving/score-foundation-models#model-types) documentation. ^[query-vision-models-databricks-on-aws.md]

### Input Image Requirements

Refer to the provider’s documentation for external models. For Foundation Model APIs, see the official Databricks documentation for specific image format and size constraints. ^[query-vision-models-databricks-on-aws.md]

### Image to Token Conversion

Each image in a request to a Foundation Model API contributes to your token usage. Use the [pricing calculator](https://www.databricks.com/product/pricing/genai-pricing-calculator) to estimate image costs based on token usage and the model used. This section applies only to Foundation Model APIs. ^[query-vision-models-databricks-on-aws.md]

### Limitations of Image Understanding

The Databricks‑hosted foundation models have limitations in image understanding. For details, consult the official documentation (this section applies only to Foundation Model APIs). For external models, refer to the provider’s documentation. ^[query-vision-models-databricks-on-aws.md]

### Additional Resources

- [Query an Embedding Model](/concepts/text-embedding-models.md)
- [Query Reasoning Models](/concepts/hybrid-reasoning-models.md)
- Query a Chat Model

### Sources

- query-vision-models-databricks-on-aws.md

# Citations

1. [query-vision-models-databricks-on-aws.md](/references/query-vision-models-databricks-on-aws-afa9c021.md)
