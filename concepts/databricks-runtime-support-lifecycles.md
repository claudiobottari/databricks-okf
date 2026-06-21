---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1697ee0f951c788f5caeaf3319e9df4f5d544590c5ffb88874dc3d0348eb993d
  pageDirectory: concepts
  sources:
    - databricks-connect-usage-requirements-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-runtime-support-lifecycles
    - DRSL
    - Databricks Runtime support lifecycle
    - Support lifecycles
    - support lifecycles
  citations:
    - file: databricks-connect-usage-requirements-databricks-on-aws.md
title: Databricks Runtime Support Lifecycles
description: The policy that Databricks Connect follows Databricks Runtime support lifecycles, with end-of-support versions requiring upgrades to supported versions.
tags:
  - databricks
  - versioning
  - support-policy
timestamp: "2026-06-19T14:48:03.119Z"
---

Here is the wiki page for "Databricks Runtime Support Lifecycles".

---

## Databricks Runtime Support Lifecycles

**Databricks Runtime Support Lifecycles** define the period during which a specific Databricks Runtime version receives official support, including bug fixes, security patches, and maintenance updates from Databricks. Understanding these lifecycles is critical for planning upgrades, ensuring compatibility with tools like [Databricks Connect](/concepts/databricks-connect.md), and maintaining a compliant and secure production environment.

### Overview

Databricks Runtime versions follow a defined support lifecycle. After a version is released, it progresses through a support phase and eventually reaches an end-of-support (EOS) date. Databricks publishes a [Databricks Runtime support lifecycle](/concepts/databricks-runtime-support-lifecycles.md) policy that outlines the specific dates and phases for each major and minor release. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

### Implications for Databricks Connect

The [Databricks Connect](/concepts/databricks-connect.md) client library, which enables remote development from an IDE or local script, directly inherits the [support lifecycles](/concepts/databricks-runtime-support-lifecycles.md) of the Databricks Runtime it is designed to connect to. Specifically:

- **Version Compatibility**: Databricks Connect version numbers correspond to Databricks Runtime version numbers. A Databricks Connect version that has reached end-of-support is no longer compatible with new Databricks Runtime features or security updates. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

- **Upgrade Requirement**: If you are using a version of Databricks Connect that has reached end-of-support, you must upgrade to a supported version to continue receiving official support and to use features available in later Databricks Runtime releases. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

- **Runtime Version Constraint**: The Databricks Runtime version of your compute (cluster or serverless) must be greater than or equal to the Databricks Connect package version. Databricks recommends using the most recent Databricks Connect package that matches your Databricks Runtime version. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

### How to Determine Support Status

To check whether a specific Databricks Runtime version is still supported:

1.  Refer to the official Databricks Runtime release notes versions and compatibility page, which lists the support lifecycle for each version. ^[databricks-connect-usage-requirements-databricks-on-aws.md]
2.  For Databricks Connect specifically, see the Databricks Connect release notes for a list of available releases and their support status. ^[databricks-connect-usage-requirements-databricks-on-aws.md]

### Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) – A client library that connects local development environments to a Databricks cluster; its support lifecycle mirrors that of the Databricks Runtime.
- Databricks Runtime – The core compute engine that runs on Databricks clusters.
- [Databricks Runtime Version Compatibility](/concepts/databricks-runtime-version-compatibility.md) – Describes which Databricks Runtime versions work with which client tools.
- [Databricks Runtime support lifecycle](/concepts/databricks-runtime-support-lifecycles.md) – The official policy defining support phases and end-of-support dates.
- Upgrade a Databricks Runtime version – Guidance on how to migrate from one runtime version to another.

### Sources

- databricks-connect-usage-requirements-databricks-on-aws.md

# Citations

1. [databricks-connect-usage-requirements-databricks-on-aws.md](/references/databricks-connect-usage-requirements-databricks-on-aws-a56357da.md)
