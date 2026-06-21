---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7f76433928f3aad39441edb8b8b3d623bb209e6cfa6e8ca30e250e765f6a9f54
  pageDirectory: concepts
  sources:
    - databricks-connect-usage-requirements-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-runtime-support-lifecycles-for-databricks-connect
    - DRSLFDC
  citations:
    - file: databricks-connect-usage-requirements-databricks-on-aws.md
title: Databricks Runtime Support Lifecycles for Databricks Connect
description: End-of-support policy where Databricks Connect versions follow Databricks Runtime support lifecycles, requiring upgrades when versions reach end-of-support.
tags:
  - databricks
  - versioning
  - lifecycle
timestamp: "2026-06-19T18:11:11.536Z"
---

## Databricks Runtime Support Lifecycles for Databricks Connect

**Databricks Connect** follows the same [Databricks Runtime Support Lifecycles](/concepts/databricks-runtime-support-lifecycles.md) as the corresponding Databricks Runtime version. This means that when a Databricks Runtime version reaches end‑of‑support (EOS), the matching Databricks Connect version also reaches EOS and is no longer supported. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

### Support Lifecycle

Databricks Connect version numbers correspond directly to Databricks Runtime version numbers. For example, Databricks Connect 13.3 LTS maps to Databricks Runtime 13.3 LTS. The support lifecycle—including the phases of preview, general availability, and end‑of‑support—is identical for both the runtime and its Databricks Connect counterpart. The full lifecycle details are published in the Databricks Runtime support lifecycles documentation. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

### End‑of‑Support Versions

Versions of Databricks Connect that have reached end‑of‑support are listed in the version compatibility table on the usage requirements page. If you are using a version that has reached EOS, you should upgrade to a supported version. Databricks recommends that you use the most recent Databricks Connect package that matches your Databricks Runtime version. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

### Compatibility Requirements

To use Databricks Connect, the Databricks Runtime version of your compute (cluster or serverless compute) must be greater than or equal to the Databricks Connect package version. This ensures that features available in the runtime are also available through the client library. For features in later runtime versions, you must upgrade the Databricks Connect package. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

### Related Concepts

- [Databricks Connect usage requirements](/concepts/databricks-connect-usage-requirements.md)
- Databricks Runtime release notes
- Databricks Connect release notes
- [Serverless compute support for Databricks Connect](/concepts/serverless-compute-with-databricks-connect.md)
- Cluster access modes for Databricks Connect

### Sources

- databricks-connect-usage-requirements-databricks-on-aws.md

# Citations

1. [databricks-connect-usage-requirements-databricks-on-aws.md](/references/databricks-connect-usage-requirements-databricks-on-aws-a56357da.md)
