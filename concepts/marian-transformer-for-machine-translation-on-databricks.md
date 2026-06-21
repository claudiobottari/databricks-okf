---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 47a8321ae24457a654e9f82aac230169b3b11c331333874da777897fd9e3e5b3
  pageDirectory: concepts
  sources:
    - natural-language-processing-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - marian-transformer-for-machine-translation-on-databricks
    - MTFMTOD
  citations:
    - file: natural-language-processing-databricks-on-aws.md
title: Marian Transformer for Machine Translation on Databricks
description: A practical example of using Spark NLP's Marian Transformer for batch machine translation on Databricks clusters, including pipeline construction and inference.
tags:
  - natural-language-processing
  - machine-translation
  - spark-nlp
timestamp: "2026-06-19T19:48:44.582Z"
---

## Marian Transformer for Machine Translation on Databricks

The **Marian Transformer** is a pre-trained deep learning model available through the open‑source [Spark NLP](/concepts/spark-nlp-library.md) library that can perform **machine translation** in batch on Databricks clusters. It is one of several transformer‑based models (alongside BERT and T5) provided by Spark NLP for tasks such as summarization, named entity recognition, text generation, and translation. ^[natural-language-processing-databricks-on-aws.md]

### Batch Inference with Spark NLP on CPUs

On Databricks, you can use the Marian Transformer to translate text by constructing a Spark ML pipeline. The pipeline typically consists of a `DocumentAssembler`, a `SentenceDetectorDLModel` (to split text into sentences), and the `MarianTransformer` annotator that performs the actual translation. ^[natural-language-processing-databricks-on-aws.md]

In the example provided in the Databricks documentation, the pipeline translates English text to French. The workflow is:

1. **DocumentAssembler** – reads an input text column and converts it into the Spark NLP document format.
2. **SentenceDetectorDLModel** – splits the document into individual sentences.
3. **MarianTransformer** – translates each sentence into the target language.
4. **Pipeline** – combines these stages; after fitting on sample data, it can be applied to any DataFrame that contains a `text` column.

```python
from sparknlp.base import DocumentAssembler
from sparknlp.annotator import SentenceDetectorDLModel, MarianTransformer
from pyspark.ml import Pipeline

document_assembler = DocumentAssembler().setInputCol("text").setOutputCol("document")
sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl", "xx") \
  .setInputCols("document").setOutputCol("sentence")
marian_transformer = MarianTransformer.pretrained() \
  .setInputCols("sentence").setOutputCol("translation")

pipeline = Pipeline().setStages([document_assembler,
                                 sentence_detector,
                                 marian_transformer])

data = spark.createDataFrame([["You can use Spark NLP to translate text. " + \
                               "This example pipeline translates English to French"]]) \
                               .toDF("text")
model = pipeline.fit(data)
result = model.transform(data)
display(result.select("text", "translation.result"))
```

^[natural-language-processing-databricks-on-aws.md]

### Requirements

To use the Marian Transformer (or any Spark NLP annotator) on Databricks:

- Install Spark NLP on the cluster using the latest Maven coordinates (e.g., `com.johnsnowlabs.nlp:spark-nlp_2.12:4.1.0`). The cluster must be started with the appropriate Spark configuration options for the library to work. ^[natural-language-processing-databricks-on-aws.md]
- The cluster must have the correct `.jar` file downloaded from John Snow Labs and must run a [Databricks Runtime version supported by Spark NLP](/concepts/databricks-runtime-version-compatibility.md). ^[natural-language-processing-databricks-on-aws.md]
- Install the `sparknlp` Python libraries in a notebook cell before using the annotators.

### Related Concepts

- [Spark NLP](/concepts/spark-nlp-library.md) – open‑source library for natural language processing on Spark.
- Natural Language Processing on Databricks – overview of NLP capabilities on the platform.
- Machine Translation – the task of automatically translating text between languages.
- [Spark ML Pipelines](/concepts/mllib-pipelines-api.md) – the framework used to compose the translation pipeline.
- MarianMT – the underlying model architecture; MarianTransformer is Spark NLP’s wrapper for it.

### Sources

- natural-language-processing-databricks-on-aws.md

# Citations

1. [natural-language-processing-databricks-on-aws.md](/references/natural-language-processing-databricks-on-aws-a823566c.md)
