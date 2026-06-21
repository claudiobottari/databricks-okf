---
title: Model inference using Hugging Face Transformers for NLP | Databricks on AWS
source: https://docs.databricks.com/aws/en/archive/machine-learning/train-model/model-inference-nlp
ingestedAt: "2026-06-18T08:03:07.747Z"
---

important

*   This documentation has been retired and might not be updated. The products, services, or technologies mentioned in this content are no longer supported.
*   Databricks recommends using `ai_query` for batch inference instead. See [Enrich data using AI Functions](https://docs.databricks.com/aws/en/large-language-models/ai-functions).

This article shows you how to use Hugging Face Transformers for natural language processing (NLP) model inference.

Hugging Face transformers provides the [pipelines](https://huggingface.co/docs/transformers/main/en/main_classes/pipelines) class to use the pre-trained model for inference. 🤗 Transformers pipelines support a [wide range of NLP tasks](https://huggingface.co/docs/transformers/main_classes/pipelines#natural-language-processing) that you can easily use on Databricks.

## Requirements[​](#requirements "Direct link to Requirements")

*   MLflow 2.3
*   Any cluster with the Hugging Face `transformers` library installed can be used for batch inference. The `transformers` library comes preinstalled on Databricks Runtime 10.4 LTS ML and above. Many of the popular NLP models work best on GPU hardware, so you may get the best performance using recent GPU hardware unless you use a model specifically optimized for use on CPUs.

## Use Pandas UDFs to distribute model computation on a Spark cluster[​](#use-pandas-udfs-to-distribute-model-computation-on-a-spark-cluster "Direct link to Use Pandas UDFs to distribute model computation on a Spark cluster")

When experimenting with pre-trained models you can use [Pandas UDFs](https://docs.databricks.com/aws/en/udf/pandas) to wrap the model and perform computation on worker CPUs or GPUs. Pandas UDFs distribute the model to each worker.

You can also create a Hugging Face Transformers pipeline for machine translation and use a Pandas UDF to run the pipeline on the workers of a Spark cluster:

Python

    import pandas as pdfrom transformers import pipelineimport torchfrom pyspark.sql.functions import pandas_udfdevice = 0 if torch.cuda.is_available() else -1translation_pipeline = pipeline(task="translation_en_to_fr", model="t5-base", device=device)@pandas_udf('string')def translation_udf(texts: pd.Series) -> pd.Series:  translations = [result['translation_text'] for result in translation_pipeline(texts.to_list(), batch_size=1)]  return pd.Series(translations)

Setting the `device` in this manner ensures that GPUs are used if they are available on the cluster.

The Hugging Face pipelines for translation return a list of Python `dict` objects, each with a single key `translation_text` and a value containing the translated text. This UDF extracts the translation from the results to return a Pandas series with just the translated text. If your pipeline was constructed to use GPUs by setting `device=0`, then Spark automatically reassigns GPUs on the worker nodes if your cluster has instances with multiple GPUs.

To use the UDF to translate a text column, you can call the UDF in a `select` statement:

Python

    texts = ["Hugging Face is a French company based in New York City.", "Databricks is based in San Francisco."]df = spark.createDataFrame(pd.DataFrame(texts, columns=["texts"]))display(df.select(df.texts, translation_udf(df.texts).alias('translation')))

## Return complex result types[​](#return-complex-result-types "Direct link to Return complex result types")

Using Pandas UDFs you can also return more structured output. For example, in named-entity recognition, pipelines return a list of `dict` objects containing the entity, its span, type, and an associated score. While similar to the example for translation, the return type for the `@pandas_udf` annotation is more complex in the case of named-entity recognition.

You can get a sense of the return types to use through inspection of pipeline results, for example by running the pipeline on the driver.

In this example, use the following code:

Python

    from transformers import pipelineimport torchdevice = 0 if torch.cuda.is_available() else -1ner_pipeline = pipeline(task="ner", model="Davlan/bert-base-multilingual-cased-ner-hrl", aggregation_strategy="simple", device=device)ner_pipeline(texts)

To yield the annotations:

Python

    [[{'entity_group': 'ORG',   'score': 0.99933606,   'word': 'Hugging Face',   'start': 0,   'end': 12},  {'entity_group': 'LOC',   'score': 0.99967843,   'word': 'New York City',   'start': 42,   'end': 55}], [{'entity_group': 'ORG',   'score': 0.9996372,   'word': 'Databricks',   'start': 0,   'end': 10},  {'entity_group': 'LOC',   'score': 0.999588,   'word': 'San Francisco',   'start': 23,   'end': 36}]]

To represent this as a return type, you can use an `array` of `struct` fields, listing the `dict` entries as the fields of the `struct`:

Python

    import pandas as pdfrom pyspark.sql.functions import pandas_udf@pandas_udf('array<struct<word string, entity_group string, score float, start integer, end integer>>')def ner_udf(texts: pd.Series) -> pd.Series:  return pd.Series(ner_pipeline(texts.to_list(), batch_size=1))display(df.select(df.texts, ner_udf(df.texts).alias('entities')))

## Tune performance[​](#tune-performance "Direct link to Tune performance")

There are several key aspects to tuning performance of the UDF. The first is to use each GPU effectively, which you can adjust by changing the size of batches sent to the GPU by the Transformers pipeline. The second is to make sure the DataFrame is well-partitioned to utilize the entire cluster.

Finally, you may wish to cache the Hugging Face model to save model load time or ingress costs.

### Choose a batch size[​](#choose-a-batch-size "Direct link to Choose a batch size")

While the UDFs described above should work out-of-the box with a `batch_size` of 1, this may not use the resources available to the workers efficiently. To improve performance, tune the batch size to the model and hardware in the cluster. Databricks recommends trying various batch sizes for the pipeline on your cluster to find the best performance. Read more about [pipeline batching](https://huggingface.co/docs/transformers/main_classes/pipelines#pipeline-batching) and other [performance options](https://huggingface.co/docs/transformers/performance) in Hugging Face documentation.

Try finding a batch size that is large enough so that it drives the full GPU utilization but does not result in `CUDA out of memory` errors. When you receive `CUDA out of memory` errors during tuning, you need to start a new session to release the memory used by the model and data in the GPU.

Monitor GPU performance by viewing the live [cluster metrics](https://docs.databricks.com/aws/en/compute/clusters-manage#metrics) for a cluster, and choosing a metric, such as `gpu0-util` for GPU processor utilization or `gpu0_mem_util` for GPU memory utilization.

### Tune parallelism with stage-level scheduling[​](#tune-parallelism-with-stage-level-scheduling "Direct link to Tune parallelism with stage-level scheduling")

By default, Spark schedules one task per GPU on each machine. To increase parallelism, you can use stage-level scheduling to tell Spark how many tasks to run per GPU. For example, if you would like Spark to run two tasks per GPU, you can specify this in the following way:

Python

    from pyspark.resource import TaskResourceRequests, ResourceProfileBuildertask_requests = TaskResourceRequests().resource("gpu", 0.5)builder = ResourceProfileBuilder()resource_profile = builder.require(task_requests).buildrdd = df.withColumn('predictions', loaded_model(struct(*map(col, df.columns)))).rdd.withResources(resource_profile)

### Repartition data to use all available hardware[​](#repartition-data-to-use-all-available-hardware "Direct link to Repartition data to use all available hardware")

The second consideration for performance is making full use of the hardware in your cluster. Generally, a small multiple of the number of GPUs on your workers (for GPU clusters) or number of cores across the workers in your cluster (for CPU clusters) works well. Your input DataFrame may already have enough partitions to take advantage of the cluster's parallelism. To see how many partitions the DataFrame contains, use `df.rdd.getNumPartitions()`. You can repartition a DataFrame using `repartitioned_df = df.repartition(desired_partition_count)`.

### Cache the model in DBFS or on mount points[​](#cache-the-model-in-dbfs-or-on-mount-points "Direct link to Cache the model in DBFS or on mount points")

If you are frequently loading a model from different or restarted clusters, you may also wish to cache the Hugging Face model in the [DBFS root volume](https://docs.databricks.com/aws/en/dbfs/) or on [a mount point](https://docs.databricks.com/aws/en/dbfs/mounts). This can decrease ingress costs and reduce the time to load the model on a new or restarted cluster. To do this, set the `TRANSFORMERS_CACHE` environment variable in your code before loading the pipeline.

For example:

Python

    import osos.environ['TRANSFORMERS_CACHE'] = '/dbfs/hugging_face_transformers_cache/'

Alternatively, you can achieve similar results by logging the model to MLflow with the [MLflow `transformers` flavor](https://mlflow.org/docs/latest/models.html#transformers-transformers-experimental).

## Notebook: Hugging Face Transformers inference and MLflow logging[​](#notebook-hugging-face-transformers-inference-and-mlflow-logging "Direct link to Notebook: Hugging Face Transformers inference and MLflow logging")

To get started quickly with example code, this notebook is an end-to-end example for text summarization by using Hugging Face Transformers pipelines inference and MLflow logging.

#### Hugging Face Transformers pipelines inference notebook

## Additional resources[​](#additional-resources "Direct link to Additional resources")

You can fine-tune your Hugging Face model with the following guides:

*   [Prepare data for fine tuning Hugging Face models](https://docs.databricks.com/aws/en/machine-learning/train-model/huggingface/load-data)
*   [Fine-tune Hugging Face models for a single GPU](https://docs.databricks.com/aws/en/machine-learning/train-model/huggingface/fine-tune-model)

Learn more about [What are Hugging Face Transformers?](https://docs.databricks.com/aws/en/machine-learning/train-model/huggingface/)
