---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 925662ebd9cc2010ca1af9579d31f30967cd6c29aded491b8a7a475a3afb99ef
  pageDirectory: concepts
  sources:
    - data-preparation-for-classification-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - large-dataset-sampling-in-automl
    - LDSIA
  citations:
    - file: data-preparation-for-classification-databricks-on-aws.md
    - file: data-preparation-for-regression-databricks-on-aws.md
title: Large Dataset Sampling in AutoML
description: How Databricks AutoML samples large datasets for classification and regression to fit within single-node memory constraints, using stratified sampling for classification.
tags:
  - databricks
  - automl
  - sampling
  - large-datasets
timestamp: "2026-06-19T09:43:08.848Z"
---

```markdown
---
title: Large Dataset Sampling in AutoML
summary: AutoML's automatic estimation of memory requirements and dataset sampling using PySpark's `sampleBy` (classification) or `sample` (regression) methods to fit models on single worker nodes.
sources:
  - data-preparation-for-classification-databricks-on-aws.md
  - data-preparation-for-regression-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:29:46.633Z"
updatedAt: "2026-06-19T15:00:00.000Z"
tags:
  - automl
  - sampling
  - large-datasets
  - pyspark
aliases:
  - large-dataset-sampling-in-automl
  - LDSIA
confidence: 1
provenanceState: merged
inferredParagraphs: 0
---

# Large Dataset Sampling in AutoML

**Large Dataset Sampling in AutoML** refers to the automatic down‑sampling that AutoML applies when a dataset is too large to fit into the memory of a single worker node during model training. Although AutoML distributes [[hyperparameter tuning]] trials across the worker nodes of a cluster, each individual model is trained on a single worker node. To avoid out‑of‑memory errors, AutoML estimates the memory required to load and train the dataset and, if necessary, samples the data before training. ^[data-preparation-for-classification-databricks-on-aws.md, data-preparation-for-regression-databricks-on-aws.md]

## How Sampling Works

AutoML performs sampling automatically when the dataset exceeds the memory capacity of a single worker. The sampling is transparent to the user — no manual configuration is required. The method used depends on the type of machine learning problem being solved. ^[data-preparation-for-classification-databricks-on-aws.md, data-preparation-for-regression-databricks-on-aws.md]

## Sampling Methods

### Classification

For classification problems, AutoML uses the PySpark `sampleBy` method to perform **stratified sampling**. This preserves the target label distribution in the sampled dataset, ensuring that rare classes remain proportionally represented. ^[data-preparation-for-classification-databricks-on-aws.md, data-preparation-for-regression-databricks-on-aws.md]

### Regression

For regression problems, AutoML uses the PySpark `sample` method, which performs a simple random sample without stratification. This is appropriate because regression targets are continuous and do not have discrete classes to preserve. ^[data-preparation-for-regression-databricks-on-aws.md, data-preparation-for-classification-databricks-on-aws.md]

## Relationship to Data Splitting

Sampling for memory management is distinct from the data splitting strategies AutoML uses to create train, validation, and test sets. While sampling reduces the overall dataset size for model training, data splitting divides the (possibly sampled) data into partitions. For classification problems, both sampling and splitting use stratified approaches to preserve class distributions. For regression, both use random approaches. ^[data-preparation-for-classification-databricks-on-aws.md, data-preparation-for-regression-databricks-on-aws.md]

## Related Concepts

- AutoML — The automated machine learning framework that handles sampling
- [[Hyperparameter Tuning]] — Distributed trials that run across cluster workers
- PySpark — The underlying computation engine used for sampling operations
- [[Data Classification|Classification]] — Problem type that uses stratified sampling
- [[AutoML Regress API|Regression]] — Problem type that uses random sampling
- Stratified Sampling — A sampling technique that preserves class proportions
- [[AutoML Data Preparation for Classification|Data Preparation for Classification]] — Related data preparation steps on AutoML
- Data Preparation for Regression — Related data preparation steps on AutoML
- [[Imbalanced Dataset Handling in AutoML|Imbalanced Dataset Support in AutoML]] — Complementary technique for handling class imbalance

## Sources

- data-preparation-for-classification-databricks-on-aws.md
- data-preparation-for-regression-databricks-on-aws.md
```

# Citations

1. [data-preparation-for-classification-databricks-on-aws.md](/references/data-preparation-for-classification-databricks-on-aws-23ffa2ac.md)
2. [data-preparation-for-regression-databricks-on-aws.md](/references/data-preparation-for-regression-databricks-on-aws-5e52b14c.md)
