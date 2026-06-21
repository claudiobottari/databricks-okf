---
title: Databricks Foundation Model APIs | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/
ingestedAt: "2026-06-18T08:10:59.206Z"
---

This article provides an overview of Foundation Model APIs on Databricks. It includes requirements for use, supported models, and limitations.

## What are Databricks Foundation Model APIs?[​](#what-are-databricks-foundation-model-apis "Direct link to What are Databricks Foundation Model APIs?")

[Model Serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/) now supports Foundation Model APIs which allow you to access and query state-of-the-art open models from a serving endpoint. These models are hosted by Databricks and you can quickly and easily build applications that use them without maintaining your own model deployment. Foundation Model APIs is a [Databricks Designated Service](https://docs.databricks.com/aws/en/resources/designated-services), which means that it uses [Databricks Geos](https://docs.databricks.com/aws/en/resources/databricks-geos) to manage data residency when processing customer content.

The Foundation Model APIs are provided in the following modes:

*   Pay-per-token: This is the easiest way to start accessing foundation models on Databricks and is recommended for beginning your journey with Foundation Model APIs. This mode is not designed for high-throughput applications, but can be used for production workloads.
*   Provisioned throughput: This mode is recommended for all production workloads, especially those that require high throughput, performance guarantees, fine-tuned models, or have additional security requirements. Provisioned throughput endpoints are available with compliance certifications like HIPAA.
*   AI Functions optimized models: This mode is recommended for batch inference workloads. You can choose to run batch inference using any generative AI or ML model using AI Functions.

See [Use Foundation Model APIs](#use-foundation-apis) for guidance on how to use these modes and the supported models.

Using the Foundation Model APIs you can do the following:

*   Query a generalized LLM to verify a project's validity before investing more resources.
*   Query a generalized LLM to create a quick proof-of-concept for an LLM-based application before investing in training and deploying a custom model.
*   Use a foundation model, along with a vector index, to build a chatbot using retrieval augmented generation (RAG).
*   Replace proprietary models with open alternatives to optimize for cost and performance.
*   Efficiently compare LLMs to see the best candidate for your use case, or swap a production model with a better performing one.
*   Build an LLM application for development or production on top of a scalable, SLA-backed LLM serving solution that can support your production traffic spikes.

## Requirements[​](#requirements "Direct link to requirements")

*   Databricks API token to authenticate endpoint requests.
*   Serverless compute (for provisioned throughput models).
*   A workspace in one of the following supported regions:
    *   [Pay-per-token regions](https://docs.databricks.com/aws/en/resources/feature-region-support#model-serving-aws).
    *   [Provisioned throughput regions](https://docs.databricks.com/aws/en/resources/feature-region-support#model-serving-aws).

## Use Foundation Model APIs[​](#use-foundation-model-apis "Direct link to use-foundation-model-apis")

You have multiple options for using the Foundation Model APIs.

The APIs are compatible with OpenAI, so you can use the OpenAI client for querying. You can also use the UI, the Foundation Models APIs Python SDK, the MLflow Deployments SDK, or the REST API for querying supported models. Databricks recommends using the OpenAI client SDK or API for extended interactions and the UI for trying out the feature.

See [Use foundation models](https://docs.databricks.com/aws/en/machine-learning/model-serving/score-foundation-models) for scoring examples.

### Pay-per-token Foundation Model APIs[​](#pay-per-token-foundation-model-apis "Direct link to pay-per-token-foundation-model-apis")

Preconfigured endpoints that serve the pay-per-token models are accessible in your Databricks workspace. These pay-per-token models are recommended for getting started. To access them in your workspace, navigate to the **Serving** tab in the left sidebar. The Foundation Model APIs are located at the top of the Endpoints list view.

![Serving endpoints list](https://docs.databricks.com/aws/en/assets/images/serving-endpoints-list-e6f5f52d6c405f624921e5e4c8802af0.png)

*   [Supported pay-per-token models](https://docs.databricks.com/aws/en/machine-learning/model-serving/foundation-model-overview).
*   See [Use foundation models](https://docs.databricks.com/aws/en/machine-learning/model-serving/score-foundation-models) for guidance on how to query Foundation Model APIs.
*   See [Foundation model REST API reference](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/api-reference) for required parameters and syntax.

### Provisioned throughput Foundation Model APIs[​](#provisioned-throughput-foundation-model-apis "Direct link to provisioned-throughput-foundation-model-apis")

Provisioned throughput provides endpoints with optimized inference for foundation model workloads that require performance guarantees. Databricks recommends provisioned throughput for production workloads.

*   [Provisioned throughput supported model architectures](https://docs.databricks.com/aws/en/machine-learning/model-serving/foundation-model-overview).
*   See [Provisioned throughput Foundation Model APIs](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/deploy-prov-throughput-foundation-model-apis) for a step-by-step guide on how to deploy Foundation Model APIs in provisioned throughout mode.

Provisioned throughput support includes:

*   **Base models of all sizes**. Base models can be accessed using the Databricks Marketplace, or you can alternatively download them from Hugging Face or another external source and register them in the Unity Catalog. The latter approach works with any fine-tuned variant of the supported models.
*   **Fine-tuned variants of base models**, such as models that are fine-tuned on proprietary data.
*   **Fully custom weights and tokenizers**, such as those trained from scratch or continued pre-trained or **other variations using the base model architecture** (for example, CodeLlama).

### AI Functions for batch inference[​](#-ai-functions-for-batch-inference "Direct link to -ai-functions-for-batch-inference")

See [Enrich data using AI Functions](https://docs.databricks.com/aws/en/large-language-models/ai-functions).

See [Deploy batch inference pipelines](https://docs.databricks.com/aws/en/large-language-models/batch-inference-pipelines) for how to create batch inference pipelines using AI Functions.

## Limitations[​](#limitations "Direct link to Limitations")

See [Foundation Model APIs limits](https://docs.databricks.com/aws/en/machine-learning/model-serving/model-serving-limits#fmapi-limits).

## Additional resources[​](#additional-resources "Direct link to Additional resources")

*   [Use foundation models](https://docs.databricks.com/aws/en/machine-learning/model-serving/score-foundation-models)
*   [Provisioned throughput Foundation Model APIs](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/deploy-prov-throughput-foundation-model-apis)
*   [Foundation model REST API reference](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/api-reference)
*   [Foundation model Unity Catalog permissions](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/model-uc-permissions)

*   [Deploy batch inference pipelines](https://docs.databricks.com/aws/en/large-language-models/batch-inference-pipelines)
*   [Databricks-hosted foundation models available in Foundation Model APIs](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/supported-models)
