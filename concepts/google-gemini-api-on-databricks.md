---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5fa1a745b304be114739d8535732f4a6b2490cdfe3804cc9b0fac3ec6d635fdd
  pageDirectory: concepts
  sources:
    - provider-native-apis-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - google-gemini-api-on-databricks
    - GGA(D
    - Google Gemini API
    - Google Gemini SDK
  citations:
    - file: provider-native-apis-databricks-on-aws.md
title: Google Gemini API (on Databricks)
description: Databricks-hosted access to Google's Gemini API for Gemini models, uniquely supporting text, image, video, and audio inputs.
tags:
  - google
  - databricks
  - api
  - gemini
timestamp: "2026-06-19T19:58:57.526Z"
---

# Google Gemini API (on Databricks)

**Google Gemini API (on Databricks)** is a provider-native API that gives you direct access to Google’s Gemini model family through Databricks Model Serving. It is one of several provider-native APIs available alongside the unified OpenAI-compatible APIs, intended for users who need provider-specific features or wish to migrate existing provider SDK code to Databricks. ^[provider-native-apis-databricks-on-aws.md]

## Overview

Provider native APIs like the Google Gemini API expose the full provider‑specific API surface, enabling access to features beyond what the unified OpenAI‑compatible endpoints offer. They are designed for scenarios where you need the latest provider‑specific capabilities or want to reuse existing Google SDK code with minimal changes. ^[provider-native-apis-databricks-on-aws.md]

## Requirements

To use the Google Gemini API on Databricks, you must meet the general requirements listed in the [Foundation Model APIs documentation](https://docs.databricks.com/aws/en/machine-learning/model-serving/score-foundation-models#required) and install the appropriate provider package on your cluster (see the [installation guide](https://docs.databricks.com/aws/en/machine-learning/model-serving/score-foundation-models#install)). ^[provider-native-apis-databricks-on-aws.md]

## Supported Models and Input Types

The Google Gemini API is compatible with **Gemini models** and supports the following input types:

- Text
- Image
- Video
- Audio

For a per‑model breakdown of supported input types, refer to the [Databricks-hosted foundation models available in Foundation Model APIs](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/supported-models) page. ^[provider-native-apis-databricks-on-aws.md]

## How to Use

Detailed documentation for querying the Google Gemini API is available on the dedicated [Google Gemini API page](https://docs.databricks.com/aws/en/machine-learning/model-serving/query-gemini-api). In general, you use the native API endpoint for Gemini models to send requests that include text, images, video, or audio, and receive model responses. ^[provider-native-apis-databricks-on-aws.md]

## Related Concepts

- [Provider Native APIs](/concepts/provider-native-apis-databricks.md) — The overarching concept of provider-specific API surfaces on Databricks.
- [OpenAI Responses API](/concepts/openai-responses-api-on-databricks.md) — Another native API for GPT‑5 and GPT‑4o models.
- [Anthropic Messages API](/concepts/anthropic-messages-api-on-databricks.md) — A native API for Claude models.
- [Foundation Model APIs](/concepts/foundation-model-apis.md) — The unified API layer for querying foundation models.
- [Databricks-hosted foundation models](/concepts/databricks-hosted-foundation-models.md) — The catalog of available models and their input type support.

## Sources

- provider-native-apis-databricks-on-aws.md

# Citations

1. [provider-native-apis-databricks-on-aws.md](/references/provider-native-apis-databricks-on-aws-188451d9.md)
