---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 497f5797647ce6a75b1658834e0aae5fc2ae3791f17227d3c89e2c9c131dead1
  pageDirectory: concepts
  sources:
    - query-audio-and-video-models-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - audiovideo-input-methods-for-foundation-models
    - AIMFFM
  citations:
    - file: query-audio-and-video-models-databricks-on-aws.md
title: Audio/Video Input Methods for Foundation Models
description: "Two supported methods for providing media to Gemini models on Databricks: publicly accessible URLs and base64-encoded inline data URIs."
tags:
  - machine-learning
  - model-serving
  - multimodal
timestamp: "2026-06-19T20:01:54.041Z"
---

# Audio/Video Input Methods for Foundation Models

**Audio/Video Input Methods for Foundation Models** describes the techniques for providing audio and video media as input to Gemini foundation models on Databricks. These inputs can be supplied through two primary methods — URL references or base64-encoded inline data — using either the [Chat Completions API](/concepts/chat-completions-api.md) or the [Google Gemini API](/concepts/google-gemini-api-on-databricks.md). ^[query-audio-and-video-models-databricks-on-aws.md]

## Overview

Foundation models that support multimodal inputs can process audio and video content alongside text prompts. On Databricks, this capability is available for select Gemini pay-per-token foundation models. Media can be provided as publicly accessible URLs or as base64-encoded data URIs embedded directly in the request. ^[query-audio-and-video-models-databricks-on-aws.md]

## Input Methods

Two methods are available for providing audio and video inputs: ^[query-audio-and-video-models-databricks-on-aws.md]

- **URL**: Pass a publicly accessible URL to the media file. For video, YouTube URLs are also supported.
- **Base64 inline data**: Encode the file as a base64 string and pass it as a data URI (for example, `data:video/mp4;base64,<encoded_data>`).

## Chat Completions API

The [Chat Completions API](/concepts/chat-completions-api.md) supports audio and video input through the `video_url` and `audio_url` content types in the `messages` array. Each content item includes a `url` field that accepts either a web URL or a base64 data URI. ^[query-audio-and-video-models-databricks-on-aws.md]

### Video Input Example

```python
import os
import base64
from openai import OpenAI

DATABRICKS_TOKEN = os.environ.get('DATABRICKS_TOKEN')
DATABRICKS_BASE_URL = os.environ.get('DATABRICKS_BASE_URL')

client = OpenAI(
    api_key=DATABRICKS_TOKEN,
    base_url=DATABRICKS_BASE_URL
)

# Encode a local video file as base64
with open("video.mp4", "rb") as f:
    video_b64 = base64.standard_b64encode(f.read()).decode("utf-8")

response = client.chat.completions.create(
    model="databricks-gemini-3-1-pro",
    messages=[{
        "role": "user",
        "content": [
            {"type": "text", "text": "Summarize what happens in these videos."},
            {
                "type": "video_url",
                "video_url": {"url": "https://example.com/sample-video.mp4"}
            },
            {
                "type": "video_url",
                "video_url": {"url": f"data:video/mp4;base64,{video_b64}"}
            },
        ]
    }],
    max_tokens=1024
)
print(response.choices[0].message.content)
```

^[query-audio-and-video-models-databricks-on-aws.md]

### Audio Input Example

```python
import os
import base64
from openai import OpenAI

DATABRICKS_TOKEN = os.environ.get('DATABRICKS_TOKEN')
DATABRICKS_BASE_URL = os.environ.get('DATABRICKS_BASE_URL')

client = OpenAI(
    api_key=DATABRICKS_TOKEN,
    base_url=DATABRICKS_BASE_URL
)

# Encode a local audio file as base64
with open("audio.mp3", "rb") as f:
    audio_b64 = base64.standard_b64encode(f.read()).decode("utf-8")

response = client.chat.completions.create(
    model="databricks-gemini-3-1-pro",
    messages=[{
        "role": "user",
        "content": [
            {"type": "text", "text": "Transcribe this audio and summarize the key points."},
            {
                "type": "audio_url",
                "audio_url": {"url": "https://example.com/sample-audio.mp3"}
            },
            {
                "type": "audio_url",
                "audio_url": {"url": f"data:audio/mp3;base64,{audio_b64}"}
            },
        ]
    }],
    max_tokens=1024
)
print(response.choices[0].message.content)
```

^[query-audio-and-video-models-databricks-on-aws.md]

## Google Gemini API

