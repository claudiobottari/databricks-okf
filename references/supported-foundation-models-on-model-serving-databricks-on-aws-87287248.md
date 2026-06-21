---
title: Supported foundation models on Model Serving | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/model-serving/foundation-model-overview
ingestedAt: "2026-06-18T08:11:56.896Z"
---

This article describes the foundation models you can serve using [Model Serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/).

Foundation models are large, pre-trained neural networks that are trained on both large and broad ranges of data. These models are designed to learn general patterns in language, images, or other data types, and can be fine-tuned for specific tasks with additional training. Your use of certain foundation models is subject to the model's terms and acceptable use policy. See [Applicable model terms](https://docs.databricks.com/aws/en/machine-learning/model-serving/acceptable-use-models).

Model Serving offers flexible options for hosting and querying foundation models based on your needs:

*   [Pay-per-token](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/#token-foundation-apis): Ideal for experimentation and quick exploration. This option allows you to query pre-configured endpoints in your Databricks workspace without upfront infrastructure commitments.
*   [AI Functions (batch inference)](https://docs.databricks.com/aws/en/large-language-models/ai-functions): A subset of Databricks-hosted models are optimized for AI Functions. You can apply AI to your data and run batch inference production workloads at scale using these functions and their supported models.
*   [Provisioned throughput](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/#throughput): Recommended for production use cases requiring performance guarantees. This option enables the deployment of fine-tuned foundation models with optimized serving endpoints.
*   [External models](https://docs.databricks.com/aws/en/generative-ai/external-models/): This option enables access to foundation models hosted outside of Databricks, such as those provided by OpenAI or Anthropic. These models can be centrally managed within Databricks for streamlined governance.

## Foundation models hosted on Databricks[​](#foundation-models-hosted-on-databricks "Direct link to foundation-models-hosted-on-databricks")

Databricks hosts state-of-the-art open foundation models. These models are made available using [Foundation Model APIs](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/). To restrict which Databricks-hosted foundation models your organization can use, see [Foundation model Unity Catalog permissions](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/model-uc-permissions).

The following table summarizes which Databricks-hosted models and model families are supported in each region based on the Model Serving feature.

important

*   Google Gemini 3.5 Flash requires [cross geography routing to be enabled](https://docs.databricks.com/aws/en/resources/databricks-geos#cross-geo-processing) for regions outside the US and EU geos.
*   Google Gemini 3 Flash and Google Gemini 3 Pro are hosted on global endpoints and require [cross geography routing to be enabled](https://docs.databricks.com/aws/en/resources/databricks-geos#cross-geo-processing) for every region. Google Gemini 3 Pro will be retired on March 26, 2026. See [Retired models](https://docs.databricks.com/aws/en/machine-learning/retired-models-policy#retired) for the recommended replacement model and guidance for how to migrate during deprecation.
    *   To allow more time for migration, between March 26, 2026 and June 7, 2026, API calls to Gemini 3 Pro will be temporarily redirected to Gemini 3.1 Pro. The pricing for both models is identical.
*   OpenAI GPT-5.1 Codex Max and OpenAI GPT-5.1 Codex Mini are hosted on global endpoints and require [cross geography routing to be enabled](https://docs.databricks.com/aws/en/resources/databricks-geos#cross-geo-processing) for every region.
*   OpenAI GPT-5.1 Codex Max, OpenAI GPT-5.1 Codex Mini, and OpenAI GPT-5.2 Codex will be retired on July 16, 2026. See [Retired models](https://docs.databricks.com/aws/en/machine-learning/retired-models-policy#retired) for the recommended replacement model and guidance for how to migrate during deprecation.
*   Anthropic Claude 3.7 Sonnet is no longer available. See [Retired models](https://docs.databricks.com/aws/en/machine-learning/retired-models-policy#retired) for the recommended replacement model and guidance for how to migrate during deprecation.
*   Meta Llama 4 Maverick is available for Foundation Model APIs provisioned throughput workloads in [Public Preview](https://docs.databricks.com/aws/en/release-notes/release-types).
*   Meta-Llama-3.1-405B-Instruct is no longer available for pay-per-token workloads. Starting May 15, 2026, it will also be retired for provisioned throughput workloads. See [Retired models](https://docs.databricks.com/aws/en/machine-learning/retired-models-policy#retired) for the recommended replacement model and guidance for how to migrate during deprecation.
*   Several older model families have been retired. See [Retired models](https://docs.databricks.com/aws/en/machine-learning/retired-models-policy#retired) for the full list of retired models and recommended replacements.

⥂ This model is supported based on GPU availability and requires [cross geography routing to be enabled](https://docs.databricks.com/aws/en/resources/databricks-geos#cross-geo-processing).

## Access foundation models hosted outside of Databricks[​](#access-foundation-models-hosted-outside-of-databricks "Direct link to access-foundation-models-hosted-outside-of-databricks")

Foundation models created by LLM providers, such as OpenAI and Anthropic, are also accessible on Databricks using [External models](https://docs.databricks.com/aws/en/generative-ai/external-models/). These models are hosted outside of Databricks and you can create an endpoint to query them. These endpoints can be centrally governed from Databricks, which streamlines the use and management of various LLM providers within your organization.

The following table presents a non-exhaustive list of supported models and corresponding [endpoint types](https://docs.databricks.com/aws/en/generative-ai/external-models/#endpoint). You can use the listed model associations to help you configure your an endpoint for any newly released model types as they become available with a given provider. Customers are responsible for ensuring compliance with applicable model licenses.

note

With the rapid development of LLMs, there is no guarantee that this list is up to date at all times. New model versions from the same provider are typically supported even if they are not on the list.

`**` Model provider supports fine-tuned completion and chat models. To query a fine-tuned model, populate the `name` field of the `external model` configuration with the name of your fine-tuned model.

`†` Model provider supports custom completion models.

## Create foundation model serving endpoints[​](#create-foundation-model-serving-endpoints "Direct link to Create foundation model serving endpoints")

To query and use foundation models in your AI applications, you must first create a model serving endpoint. Model Serving uses a unified API and UI for creating and updating foundation model serving endpoints.

*   To create an endpoint that serves fine-tuned variants of foundation models made available using Foundation Model APIs provisioned throughput, see [Create your provisioned throughput endpoint using the REST API](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/deploy-prov-throughput-foundation-model-apis#provisioned-throughput-api).
*   For creating serving endpoints that access foundation models made available using the External models offering, see [Create an external model serving endpoint](https://docs.databricks.com/aws/en/machine-learning/model-serving/create-foundation-model-endpoints#ext-model-endpoint).

## Query foundation model serving endpoints[​](#query-foundation-model-serving-endpoints "Direct link to Query foundation model serving endpoints")

After you create your serving endpoint you are able to query your foundation model. Model Serving uses a unified OpenAI-compatible API and SDK for querying foundation models. This unified experience simplifies how you experiment with and customize foundation models for production across supported clouds and providers.

See [Use foundation models](https://docs.databricks.com/aws/en/machine-learning/model-serving/score-foundation-models).
