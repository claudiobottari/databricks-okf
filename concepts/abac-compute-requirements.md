---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c1a5e219d2b1357c6b4f79367c191a23f2e983109da6017bf7a5201ba9aec8b9
  pageDirectory: concepts
  sources:
    - requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - abac-compute-requirements
    - ACR
    - compute requirements
    - Compute Requirements for ABAC Policies
    - Compute requirements for ABAC policies
  citations:
    - file: requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md
title: ABAC Compute Requirements
description: Compute types and runtime versions required to use attribute-based access control row filter and column mask policies in Unity Catalog
tags:
  - access-control
  - unity-catalog
  - compute
  - databricks
timestamp: "2026-06-19T20:13:42.036Z"
---

# ABAC Compute Requirements

**ABAC Compute Requirements** define the specific compute configurations and runtime versions needed to use [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) row filter and column mask policies within [Unity Catalog](/concepts/unity-catalog.md) on Databricks. These policies can only be applied when workloads run on supported compute infrastructure. ^[requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Supported Compute Configurations

To use ABAC policies, you must use one of the following compute configurations: ^[requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

- **Serverless compute** — Fully managed compute that supports ABAC policies natively.
- **Standard compute** on Databricks Runtime 16.4 or above.
- **Dedicated compute** on Databricks Runtime 16.4 or above, with [fine-grained access control filtering](/concepts/dynamic-views-for-fine-grained-access-control.md) enabled.

These configurations are the only ones capable of evaluating ABAC policies at query time. ^[requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Governed Tags

ABAC policies use **governed tags**, not ungoverned tags. Governed tags are defined at the account level with access controls that determine who can create, assign, and manage them. For full details, see the [governed tags documentation](/concepts/governed-tags-unity-catalog.md). After assigning or modifying a tag, it can take a few minutes for the change to take effect. ^[requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Access from Older Runtimes

Standard and dedicated compute on Databricks Runtime versions **earlier than 16.4** cannot access ABAC-secured tables. If certain workloads must continue running on an older runtime, you can scope the ABAC policy to a specific group using the `EXCEPT` clause rather than applying it broadly. Users outside the group retain full access to the underlying tables, allowing the older-runtime workload to continue while you transition to a supported runtime. ^[requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Related Concepts

- ABAC Limitations — Additional constraints and considerations for ABAC policy usage.
- [Unity Catalog](/concepts/unity-catalog.md) — The data governance platform where ABAC policies are defined.
- [Row Filters](/concepts/row-filter-policies.md) — ABAC policies that restrict which rows a user can see.
- Column Masks — ABAC policies that obfuscate column values for unauthorized users.
- [Delta Sharing](/concepts/delta-sharing.md) — How ABAC policies interact with shared data.
- [Compatibility Matrix](/concepts/feature-engineering-compatibility-matrix.md) — Full details on which runtimes support ABAC features.

## Sources

- requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md

# Citations

1. [requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md](/references/requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws-43ef91f3.md)
