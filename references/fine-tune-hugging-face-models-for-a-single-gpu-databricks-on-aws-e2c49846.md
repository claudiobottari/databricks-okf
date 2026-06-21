---
title: Fine-tune Hugging Face models for a single GPU | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/train-model/huggingface/fine-tune-model
ingestedAt: "2026-06-18T08:13:28.851Z"
---

This article describes how to fine-tune a Hugging Face model with the Hugging Face `transformers` library on a single GPU. It also includes Databricks-specific recommendations for loading data from the lakehouse and logging models to MLflow, which enables you to use and govern your models on Databricks.

The Hugging Face `transformers` library provides the [Trainer](https://huggingface.co/docs/transformers/main_classes/trainer) utility and [Auto Model](https://huggingface.co/docs/transformers/model_doc/auto) classes that enable loading and fine-tuning Transformers models.

These tools are available for the following tasks with simple modifications:

*   Loading models to fine-tune.
*   Constructing the configuration for the Hugging Face Transformers Trainer utility.
*   Performing training on a single GPU.

See [What are Hugging Face Transformers?](https://docs.databricks.com/aws/en/machine-learning/train-model/huggingface/)

## Requirements[​](#requirements "Direct link to Requirements")

*   A single-node [cluster](https://docs.databricks.com/aws/en/compute/configure) with one GPU on the driver.
*   The GPU version of Databricks Runtime 13.0 ML and above.
    *   This example for fine-tuning requires the 🤗 Transformers, 🤗 Datasets, and 🤗 Evaluate packages which are included in Databricks Runtime 13.0 ML and above.
*   MLflow 2.3.
*   [Data prepared and loaded for fine-tuning a model with transformers](https://docs.databricks.com/aws/en/machine-learning/train-model/huggingface/load-data).

## Tokenize a Hugging Face dataset[​](#tokenize-a-hugging-face-dataset "Direct link to Tokenize a Hugging Face dataset")

Hugging Face Transformers models expect tokenized input, rather than the text in the downloaded data. To ensure compatibility with the base model, use an [AutoTokenizer](https://huggingface.co/docs/transformers/v4.26.1/en/autoclass_tutorial#autotokenizer) loaded from the base model. Hugging Face `datasets` allows you to directly apply the tokenizer consistently to both the training and testing data.

For example:

Python

    from transformers import AutoTokenizertokenizer = AutoTokenizer.from_pretrained(base_model)def tokenize_function(examples):    return tokenizer(examples["text"], padding=False, truncation=True)train_test_tokenized = train_test_dataset.map(tokenize_function, batched=True)

## Set up the training configuration[​](#set-up-the-training-configuration "Direct link to Set up the training configuration")

Hugging Face training configuration tools can be used to configure a [Trainer](https://huggingface.co/docs/transformers/main_classes/trainer). The Trainer classes require the user to provide:

*   Metrics
*   A base model
*   A training configuration

You can configure evaluation metrics in addition to the default `loss` metric that the `Trainer` computes. The following example demonstrates adding `accuracy` as a metric:

Python

    import numpy as npimport evaluatemetric = evaluate.load("accuracy")def compute_metrics(eval_pred):    logits, labels = eval_pred    predictions = np.argmax(logits, axis=-1)    return metric.compute(predictions=predictions, references=labels)

Use the [Auto Model classes for NLP](https://huggingface.co/docs/transformers/v4.26.1/en/model_doc/auto#natural-language-processing) to load the appropriate model for your task.

For text classification, use [AutoModelForSequenceClassification](https://huggingface.co/docs/transformers/v4.26.1/en/model_doc/auto#transformers.AutoModelForSequenceClassification) to load a base model for text classification. When creating the model, provide the number of classes and the label mappings created during dataset preparation.

Python

    from transformers import AutoModelForSequenceClassificationmodel = AutoModelForSequenceClassification.from_pretrained(        base_model,        num_labels=len(label2id),        label2id=label2id,        id2label=id2label        )

Next, create the training configuration. The [TrainingArguments](https://huggingface.co/docs/transformers/v4.26.1/en/main_classes/trainer#transformers.TrainingArguments) class allows you to specify the output directory, evaluation strategy, learning rate, and other parameters.

Python

    from transformers import TrainingArguments, Trainertraining_args = TrainingArguments(output_dir=training_output_dir, evaluation_strategy="epoch")

Using a [data collator](https://huggingface.co/docs/transformers/v4.26.1/en/main_classes/data_collator) batches input in training and evaluation datasets. [DataCollatorWithPadding](https://huggingface.co/docs/transformers/v4.26.1/en/main_classes/data_collator#transformers.DataCollatorWithPadding) gives good baseline performance for text classification.

Python

    from transformers import DataCollatorWithPaddingdata_collator = DataCollatorWithPadding(tokenizer)

With all of these parameters constructed, you can now create a `Trainer`.

Python

    trainer = Trainer(    model=model,    args=training_args,    train_dataset=train_test_dataset["train"],    eval_dataset=train_test_dataset["test"],    compute_metrics=compute_metrics,    data_collator=data_collator,)

## Train and log to MLflow[​](#train-and-log-to-mlflow "Direct link to Train and log to MLflow")

Hugging Face interfaces well with MLflow and automatically logs metrics during model training using the [MLflowCallback](https://huggingface.co/docs/transformers/main/en/main_classes/callback#transformers.integrations.MLflowCallback). However, you must log the trained model yourself.

Wrap training in an MLflow run. This constructs a Transformers pipeline from the tokenizer and the trained model, and writes it to local disk. Finally, log the model to MLflow with [mlflow.transformers.log\_model](https://mlflow.org/docs/latest/models.html#transformers-transformers-experimental).

Python

    from transformers import pipelinewith mlflow.start_run() as run:  trainer.train()  trainer.save_model(model_output_dir)  pipe = pipeline("text-classification", model=AutoModelForSequenceClassification.from_pretrained(model_output_dir), batch_size=1, tokenizer=tokenizer)  model_info = mlflow.transformers.log_model(        transformers_model=pipe,        artifact_path="classification",        input_example="Hi there!",    )

If you don't need to create a pipeline, you can submit the components that are used in training into a dictionary:

Python

    model_info = mlflow.transformers.log_model(  transformers_model={"model": trainer.model, "tokenizer": tokenizer},  task="text-classification",  artifact_path="text_classifier",  input_example=["MLflow is great!", "MLflow on Databricks is awesome!"],)

## Load the model for inference[​](#load-the-model-for-inference "Direct link to Load the model for inference")

When your model is logged and ready, loading the model for inference is the same as loading the MLflow wrapped pre-trained model.

Python

    logged_model = "runs:/{run_id}/{model_artifact_path}".format(run_id=run.info.run_id, model_artifact_path=model_artifact_path)# Load model as a Spark UDF. Override result_type if the model does not return double values.loaded_model_udf = mlflow.pyfunc.spark_udf(spark, model_uri=logged_model, result_type='string')test = test.select(test.text, test.label, loaded_model_udf(test.text).alias("prediction"))display(test)

See [Deploy models using Model Serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/) for more information.

## Troubleshoot common CUDA errors[​](#troubleshoot-common-cuda-errors "Direct link to Troubleshoot common CUDA errors")

This section describes common CUDA errors and guidance on how to resolve them.

### OutOfMemoryError: CUDA out of memory[​](#outofmemoryerror-cuda-out-of-memory "Direct link to OutOfMemoryError: CUDA out of memory")

When training large models, a common error you may encounter is the CUDA out of memory error.

Example:

Console

    OutOfMemoryError: CUDA out of memory. Tried to allocate 20.00 MiB (GPU 0; 14.76 GiB total capacity; 666.34 MiB already allocated; 17.75 MiB free; 720.00 MiB reserved in total by PyTorch) If reserved memory is >> allocated memory try setting max_split_size_mb to avoid fragmentation.  See documentation for Memory Management and PYTORCH_CUDA_ALLOC_CONF.

Try the following recommendations to resolve this error:

*   Reduce the batch size for training. You can reduce the `per_device_train_batch_size` value in [TrainingArguments](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.TrainingArguments).
    
*   Use lower precision training. You can set `fp16=True` in [TrainingArguments](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.TrainingArguments).
    
*   Use gradient\_accumulation\_steps in [TrainingArguments](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.TrainingArguments) to effectively increase overall batch size.
    
*   Use [8-bit Adam optimizer](https://huggingface.co/docs/transformers/main/en/perf_train_gpu_one#8bit-adam).
    
*   Clean up the GPU memory before training. Sometimes, GPU memory may be occupied by some unused code.
    
    Python
    
        from numba import cudadevice = cuda.get_current_device()device.reset()
    

### CUDA kernel errors[​](#cuda-kernel-errors "Direct link to CUDA kernel errors")

When running the training, you may get CUDA kernel errors.

Example:

Console

    CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect.For debugging, consider passing CUDA_LAUNCH_BLOCKING=1.

To troubleshoot:

*   Try running the code on CPU to see if the error is reproducible.
    
*   Another option is to get a better traceback by setting `CUDA_LAUNCH_BLOCKING=1`:
    
    Python
    
        import osos.environ["CUDA_LAUNCH_BLOCKING"] = "1"
    

## Notebook: Fine-tune text classification on a single GPU[​](#notebook-fine-tune-text-classification-on-a-single-gpu "Direct link to Notebook: Fine-tune text classification on a single GPU")

To get started quickly with example code, this example notebook provides an end-to-end example for fine-tuning a model for text classification. The subsequent sections of this article go into more detail around using Hugging Face for fine-tuning on Databricks.

#### Fine-tuning Hugging Face text classification models notebook

## Additional resources[​](#additional-resources "Direct link to Additional resources")

Learn more about Hugging Face on Databricks.

*   [What are Hugging Face Transformers?](https://docs.databricks.com/aws/en/machine-learning/train-model/huggingface/)
*   You can use Hugging Face Transformers models on Spark to scale out your NLP batch applications, see [Model inference using Hugging Face Transformers for NLP](https://docs.databricks.com/aws/en/archive/machine-learning/train-model/model-inference-nlp).
