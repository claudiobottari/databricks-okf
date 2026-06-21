---
title: Query audio and video models | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/model-serving/query-audio-video-models
ingestedAt: "2026-06-18T08:12:28.218Z"
---

This page describes how to send audio and video inputs to Gemini foundation models on Databricks. You can provide media as a URL or as base64-encoded inline data using the [Chat Completions API](https://docs.databricks.com/aws/en/machine-learning/model-serving/query-chat-models) or the [Google Gemini API](https://docs.databricks.com/aws/en/machine-learning/model-serving/query-gemini-api).

## Requirements[​](#requirements "Direct link to Requirements")

*   See [requirements to use foundation models](https://docs.databricks.com/aws/en/machine-learning/model-serving/score-foundation-models#required).
*   [Install the appropriate package](https://docs.databricks.com/aws/en/machine-learning/model-serving/score-foundation-models#install) to your cluster based on the [querying client option](https://docs.databricks.com/aws/en/machine-learning/model-serving/score-foundation-models#client-options) you choose.

## Input methods[​](#input-methods "Direct link to Input methods")

You can provide audio and video inputs using two methods:

*   **URL**: Pass a publicly accessible URL to the media file. For video, YouTube URLs are also supported.
*   **Base64 inline data**: Encode the file as a base64 string and pass it as a data URI (for example, `data:video/mp4;base64,<encoded_data>`).

## Chat Completions API[​](#chat-completions-api "Direct link to Chat Completions API")

The [chat completions API](https://docs.databricks.com/aws/en/machine-learning/model-serving/query-chat-models#query-chat) allows you to pass video and audio input. Use the `video_url` and `audio_url` content types in the `messages` array to pass media inputs. Each content item includes a `url` field that accepts either a web URL or a base64 data URI.

### Video input[​](#video-input "Direct link to Video input")

*   Python
*   REST API

Python

    import osimport base64from openai import OpenAIDATABRICKS_TOKEN = os.environ.get('DATABRICKS_TOKEN')DATABRICKS_BASE_URL = os.environ.get('DATABRICKS_BASE_URL')client = OpenAI(    api_key=DATABRICKS_TOKEN,    base_url=DATABRICKS_BASE_URL)# Encode a local video file as base64with open("video.mp4", "rb") as f:    video_b64 = base64.standard_b64encode(f.read()).decode("utf-8")response = client.chat.completions.create(    model="databricks-gemini-3-1-pro",    messages=[{        "role": "user",        "content": [            {"type": "text", "text": "Summarize what happens in these videos."},            {                "type": "video_url",                "video_url": {"url": "https://example.com/sample-video.mp4"}            },            {                "type": "video_url",                "video_url": {"url": f"data:video/mp4;base64,{video_b64}"}            },        ]    }],    max_tokens=1024)print(response.choices[0].message.content)

### Audio input[​](#audio-input "Direct link to Audio input")

*   Python
*   REST API

Python

    import osimport base64from openai import OpenAIDATABRICKS_TOKEN = os.environ.get('DATABRICKS_TOKEN')DATABRICKS_BASE_URL = os.environ.get('DATABRICKS_BASE_URL')client = OpenAI(    api_key=DATABRICKS_TOKEN,    base_url=DATABRICKS_BASE_URL)# Encode a local audio file as base64with open("audio.mp3", "rb") as f:    audio_b64 = base64.standard_b64encode(f.read()).decode("utf-8")response = client.chat.completions.create(    model="databricks-gemini-3-1-pro",    messages=[{        "role": "user",        "content": [            {"type": "text", "text": "Transcribe this audio and summarize the key points."},            {                "type": "audio_url",                "audio_url": {"url": "https://example.com/sample-audio.mp3"}            },            {                "type": "audio_url",                "audio_url": {"url": f"data:audio/mp3;base64,{audio_b64}"}            },        ]    }],    max_tokens=1024)print(response.choices[0].message.content)

## Google Gemini API[​](#google-gemini-api "Direct link to Google Gemini API")

Use the [Google Gemini API](https://docs.databricks.com/aws/en/machine-learning/model-serving/query-gemini-api) to pass media as `inlineData` (base64-encoded) or `fileData` (URL reference) within the `parts` array.

### Video input[​](#video-input-1 "Direct link to Video input")

*   Python
*   REST API

Python

    from google import genaifrom google.genai import typesimport base64import osDATABRICKS_TOKEN = os.environ.get('DATABRICKS_TOKEN')client = genai.Client(    api_key="databricks",    http_options=types.HttpOptions(        base_url="https://example.staging.cloud.databricks.com/serving-endpoints/gemini",        headers={            "Authorization": f"Bearer {DATABRICKS_TOKEN}",        },    ),)# Encode a local video file as base64with open("video.mp4", "rb") as f:    video_b64 = base64.standard_b64encode(f.read()).decode("utf-8")response = client.models.generate_content(    model="databricks-gemini-3-1-pro",    contents=[        types.Content(            role="user",            parts=[                types.Part(text="Summarize what happens in these videos."),                types.Part(                    file_data=types.FileData(                        mime_type="video/mp4",                        file_uri="https://example.com/sample-video.mp4",                    )                ),                types.Part(                    inline_data=types.Blob(                        mime_type="video/mp4",                        data=video_b64,                    )                ),            ],        ),    ],    config=types.GenerateContentConfig(        max_output_tokens=1024,    ),)print(response.text)

### Audio input[​](#audio-input-1 "Direct link to Audio input")

*   Python
*   REST API

Python

    from google import genaifrom google.genai import typesimport base64import osDATABRICKS_TOKEN = os.environ.get('DATABRICKS_TOKEN')client = genai.Client(    api_key="databricks",    http_options=types.HttpOptions(        base_url="https://example.staging.cloud.databricks.com/serving-endpoints/gemini",        headers={            "Authorization": f"Bearer {DATABRICKS_TOKEN}",        },    ),)# Encode a local audio file as base64with open("audio.mp3", "rb") as f:    audio_b64 = base64.standard_b64encode(f.read()).decode("utf-8")response = client.models.generate_content(    model="databricks-gemini-3-1-pro",    contents=[        types.Content(            role="user",            parts=[                types.Part(text="Transcribe this audio and summarize the key points."),                types.Part(                    file_data=types.FileData(                        mime_type="audio/mp3",                        file_uri="https://example.com/sample-audio.mp3",                    )                ),                types.Part(                    inline_data=types.Blob(                        mime_type="audio/mp3",                        data=audio_b64,                    )                ),            ],        ),    ],    config=types.GenerateContentConfig(        max_output_tokens=1024,    ),)print(response.text)

## Supported models[​](#supported-models "Direct link to Supported models")

Audio and video inputs are supported on the following Gemini pay-per-token foundation models. See [Databricks-hosted foundation models available in Foundation Model APIs](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/supported-models) for region availability.

*   `databricks-gemini-3-1-pro`
*   `databricks-gemini-3-pro`
*   `databricks-gemini-2-5-pro`
*   `databricks-gemini-3-1-flash-lite`
*   `databricks-gemini-3-flash`
*   `databricks-gemini-2-5-flash`

## Limitations[​](#limitations "Direct link to Limitations")

*   Audio and video inputs are only available on Gemini pay-per-token foundation models. Provisioned throughput endpoints are not supported.
*   Multiple audio or video inputs can be included in a single request, but large files increase latency and token usage.

## Additional resources[​](#additional-resources "Direct link to Additional resources")

*   [Query vision models](https://docs.databricks.com/aws/en/machine-learning/model-serving/query-vision-models).
*   [Query with the Google Gemini API](https://docs.databricks.com/aws/en/machine-learning/model-serving/query-gemini-api).
*   [Query a chat model](https://docs.databricks.com/aws/en/machine-learning/model-serving/query-chat-models).
