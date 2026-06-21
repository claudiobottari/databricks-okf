---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e61fee7b9d2d8e4e4e32239cb6f4be237d1e81d459e21712718a34108bf1c356
  pageDirectory: concepts
  sources:
    - natural-language-processing-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - spark-nlp-transformers
    - SNT
  citations:
    - file: natural-language-processing-databricks-on-aws.md
title: Spark NLP Transformers
description: Pre-trained deep learning models available in Spark NLP (including BERT, T5, and Marian) for tasks such as text generation, summarization, named entity recognition, and machine translation.
tags:
  - natural-language-processing
  - transformers
  - deep-learning
timestamp: "2026-06-19T19:49:15.580Z"
---


# Spark NLP Transformers

**Spark NLP Transformers** are a core component of the open-source [Spark NLP](/concepts/spark-nlp-library.md) library, providing pre-trained deep learning models for natural language processing (NLP) tasks that can be scaled across Apache Spark clusters. These transformers enable a wide range of NLP operations, including text generation, named entity recognition, translation, and summarization, using state-of-the-art architectures. ^[natural-language-processing-databricks-on-aws.md]

## Overview

Spark NLP transformers are neural network models designed for distributed NLP pipelines on Spark. They support standard NLP tasks such as tokenization, named entity recognition, and vectorization through the library's included annotators. More advanced transformers based on architectures like BERT and T5 (including T5 Marion) allow for tasks such as text summarization, translation, and generation. ^[natural-language-processing-databricks-on-aws.md]

The library is built on top of Spark ML, enabling users to combine Spark NLP transformers with existing [Spark ML Pipelines](/concepts/mllib-pipelines-api.md) and text processing tools for feature engineering and model training. ^[natural-language-processing-databricks-on-aws.md]

## Key Capabilities

Spark NLP transformers provide pre-trained models that require minimal code to use. Key capabilities include:

- **Machine Translation**: Using models like the MarianTransformer, which supports translation between multiple language pairs. ^[natural-language-processing-databricks-on-aws.md]
- **Named Entity Recognition (NER)**: Identifying entities such as persons, organizations, and locations in text. ^[natural-language-processing-databricks-on-aws.md]
- **Text Summarization and Generation**: Generating concise summaries or producing text from prompts. ^[natural-language-processing-databricks-on-aws.md]
- **Sentence Detection**: Using the SentenceDetectorDLModel to split text into sentences. ^[natural-language-processing-databricks-on-aws.md]

## Architecture and Components

Spark NLP transformers are organized around a pipeline-based architecture. Common components include:

- **DocumentAssembler**: Converts input text into a format suitable for NLP processing. ^[natural-language-processing-databricks-on-aws.md]
- **SentenceDetectorDLModel**: Deep learning-based sentence detection for multiple languages. ^[natural-language-processing-databricks-on-aws.md]
- **MarianTransformer**: The underlying transformer model for machine translation tasks. ^[natural-language-processing-databricks-on-aws.md]

## Usage on Databricks

Spark NLP transformers can be deployed on Databricks clusters by installing the library via Maven coordinates (e.g., `com.johnsnowlabs.nlp:spark-nlp_2.12:4.1.0`). The cluster must have the correct `.jar` file from John Snow Labs and be started with appropriate Spark configuration options. ^[natural-language-processing-databricks-on-aws.md]

### Example: Machine Translation Pipeline

A typical pipeline for machine translation using Spark NLP transformers involves:

1. **DocumentAssembler**: Takes input text and converts it to a `document` column.
2. **SentenceDetectorDLModel**: Detects sentence boundaries.
3. **MarianTransformer**: Performs translation on detected sentences.

This pipeline can be trained and reused across multiple data frames for batch inference. ^[natural-language-processing-databricks-on-aws.md]

### Example: Named Entity Recognition

Spark NLP transformers can be used to train named entity recognition models, which can then be saved to [MLflow](/concepts/mlflow.md) for deployment and inference on new text data. ^[natural-language-processing-databricks-on-aws.md]

## Healthcare NLP

Through the John Snow Labs partnership, Databricks also supports **Spark NLP for Healthcare**, a proprietary library providing pre-trained transformers for clinical and biomedical text mining. These models can recognize clinical entities, drugs, risk factors, anatomy, demographics, and sensitive data. Access requires a trial or paid account with John Snow Labs via Partner Connect. ^[natural-language-processing-databricks-on-aws.md]

## Related Concepts

- [Spark NLP](/concepts/spark-nlp-library.md)
- [Spark ML Pipelines](/concepts/mllib-pipelines-api.md)
- Natural Language Processing (NLP)
- BERT
- T5
- MarianTransformer
- [MLflow](/concepts/mlflow.md)
- John Snow Labs
- Annotators
- Deep Learning

## Sources

- natural-language-processing-databricks-on-aws.md

# Citations

1. [natural-language-processing-databricks-on-aws.md](/references/natural-language-processing-databricks-on-aws-a823566c.md)
