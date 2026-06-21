---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 38ab51e1079a003cbac5850b2d04300e15de8f4d9da0fda0e0574fa3589b56e2
  pageDirectory: concepts
  sources:
    - data-preparation-for-classification-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - imbalanced-dataset-handling-in-automl
    - IDHIA
    - Imbalanced Dataset Support in AutoML
  citations:
    - file: data-preparation-for-classification-databricks-on-aws.md
title: Imbalanced Dataset Handling in AutoML
description: Techniques AutoML uses to address class imbalance in classification datasets, including downsampling majority classes and applying class weights.
tags:
  - machine-learning
  - automl
  - classification
  - imbalanced-data
timestamp: "2026-06-19T18:05:19.040Z"
---

# Imbalanced Dataset Handling in AutoML

**Imbalanced Dataset Handling in AutoML** refers to the automatic techniques employed by [AutoML for Classification](/concepts/automl-classification-classify.md) to mitigate skewed class distributions in training data. Starting with Databricks Runtime 11.3 LTS ML, AutoML automatically detects imbalanced datasets and applies a combination of downsampling and class weight adjustments to improve model training while preserving the integrity of evaluation datasets. ^[data-preparation-for-classification-databricks-on-aws.md]

## Detection Mechanism

AutoML automatically identifies whether a classification dataset exhibits class imbalance. When detected, the system intervenes by modifying only the training dataset to reduce the imbalance. The test and validation datasets remain untouched throughout this process, ensuring that model performance evaluations reflect the true input class distribution of the original data. ^[data-preparation-for-classification-databricks-on-aws.md]

## Downsampling Strategy

To address class imbalance, AutoML downsamples the majority class(es) while leaving minority classes unchanged. The downsampling ratio is determined automatically based on the dataset's characteristics. For example, in a training dataset with 100 samples where 95 belong to class A and 5 belong to class B, AutoML may downsample class A to 70 samples, achieving a downsampling ratio of 70/95 (approximately 0.736). Class B remains at 5 samples. ^[data-preparation-for-classification-databricks-on-aws.md]

## Class Weight Adjustment

Following downsampling, AutoML applies class weights to compensate for the altered class distribution. These weights are inversely related to the degree of downsampling applied to each class. The weight for the downsampled majority class is scaled up by the inverse of its downsampling ratio to ensure proper calibration. In the example above, class A receives a weight of 1/0.736 (approximately 1.358), while class B retains a weight of 1. AutoML uses these class weights as parameters during model training to ensure appropriate weighting of samples from each class. ^[data-preparation-for-classification-databricks-on-aws.md]

## Purpose and Benefits

The primary goal of this handling is to ensure that the final model is correctly calibrated and that the probability distribution of the model output matches that of the input data. By balancing only the training dataset and not the test or validation datasets, AutoML ensures that model performance evaluation always occurs on a non-enriched dataset that accurately represents the true input class distribution. ^[data-preparation-for-classification-databricks-on-aws.md]

## Availability

The imbalanced dataset handling feature is available in Databricks Runtime 11.3 LTS ML and above. It applies automatically for classification problems and requires no manual configuration from users. ^[data-preparation-for-classification-databricks-on-aws.md]

## Related Concepts

- Class Imbalance — A condition where classes in a dataset are not represented equally
- Downsampling — A technique for reducing the number of samples from a majority class
- Class Weight — A method for weighting samples in loss functions during model training
- Model Calibration — The process of ensuring predicted probabilities match true class proportions
- Stratified Sampling — A sampling technique that preserves class distributions
- [AutoML for Classification](/concepts/automl-classification-classify.md) — The broader automated machine learning pipeline for classification tasks

## Sources

- data-preparation-for-classification-databricks-on-aws.md

# Citations

1. [data-preparation-for-classification-databricks-on-aws.md](/references/data-preparation-for-classification-databricks-on-aws-23ffa2ac.md)
