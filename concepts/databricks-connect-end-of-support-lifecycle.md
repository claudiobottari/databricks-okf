---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9380673e05dd29a7b9beba7ac7df6189acb62ba1d08940c6b7e9647a7da24f36
  pageDirectory: concepts
  sources:
    - databricks-connect-usage-requirements-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-end-of-support-lifecycle
    - DCEL
  citations:
    - file: databricks-connect-usage-requirements-databricks-on-aws.md
title: Databricks Connect End-of-Support Lifecycle
description: Databricks Connect follows the Databricks Runtime support lifecycle policy; versions that have reached end-of-support should be upgraded to a currently supported version.
tags:
  - databricks
  - lifecycle
  - support
  - versioning
timestamp: "2026-06-19T09:49:58.452Z"
---

# Databricks Connect End-of-Support Lifecycle

**Databricks Connect End-of-Support Lifecycle** refers to the policy by which older versions of the Databricks Connect client library are declared end-of-support (EOS) and are no longer eligible for updates, bug fixes, or technical support. Users of EOS versions are strongly advised to upgrade to a currently supported version.

## Lifecycle Policy

Databricks Connect follows the same [support lifecycles](/concepts/databricks-runtime-support-lifecycles.md) as the Databricks Runtime. When a Databricks Runtime version reaches end-of-support, the corresponding Databricks Connect version (which is numbered to match the Databricks Runtime) also reaches end-of-support. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

## End-of-Support Versions

The Databricks documentation lists specific Databricks Connect versions that have reached end-of-support. Users of these versions will not receive new features, compatibility patches, or security updates. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

The exact set of EOS versions is version‑specific and is published in the Databricks Connect release notes and the requirements documentation.

## Recommendation

If you are using a version of Databricks Connect that has reached end-of-support, Databricks recommends upgrading to a [Databricks Connect versions|supported version](/concepts/databricks-connect-requirements.md). To upgrade, install the latest Databricks Connect package that matches your workspace’s Databricks Runtime version. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — The client library for connecting local IDEs to Databricks clusters and serverless compute.
- [Databricks Runtime Support Lifecycles](/concepts/databricks-runtime-support-lifecycles.md) — The overarching support policy that governs Databricks Connect EOS dates.
- [Databricks Connect versions](/concepts/databricks-connect.md) — The table of compatible Databricks Connect and language versions, including which versions are currently supported.
- Upgrade Databricks Connect — Instructions for migrating from an older to a newer Databricks Connect version.

## Sources

- databricks-connect-usage-requirements-databricks-on-aws.md

# Citations

1. [databricks-connect-usage-requirements-databricks-on-aws.md](/references/databricks-connect-usage-requirements-databricks-on-aws-a56357da.md)
