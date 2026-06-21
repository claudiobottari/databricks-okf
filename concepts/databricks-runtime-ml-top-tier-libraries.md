---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c2c88af51f8c85591ea887699d2302db33288a401d2c5e25b0904fcfdb4a1962
  pageDirectory: concepts
  sources:
    - databricks-runtime-ml-maintenance-policy-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-runtime-ml-top-tier-libraries
    - DRMTL
  citations:
    - file: databricks-runtime-ml-maintenance-policy-databricks-on-aws.md
title: Databricks Runtime ML Top-tier Libraries
description: A designated subset of pre-installed ML/DL libraries in Databricks Runtime ML that receive faster updates, advanced testing, and embedded optimizations.
tags:
  - databricks
  - machine-learning
  - library-management
timestamp: "2026-06-19T18:15:08.348Z"
---

```markdown
---
title: Databricks Runtime ML Top-Tier Libraries
summary: A curated subset of pre-installed ML/DL libraries in Databricks Runtime ML that receive faster updates, advanced support, testing, and embedded optimizations, updated with each runtime release barring dependency conflicts.
sources:
  - databricks-runtime-ml-maintenance-policy-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T09:54:35.757Z"
updatedAt: "2026-06-19T09:54:35.757Z"
tags:
  - databricks
  - machine-learning
  - library-management
aliases:
  - databricks-runtime-ml-top-tier-libraries
  - DRMTL
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Databricks Runtime ML Top-Tier Libraries

**Databricks Runtime ML Top-Tier Libraries** are a designated subset of pre-installed machine learning and deep learning libraries in [[Databricks Runtime ML]] that receive preferential support, faster updates, and embedded optimizations. Databricks defines and maintains this list to provide customers with a curated set of libraries for production-grade ML workloads. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

## Overview

Databricks Runtime ML ships with many popular ML and DL libraries. Among them, a subset is designated as **top-tier libraries**. For these libraries, Databricks provides:

- A **faster update cadence** – each runtime release updates them to the latest package releases, barring dependency conflicts. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]
- **Advanced support, testing, and embedded optimizations** specifically for the Databricks environment. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

Top-tier libraries are added or removed only with major runtime versions (e.g., Databricks Runtime 18.0 ML). ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

## Full List of Top-Tier Libraries

| Library | Description |
|---------|-------------|
| datasets | [Loading and processing datasets](https://docs.databricks.com/aws/en/machine-learning/train-model/huggingface/load-data) |
| GraphFrames | [Graph processing](https://docs.databricks.com/aws/en/integrations/graphframes/) |
| MLflow | [ML lifecycle management](https://docs.databricks.com/aws/en/mlflow/) |
| PyTorch | [Deep learning framework](https://docs.databricks.com/aws/en/machine-learning/train-model/pytorch) |
| Scikit-learn | [Classic ML library](https://docs.databricks.com/aws/en/machine-learning/train-model/scikit-learn) |
| streaming | [Streaming data ingestion](https://docs.databricks.com/aws/en/machine-learning/load-data/streaming) |
| TensorBoard | [Visualization toolkit](https://docs.databricks.com/aws/en/machine-learning/train-model/tensorboard) |
| transformers | [Hugging Face model library](https://docs.databricks.com/aws/en/machine-learning/train-model/huggingface/) |

**Note:** Starting with Databricks Runtime 18.0 ML, TensorFlow and spark-tensorflow-connector are no longer top-tier libraries. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

For a complete inventory of all libraries in each runtime version, see the Databricks Runtime ML release notes. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

## Library Deprecation and Removal Policy

### Top-Tier Status Removal

A library may be removed from the top-tier list in the following situations:

- **Inactivity** – no new commits in two months and no new releases in more than six months. It may be reinstated if active maintenance resumes. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]
- **Low usage** – if usage drops significantly. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]
- **Replacement** – if new packages fill major gaps and supersede the library. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

### Pre-Installed Library Removal

A library is removed from pre-installed status when it reaches any of the following conditions:

- No longer actively maintained (no new commits in three months and no new releases in more than nine months; the repository is archived; or maintenance is formally stopped). ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]
- No stable release is found to be functional for the new runtime. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

Before removal, Databricks notifies customers via:

- A deprecation warning in the runtime release notes. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]
- A notification when importing the library. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]
- Updates to Databricks documentation referencing the library. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

To continue using a removed library, you can either install it manually into your cluster or use an earlier Databricks Runtime ML version. ^[databricks-runtime-ml-maintenance-policy-databricks-on-aws.md]

## Related Concepts

- [[Databricks Runtime ML]] – the runtime that includes these libraries.
- Databricks Runtime ML maintenance policy – detailed policy for all libraries.
- [[MLflow]] – top-tier library for experiment tracking and model management.
- PyTorch, Scikit-learn, [[MLflow Transformers Flavor|transformers]] – popular top-tier deep learning and ML libraries.
- [[GraphFrames]], [[TensorBoard on Databricks|TensorBoard]], datasets, [[Mosaic Streaming|streaming]] – other top-tier libraries.
- TensorFlow – previously a top-tier library, removed as of Runtime 18.0 ML.
- Databricks Runtime ML release notes – official changelogs for each runtime version.

## Sources

- databricks-runtime-ml-maintenance-policy-databricks-on-aws.md
```

# Citations

1. [databricks-runtime-ml-maintenance-policy-databricks-on-aws.md](/references/databricks-runtime-ml-maintenance-policy-databricks-on-aws-f898bc32.md)
