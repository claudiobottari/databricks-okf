---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5791b3ff60ff5b94054590b5cd77b845939b7ac8cb6da2d3cadd02470d5929d9
  pageDirectory: concepts
  sources:
    - natural-language-processing-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - john-snow-labs-healthcare-nlp
    - JSLHN
  citations:
    - file: natural-language-processing-databricks-on-aws.md
title: John Snow Labs Healthcare NLP
description: A proprietary library (Spark NLP for Healthcare) for clinical and biomedical text mining, offering pre-trained models for entities, drugs, risk factors, anatomy, and demographics, available via Databricks Partner Connect.
tags:
  - natural-language-processing
  - healthcare
  - biomedical
timestamp: "2026-06-19T19:48:54.802Z"
---

# John Snow Labs Healthcare NLP

**John Snow Labs Healthcare NLP** (also known as Spark NLP for Healthcare) is a proprietary library for clinical and biomedical text mining that runs on the Apache Spark platform. It provides pre-trained deep learning models for recognizing and working with clinical entities, drugs, risk factors, anatomy, demographics, and sensitive data within unstructured medical text. ^[natural-language-processing-databricks-on-aws.md]

## Overview

John Snow Labs Healthcare NLP is built on top of the open-source [Spark NLP](/concepts/spark-nlp-library.md) library and extends it with domain-specific models and annotators designed for the healthcare and life sciences sectors. The library is available through the Databricks partnership with John Snow Labs and can be accessed via Partner Connect. ^[natural-language-processing-databricks-on-aws.md]

## Features

The library offers pre-trained models for a variety of clinical NLP tasks, including:

- **Clinical entity recognition** — Identifying medical conditions, procedures, medications, and laboratory tests within clinical notes.
- **Drug recognition** — Extracting drug names, dosages, strengths, and routes of administration.
- **Risk factor identification** — Detecting mentions of smoking status, alcohol use, family history, and other clinical risk factors.
- **Anatomy recognition** — Identifying anatomical structures and body parts mentioned in text.
- **Demographic extraction** — Recognizing patient age, gender, race, and ethnicity information.
- **Sensitive data detection** — Identifying protected health information (PHI) and personally identifiable information (PII) for de-identification purposes.

## Access and Requirements

To use John Snow Labs Healthcare NLP, users need a trial or paid account with John Snow Labs. The library is a proprietary offering and is not included in the open-source Spark NLP distribution. ^[natural-language-processing-databricks-on-aws.md]

On Databricks, users can try Spark NLP for Healthcare using the Partner Connect integration with John Snow Labs. This integration simplifies the setup process for getting started with the library on the Databricks platform. ^[natural-language-processing-databricks-on-aws.md]

## Relationship to Open-Source Spark NLP

While John Snow Labs Healthcare NLP is proprietary, the open-source [Spark NLP](/concepts/spark-nlp-library.md) library provides a foundation of standard NLP operations such as tokenizing, named entity recognition, and vectorization. Healthcare NLP builds on this foundation with specialized clinical and biomedical models, including deep learning transformers based on architectures like BERT and T5. ^[natural-language-processing-databricks-on-aws.md]

## Use Cases

Typical use cases for John Snow Labs Healthcare NLP include:

- **Clinical text mining** — Extracting structured information from electronic health records (EHRs), clinical notes, and discharge summaries.
- **Pharmacovigilance** — Identifying adverse drug events and medication-related information from unstructured text.
- **Cohort identification** — Finding patient populations matching specific clinical criteria for research or clinical trials.
- **De-identification** — Removing protected health information from clinical documents for secondary use.
- **Biomedical literature mining** — Extracting entities and relationships from research articles and publications.

## Related Concepts

- [Spark NLP](/concepts/spark-nlp-library.md) — The open-source NLP library on which Healthcare NLP is built.
- Natural Language Processing (NLP) — The broader field of computational linguistics.
- Clinical NLP — The subfield focused on processing medical and clinical text.
- Named Entity Recognition (NER) — A key task performed by Healthcare NLP models.
- Databricks Partner Connect — The integration mechanism for accessing the library.
- [MLflow](/concepts/mlflow.md) — For managing and deploying Healthcare NLP models.
- BERT — A transformer architecture used by some Healthcare NLP models.
- T5 — Another transformer architecture supported by the library.

## Sources

- natural-language-processing-databricks-on-aws.md

# Citations

1. [natural-language-processing-databricks-on-aws.md](/references/natural-language-processing-databricks-on-aws-a823566c.md)
