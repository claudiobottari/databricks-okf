---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 53527e9ca576e0296299c1e81f30895f954df522cb3662f618b96e86c1ecbf8c
  pageDirectory: concepts
  sources:
    - natural-language-processing-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - spark-nlp-library
    - SNL
    - Spark NLP
  citations:
    - file: natural-language-processing-databricks-on-aws.md
title: Spark NLP Library
description: An open-source library for scaling deep learning NLP methods on Apache Spark, providing annotators and pre-trained transformers for tasks like tokenization, named entity recognition, summarization, and translation.
tags:
  - natural-language-processing
  - spark
  - deep-learning
timestamp: "2026-06-19T19:48:48.419Z"
---

# Spark NLP Library

**Spark NLP** is an open-source natural language processing (NLP) library built on top of Apache Spark, designed to scale out deep learning methods for NLP tasks across distributed computing environments. It provides standard NLP operations such as tokenization, named entity recognition, and vectorization through its included annotators, and also supports advanced transformer-based models like BERT and T5 Marion for summarization, translation, and text generation. ^[natural-language-processing-databricks-on-aws.md]

## Overview

Spark NLP enables practitioners to perform natural language processing tasks on Databricks and other Spark-compatible platforms using deep learning models at scale. The library is maintained by John Snow Labs and integrates seamlessly with Spark ML pipelines for feature creation and model training. ^[natural-language-processing-databricks-on-aws.md]

## Key Features

### Annotators and Transformers

Spark NLP includes a comprehensive set of [annotators](https://nlp.johnsnowlabs.com/docs/en/annotators) that perform standard NLP operations. For advanced use cases, the library provides [transformer models](https://nlp.johnsnowlabs.com/docs/en/transformers) based on architectures such as BERT and T5 Marion, enabling tasks like text summarization, named entity recognition, translation, and text generation. ^[natural-language-processing-databricks-on-aws.md]

### Pre-trained Models

Spark NLP offers many pre-trained models that can be used with minimal code for batch inference on CPUs. For example, the Marian Transformer can perform machine translation with a short pipeline. ^[natural-language-processing-databricks-on-aws.md]

## Installation and Configuration

To use Spark NLP on Databricks:

1. Install Spark NLP on the cluster using the latest Maven coordinates, such as `com.johnsnowlabs.nlp:spark-nlp_2.12:4.1.0`.
2. Configure the cluster with appropriate Spark configuration options.
3. Use a cluster running any [compatible runtime](https://nlp.johnsnowlabs.com/docs/en/install#databricks-support).

The cluster must download the correct `.jar` file from John Snow Labs. ^[natural-language-processing-databricks-on-aws.md]

## Usage Examples

### Machine Translation with Marian Transformer

Spark NLP allows constructing a pipeline for translation with minimal code. The following components are used:

- `DocumentAssembler` – Converts input text into a document format.
- `SentenceDetectorDLModel` – Detects sentence boundaries.
- `MarianTransformer` – Performs neural machine translation.

After fitting the pipeline on sample data, the resulting model can be reused across multiple data frames containing a "text" column. ^[natural-language-processing-databricks-on-aws.md]

### Named Entity Recognition (NER)

Spark NLP supports training and inference for NER models. A dedicated notebook example demonstrates how to train an NER model using Spark NLP, save it to [MLflow](/concepts/mlflow.md), and use it for inference on text. For additional training guidance, see the [John Snow Labs documentation for Spark NLP](https://nlp.johnsnowlabs.com/docs/en/training). ^[natural-language-processing-databricks-on-aws.md]

## Healthcare NLP

Through the Databricks partnership with John Snow Labs, proprietary **Spark NLP for Healthcare** libraries are available for clinical and biomedical text mining. This library provides pre-trained models for recognizing and working with clinical entities, drugs, risk factors, anatomy, demographics, and sensitive data. Users can try Spark NLP for Healthcare using the Partner Connect integration with John Snow Labs, though a trial or paid account with John Snow Labs is required. ^[natural-language-processing-databricks-on-aws.md]

## Related Concepts

- Spark ML – Core machine learning library for feature creation and pipelines.
- [MLflow](/concepts/mlflow.md) – Model lifecycle management for tracking and deploying Spark NLP models.
- [Natural Language Processing](/concepts/spark-ml-text-processing.md) – Broader domain of text analysis and language understanding.
- John Snow Labs – Vendor and maintainer of the Spark NLP library.
- [Named Entity Recognition](/concepts/named-entity-recognition-with-spark-nlp-and-mlflow.md) – A common NLP task supported by Spark NLP.
- Transformers – Deep learning model architectures (BERT, T5) available in Spark NLP.
- Partner Connect – Integration mechanism for accessing John Snow Labs Healthcare NLP.

## Sources

- natural-language-processing-databricks-on-aws.md

# Citations

1. [natural-language-processing-databricks-on-aws.md](/references/natural-language-processing-databricks-on-aws-a823566c.md)
