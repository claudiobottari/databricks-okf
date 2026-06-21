---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6517c010caafc555ae2e66979bd878d11b2a13f113e6b21efda06e1dc9f35e93
  pageDirectory: concepts
  sources:
    - limitations-with-databricks-connect-for-python-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-udf-custom-library-restriction-on-serverless-compute
    - DCUCLROSC
  citations:
    - file: limitations-with-databricks-connect-for-python-databricks-on-aws.md
title: Databricks Connect UDF Custom Library Restriction on Serverless Compute
description: On serverless compute with Databricks Connect for Runtime 16.3 and below, UDFs cannot include custom libraries.
tags:
  - databricks
  - limitations
  - udf
  - serverless
timestamp: "2026-06-19T19:12:21.792Z"
---

# Databricks Connect UDF Custom Library Restriction on Serverless Compute

The **Databricks Connect UDF Custom Library Restriction on Serverless Compute** is a limitation that prevents user-defined functions (UDFs) from using custom (third‑party) libraries when running through [Databricks Connect](/concepts/databricks-connect.md) on Serverless Compute. This restriction applies specifically to Databricks Connect for Python. ^[limitations-with-databricks-connect-for-python-databricks-on-aws.md]

## Scope

The restriction is in effect for Databricks Runtime **16.3 and below**. On these runtime versions, any UDF executed on a serverless compute endpoint cannot import or rely on libraries that are not part of the default Databricks runtime environment. ^[limitations-with-databricks-connect-for-python-databricks-on-aws.md]

## Impact

- UDFs that depend on custom Python packages (e.g., `pandas`, `numpy`, or any package installed via `%pip` or cluster libraries) will fail on serverless compute when invoked through Databricks Connect.
- The restriction applies to all UDF types: Pandas UDFs (vectorized UDFs), scalar UDFs, and grouped map UDFs.
- It does **not** affect UDFs run on classic clusters in Databricks Connect; only serverless compute is subject to this limitation.

## Workarounds

- For Databricks Runtime 16.3 and below, use classic compute (non‑serverless) clusters when your UDFs require custom libraries.
- Upgrade to a later Databricks Runtime version (if available) to check whether the restriction has been lifted. The documentation notes that this limitation applies to **16.3 and below**, implying that newer versions may have removed it.

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) – The client library that connects remote IDEs to Databricks clusters.
- Serverless Compute – The on‑demand compute model that automatically scales resources.
- User-Defined Functions (UDFs) – Custom functions that operate on DataFrame rows.
- Databricks Runtime – The versioned runtime environment for clusters and serverless compute.
- Limitations with Databricks Connect for Python – The full list of known limitations.

## Sources

- limitations-with-databricks-connect-for-python-databricks-on-aws.md

# Citations

1. [limitations-with-databricks-connect-for-python-databricks-on-aws.md](/references/limitations-with-databricks-connect-for-python-databricks-on-aws-334fca41.md)
