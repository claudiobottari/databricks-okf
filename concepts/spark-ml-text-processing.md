---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6caf24b41e522b3c1548571a5c4248dc27fc56d80d393f6e69cb1212d43e0d4a
  pageDirectory: concepts
  sources:
    - natural-language-processing-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - spark-ml-text-processing
    - SMTP
    - Natural Language Processing
  citations:
    - file: natural-language-processing-databricks-on-aws.md
title: Spark ML Text Processing
description: Using Spark ML's built-in text processing tools (tokenization, stop-word removal, word2vec, feature hashing) to create features from text columns within ML pipelines.
tags:
  - natural-language-processing
  - spark
  - feature-engineering
timestamp: "2026-06-19T19:48:28.350Z"
---

# Spark ML Text Processing

**Spark ML Text Processing** refers to the set of text feature extraction and transformation tools provided by Spark ML (the machine learning library within Apache Spark) for preparing text data for model training. These tools are available on Databricks and can be integrated directly into Spark ML pipelines. ^[natural-language-processing-databricks-on-aws.md]

## Overview

Spark ML includes a range of text processors that convert raw text columns into numerical feature vectors suitable for downstream algorithms. This allows users to build end-to-end NLP Pipelines without leaving the Spark ecosystem. The supported processors cover common NLP preprocessing steps. ^[natural-language-processing-databricks-on-aws.md]

## Supported Text Processors

Spark ML provides the following text processing capabilities, each implemented as a PipelineStage that can be chained together:

- **Tokenization** – Splits text into individual tokens (words, subwords, or characters), forming the foundation for further feature engineering.
- **Stop-word removal** – Filters out common words (e.g., “the”, “a”, “and”) that carry little semantic meaning, reducing noise in the feature space.
- **Word2Vec** – Learns dense vector representations (embeddings) for words, capturing semantic relationships by training a shallow neural network on the corpus.
- **Feature hashing** – Maps tokens to a lower-dimensional feature space using a hash function, enabling efficient storage and computation for high-cardinality text data.

^[natural-language-processing-databricks-on-aws.md]

## Usage in Spark ML Pipelines

These text processors can be used as stages in a [Spark ML Pipeline](/concepts/mllib-pipelines-api.md). For example, a pipeline for text classification might start with tokenization, followed by stop-word removal, then Word2Vec or feature hashing, and finally a classifier. This approach streamlines feature creation from text columns and ensures reproducibility across training and inference. ^[natural-language-processing-databricks-on-aws.md]

## Related Concepts

- Natural Language Processing on Databricks
- [Spark NLP](/concepts/spark-nlp-library.md) – A complementary library for deep learning NLP on Spark
- [Feature Engineering](/concepts/featureengineeringclient-api.md)
- Tokenizer (Spark ML)
- StopWordsRemover (Spark ML)
- Word2Vec (Spark ML)
- HashingTF (Spark ML)
- [Spark ML Pipeline](/concepts/mllib-pipelines-api.md)

## Sources

- natural-language-processing-databricks-on-aws.md

# Citations

1. [natural-language-processing-databricks-on-aws.md](/references/natural-language-processing-databricks-on-aws-a823566c.md)
