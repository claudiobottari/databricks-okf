---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 59a94148b01ccac49c7d5e123e9f29d2fce57909cbccb31d33f6509d40e128f2
  pageDirectory: concepts
  sources:
    - databricks-runtime-ml-maintenance-policy-databricks-on-aws.md
    - deep-learning-databricks-on-aws.md
    - tensorflow-databricks-on-aws.md
    - use-scikit-learn-on-databricks-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - databricks-runtime-ml
    - DRM
    - Databricks Runtime
    - Databricks Runtime 13.2 ML
    - Databricks Runtime 18.1
  citations:
    - file: databricks-runtime-ml-maintenance-policy-databricks-on-aws.md
    - file: deep-learning-databricks-on-aws.md
    - file: use-scikit-learn-on-databricks-databricks-on-aws.md
    - file: tensorflow-databricks-on-aws.md
title: Databricks Runtime ML
description: A Databricks runtime variant that includes pre-installed popular machine learning and deep learning libraries for ML workloads.
tags:
  - databricks
  - machine-learning
  - runtime
timestamp: "2026-06-19T18:15:35.618Z"
---

# Databricks Runtime ML

**Databricks Runtime ML** is a pre-configured version of Databricks Runtime that includes a curated set of popular machine learning and deep learning libraries. It provides a ready-to-use environment for developing, training, and deploying ML models on Databricks without requiring additional package installation. Libraries are updated with each release to include new features and fixes. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md, deep-learning-databricks-on-aws.md, use-scikit-learn-on-databricks-databricks-on-aws.md]

## Top-tier libraries

Databricks designates a subset of the supported libraries as *top-tier* libraries. For these libraries, Databricks provides a faster update cadence (updating to the latest package releases with each runtime release, barring dependency conflicts), advanced support, testing, and embedded optimizations. Top-tier libraries are added or removed only with major releases. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

The full list of top-tier libraries (as of the latest policy document) includes:

- [datasets](https://docs.databricks.com/aws/en/machine-learning/train-model/huggingface/load-data)
- [GraphFrames](https://docs.databricks.com/aws/en/integrations/graphframes/)
- [MLflow](https://docs.databricks.com/aws/en/mlflow/)
- [PyTorch](https://docs.databricks.com/aws/en/machine-learning/train-model/pytorch)
- [Scikit-learn](https://docs.databricks.com/aws/en/machine-learning/train-model/scikit-learn)
- [streaming](https://docs.databricks.com/aws/en/machine-learning/load-data/streaming)
- [TensorBoard](https://docs.databricks.com/aws/en/machine-learning/train-model/tensorboard)
- [transformers](https://docs.databricks.com/aws/en/machine-learning/train-model/huggingface/)

Starting with Databricks Runtime 18.0 ML, TensorFlow and spark-tensorflow-connector are no longer top-tier libraries. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

For a complete list of libraries included in each runtime version, see the release notes for Databricks Runtime ML. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

## PyTorch

PyTorch is included in Databricks Runtime ML and provides GPU‑accelerated tensor computation and high‑level functionalities for building deep learning networks. You can perform single‑node training or distributed training with PyTorch on Databricks. For an end‑to‑end tutorial notebook using PyTorch and MLflow, see the MLflow 3 deep learning workflow. ^[deep-learning-databricks-on-aws.md]

## TensorFlow

Databricks Runtime ML includes TensorFlow and TensorBoard, so you can use these libraries without installing any packages. TensorFlow supports deep‑learning and general numerical computations on CPUs, GPUs, and clusters of GPUs. TensorBoard provides visualization tools to help you debug and optimize machine learning and deep learning workflows. ^[deep-learning-databricks-on-aws.md, tensorflow-databricks-on-aws.md]

**Note:** The open‑source version of TensorFlow is not compatible with the latest CUDA versions. TensorFlow will be removed in the next major Databricks Runtime ML version. Databricks recommends you install your own versions as needed. ^[tensorflow-databricks-on-aws.md]

For distributed training options, see the distributed training documentation. Single‑node workflows can be tested using a Single Node cluster. ^[tensorflow-databricks-on-aws.md]

## scikit-learn

scikit-learn is one of the most popular Python libraries for single‑node machine learning and is included in Databricks Runtime and Databricks Runtime ML. It can be used for model training, hyperparameter tuning, and inference, and integrates with [MLflow](/concepts/mlflow.md) for tracking. Example notebooks demonstrate basic classification, end‑to‑end workflows with model registration, and distributed hyperparameter tuning with Optuna. ^[use-scikit-learn-on-databricks-databricks-on-aws.md]

## Track deep learning model development

Tracking remains a cornerstone of the [MLflow](/concepts/mlflow.md) ecosystem and is especially vital for the iterative nature of deep learning. Databricks uses MLflow to track deep learning training runs and model development. ^[deep-learning-databricks-on-aws.md]

## Library support policy

Databricks has designated a subset of supported libraries as top-tier libraries (see list above). For these libraries, Databricks provides a faster update cadence, updating to the latest package releases with each runtime release (barring dependency conflicts). Databricks also provides advanced support, testing, and embedded optimizations. Top-tier libraries are added or removed only with major releases. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

## Library deprecation policy

Databricks might remove a library from the top-tier list in the following situations:

- The library has no new commits in two months and no new releases in more than six months. (The library may be added back when active maintenance resumes.)
- Usage of the library drops significantly.
- New packages fill major gaps, replacing the library.

Databricks will remove a pre‑installed library when the library reaches any of the following conditions:

- It is no longer actively maintained (no new commits in three months and no new releases in more than nine months, the repository is archived, or maintenance is announced to stop).
- No stable release is found to be functional for the new runtime.

When a library is planned for removal, Databricks adds a deprecation warning in the runtime release notes, displays a notification when importing the library, and updates documentation that references the library. To continue using a library after removal, you can install it manually or use an earlier Databricks Runtime ML version. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

## Related Concepts

- Databricks Runtime — The base runtime environment that Databricks Runtime ML extends.
- [MLflow](/concepts/mlflow.md) — Tracking and model management integrated with Databricks Runtime ML.
- PyTorch — Deep learning framework included as a top-tier library.
- TensorFlow — Deep learning framework (currently deprecated in Databricks Runtime ML).
- scikit-learn — Classical machine learning library included in the runtime.
- [Optuna](/concepts/optuna.md) — Hyperparameter optimization tool used with scikit-learn.
- [Best Practices for Deep Learning on Databricks](/concepts/best-practices-for-deep-learning-on-databricks.md)
- [AI Runtime](/concepts/ai-runtime.md) — Serverless GPU compute for deep learning workloads.

## Sources

- databricks-runtime-ml-maintenance-policy-databricks-on-aws.md
- deep-learning-databricks-on-aws.md
- tensorflow-databricks-on-aws.md
- use-scikit-learn-on-databricks-databricks-on-aws.md

# Citations

1. [databricks-runtime-ml-maintenance-policy-databricks-on-aws.md](/references/databricks-runtime-ml-maintenance-policy-databricks-on-aws-f898bc32.md)
2. [deep-learning-databricks-on-aws.md](/references/deep-learning-databricks-on-aws-50a1d868.md)
3. [use-scikit-learn-on-databricks-databricks-on-aws.md](/references/use-scikit-learn-on-databricks-databricks-on-aws-a9e701f4.md)
4. [tensorflow-databricks-on-aws.md](/references/tensorflow-databricks-on-aws-9b7ef20f.md)
