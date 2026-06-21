---
title: Natural language processing | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/reference-solutions/natural-language-processing
ingestedAt: "2026-06-18T08:13:13.685Z"
---

You can perform natural language processing tasks on Databricks using popular open source libraries such as Spark ML and spark-nlp or proprietary libraries through the Databricks partnership with John Snow Labs.

For examples of NLP with Hugging Face, see [Additional resources](https://docs.databricks.com/aws/en/machine-learning/train-model/huggingface/#hugging-face-db)

## Feature creation from text using Spark ML[​](#feature-creation-from-text-using-spark-ml "Direct link to Feature creation from text using Spark ML")

Spark ML contains a range of text processing tools to create features from text columns. You can create input features from text for model training algorithms directly in your [Spark ML pipelines](https://spark.apache.org/docs/latest/ml-pipeline.html) using Spark ML. Spark ML supports a range of [text processors](https://spark.apache.org/docs/latest/ml-features.html), including tokenization, stop-word processing, word2vec, and feature hashing.

## Training and inference using Spark NLP[​](#training-and-inference-using-spark-nlp "Direct link to Training and inference using Spark NLP")

You can scale out many deep learning methods for natural language processing on Spark using the open-source Spark NLP library. This library supports standard natural language processing operations such as tokenizing, named entity recognition, and vectorization using the included [annotators](https://nlp.johnsnowlabs.com/docs/en/annotators). You can also summarize, perform named entity recognition, translate, and generate text using many pre-trained deep learning models based on [Spark NLP's transformers](https://nlp.johnsnowlabs.com/docs/en/transformers) such as BERT and T5 Marion.

### Perform inference in batch using Spark NLP on CPUs[​](#perform-inference-in-batch-using-spark-nlp-on-cpus "Direct link to Perform inference in batch using Spark NLP on CPUs")

Spark NLP provides many pre-trained models you can use with minimal code. This section contains an example of using the Marian Transformer for machine translation. For the full set of examples, see the [Spark NLP documentation](https://nlp.johnsnowlabs.com/docs/en/quickstart).

#### Requirements[​](#requirements "Direct link to Requirements")

*   Install Spark NLP on the cluster using the latest Maven coordinates for Spark NLP, such as `com.johnsnowlabs.nlp:spark-nlp_2.12:4.1.0`. Your cluster must be started with the appropriate Spark configuration options set in order for this library to work.
*   To use Spark NLP, your cluster must have the correct `.jar` file downloaded from John Snow Labs. You can create or use a cluster running [any compatible runtime](https://nlp.johnsnowlabs.com/docs/en/install#databricks-support).

#### Example code for Machine Translation[​](#example-code-for-machine-translation "Direct link to Example code for Machine Translation")

In a notebook cell, install `sparknlp` python libraries:

Construct a pipeline for translation and run it on some sample text:

Python

    from sparknlp.base import DocumentAssemblerfrom sparknlp.annotator import SentenceDetectorDLModel, MarianTransformerfrom pyspark.ml import Pipelinedocument_assembler = DocumentAssembler().setInputCol("text").setOutputCol("document")sentence_detector = SentenceDetectorDLModel.pretrained("sentence_detector_dl", "xx") \  .setInputCols("document").setOutputCol("sentence")marian_transformer = MarianTransformer.pretrained() \  .setInputCols("sentence").setOutputCol("translation")pipeline = Pipeline().setStages([document_assembler,  sentence_detector, marian_transformer])data = spark.createDataFrame([["You can use Spark NLP to translate text. " + \                               "This example pipeline translates English to French"]]).toDF("text")# Create a pipeline model that can be reused across multiple data framesmodel = pipeline.fit(data)# You can use the model on any data frame that has a “text” columnresult = model.transform(data)display(result.select("text", "translation.result"))

## Example: Named-entity recognition model using Spark NLP and MLflow[​](#example-named-entity-recognition-model-using-spark-nlp-and-mlflow "Direct link to example-named-entity-recognition-model-using-spark-nlp-and-mlflow")

The example notebook illustrates how to train a named entity recognition model using Spark NLP, save the model to MLflow, and use the model for inference on text. Refer to the [John Snow Labs documentation for Spark NLP](https://nlp.johnsnowlabs.com/docs/en/training) to learn how to train additional natural language processing models.

#### Spark NLP model training and inference notebook

## Healthcare NLP with John Snow Labs partnership[​](#healthcare-nlp-with-john-snow-labs-partnership "Direct link to Healthcare NLP with John Snow Labs partnership")

John Snow Labs Spark NLP for Healthcare is a proprietary library for clinical and biomedical text mining. This library provides pre-trained models for recognizing and working with clinical entities, drugs, risk factors, anatomy, demographics, and sensitive data. You can try Spark NLP for Healthcare using the [Partner Connect integration with John Snow Labs](https://docs.databricks.com/aws/en/partners/ml/john-snow-labs). You need a trial or paid account with John Snow Labs to try out the commands demonstrated in this guide.

Read more about the full capabilities of John Snow Labs Spark NLP for Healthcare and documentation for use at their [website](https://nlp.johnsnowlabs.com/docs/en/license_getting_started).
