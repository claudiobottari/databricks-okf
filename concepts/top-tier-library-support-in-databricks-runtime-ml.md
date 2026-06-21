---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0584c58fd9663ca9b28ef1686462605a3cea458e8dc402c273e7372048e9e282
  pageDirectory: concepts
  sources:
    - databricks-runtime-for-machine-learning-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - top-tier-library-support-in-databricks-runtime-ml
    - TLSIDRM
  citations:
    - file: databricks-runtime-for-machine-learning-databricks-on-aws.md
title: Top-Tier Library Support in Databricks Runtime ML
description: A subset of ML libraries in Databricks Runtime ML that receive faster update cadence, advanced support, testing, and embedded optimizations from Databricks.
tags:
  - databricks
  - libraries
  - machine-learning
timestamp: "2026-06-18T11:41:15.111Z"
---

# Top-Tier Library Support in Databricks Runtime ML

**Databricks Runtime for Machine Learning** (Databricks Runtime ML) provides a curated set of machine learning and deep learning libraries that are pre-installed and optimized for use on Databricks compute resources. A subset of these libraries is designated as **top-tier** by Databricks, receiving a faster update cadence, advanced support, testing, and embedded optimizations compared to other provided libraries. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

## Top-Tier Library Designation

Databricks designates a subset of the supported libraries in Databricks Runtime ML as top-tier libraries. For these libraries, Databricks provides:

- **Faster update cadence:** Top-tier libraries are updated to the latest package releases with each runtime release, barring dependency conflicts.
- **Advanced support:** Databricks provides enhanced support and troubleshooting for top-tier libraries.
- **Testing and optimizations:** Top-tier libraries undergo additional testing and may include embedded performance optimizations.

Top-tier libraries are added or removed only with major runtime releases. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

## Benefits of Top-Tier Library Support

The top-tier designation indicates that Databricks has committed significant engineering resources to ensure these libraries work optimally within the Databricks Runtime ML environment. Benefits include:

- **Regular updates:** Top-tier libraries are refreshed with each Databricks Runtime ML version, keeping them current with upstream releases.
- **Compatibility testing:** These libraries are tested for compatibility with other components of the runtime, including Spark, Photon, and [Unity Catalog](/concepts/unity-catalog.md).
- **Performance tuning:** Certain top-tier libraries may include Databricks-specific optimizations that improve performance on Databricks infrastructure.

^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

## List of Top-Tier Libraries

For the complete and current list of top-tier libraries included in each Databricks Runtime ML version, see the [release notes](https://docs.databricks.com/aws/en/release-notes/runtime/) for the specific runtime version. The release notes document which libraries are designated as top-tier for each release. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

## Using Top-Tier Libraries

When you create a compute resource using Databricks Runtime ML by selecting the **Machine learning** checkbox in the create compute UI, top-tier libraries are automatically available for use. The runtime also includes many other non-top-tier libraries for broader machine learning and deep learning workflows. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

### Installing Additional Libraries

If you need libraries not included in Databricks Runtime ML, you can install them:

- **Compute-scoped libraries:** Make a library available for all notebooks running on a compute resource.
- **Notebook-scoped Python libraries:** Install libraries that are available only to a specific notebook session.

^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

## Maintenance Policy

Databricks follows a Databricks Runtime ML maintenance policy that defines how often libraries are updated and when they are deprecated. Top-tier libraries generally receive more frequent updates and longer support periods than other libraries in the runtime. ^[databricks-runtime-for-machine-learning-databricks-on-aws.md]

## Related Concepts

- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) — The runtime environment that includes top-tier libraries
- Databricks Runtime ML maintenance policy — The policy governing library update and deprecation schedules
- Libraries included in Databricks Runtime ML — The full list of libraries provided with each runtime version
- [Compute-scoped libraries](/concepts/compute-scoped-vs-notebook-scoped-library-installation.md) — Method for installing additional libraries on a compute resource
- [Notebook-scoped Python libraries](/concepts/compute-scoped-vs-notebook-scoped-library-installation.md) — Method for installing libraries within a notebook session
- [Init scripts](/concepts/init-script-allowlisting.md) — Alternative method for library installation during compute creation
- Photon — Performance engine that may not benefit all library types

## Sources

- databricks-runtime-for-machine-learning-databricks-on-aws.md

# Citations

1. [databricks-runtime-for-machine-learning-databricks-on-aws.md](/references/databricks-runtime-for-machine-learning-databricks-on-aws-0de5727c.md)
