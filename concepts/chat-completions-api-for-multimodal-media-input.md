---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c1909d224a32b88611235c19537297764d8c39eb9656da28c2e912442a746b64
  pageDirectory: concepts
  sources:
    - query-audio-and-video-models-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - chat-completions-api-for-multimodal-media-input
    - CCAFMMI
  citations:
    - file: query-audio-and-video-models-databricks-on-aws.md
title: Chat Completions API for Multimodal Media Input
description: How to use the OpenAI-compatible Chat Completions API on Databricks to pass video_url and audio_url content types in the messages array.
tags:
  - api
  - model-serving
  - multimodal
timestamp: "2026-06-19T20:01:52.506Z"
---

# Chat Completions API for Multimodal Media Input

The **Chat Completions API for Multimodal Media Input** refers to the ability to pass audio and video files as part of a chat request to supported Gemini foundation models on Databricks. Media can be provided as a publicly accessible URL or as base64-encoded inline data via the OpenAI-compatible [Chat Completions API](/concepts/chat-completions-api.md) or the [Google Gemini API](/concepts/google-gemini-api-on-databricks.md). ^[query-audio-and-video-models-databricks-on-aws.md]

## Requirements

To use multimodal media input, users must meet the general requirements for scoring foundation models on Databricks, including having the appropriate [package installed](https://docs.databricks.com/aws/en/machine-learning/model-serving/score-foundation-models#install) for the chosen querying client. ^[query-audio-and-video-models-databricks-on-aws.md]

## Input Methods

Two methods are available for providing audio and video input:

- **URL**: A publicly accessible web URL pointing to the media file. For video, YouTube URLs are also supported.
- **Base64 inline data**: The file is encoded as a base64 string and passed as a data URI (e.g., `data:video/mp4;base64,<encoded_data>`).

^[query-audio-and-video-models-databricks-on-aws.md]

## Using the Chat Completions API

The Chat Completions API uses the `messages` array with content parts of type `video_url` and `audio_url`. Each part includes a `url` field that accepts either a web URL or a base64 data URI. The `model` parameter must be set to a supported Gemini foundation model. ^[query-audio-and-video-models-databricks-on-aws.md]

### Video Input

Video can be provided as one or more `video_url` content parts. The example below shows how to pass a video via URL and via base64-encoded data:

```python
import os
import base64
from openai import OpenAI

DATABRICKS_TOKEN = os.environ.get('DATABRICKS_TOKEN')
DATABRICKS_BASE_URL = os.environ.get('DATABRICKS_BASE_URL')
client = OpenAI(api_key=DATABRICKS_TOKEN, base_url=DATABRICKS_BASE_URL)

with open("video.mp4", "rb") as f:
    video_b64 = base64.standard_b64encode(f.read()).decode("utf-8")

response = client.chat.completions.create(
    model="databricks-gemini-3-1-pro",
    messages=[{
        "role": "user",
        "content": [
            {"type": "text", "text": "Summarize what happens in these videos."},
            {"type": "video_url", "video_url": {"url": "https://example.com/sample-video.mp4"}},
            {"type": "video_url", "video_url": {"url": f"data:video/mp4;base64,{video_b64}"}},
        ]
    }],
    max_tokens=1024
)
print(response.choices[0].message.content)
```

The API also supports passing multiple video inputs in a single request. ^[query-audio-and-video-models-databricks-on-aws.md]

### Audio Input

Audio is provided using `audio_url` content parts. The structure is identical to video input:

```python
with open("audio.mp3", "rb") as f:
    audio_b64 = base64.standard_b64encode(f.read()).decode("utf-8")

response = client.chat.completions.create(
    model="databricks-gemini-3-1-pro",
    messages=[{
        "role": "user",
        "content": [
            {"type": "text", "text": "Transcribe this audio and summarize the key points."},
            {"type": "audio_url", "audio_url": {"url": "https://example.com/sample-audio.mp3"}},
            {"type": "audio_url", "audio_url": {"url": f"data:audio/mp3;base64,{audio_b64}"}},
        ]
    }],
    max_tokens=1024
)
print(response.choices[0].message.content)
```

Multiple audio files can be included per request, though large files increase latency and token usage. ^[query-audio-and-video-models-databricks-on-aws.md]

## Supported Models

Audio and video inputs are supported on the following Gemini pay-per-token foundation models. Provisioned throughput endpoints are not supported. ^[query-audio-and-video-models-databricks-on-aws.md]

- `databricks-gemini-3-1-pro`
- `databricks-gemini-3-pro`
- `databricks-gemini-2-5-pro`
- `databricks-gemini-3-1-flash-lite`
- `databricks-gemini-3-flash`
- `databricks-gemini-2-5-flash`

## Limitations

- Audio and video input is only available on Gemini pay-per-token foundation models; provisioned throughput endpoints are not supported.
- Multiple audio or video inputs can be included in a single request, but large files increase latency and token usage.

^[query-audio-and-video-models-databricks-on-aws.md]

## See Also

- [Chat Completions API](/concepts/chat-completions-api.md) — The standard interface for conversational AI.
- Gemini foundation models — The model family supporting multimodal input.
- [Google Gemini API](/concepts/google-gemini-api-on-databricks.md) — An alternative API for sending media inputs.
- Base64 encoding — Used to convert media files to inline data URIs.
- [Vision model queries](/concepts/multi-image-input-in-vision-model-queries.md) — Related capability for image input.

## Sources

- query-audio-and-video-models-databricks-on-aws.md

# Citations

1. [query-audio-and-video-models-databricks-on-aws.md](/references/query-audio-and-video-models-databricks-on-aws-744ec6c3.md)
