---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8cd082f21c0047bea1deff895fb43f2c160107da832e8a39fb728eb75639dce4
  pageDirectory: concepts
  sources:
    - natural-language-processing-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - named-entity-recognition-with-spark-nlp-and-mlflow
    - MLflow and Named Entity Recognition with Spark NLP
    - NERWSNAM
    - Named Entity Recognition
    - Named entity recognition
    - Named-Entity Recognition (NER)
  citations:
    - file: natural-language-processing-databricks-on-aws.md
title: Named Entity Recognition with Spark NLP and MLflow
description: Training a named entity recognition (NER) model using Spark NLP and tracking/saving it with MLflow for reusable inference on Databricks.
tags:
  - natural-language-processing
  - named-entity-recognition
  - mlflow
timestamp: "2026-06-19T19:49:02.177Z"
---

#Named Entity Recognition with Spark NLP and MLflow

**Named Entity Recognition (NER) with Spark NLP and MLflow** refers to the workflow of training a named entity recognition model using the open-source [Spark NLP](/concepts/spark-nlp-library.md) library on Databricks, saving the trained model to [MLflow](/concepts/mlflow.md), and then using that model for batch inference on text data. This approach combines the distributed scaling capabilities of Spark NLP with MLflow’s model management and reproducibility features. ^[natural-language-processing-databricks-on-aws.md]

## Overview

Spark NLP is an open-source library that provides a wide range of natural language processing annotators, including tokenization, sentence detection, named entity recognition, and vectorization. It supports both standard NLP operations and deep learning‑based transformers such as BERT and T5. On Databricks, you can scale out these deep learning methods across a Spark cluster. ^[natural-language-processing-databricks-on-aws.md]

MLflow serves as the model registry and tracking layer. By saving a Spark NLP NER model to MLflow, you can version the model, track its training parameters, and later load it for inference in production or batch scoring jobs. ^[natural-language-processing-databricks-on-aws.md]

## Training an NER Model

Databricks provides an example notebook that demonstrates the full training pipeline for a named entity recognition model using Spark NLP. The workflow typically involves:

1. **Preparing the data** – loading labeled text data into a Spark DataFrame.
2. **Constructing a Spark NLP pipeline** – assembling stages such as document assembler, sentence detector, tokenizer, and a named entity recognition annotator (for example, `NerDLModel` or `NerCrf`).
3. **Fitting the pipeline** using `pipeline.fit()` on the training data.
4. **Saving the trained model to MLflow** – logging the pipeline model as an MLflow artifact so it can be registered, versioned, and reused.

The notebook illustrates this end‑to‑end process. For additional details on training other Spark NLP models, refer to the official Spark NLP documentation. ^[natural-language-processing-databricks-on-aws.md]

## Performing Inference

After the model is saved in MLflow, you can load it back and apply it to new text data. Spark NLP also provides many pre‑trained NER models out‑of‑the‑box, which can be used with minimal code. Inference runs in batch across a Spark cluster, typically on CPUs, using the pipeline’s `.transform()` method. ^[natural-language-processing-databricks-on-aws.md]

## Requirements

To use Spark NLP on Databricks, the cluster must be configured with the correct Maven coordinates for the Spark NLP library (for example, `com.johnsnowlabs.nlp:spark-nlp_2.12:4.1.0`). The cluster must also have the appropriate `.jar` file downloaded from John Snow Labs. Any compatible Databricks Runtime can be used. ^[natural-language-processing-databricks-on-aws.md]

## Related Concepts

- [Spark NLP](/concepts/spark-nlp-library.md) – The open-source library used for NLP annotators and transformers.
- [MLflow](/concepts/mlflow.md) – Platform for managing the full machine learning lifecycle.
- Natural Language Processing with Spark ML – Feature creation using Spark ML text processors.
- Healthcare NLP with John Snow Labs – Proprietary library for clinical and biomedical NER.
- [Named Entity Recognition](/concepts/named-entity-recognition-with-spark-nlp-and-mlflow.md) – The underlying NLP task.

## Sources

- natural-language-processing-databricks-on-aws.md

# Citations

1. [natural-language-processing-databricks-on-aws.md](/references/natural-language-processing-databricks-on-aws-a823566c.md)
