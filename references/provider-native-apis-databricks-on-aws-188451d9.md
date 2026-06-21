---
title: Provider native APIs | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/model-serving/provider-native-apis
ingestedAt: "2026-06-18T08:12:24.886Z"
---

[Skip to main content](#__docusaurus_skipToContent_fallback)

[

![Databricks Logo](https://docs.databricks.com/aws/en/img/logo.svg)![Databricks Logo](https://docs.databricks.com/aws/en/img/logo-dark.svg)

](https://www.databricks.com/)

[Get started](https://docs.databricks.com/aws/en/introduction/)[Guides](https://docs.databricks.com/aws/en/)[Develop](https://docs.databricks.com/aws/en/getting-started/connect/)[Reference](https://docs.databricks.com/aws/en/reference/api)[Resources](https://docs.databricks.com/aws/en/resources/)[Release notes](https://docs.databricks.com/aws/en/release-notes/)

[Help](#)

*   [Support](https://help.databricks.com/)
*   [Knowledge Base](https://kb.databricks.com/)
*   [Community](https://community.databricks.com/)
*   [Training](https://customer-academy.databricks.com/)

[English](#)

*   [English](https://docs.databricks.com/aws/en/machine-learning/model-serving/provider-native-apis)
*   [日本語](https://docs.databricks.com/aws/en/aws/ja/machine-learning/model-serving/provider-native-apis)
*   [Português](https://docs.databricks.com/aws/en/aws/pt/machine-learning/model-serving/provider-native-apis)

[AWS](#)

*   [Azure](https://learn.microsoft.com/azure/databricks/machine-learning/model-serving/provider-native-apis)
*   [GCP](https://docs.databricks.com/aws/en/gcp/en/machine-learning/model-serving/provider-native-apis)
*   [SAP](https://docs.databricks.com/aws/en/sap)

[Try Databricks](https://signup.databricks.com/?dbx_source=docs)

*   [](https://docs.databricks.com/aws/en/)
*   [Agents](https://docs.databricks.com/aws/en/agents/)
*   [Query LLMs and agents](https://docs.databricks.com/aws/en/agents/query-llms)
*   [Serve and query foundation models](https://docs.databricks.com/aws/en/machine-learning/model-serving/foundation-model-overview)
*   [Use foundation models](https://docs.databricks.com/aws/en/machine-learning/model-serving/score-foundation-models)
*   Provider native APIs

Last updated on **May 7, 2026**

Provider native APIs give you direct access to provider-specific API surfaces when you need features beyond the unified OpenAI-compatible APIs. Use native APIs to access the latest provider-specific features or to migrate existing provider SDK code to Databricks.

## Requirements[​](#requirements "Direct link to Requirements")

*   See [Requirements](https://docs.databricks.com/aws/en/machine-learning/model-serving/score-foundation-models#required).
*   [Install the appropriate package](https://docs.databricks.com/aws/en/machine-learning/model-serving/score-foundation-models#install) to your cluster based on the provider you choose.

## Available native APIs[​](#available-native-apis "Direct link to Available native APIs")

Provider

API

Compatible models

Supported input types

OpenAI

[OpenAI Responses API](https://docs.databricks.com/aws/en/machine-learning/model-serving/query-openai-responses)

GPT-5 series, GPT-4o

text, image

Anthropic

[Anthropic Messages API](https://docs.databricks.com/aws/en/machine-learning/model-serving/query-anthropic-messages)

Claude models

text, image

Google

[Google Gemini API](https://docs.databricks.com/aws/en/machine-learning/model-serving/query-gemini-api)

Gemini models

text, image, video, audio

For per-model input types, see [Databricks-hosted foundation models available in Foundation Model APIs](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/supported-models).

## Additional resources[​](#additional-resources "Direct link to Additional resources")

*   [Query a chat model](https://docs.databricks.com/aws/en/machine-learning/model-serving/query-chat-models).
*   [Use foundation models](https://docs.databricks.com/aws/en/machine-learning/model-serving/score-foundation-models).
*   [Databricks-hosted foundation models available in Foundation Model APIs](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/supported-models).

On this page

*   [Requirements](#requirements)
*   [Available native APIs](#available-native-apis)
*   [Additional resources](#additional-resources)
