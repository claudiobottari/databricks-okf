---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e72a85cc897b527d69e82a13add0fcf306be693c2bc13d6dd5a37662a69be93e
  pageDirectory: concepts
  sources:
    - grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sap-bdc-sdk
    - SBS
  citations:
    - file: grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md
title: SAP BDC SDK
description: A Python SDK (sap-bdc-connect-sdk) used to describe Delta Shares in Core Schema Notation for consumption by SAP BDC users.
tags:
  - sdk
  - python
  - sap-bdc
timestamp: "2026-06-19T10:45:58.374Z"
---

# SAP BDC SDK

The **SAP BDC SDK** (SAP Business Data Cloud Connect SDK) is a Python package available on PyPI that provides programmatic access to describe data shares in Core Schema Notation (CSN) for consumption by SAP Business Data Cloud (BDC) recipients. ^[grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md]

## Overview

The SAP BDC SDK is used as part of the data sharing workflow between Databricks and SAP Business Data Cloud. After granting an SAP BDC recipient access to a [Delta Sharing](/concepts/delta-sharing.md) share, you run a notebook that uses the SDK to describe the share in CSN format. This description enables SAP BDC users to read and understand the shared data assets. ^[grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md]

## Installation

The SDK is published as `sap-bdc-connect-sdk` on PyPI:

```
pip install sap-bdc-connect-sdk
```

^[grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md]

## Usage

The SDK is typically invoked from a Databricks notebook as part of the data publishing workflow. After the following prerequisites are met:

1. A connection exists between your Databricks workspace and the desired SAP BDC account (see [Create and manage the SAP BDC connector](/concepts/sap-bdc-connector.md)).
2. A share object exists with data assets to share with the SAP BDC recipient (see Create shares for OpenSharing).
3. The SAP BDC recipient has been granted access to the share.

You run a notebook that uses the SAP BDC SDK to describe the share. The exact notebook code is provided in the Databricks documentation under "Publish data share to SAP BDC notebook." ^[grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md]

## Requirements for Shared Data Assets

Any data asset shared with SAP BDC must have a primary key or identity column. You can meet this requirement either by:

- Adding a primary key constraint before sharing the table.
- Defining a primary key in the CSN schema when sharing to SAP BDC.

^[grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md]

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) — The open protocol used for sharing data with SAP BDC
- [OpenSharing](/concepts/opensharing.md) — Databricks' sharing interface where recipients are managed
- SAP Business Data Cloud (BDC) — The target system consuming the shared data
- [Core Schema Notation (CSN)](/concepts/core-schema-notation-csn.md) — The schema format used to describe shared data assets
- Create shares for OpenSharing — Prerequisite for using the SDK
- Databricks notebooks — The execution environment for SDK scripts

## Sources

- grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md

# Citations

1. [grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md](/references/grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws-7790bd51.md)
