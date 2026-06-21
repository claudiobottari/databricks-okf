---
title: What are Hugging Face Transformers? | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/train-model/huggingface/
ingestedAt: "2026-06-18T08:13:27.267Z"
---

This article provides an introduction to Hugging Face Transformers on Databricks. It includes guidance on why to use Hugging Face Transformers and how to install it on your cluster.

## Background for Hugging Face Transformers[​](#background-for-hugging-face-transformers "Direct link to Background for Hugging Face Transformers")

[Hugging Face Transformers](https://huggingface.co/docs/transformers/index) is an open-source framework for deep learning created by Hugging Face. It provides APIs and tools to download state-of-the-art pre-trained models and further tune them to maximize performance. These models support common tasks in different modalities, such as natural language processing, computer vision, audio, and multi-modal applications.

[Databricks Runtime for Machine Learning](https://docs.databricks.com/aws/en/machine-learning/) includes Hugging Face `transformers` in Databricks Runtime 10.4 LTS ML and above, and includes Hugging Face [datasets](https://huggingface.co/docs/datasets/index), [accelerate](https://huggingface.co/docs/accelerate/index), and [evaluate](https://huggingface.co/docs/evaluate/index) in Databricks Runtime 13.0 ML and above.

To check which version of Hugging Face is included in your configured Databricks Runtime ML version, see the Python libraries section on the relevant [release notes](https://docs.databricks.com/aws/en/release-notes/runtime/).

## Why use Hugging Face Transformers?[​](#why-use-hugging-face-transformers "Direct link to Why use Hugging Face Transformers?")

For many applications, such as sentiment analysis and text summarization, pre-trained models work well without any additional model training.

Hugging Face Transformers pipelines encode best practices and have default models selected for different tasks, making it easy to get started. Pipelines make it easy to use GPUs when available and allow batching of items sent to the GPU for better throughput performance.

Hugging Face provides:

*   A [model hub](https://huggingface.co/models) containing many pre-trained models.
*   The [🤗 Transformers library](https://huggingface.co/docs/transformers/index) that supports the download and use of these models for NLP applications and fine-tuning. It is common to need both a tokenizer and a model for natural language processing tasks.
*   [🤗 Transformers pipelines](https://huggingface.co/docs/transformers/v4.26.1/en/pipeline_tutorial) that have a simple interface for most natural language processing tasks.

## Install `transformers`[​](#install-transformers "Direct link to install-transformers")

If the Databricks Runtime version on your cluster does not include Hugging Face `transformers`, you can install the latest Hugging Face `transformers` library as a [Databricks PyPI library](https://docs.databricks.com/aws/en/libraries/).

Bash

      %pip install transformers

## Install model dependencies[​](#install-model-dependencies "Direct link to Install model dependencies")

Different models may have different dependencies. Databricks recommends that you use [%pip magic commands](https://docs.databricks.com/aws/en/libraries/notebooks-python-libraries#manage-libraries-with-pip-commands) to install these dependencies as needed.

The following are common dependencies:

*   `librosa`: supports decoding audio files.
*   `soundfile`: required while generating some audio datasets.
*   `bitsandbytes`: required when using `load_in_8bit=True`.
*   `SentencePiece`: used as the tokenizer for NLP models.
*   `timm`: required by [DetrForSegmentation](https://huggingface.co/docs/transformers/v4.27.2/en/model_doc/detr#transformers.DetrForSegmentation).

## Single node training[​](#single-node-training "Direct link to Single node training")

To test and migrate single-machine workflows, use a [Single Node cluster](https://docs.databricks.com/aws/en/compute/configure#single-node).

## Additional resources[​](#additional-resources "Direct link to additional-resources")

The following articles include example notebooks and guidance for how to use Hugging Face `transformers` for large language model (LLM) fine-tuning and model inference on Databricks.

*   [Prepare data for fine tuning Hugging Face models](https://docs.databricks.com/aws/en/machine-learning/train-model/huggingface/load-data)
*   [Fine-tune Hugging Face models for a single GPU](https://docs.databricks.com/aws/en/machine-learning/train-model/huggingface/fine-tune-model)
