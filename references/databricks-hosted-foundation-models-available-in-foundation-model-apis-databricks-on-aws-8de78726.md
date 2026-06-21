---
title: Databricks-hosted foundation models available in Foundation Model APIs | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/supported-models
ingestedAt: "2026-06-18T08:11:12.420Z"
---

This article describes the state-of-the-art open models that are supported by [Databricks Foundation Model APIs](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/).

You can send query requests to these models using the pay-per-token endpoints available in your Databricks workspace. See [Use foundation models](https://docs.databricks.com/aws/en/machine-learning/model-serving/score-foundation-models) and [pay-per-token supported models table](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/#token-foundation-apis) for the names of the model endpoints to use.

In addition to supporting models in pay-per-token mode, Foundation Model APIs also offers provisioned throughput mode. Databricks recommends provisioned throughput for production workloads. This mode supports all models of a model architecture family, including the fine-tuned and custom pre-trained models supported in pay-per-token mode. See [Provisioned throughput Foundation Model APIs](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/#throughput) for the list of supported architectures.

You can interact with these supported models using the [AI Playground](https://docs.databricks.com/aws/en/large-language-models/ai-playground).

## OpenAI GPT-5.5 Pro[​](#openai-gpt-55-pro "Direct link to openai-gpt-55-pro")

**Endpoint name**: `databricks-gpt-5-5-pro`

**Supported inputs**: text, image

[GPT-5.5 Pro](https://openai.com/index/introducing-gpt-5-5/) is a higher-accuracy variant of GPT-5.5 aimed at the hardest problems, including deep research, advanced math, and high-stakes reasoning. This model supports multimodal inputs and features a 400K total token context window with 128K maximum output tokens.

As with other large language models, GPT-5.5 Pro output might omit some facts and occasionally produce false information. Databricks recommends using retrieval augmented generation (RAG) in scenarios where accuracy is especially important.

This endpoint is hosted by Databricks within the Databricks security perimeter.

## OpenAI GPT-5.5[​](#openai-gpt-55 "Direct link to openai-gpt-55")

**Endpoint name**: `databricks-gpt-5-5`

**Supported inputs**: text, image

[GPT-5.5](https://openai.com/index/introducing-gpt-5-5/) is OpenAI's strongest frontier model for enterprise agent workflows, complex document reasoning, and long-horizon coding agents. GPT-5.5 also powers Codex, OpenAI's coding agent. This model supports multimodal inputs and features a 400K total token context window with 128K maximum output tokens.

As with other large language models, GPT-5.5 output might omit some facts and occasionally produce false information. Databricks recommends using retrieval augmented generation (RAG) in scenarios where accuracy is especially important.

This endpoint is hosted by Databricks within the Databricks security perimeter.

## OpenAI GPT-5.4[​](#openai-gpt-54 "Direct link to openai-gpt-54")

**Endpoint name**: `databricks-gpt-5-4`

**Supported inputs**: text, image

[GPT-5.4](https://openai.com/index/gpt-5-4/) is a general purpose large language model with reasoning capabilities developed by OpenAI. It delivers improved performance on complex tasks with enhanced accuracy and more deliberate scaffolded reasoning. This model supports multimodal inputs and features a 400K total token context window with 128K maximum output tokens.

As with other large language models, GPT-5.4 output might omit some facts and occasionally produce false information. Databricks recommends using retrieval augmented generation (RAG) in scenarios where accuracy is especially important.

This endpoint is hosted by Databricks within the Databricks security perimeter.

## OpenAI GPT-5.4 mini[​](#openai-gpt-54-mini "Direct link to openai-gpt-54-mini")

**Endpoint name**: `databricks-gpt-5-4-mini`

**Supported inputs**: text, image

GPT-5.4 mini is a cost-optimized general purpose large language model with reasoning capabilities developed by OpenAI. Built on the GPT-5.4 architecture, this model delivers improved performance on well-defined tasks that require reliable reasoning, precise language, and rapid output. It supports multimodal inputs and features a 400K total token context window with 128K maximum output tokens.

As with other large language models, GPT-5.4 mini output might omit some facts and occasionally produce false information. Databricks recommends using retrieval augmented generation (RAG) in scenarios where accuracy is especially important.

This endpoint is hosted by Databricks within the Databricks security perimeter.

## OpenAI GPT-5.4 nano[​](#openai-gpt-54-nano "Direct link to openai-gpt-54-nano")

**Endpoint name**: `databricks-gpt-5-4-nano`

**Supported inputs**: text, image

GPT-5.4 nano is a general purpose large language model with reasoning capabilities developed by OpenAI. Built on the GPT-5.4 architecture, this model excels at high-throughput tasks like simple instruction-following or classification for routine business processes or mobile applications. It supports multimodal inputs and features a 400K total token context window with 128K maximum output tokens.

As with other large language models, GPT-5.4 nano output might omit some facts and occasionally produce false information. Databricks recommends using retrieval augmented generation (RAG) in scenarios where accuracy is especially important.

This endpoint is hosted by Databricks within the Databricks security perimeter.

## OpenAI GPT-5.3 Codex[​](#openai-gpt-53-codex "Direct link to openai-gpt-53-codex")

**Endpoint name**: `databricks-gpt-5-3-codex`

**Supported inputs**: text, image

GPT-5.3 Codex is OpenAI’s most advanced agentic coding model, designed to handle complex, long-running tasks that involve research, tool use, and execution. It combines the frontier coding performance of GPT-5.2 Codex with the reasoning and professional knowledge of GPT-5.2, while operating 25% faster. The model supports multimodal inputs and features a 400K total token context window with 128K maximum output tokens.

As with other large language models, GPT-5.3 Codex output might omit some facts and occasionally produce false information. Databricks recommends using retrieval augmented generation (RAG) in scenarios where accuracy is especially important.

This endpoint is hosted by Databricks within the Databricks security perimeter.

## OpenAI GPT-5.2 Codex[​](#openai-gpt-52-codex "Direct link to openai-gpt-52-codex")

important

*   Customers are responsible for ensuring their compliance with [applicable model terms](https://docs.databricks.com/aws/en/machine-learning/model-serving/acceptable-use-models).
    
*   OpenAI GPT-5.2 Codex will be retired on July 16, 2026. See [Retired models](https://docs.databricks.com/aws/en/machine-learning/retired-models-policy#retired) for the recommended replacement model and guidance for how to migrate during deprecation.
    

**Endpoint name**: `databricks-gpt-5-2-codex`

**Supported inputs**: text, image

GPT-5.2 Codex is a code-specialized large language model built on GPT-5.2 architecture with enhanced coding capabilities, it excels at code generation, refactoring, debugging, and software engineering tasks. The model supports multimodal inputs and features a 400K total token context window with 128K maximum output tokens.

As with other large language models, GPT-5.2 Codex output might omit some facts and occasionally produce false information. Databricks recommends using retrieval augmented generation (RAG) in scenarios where accuracy is especially important.

This endpoint is hosted by Databricks within the Databricks security perimeter.

## OpenAI GPT-5.2[​](#openai-gpt-52 "Direct link to openai-gpt-52")

**Endpoint name**: `databricks-gpt-5-2`

**Supported inputs**: text, image

GPT-5.2 is a general purpose large language model with reasoning capabilities developed by OpenAI. This model builds directly upon GPT-5.1, offering higher accuracy, improved token efficiency on medium-to-complex tasks, and more deliberate scaffolded reasoning. This model excels at structured extraction, multi-step workflows, and multimodal tasks. It supports multimodal inputs and features a 400K total token context window with 128K maximum output tokens.

As with other large language models, GPT-5.2 output might omit some facts and occasionally produce false information. Databricks recommends using retrieval augmented generation (RAG) in scenarios where accuracy is especially important.

This endpoint is hosted by Databricks within the Databricks security perimeter.

## OpenAI GPT-5.1[​](#openai-gpt-51 "Direct link to openai-gpt-51")

**Endpoint name**: `databricks-gpt-5-1`

**Supported inputs**: text, image

GPT-5.1 is a general purpose large language model with reasoning capabilities developed by OpenAI. This model features both Instant and Thinking modes for fast conversation or deep reasoning, automatically adjusting for simple or complex tasks. The model excels at content creation, tutoring, technical support, and coding, with less reliance on strict prompt engineering than prior versions. It supports multimodal inputs and features a 400K total token context window with 128K maximum output tokens. [Learn more about GPT-5.1](https://openai.com/index/gpt-5-1/).

As with other large language models, GPT-5.1 output might omit some facts and occasionally produce false information. Databricks recommends using retrieval augmented generation (RAG) in scenarios where accuracy is especially important.

This endpoint is hosted by Databricks within the Databricks security perimeter.

## OpenAI GPT-5.1 Codex Max[​](#openai-gpt-51-codex-max "Direct link to openai-gpt-51-codex-max")

important

*   Customers are responsible for ensuring their compliance with [applicable model terms](https://docs.databricks.com/aws/en/machine-learning/model-serving/acceptable-use-models).
    
*   This model is hosted on a global endpoint and requires [cross geography routing to be enabled](https://docs.databricks.com/aws/en/resources/databricks-geos#cross-geo-processing).
    
*   OpenAI GPT-5.1 Codex Max will be retired on July 16, 2026. See [Retired models](https://docs.databricks.com/aws/en/machine-learning/retired-models-policy#retired) for the recommended replacement model and guidance for how to migrate during deprecation.
    

**Endpoint name**: `databricks-gpt-5-1-codex-max`

**Supported inputs**: text, image

GPT-5.1 Codex Max is OpenAI's high-performance code-specialized large language model. Built on GPT-5.1 architecture with maximum coding performance, it excels at complex code generation, large-scale refactoring, and enterprise software engineering tasks. It supports multimodal inputs and features a 400K total token context window with 128K maximum output tokens.

As with other large language models, GPT-5.1 Codex Max output might omit some facts and occasionally produce false information. Databricks recommends using retrieval augmented generation (RAG) in scenarios where accuracy is especially important.

This endpoint is hosted by Databricks within the Databricks security perimeter.

## OpenAI GPT-5.1 Codex Mini[​](#openai-gpt-51-codex-mini "Direct link to openai-gpt-51-codex-mini")

important

*   Customers are responsible for ensuring their compliance with [applicable model terms](https://docs.databricks.com/aws/en/machine-learning/model-serving/acceptable-use-models).
    
*   This model is hosted on a global endpoint and requires [cross geography routing to be enabled](https://docs.databricks.com/aws/en/resources/databricks-geos#cross-geo-processing).
    
*   OpenAI GPT-5.1 Codex Mini will be retired on July 16, 2026. See [Retired models](https://docs.databricks.com/aws/en/machine-learning/retired-models-policy#retired) for the recommended replacement model and guidance for how to migrate during deprecation.
    

**Endpoint name**: `databricks-gpt-5-1-codex-mini`

**Supported inputs**: text, image

GPT-5.1 Codex Mini is OpenAI's cost-optimized code-specialized large language model. Built on GPT-5.1 architecture with efficient coding capabilities, it excels at code completion, simple refactoring, and everyday coding tasks. It supports multimodal inputs and features a 400K total token context window with 128K maximum output tokens.

As with other large language models, GPT-5.1 Codex Mini output might omit some facts and occasionally produce false information. Databricks recommends using retrieval augmented generation (RAG) in scenarios where accuracy is especially important.

This endpoint is hosted by Databricks within the Databricks security perimeter.

## OpenAI GPT-5[​](#openai-gpt-5 "Direct link to openai-gpt-5")

**Endpoint name**: `databricks-gpt-5`

**Supported inputs**: text, image

GPT-5 is a state-of-the-art, general purpose large language model and reasoning model built and trained by OpenAI. It supports multimodal inputs and features a 400K total token context window with 128K maximum output tokens. The model is built for coding, chat, reasoning and agent-driven tasks.

As with other large language models, GPT-5 output might omit some facts and occasionally produce false information. Databricks recommends using retrieval augmented generation (RAG) in scenarios where accuracy is especially important.

This endpoint is hosted by Databricks within the Databricks security perimeter.

## OpenAI GPT-5 mini[​](#openai-gpt-5-mini "Direct link to openai-gpt-5-mini")

**Endpoint name**: `databricks-gpt-5-mini`

**Supported inputs**: text, image

GPT-5 mini is a state-of-the-art, general purpose large language model and reasoning model built and trained by OpenAI. It supports multimodal inputs and features a 400K total token context window with 128K maximum output tokens. The model is cost-optimized for reasoning and chat workloads and excels at well-defined tasks that require reliable reasoning, precise language, and rapid output for text and images.

As with other large language models, GPT-5 output might omit some facts and occasionally produce false information. Databricks recommends using retrieval augmented generation (RAG) in scenarios where accuracy is especially important.

This endpoint is hosted by Databricks within the Databricks security perimeter.

## OpenAI GPT-5 nano[​](#openai-gpt-5-nano "Direct link to openai-gpt-5-nano")

**Endpoint name**: `databricks-gpt-5-nano`

**Supported inputs**: text, image

GPT-5 nano is a state-of-the-art, general purpose large language model and reasoning model built and trained by OpenAI. It supports multimodal inputs and features a 400K total token context window with 128K maximum output tokens. The model excels at high-throughput tasks like simple instruction-following or classification for routine business processes or mobile applications.

As with other large language models, GPT-5 output may omit some facts and occasionally produce false information. Databricks recommends using retrieval augmented generation (RAG) in scenarios where accuracy is especially important.

This endpoint is hosted by Databricks within the Databricks security perimeter.

## Google Gemini 3.1 Flash Lite[​](#google-gemini-31-flash-lite "Direct link to google-gemini-31-flash-lite")

**Endpoint name**: `databricks-gemini-3-1-flash-lite`

**Supported inputs**: text, image, video, audio

Gemini 3.1 Flash Lite is the fastest and most cost-efficient model in the Gemini 3 series, developed and trained by Google. Built for intelligence at scale, the model supports multimodal inputs with image capabilities, function calling, and structured output. Gemini 3.1 Flash Lite is optimized for high-throughput, cost-effective deployments. [Learn more about Gemini 3.1 Flash Lite](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-flash-lite/).

As with other large language models, Gemini 3.1 Flash Lite output might omit some facts and occasionally produce false information. Databricks recommends using retrieval augmented generation (RAG) in scenarios where accuracy is especially important.

This endpoint is hosted by Databricks within the Databricks security perimeter.

## Google Gemini 3.5 Flash[​](#google-gemini-35-flash "Direct link to google-gemini-35-flash")

**Endpoint name**: `databricks-gemini-3-5-flash`

**Supported inputs**: text, image, video, audio

Gemini 3.5 Flash is a high-speed, cost-efficient, multimodal AI model developed and trained by Google. As a significant step up from Gemini 3 Flash, this model offers stronger reasoning, advanced multimodal capabilities, and improved price performance for production-scale deployments. Gemini 3.5 Flash is optimized for high-throughput workloads such as complex video analysis, data extraction, and visual Q&As. [Learn more about Gemini 3.5 Flash](https://blog.google/products/gemini/gemini-3-5-flash/).

As with other large language models, Gemini 3.5 Flash output might omit some facts and occasionally produce false information. Databricks recommends using retrieval augmented generation (RAG) in scenarios where accuracy is especially important.

This endpoint is hosted by Databricks within the Databricks security perimeter.

## Google Gemini 3 Flash[​](#google-gemini-3-flash "Direct link to google-gemini-3-flash")

**Endpoint name**: `databricks-gemini-3-flash`

**Supported inputs**: text, image, video, audio

Gemini 3 Flash is a high-speed, cost-efficient multimodal AI model developed and trained by Google. This model offers speed and scale without compromising quality, featuring advanced multimodal capabilities for complex video analysis, data extraction, and visual Q&As in near real-time. Gemini 3 Flash delivers better price performance and faster speeds, enabling production-scale deployments. [Learn more about Gemini 3 Flash](https://blog.google/products/gemini/gemini-3-flash/).

As with other large language models, Gemini 3 Flash output might omit some facts and occasionally produce false information. Databricks recommends using retrieval augmented generation (RAG) in scenarios where accuracy is especially important.

This endpoint is hosted by Databricks within the Databricks security perimeter.

## Google Gemini 3.1 Pro Preview[​](#google-gemini-31-pro-preview "Direct link to google-gemini-31-pro-preview")

**Endpoint name**: `databricks-gemini-3-1-pro`

**Supported inputs**: text, image, video, audio

Gemini 3.1 Pro Preview is a state-of-the-art hybrid reasoning model with a 1-million-token context window developed and trained by Google. Compared to Gemini 3 Pro, Gemini 3.1 Pro delivers stronger reasoning and document intelligence, making it an overall smarter model for complex workflows and tasks. It excels at complex reasoning, deep analysis, and multimodal understanding across a wide range of inputs and tasks

As with other large language models, Gemini 3.1 Pro Preview output might omit some facts and occasionally produce false information. Databricks recommends using retrieval augmented generation (RAG) in scenarios where accuracy is especially important.

This endpoint is hosted by Databricks within the Databricks security perimeter.

## Google Gemini 3 Pro Preview[​](#google-gemini-3-pro-preview "Direct link to google-gemini-3-pro-preview")

important

See [Applicable model terms](https://docs.databricks.com/aws/en/machine-learning/model-serving/acceptable-use-models) for Gemini 3 Pro Preview.

This model is hosted on a global endpoint and requires [cross geography routing to be enabled](https://docs.databricks.com/aws/en/resources/databricks-geos#cross-geo-processing).

Google Gemini 3 Pro Preview will be retired on March 26, 2026. See [Retired models](https://docs.databricks.com/aws/en/machine-learning/retired-models-policy#retired) for the recommended replacement model and guidance for how to migrate during deprecation. To allow more time for migration, between March 26, 2026 and June 7, 2026, API calls to Gemini 3 Pro will be temporarily redirected to Gemini 3.1 Pro. The pricing for both models is identical.

**Endpoint name**: `databricks-gemini-3-pro`

**Supported inputs**: text, image, video, audio

Gemini 3 Pro Preview is a state-of-the-art hybrid reasoning model with a 1-million-token context window developed and trained by Google. Gemini 3 Pro's advanced reasoning capabilities and built-in multimodal capabilities allow it to excel at complex reasoning, deep analysis, and multimodal understanding across a wide range of inputs and tasks.

As with other large language models, Gemini 3 Pro Preview output might omit some facts and occasionally produce false information. Databricks recommends using retrieval augmented generation (RAG) in scenarios where accuracy is especially important.

This endpoint is hosted by Databricks within the Databricks security perimeter.

## Google Gemini 2.5 Pro[​](#google-gemini-25-pro "Direct link to google-gemini-25-pro")

**Endpoint name**: `databricks-gemini-2-5-pro`

**Supported inputs**: text, image, video, audio

Gemini 2.5 Pro is a hybrid reasoning model with a 1-million-token context window developed and trained by Google. Gemini 2.5 Pro's "Deep Think Mode" and built-in audio output set it apart as a leading model for enterprise, research, and creative applications. It is designed to excel at complex reasoning, deep analysis, and multimodal understanding across a wide range of inputs and tasks. [Learn more about Gemini 2.5 Pro](https://cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/2-5-pro).

As with other large language models, Gemini 2.5 Pro output might omit some facts and occasionally produce false information. Databricks recommends using retrieval augmented generation (RAG) in scenarios where accuracy is especially important.

This endpoint is hosted by Databricks within the Databricks security perimeter.

## Google Gemini 2.5 Flash[​](#google-gemini-25-flash "Direct link to google-gemini-25-flash")

**Endpoint name**: `databricks-gemini-2-5-flash`

**Supported inputs**: text, image, video, audio

Gemini 2.5 Flash is a high-speed, cost-efficient, multimodal AI model developed and trained by Google. It is Google's first fully hybrid reasoning model, designed for developers and enterprises seeking rapid, scalable, and affordable AI solutions. Gemini 2.5 Flash can process up to 1 million tokens in a single context, allowing it to handle extremely large documents or datasets. Gemini 2.5 Flash is optimized for real-time and high-volume applications like chatbots, data extraction, translation, and document parsing. [Learn more about Gemini 2.5 Flash](https://cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/2-5-flash).

As with other large language models, Gemini 2.5 Flash output might omit some facts and occasionally produce false information. Databricks recommends using retrieval augmented generation (RAG) in scenarios where accuracy is especially important.

This endpoint is hosted by Databricks within the Databricks security perimeter.

## Alibaba Cloud Qwen3.5 122B A10B[​](#alibaba-cloud-qwen35-122b-a10b "Direct link to alibaba-cloud-qwen35-122b-a10b")

**Endpoint name**: `databricks-qwen35-122b-a10b`

**Supported inputs**: text

Qwen3.5 122B A10B is a hybrid Mixture-of-Experts (MoE) reasoning model built and trained by Alibaba Cloud, with 122 billion total parameters and 10 billion active parameters per inference. The model supports a 256K context window and up to 8,000 output tokens, and delivers strong performance on reasoning, coding, and agentic tasks. As a reasoning-only model, Qwen3.5 122B A10B always reasons before responding, and reasoning cannot be disabled.

As with other large language models, Qwen3.5 122B A10B output might omit some facts and occasionally produce false information. Databricks recommends using retrieval augmented generation (RAG) in scenarios where accuracy is especially important.

## Alibaba Cloud Qwen3-Embedding-0.6B[​](#alibaba-cloud-qwen3-embedding-06b "Direct link to alibaba-cloud-qwen3-embedding-06b")

**Endpoint name**: `databricks-qwen3-embedding-0-6b`

**Supported inputs**: text

[Qwen3-Embedding-0.6B](https://huggingface.co/Qwen/Qwen3-Embedding-0.6B) is a compact text embedding model with ~600M parameters, designed for semantic tasks such as retrieval, similarity search, clustering, and classification. It encodes text into dense vectors that represent meaning rather than surface form.

The model supports 100+ languages (including code) and handles long contexts up to ~32K tokens, making it suitable for embedding long documents. It produces embeddings with a configurable dimensionality up to 1024 and is instruction-aware, allowing task-specific biasing through prompts.

Built on a transformer encoder and fine-tuned specifically for embedding generation, Qwen3-Embedding-0.6B balances embedding quality with efficient inference.

Embedding models are especially effective when used in tandem with LLMs for retrieval augmented generation (RAG) use cases. Qwen3-Embedding-0.6B can be used to find relevant text snippets in large chunks of documents that can be used in the context of an LLM.

## Alibaba Cloud Qwen3-Next 80B A3B Instruct[​](#-alibaba-cloud-qwen3-next-80b-a3b-instruct "Direct link to -alibaba-cloud-qwen3-next-80b-a3b-instruct")

**Endpoint name**: `databricks-qwen3-next-80b-a3b-instruct`

**Supported inputs**: text

Qwen3-Next-80B-A3B-Instruct is a highly efficient large language model optimized for instruction-following tasks built and trained by Alibaba Cloud. This model is designed to handle ultra-long contexts and excels at multi-step workflows, retrieval-augmented generation, and enterprise applications that require deterministic outputs at high throughput.

As with other large language models, Qwen3-Next 80B A3B Instruct output might omit some facts and occasionally produce false information. Databricks recommends using retrieval augmented generation (RAG) in scenarios where accuracy is especially important.

## OpenAI GPT OSS 120B[​](#openai-gpt-oss-120b "Direct link to openai-gpt-oss-120b")

**Endpoint name**: `databricks-gpt-oss-120b`

**Supported inputs**: text

GPT OSS 120B is a state-of-the-art, reasoning model with chain-of-thought and adjustable reasoning effort levels built and trained by OpenAI. It is OpenAI's flagship open-weight model and features a 128K token context window. The model is built for high-quality reasoning tasks.

As with other large language models, GPT OSS 120B output may omit some facts and occasionally produce false information. Databricks recommends using retrieval augmented generation (RAG) in scenarios where accuracy is especially important.

## OpenAI GPT OSS 20B[​](#openai-gpt-oss-20b "Direct link to openai-gpt-oss-20b")

**Endpoint name**: `databricks-gpt-oss-20b`

**Supported inputs**: text

GPT OSS 20B is a state-of-the-art, lightweight reasoning model built and trained by OpenAI. This model has a 128K token context window and excels at real-time copilots and batch inference tasks.

As with other large language models, GPT OSS 20B output may omit some facts and occasionally produce false information. Databricks recommends using retrieval augmented generation (RAG) in scenarios where accuracy is especially important.

## Google Gemma 3 12B[​](#google-gemma-3-12b "Direct link to google-gemma-3-12b")

**Endpoint name**: `databricks-gemma-3-12b`

**Supported inputs**: text, image

Gemma 3 12B is a 12-billion parameter multimodal and vision language model developed by Google as part of the Gemma 3 family. Gemma 3 has up to a 128K token context and provides multilingual support for over 140 languages. This model is designed to handle both text and image inputs and generate text outputs, and is optimized for dialogue use cases, text generation and image understanding tasks, including question answering.

As with other large language models, Gemma 3 output may omit some facts and occasionally produce false information. Databricks recommends using retrieval augmented generation (RAG) in scenarios where accuracy is especially important.

**Endpoint name**: `databricks-llama-4-maverick`

**Supported inputs**: text, image

Llama 4 Maverick is a state-of-the-art large language model built and trained by Meta. It is the first of the Llama model family to use a mixture of experts architecture for compute efficiency. Llama 4 Maverick supports multiple languages and is optimized for precise image and text understanding use cases. [Learn more about Llama 4 Maverick](https://github.com/meta-llama/llama-models/blob/main/models/llama4/MODEL_CARD.md).

As with other large language models, Llama 4 output may omit some facts and occasionally produce false information. Databricks recommends using retrieval augmented generation (RAG) in scenarios where accuracy is especially important.

important

Starting December 11, 2024, Meta-Llama-3.3-70B-Instruct replaces support for Meta-Llama-3.1-70B-Instruct in Foundation Model APIs pay-per-token endpoints.

See [Applicable model terms](https://docs.databricks.com/aws/en/machine-learning/model-serving/acceptable-use-models) for the LLama 3.3 Community License and Acceptable Use Policy.

**Endpoint name**: `databricks-meta-llama-3-3-70b-instruct`

**Supported inputs**: text

Meta-Llama-3.3-70B-Instruct is a state-of-the-art large language model with a context of 128,000 tokens that was built and trained by Meta. The model supports multiple languages and is optimized for dialogue use cases. [Learn more about the Meta Llama 3.3](https://github.com/meta-llama/llama-models/blob/main/models/llama3_3/MODEL_CARD.md).

Similar to other large language models, Llama-3's output may omit some facts and occasionally produce false information. Databricks recommends using retrieval augmented generation (RAG) in scenarios where accuracy is especially important.

important

Meta-Llama-3.1-405B-Instruct will be retired,

*   Starting February 15, 2026 for pay-per-token workloads.
*   Starting May 15, 2026 for provisioned throughput workloads.

See [Retired models](https://docs.databricks.com/aws/en/machine-learning/retired-models-policy#retired) for the recommended replacement model and guidance for how to migrate during deprecation.

Preview

The use of this model with Foundation Model APIs is in [Public Preview](https://docs.databricks.com/aws/en/release-notes/release-types). Reach out to your Databricks account team if you encounter endpoint failures or stabilization errors when using this model.

See [Applicable model terms](https://docs.databricks.com/aws/en/machine-learning/model-serving/acceptable-use-models) for the Llama 3.1 Community License and Acceptable Use Policy.

**Endpoint name**: `databricks-meta-llama-3-1-405b-instruct`

**Supported inputs**: text

Meta-Llama-3.1-405B-Instruct is the largest openly available state-of-the-art large language model, built and trained by Meta. The use of this model enables customers to unlock new capabilities, such as advanced, multi-step reasoning and [high-quality synthetic data generation](https://docs.databricks.com/aws/en/large-language-models/foundation-model-training/create-fine-tune-run). This model is competitive with GPT-4-Turbo in terms of quality.

Like Meta-Llama-3.1-70B-Instruct, this model has a context of 128,000 tokens and support across ten languages. It aligns with human preferences for helpfulness and safety, and is optimized for dialogue use cases. [Learn more about the Meta Llama 3.1 models](https://ai.meta.com/blog/meta-llama-3/).

Similar to other large language models, Llama-3.1's output may omit some facts and occasionally produce false information. Databricks recommends using retrieval augmented generation (RAG) in scenarios where accuracy is especially important.

**Endpoint name**: `databricks-meta-llama-3-1-8b-instruct`

**Supported inputs**: text

Meta-Llama-3.1-8B-Instruct is a state-of-the-art large language model with a context of 128,000 tokens that was built and trained by Meta. The model supports multiple languages and is optimized for dialogue use cases. [Learn more about the Meta Llama 3.1](https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/MODEL_CARD.md).

Similar to other large language models, Llama-3's output may omit some facts and occasionally produce false information. Databricks recommends using retrieval augmented generation (RAG) in scenarios where accuracy is especially important.

## Anthropic Claude Haiku 4.5[​](#-anthropic-claude-haiku-45 "Direct link to -anthropic-claude-haiku-45")

important

Customers are responsible for ensuring their compliance with the terms of Anthropic's [usage policy](https://docs.databricks.com/aws/en/machine-learning/model-serving/acceptable-use-models).

**Endpoint name**: `databricks-claude-haiku-4-5`

**Supported inputs**: text, image

Claude Haiku 4.5 is Anthropic's fastest and most cost-effective model, delivering near-frontier coding quality with exceptional speed and efficiency. It excels at real-time, low-latency applications including chat assistants, customer service agents, pair programming, and rapid prototyping. This model is ideal for cost-conscious production deployments and agentic systems requiring responsive AI assistance.

As with other large language models, Claude Haiku 4.5 output may omit some facts and occasionally produce false information. Databricks recommends using retrieval augmented generation (RAG) in scenarios where accuracy is especially important.

This endpoint is hosted by Databricks within the Databricks security perimeter.

## Anthropic Claude Sonnet 4.6[​](#-anthropic-claude-sonnet-46 "Direct link to -anthropic-claude-sonnet-46")

important

Customers are responsible for ensuring their compliance with the terms of Anthropic's [usage policy](https://docs.databricks.com/aws/en/machine-learning/model-serving/acceptable-use-models).

**Endpoint name**: `databricks-claude-sonnet-4-6`

**Supported inputs**: text, image

Claude Sonnet 4.6 is Anthropic's most advanced hybrid reasoning model. It offers two modes: near-instant responses and extended thinking for deeper reasoning based on the complexity of the task. Claude Sonnet 4.6 specializes in applications that require a balance of practical throughput and advanced thinking such as customer-facing agents, production coding workflows, and content generation at scale.

As with other large language models, Claude Sonnet 4.6 output may omit some facts and occasionally produce false information. Databricks recommends using retrieval augmented generation (RAG) in scenarios where accuracy is especially important.

This endpoint is hosted by Databricks within the Databricks security perimeter.

## Anthropic Claude Sonnet 4.5[​](#-anthropic-claude-sonnet-45 "Direct link to -anthropic-claude-sonnet-45")

important

Customers are responsible for ensuring their compliance with the terms of Anthropic's [usage policy](https://docs.databricks.com/aws/en/machine-learning/model-serving/acceptable-use-models).

**Endpoint name**: `databricks-claude-sonnet-4-5`

**Supported inputs**: text, image

Claude Sonnet 4.5 is Anthropic’s most advanced hybrid reasoning model. It offers two modes: near-instant responses and extended thinking for deeper reasoning based on the complexity of the task. Claude Sonnet 4.5 specializes in application that require a balance of practical throughput and advanced thinking such as customer-facing agents, production coding workflows, and content generation at scale.

As with other large language models, Claude Sonnet 4.5 output may omit some facts and occasionally produce false information. Databricks recommends using retrieval augmented generation (RAG) in scenarios where accuracy is especially important.

This endpoint is hosted by Databricks within the Databricks security perimeter.

## Anthropic Claude Fable 5[​](#-anthropic-claude-fable-5 "Direct link to -anthropic-claude-fable-5")

important

Customers are responsible for ensuring their compliance with the terms of Anthropic's [usage policy](https://docs.databricks.com/aws/en/machine-learning/model-serving/acceptable-use-models).

important

For Claude Fable 5, prompts and responses are retained for 30 days for trust and safety purposes. This data is processed by automated safety systems and may in certain instances be flagged for human review. The data is deleted automatically after 30 days, except in the event of a safety investigation, or legal requirements to retain the data beyond 30 days. Anthropic is a limited subprocessor for this safety retention purpose.

**Endpoint name**: `databricks-claude-fable-5`

**Supported inputs**: text

Claude Fable 5 is a Mythos-class model from Anthropic designed for autonomous knowledge work and coding. With robust safeguards built in, it can handle long-running, complex, and asynchronous tasks with less need for human check-ins than previous models, making it well suited for agentic workflows that require sustained focus across extended contexts.

As with other large language models, Claude Fable 5 output may omit some facts and occasionally produce false information. Databricks recommends using retrieval augmented generation (RAG) in scenarios where accuracy is especially important.

This endpoint is hosted by Databricks within the Databricks security perimeter.

## Anthropic Claude Opus 4.8[​](#-anthropic-claude-opus-48 "Direct link to -anthropic-claude-opus-48")

important

Customers are responsible for ensuring their compliance with the terms of Anthropic's [usage policy](https://docs.databricks.com/aws/en/machine-learning/model-serving/acceptable-use-models).

**Endpoint name**: `databricks-claude-opus-4-8`

**Supported inputs**: text, image

Claude Opus 4.8 is Anthropic's most capable hybrid reasoning model, building on the Opus series with further improvements to accuracy, efficiency, and reasoning capabilities. This model excels at complex extraction and agentic reasoning tasks with image support, making it ideal for enterprise applications that require deep analysis, document understanding, and sophisticated multi-step workflows.

As with other large language models, Claude Opus 4.8 output may omit some facts and occasionally produce false information. Databricks recommends using retrieval augmented generation (RAG) in scenarios where accuracy is especially important.

This endpoint is hosted by Databricks within the Databricks security perimeter.

## Anthropic Claude Opus 4.7[​](#-anthropic-claude-opus-47 "Direct link to -anthropic-claude-opus-47")

important

Customers are responsible for ensuring their compliance with the terms of Anthropic's [usage policy](https://docs.databricks.com/aws/en/machine-learning/model-serving/acceptable-use-models).

**Endpoint name**: `databricks-claude-opus-4-7`

**Supported inputs**: text, image

Claude Opus 4.7 is Anthropic's most capable hybrid reasoning model, advancing the Opus series with improved accuracy, efficiency, and enhanced vision capabilities. This model delivers stronger performance on complex extraction and agentic reasoning tasks while using fewer output tokens than its predecessor. Claude Opus 4.7 features a 1 million token context window and increased image resolution support, making it ideal for enterprise applications that require deep analysis, document understanding, and sophisticated multi-step workflows.

As with other large language models, Claude Opus 4.7 output may omit some facts and occasionally produce false information. Databricks recommends using retrieval augmented generation (RAG) in scenarios where accuracy is especially important.

This endpoint is hosted by Databricks within the Databricks security perimeter.

## Anthropic Claude Opus 4.6[​](#-anthropic-claude-opus-46 "Direct link to -anthropic-claude-opus-46")

important

Customers are responsible for ensuring their compliance with the terms of Anthropic's [usage policy](https://docs.databricks.com/aws/en/machine-learning/model-serving/acceptable-use-models).

**Endpoint name**: `databricks-claude-opus-4-6`

**Supported inputs**: text, image

Claude Opus 4.6 is Anthropic's most capable hybrid reasoning model with adaptive thinking capabilities. This model introduces a new max effort level for the most demanding tasks, with high effort set as the default for optimal performance. Claude Opus 4.6 excels at complex reasoning, deep analysis, code generation, research, and sophisticated multi-step workflows. It features a 1 million token context window, making it ideal for enterprise applications that require both extensive analysis and comprehensive outputs.

As with other large language models, Claude Opus 4.6 output may omit some facts and occasionally produce false information. Databricks recommends using retrieval augmented generation (RAG) in scenarios where accuracy is especially important.

This endpoint is hosted by Databricks within the Databricks security perimeter.

## Anthropic Claude Opus 4.5[​](#-anthropic-claude-opus-45 "Direct link to -anthropic-claude-opus-45")

important

Customers are responsible for ensuring their compliance with the terms of Anthropic's [usage policy](https://docs.databricks.com/aws/en/machine-learning/model-serving/acceptable-use-models).

**Endpoint name**: `databricks-claude-opus-4-5`

**Supported inputs**: text, image

Claude Opus 4.5 is Anthropic's most capable hybrid reasoning model, built for the most complex tasks requiring deep analysis and extended thinking. This model combines powerful general purpose capabilities with advanced reasoning, excelling at code generation, research, content creation, and sophisticated multi-step agentic workflows. Claude Opus 4.5 supports text and vision inputs with a 200K token context window, making it ideal for enterprise applications that demand both breadth and depth of understanding.

As with other large language models, Claude Opus 4.5 output may omit some facts and occasionally produce false information. Databricks recommends using retrieval augmented generation (RAG) in scenarios where accuracy is especially important.

This endpoint is hosted by Databricks within the Databricks security perimeter.

## Anthropic Claude Sonnet 4[​](#-anthropic-claude-sonnet-4 "Direct link to -anthropic-claude-sonnet-4")

important

Customers are responsible for ensuring their compliance with the terms of Anthropic's [usage policy](https://docs.databricks.com/aws/en/machine-learning/model-serving/acceptable-use-models).

**Endpoint name**: `databricks-claude-sonnet-4`

**Supported inputs**: text, image

Claude Sonnet 4 is a state-of-the-art, hybrid reasoning model built and trained by Anthropic. This model offers two modes: near-instant responses and extended thinking for deeper reasoning based on the complexity of the task. Claude Sonnet 4 is optimized for various tasks such as code development, large-scale content analysis, and agent application development.

As with other large language models, Claude Sonnet 4 output may omit some facts and occasionally produce false information. Databricks recommends using retrieval augmented generation (RAG) in scenarios where accuracy is especially important.

This endpoint is hosted by Databricks within the Databricks security perimeter.

## Anthropic Claude Opus 4.1[​](#-anthropic-claude-opus-41 "Direct link to -anthropic-claude-opus-41")

important

Customers are responsible for ensuring their compliance with the terms of Anthropic's [usage policy](https://docs.databricks.com/aws/en/machine-learning/model-serving/acceptable-use-models).

**Endpoint name**: `databricks-claude-opus-4-1`

**Supported inputs**: text, image

Claude Opus 4.1 is a state-of-the-art, hybrid reasoning model built and trained by Anthropic. This general purpose large language model is designed for both complex reasoning and real-world applications at enterprise scale. It supports text and image input, with a 200K token context window and 32K output token capabilities. This model excels at tasks like code generation, research and content creation, and multi-step agents workflows without constant human intervention.

As with other large language models, Claude Opus 4.1 output may omit some facts and occasionally produce false information. Databricks recommends using retrieval augmented generation (RAG) in scenarios where accuracy is especially important.

This endpoint is hosted by Databricks within the Databricks security perimeter.

## GTE Large (En)[​](#gte-large-en "Direct link to gte-large-en")

**Endpoint name**: `databricks-gte-large-en`

**Supported inputs**: text

[General Text Embedding (GTE)](https://huggingface.co/Alibaba-NLP/gte-large-en-v1.5) is a text embedding model that can map any text to a 1024-dimension embedding vector and an embedding window of 8192 tokens. These vectors can be used in vector indexes for LLMs, and for tasks like retrieval, classification, question-answering, clustering, or semantic search. This endpoint serves the English version of the model and does not generate normalized embeddings.

Embedding models are especially effective when used in tandem with LLMs for retrieval augmented generation (RAG) use cases. GTE can be used to find relevant text snippets in large chunks of documents that can be used in the context of an LLM.

## BGE Large (En)[​](#bge-large-en "Direct link to bge-large-en")

**Endpoint name**: `databricks-bge-large-en`

**Supported inputs**: text

[BAAI General Embedding (BGE)](https://huggingface.co/BAAI/bge-large-en-v1.5) is a text embedding model that can map any text to a 1024-dimension embedding vector and an embedding window of 512 tokens. These vectors can be used in vector indexes for LLMs, and for tasks like retrieval, classification, question-answering, clustering, or semantic search. This endpoint serves the English version of the model and generates normalized embeddings.

Embedding models are especially effective when used in tandem with LLMs for retrieval augmented generation (RAG) use cases. BGE can be used to find relevant text snippets in large chunks of documents that can be used in the context of an LLM.

In RAG applications, you may be able to improve the performance of your retrieval system by including an instruction parameter. The BGE authors recommend trying the instruction `"Represent this sentence for searching relevant passages:"` for query embeddings, though its performance impact is domain dependent.

## Additional resources[​](#additional-resources "Direct link to Additional resources")

*   [Use foundation models](https://docs.databricks.com/aws/en/machine-learning/model-serving/score-foundation-models)
*   [Foundation model REST API reference](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/api-reference)
*   [Applicable model terms](https://docs.databricks.com/aws/en/machine-learning/model-serving/acceptable-use-models)
