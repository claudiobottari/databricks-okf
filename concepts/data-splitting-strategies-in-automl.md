---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 448fd03c5c1860ffeb229b266535251182fba23edb3c617b9ce90bacc9d401f7
  pageDirectory: concepts
  sources:
    - data-preparation-for-classification-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - data-splitting-strategies-in-automl
    - DSSIA
    - Split Strategies in AutoML
    - Data Splitting in AutoML
  citations:
    - file: data-preparation-for-classification-databricks-on-aws.md
title: Data Splitting Strategies in AutoML
description: Methods for splitting data into training, validation, and test sets, including random split, chronological split, and manual split options.
tags:
  - machine-learning
  - automl
  - data-splitting
timestamp: "2026-06-19T18:05:57.082Z"
---

# Data Splitting Strategies in AutoML

**Data Splitting Strategies in AutoML** refers to the methods by which automated machine learning (AutoML) systems partition a dataset into training, validation, and test subsets. Proper data splitting is essential for unbiased model evaluation, hyperparameter tuning, and preventing data leakage.

## Standard Split Methods

AutoML supports three primary strategies for dividing data into training, validation, and test sets:

### 1. Random Split (Default)

If no data split strategy is specified, AutoML uses a **random split** by default. The dataset is randomly divided into **60% train split, 20% validate split, and 20% test split**. ^[data-preparation-for-classification-databricks-on-aws.md]

For **classification** problems, AutoML applies a **stratified random split** to ensure that each class is adequately represented in all three splits — training, validation, and test. This preserves the original class distribution and prevents a class from being absent in one split entirely. ^[data-preparation-for-classification-databricks-on-aws.md]

### 2. Chronological Split

Available in **Databricks Runtime 10.4 LTS ML and above**, chronological splitting uses a **time column** to create ordered train, validate, and test splits. ^[data-preparation-for-classification-databricks-on-aws.md]

- **Training**: uses the **earliest** data points
- **Validation**: uses the **next earliest** data points
- **Testing**: uses the **latest** data points

The time column can be a **timestamp, integer, or string** column. This method is particularly useful for time series forecasting and other scenarios where temporal ordering matters (e.g., predicting future events from past observations). ^[data-preparation-for-classification-databricks-on-aws.md]

### 3. Manual Split

Available in **Databricks Runtime 15.3 ML and above**, users can set up a **manual split** via the API. This approach requires specifying a split column with the values `train`, `validate`, or `test` to identify which rows belong to which dataset. ^[data-preparation-for-classification-databricks-on-aws.md]

Any rows with split column values other than `train`, `test`, or `validate` are **ignored**, and a corresponding alert is raised. This method gives users explicit control over which data points go into each partition. ^[data-preparation-for-classification-databricks-on-aws.md]

## Supported Data Feature Types

AutoML classification only supports the following feature types for splitting and modeling:
- Numeric (`ByteType`, `ShortType`, `IntegerType`, `LongType`, `FloatType`, `DoubleType`)
- Boolean
- String (categorical or English text)
- Timestamps (`TimestampType`, `DateType`)
- `ArrayType[Numeric]` (Databricks Runtime 10.4 LTS ML and above)
- `DecimalType` (Databricks Runtime 11.3 LTS ML and above)

Images are **not** supported as feature types. ^[data-preparation-for-classification-databricks-on-aws.md]

## Imbalanced Dataset Handling

When AutoML detects an **imbalanced dataset** (in Databricks Runtime 11.3 LTS ML and above), it attempts to reduce imbalance **only in the training dataset** by:
1. **Downsampling** the major class(es)
2. Adding **class weights**

The test and validation datasets remain **unbalanced**, ensuring that model performance is evaluated on the **true input class distribution**. ^[data-preparation-for-classification-databricks-on-aws.md]

**Example of class weighting behavior:** Given a training dataset with 100 samples (95 class A, 5 class B), AutoML may downsample class A to 70 samples (ratio 70/95 = 0.736). To compensate, it scales the class weight for class A by **1/0.736 ≈ 1.358**, while keeping class B weight at 1. These weights are used during model training to ensure proper calibration. ^[data-preparation-for-classification-databricks-on-aws.md]

## Sampling Large Datasets

Although AutoML distributes hyperparameter tuning trials across worker nodes, **each model is trained on a single worker node**. AutoML automatically estimates the memory required and samples the dataset if necessary.

- **Classification**: uses PySpark `sampleBy` for **stratified sampling** to preserve target label distribution
- **Regression**: uses PySpark `sample` for simple random sampling

## Related Concepts

- Train-Test Split — General concept of splitting data for evaluation
- Data Leakage — How improper splitting can bias results
- Stratified Sampling — Preserving class proportions across splits
- [Time Series Cross-Validation](/concepts/time-series-cross-validation.md) — Alternative validation methods for temporal data
- Class Imbalance — Techniques for handling skewed target distributions
- AutoML — Overview of automated machine learning pipelines

## Sources

- data-preparation-for-classification-databricks-on-aws.md

# Citations

1. [data-preparation-for-classification-databricks-on-aws.md](/references/data-preparation-for-classification-databricks-on-aws-23ffa2ac.md)
