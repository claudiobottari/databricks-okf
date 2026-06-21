---
title: Reference solution for image applications | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/reference-solutions/images-etl-inference
ingestedAt: "2026-06-18T08:13:12.196Z"
---

Learn how to do distributed image model inference from reference solution notebooks using pandas UDF, PyTorch, and TensorFlow in a common configuration shared by many real-world image applications. This configuration assumes that you store many images in an object store and optionally have continuously arriving new images.

## Workflow for image model inferencing[​](#workflow-for-image-model-inferencing "Direct link to Workflow for image model inferencing")

Suppose you have several trained deep learning (DL) models for image classification and object detection—for example, MobileNetV2 for detecting human objects in user-uploaded photos to help protect privacy—and you want to apply these DL models to the stored images.

You might re-train the models and update previously computed predictions. However, it is both I/O-heavy and compute-heavy to load many images and apply DL models. Fortunately, the inference workload is embarrassingly parallel and in theory can be distributed easily. This guide walks you through a practical solution that contains two major stages:

1.  ETL images into a Delta table using Auto Loader
2.  Perform distributed inference using pandas UDF

## ETL images into a Delta table using Auto Loader[​](#etl-images-into-a-delta-table-using-auto-loader "Direct link to ETL images into a Delta table using Auto Loader")

For image applications, including training and inference tasks, Databricks recommends that you ETL images into a Delta table with the [Auto Loader](https://docs.databricks.com/aws/en/ingestion/cloud-object-storage/auto-loader/). The Auto Loader helps data management and automatically handles continuously arriving new images.

#### ETL image dataset into a Delta table notebook

## Perform distributed inference using pandas UDF[​](#perform-distributed-inference-using-pandas-udf "Direct link to Perform distributed inference using pandas UDF")

The following notebooks use PyTorch and TensorFlow tf.Keras to demonstrate the reference solution.

#### Distributed inference via Pytorch and pandas UDF notebook

#### Distributed inference via Keras and pandas UDF notebook

## Limitations: Image file sizes[​](#limitations-image-file-sizes "Direct link to Limitations: Image file sizes")

For large image files (average image size greater than 100 MB), Databricks recommends using the Delta table only to manage the metadata (list of file names) and loading the images from the object store using their paths when needed.
