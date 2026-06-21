---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 627c0b0d47599dcaf4dbd216ad050c66b508a0e57b228bb824e9ecad77406cb8
  pageDirectory: concepts
  sources:
    - databricks-runtime-for-machine-learning-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - top-tier-libraries-in-databricks-runtime-ml
    - TLIDRM
    - Pre-installed libraries in Databricks Runtime ML
  citations:
    - file: databricks-runtime-for-machine-learning-databricks-on-aws.md
title: Top-tier Libraries in Databricks Runtime ML
description: A subset of libraries designated for faster update cadence, advanced support, testing, and embedded optimizations, updated with each runtime release.
tags:
  - databricks
  - libraries
  - machine-learning
timestamp: "2026-06-19T18:14:42.234Z"
---

---
title: Top-tier Libraries in Databricks Runtime ML
summary: A designated subset of ML libraries in Databricks Runtime ML that receive faster update cadence, advanced support, testing, and embedded optimizations
sources:
  - databricks-runtime-for-machine-learning-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T15:09:44.453Z"
updatedAt: "2026-06-19T09:53:40.795Z"
tags:
  - machine-learning
  - libraries
  - databricks
aliases:
  - top-tier-libraries-in-databricks-runtime-ml
  - TLIDRM
confidence: 0.9
provenanceState: extracted
inferredParagraphs: 0
---

# Top-tier Libraries in Databricks Runtime ML

**Top-tier Libraries** are a subset of the supported machine learning (ML) and deep learning (DL) libraries in [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) (Databricks Runtime ML) that receive a higher level of support from Databricks, including a faster update cadence, advanced testing, and embedded performance optimizations. Databricks updates these libraries to the latest package releases with each runtime release, barring dependency conflicts. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

## Definition and Benefits

While Databricks Runtime ML includes many popular ML and DL libraries, a designated subset are classified as top-tier. For these libraries, Databricks provides: ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

- **Faster update cadence:** Top-tier libraries are updated to the latest package releases with each runtime release, provided there are no dependency conflicts. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]
- **Advanced support:** Databricks offers enhanced technical support for these libraries. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]
- **Testing and embedded optimizations:** Top-tier libraries undergo rigorous testing and include optimizations built into Databricks Runtime ML. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

## Lifecycle and Stability

The set of top-tier libraries is stable. New libraries are added or existing ones are removed only with major releases of Databricks Runtime ML. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

## Finding the Current List

For the full list of top-tier and other provided libraries for a specific version of Databricks Runtime ML, see the [release notes](https://docs.databricks.com/aws/en/release-notes/runtime/). ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

For information about library update frequency and deprecation schedules, see the Databricks Runtime ML maintenance policy. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

## Installing Additional Libraries

You can install additional libraries to create a custom environment for your notebook or compute resource: ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

- To make a library available for all notebooks running on a compute resource, create a cluster-scoped library. You can also use an init script to install libraries during compute creation. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]
- To install a library that is available only to a specific notebook session, use notebook-scoped Python libraries. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

## Related Concepts

- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) – The runtime that hosts these libraries.
- Databricks Runtime ML maintenance policy – Defines the update and deprecation cadence for all libraries.
- [Deep Learning on Databricks](/concepts/deep-learning-on-databricks.md) – Best practices for deep learning workflows.
- GPU Scheduling – Optimizing GPU utilization for training.

## Sources

- databricks-runtime-for-machine-learning-databricks-on-aws.md

# Citations

1. [databricks-runtime-for-machine-learning-databricks-on-aws.md](/references/databricks-runtime-for-machine-learning-databricks-on-aws-0de5727c.md)
