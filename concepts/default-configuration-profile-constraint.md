---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ee2abc2ab4784ad3b8f8165effced6350249a54bf6f7f817433d9d90ed7cd806
  pageDirectory: concepts
  sources:
    - testing-for-databricks-connect-for-python-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - default-configuration-profile-constraint
    - DCPC
    - DEFAULT configuration profile
  citations:
    - file: testing-for-databricks-connect-for-python-databricks-on-aws.md
title: DEFAULT Configuration Profile Constraint
description: A constraint that pytest with Databricks Connect only works with the DEFAULT configuration profile, which must include the target cluster or serverless compute.
tags:
  - databricks
  - configuration
  - constraint
timestamp: "2026-06-19T23:06:34.794Z"
---

## DEFAULT Configuration Profile Constraint

The **DEFAULT Configuration Profile Constraint** is a restriction that applies when running pytest tests with [Databricks Connect](/concepts/databricks-connect.md) from the terminal. In this environment, `pytest` only operates correctly when using the **DEFAULT** [Configuration Profile](/concepts/databricks-configuration-profiles.md). ^[testing-for-databricks-connect-for-python-databricks-on-aws.md]

### Details

The DEFAULT configuration profile must include the Databricks compute resource that the test suite will use. This can be either a traditional cluster or Databricks Serverless Compute. If a different profile is specified or no DEFAULT profile exists, `pytest` will not function as expected when running from the terminal. ^[testing-for-databricks-connect-for-python-databricks-on-aws.md]

This constraint is specific to terminal-based `pytest` runs. Other workflows (such as running from a notebook or using a different test runner) may not have the same requirement. The constraint ensures that tests have a consistent, predictable configuration profile to connect to the Databricks environment.

### Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) – The client library that allows remote execution of Spark code.
- pytest – The testing framework used with [Databricks Connect](/concepts/databricks-connect.md).
- [Configuration Profile](/concepts/databricks-configuration-profiles.md) – A named set of connection and authentication settings for Databricks.
- Databricks Compute – The cluster or serverless compute resource used for execution.
- Databricks Serverless Compute – A serverless compute option for Databricks environments.

### Sources

- testing-for-databricks-connect-for-python-databricks-on-aws.md

# Citations

1. [testing-for-databricks-connect-for-python-databricks-on-aws.md](/references/testing-for-databricks-connect-for-python-databricks-on-aws-880303eb.md)
