---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3edeb673fb99925ab1591932234a905b41c853619e1f8610594f44fb1ba56d27
  pageDirectory: concepts
  sources:
    - natural-language-processing-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - databricks-nlp-platform
    - DNP
  citations:
    - file: natural-language-processing-databricks-on-aws.md
title: Databricks NLP Platform
description: Databricks' overall support for natural language processing tasks using open-source libraries (Spark ML, Spark NLP, Hugging Face) and proprietary integrations (John Snow Labs), enabling distributed NLP workloads.
tags:
  - natural-language-processing
  - databricks
  - platform
timestamp: "2026-06-19T19:48:59.870Z"
---

# Databricks NLP Platform

The **Databricks NLP Platform** provides a comprehensive environment for performing natural language processing (NLP) tasks using popular open-source libraries such as Apache Spark ML and Spark NLP, as well as proprietary libraries available through the partnership with John Snow Labs. The platform supports feature creation, model training, batch inference, and integration with MLflow for model management. ^[natural-language-processing-databricks-on-aws.md]

## Feature Creation from Text Using Spark ML

Spark ML offers a range of text processing tools to create features from text columns. These tools can be incorporated directly into [Spark ML pipelines](/concepts/mllib-pipelines-api.md) and include tokenization, stop-word removal, word2vec, and feature hashing. They provide input features for model training algorithms without requiring additional libraries. ^[natural-language-processing-databricks-on-aws.md]

## Training and Inference Using Spark NLP

The open-source [Spark NLP](/concepts/spark-nlp-library.md) library scales out deep learning methods for NLP on Apache Spark. It provides standard operations such as tokenizing, named entity recognition, and vectorization through included annotators. Additionally, it supports pre-trained deep learning models based on [transformers](/concepts/mlflow-transformers-flavor.md) like BERT and T5, enabling tasks like summarization, named entity recognition, translation, and text generation. ^[natural-language-processing-databricks-on-aws.md]

### Batch Inference on CPUs

Spark NLP supplies many pre-trained models that can be used with minimal code. For example, the Marian Transformer can perform machine translation in batch. To use it, install the Spark NLP library on the cluster with the appropriate Maven coordinates and Spark configuration. A typical pipeline includes a `DocumentAssembler`, `SentenceDetectorDLModel`, and `MarianTransformer`, as shown in the product documentation. ^[natural-language-processing-databricks-on-aws.md]

### Example: Named-Entity Recognition with MLflow

A notebook example demonstrates how to train a named entity recognition (NER) model using Spark NLP, save the model to [MLflow](/concepts/mlflow.md), and reuse it for inference on text. The same approach can be extended to other NLP models by following the Spark NLP training documentation. ^[natural-language-processing-databricks-on-aws.md]

## Healthcare NLP with John Snow Labs

Through a partnership with John Snow Labs, Databricks offers Spark NLP for Healthcare, a proprietary library for clinical and biomedical text mining. It provides pre-trained models for recognizing clinical entities, drugs, risk factors, anatomy, demographics, and sensitive data. You can try it using the Partner Connect integration with John Snow Labs, which requires a trial or paid account. ^[natural-language-processing-databricks-on-aws.md]

## Additional Resources

For examples of NLP with [Hugging Face](/concepts/hugging-face-trainer.md), see the Databricks documentation on Hugging Face integration. ^[natural-language-processing-databricks-on-aws.md]

## Related Concepts

- [Spark ML pipelines](/concepts/mllib-pipelines-api.md)
- [Spark NLP](/concepts/spark-nlp-library.md)
- [MLflow](/concepts/mlflow.md)
- [Hugging Face](/concepts/hugging-face-trainer.md)
- John Snow Labs
- Partner Connect
- Feature engineering for text
- ai_translate|Machine translation
- [Named entity recognition](/concepts/named-entity-recognition-with-spark-nlp-and-mlflow.md)
- Clinical text mining

## Sources

- natural-language-processing-databricks-on-aws.md

# Citations

1. [natural-language-processing-databricks-on-aws.md](/references/natural-language-processing-databricks-on-aws-a823566c.md)