The [Google Gemini API](/concepts/google-gemini-api-on-databricks.md) provides an alternative interface for passing media inputs. Use `inlineData` for base64-encoded content or `fileData` for URL references within the `parts` array. ^[query-audio-and-video-models-databricks-on-aws.md]

### Video Input Example

```python
from google import genai
from google.genai import types
import base64
import os

DATABRICKS_TOKEN = os.environ.get('DATABRICKS_TOKEN')

client = genai.Client(
    api_key="databricks",
    http_options=types.HttpOptions(
        base_url="https://example.staging.cloud.databricks.com/serving-endpoints/gemini",
        headers={
            "Authorization": f"Bearer {DATABRICKS_TOKEN}",
        },
    ),
)

# Encode a local video file as base64
with open("video.mp4", "rb") as f:
    video_b64 = base64.standard_b64encode(f.read()).decode("utf-8")

response = client.models.generate_content(
    model="databricks-gemini-3-1-pro",
    contents=[
        types.Content(
            role="user",
            parts=[
                types.Part(text="Summarize what happens in these videos."),
                types.Part(
                    file_data=types.FileData(
                        mime_type="video/mp4",
                        file_uri="https://example.com/sample-video.mp4",
                    )
                ),
                types.Part(
                    inline_data=types.Blob(
                        mime_type="video/mp4",
                        data=video_b64,
                    )
                ),
            ],
        ),
    ],
    config=types.GenerateContentConfig(
        max_output_tokens=1024,
    ),
)
print(response.text)
```

^[query-audio-and-video-models-databricks-on-aws.md]

### Audio Input Example

```python
from google import genai
from google.genai import types
import base64
import os

DATABRICKS_TOKEN = os.environ.get('DATABRICKS_TOKEN')

client = genai.Client(
    api_key="databricks",
    http_options=types.HttpOptions(
        base_url="https://example.staging.cloud.databricks.com/serving-endpoints/gemini",
        headers={
            "Authorization": f"Bearer {DATABRICKS_TOKEN}",
        },
    ),
)

# Encode a local audio file as base64
with open("audio.mp3", "rb") as f:
    audio_b64 = base64.standard_b64encode(f.read()).decode("utf-8")

response = client.models.generate_content(
    model="databricks-gemini-3-1-pro",
    contents=[
        types.Content(
            role="user",
            parts=[
                types.Part(text="Transcribe this audio and summarize the key points."),
                types.Part(
                    file_data=types.FileData(
                        mime_type="audio/mp3",
                        file_uri="https://example.com/sample-audio.mp3",
                    )
                ),
                types.Part(
                    inline_data=types.Blob(
                        mime_type="audio/mp3",
                        data=audio_b64,
                    )
                ),
            ],
        ),
    ],
    config=types.GenerateContentConfig(
        max_output_tokens=1024,
    ),
)
print(response.text)
```

^[query-audio-and-video-models-databricks-on-aws.md]

## Supported Models

Audio and video inputs are supported on the following Gemini pay-per-token foundation models: ^[query-audio-and-video-models-databricks-on-aws.md]

- `databricks-gemini-3-1-pro`
- `databricks-gemini-3-pro`
- `databricks-gemini-2-5-pro`
- `databricks-gemini-3-1-flash-lite`
- `databricks-gemini-3-flash`
- `databricks-gemini-2-5-flash`

## Limitations

- Audio and video inputs are only available on Gemini pay-per-token foundation models. Provisioned throughput endpoints are not supported. ^[query-audio-and-video-models-databricks-on-aws.md]
- Multiple audio or video inputs can be included in a single request, but large files increase latency and token usage. ^[query-audio-and-video-models-databricks-on-aws.md]

## Requirements

- See requirements to use foundation models for prerequisites. ^[query-audio-and-video-models-databricks-on-aws.md]
- Install the appropriate package to your cluster based on the querying client option you choose. ^[query-audio-and-video-models-databricks-on-aws.md]

## Related Concepts

- Query vision models — Image input methods for foundation models
- [Foundation Model APIs](/concepts/foundation-model-apis.md) — Overview of model serving on Databricks
- Multimodal AI — Models that process multiple input types
- [Pay-per-Token Pricing](/concepts/pay-per-token-pricing.md) — Usage-based billing for foundation model inference

## Sources

- query-audio-and-video-models-databricks-on-aws.md

# Citations

1. [query-audio-and-video-models-databricks-on-aws.md](/references/query-audio-and-video-models-databricks-on-aws-744ec6c3.md)
