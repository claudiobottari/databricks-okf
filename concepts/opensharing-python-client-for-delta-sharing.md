---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2a9a57df1787a37ec4cd9c049820565b747e27bb0abaf888f71d14acc0c0c5a0
  pageDirectory: concepts
  sources:
    - read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - opensharing-python-client-for-delta-sharing
    - OPCFDS
    - OpenSharing Python OSS Client
    - OpenSharing Python OSS client
  citations:
    - file: read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws.md
title: OpenSharing Python Client for Delta Sharing
description: The open-source Python library (delta-sharing >=1.3.1) used by non-Databricks recipients to list shared tables and read shared data via the SharingClient, configured with the oauth_config.share profile.
tags:
  - python-client
  - delta-sharing
  - opensharing
  - sdk
timestamp: "2026-06-19T20:10:35.538Z"
---

# OpenSharing Python Client for Delta Sharing

The **OpenSharing Python Client** is an open-source Python library that enables data recipients to read data shared through [Delta Sharing](/concepts/delta-sharing.md) from non-Databricks environments. It provides programmatic access to shared tables and supports OAuth 2.0 authentication flows for secure, short-lived credential exchange. ^[read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws.md]

## Overview

The OpenSharing Python OSS client is designed for scenarios where recipients do not have access to a [Unity Catalog](/concepts/unity-catalog.md)-enabled Databricks workspace. It allows applications, such as nightly jobs running on virtual machines, to autonomously access shared data using the OAuth Client Credentials grant flow (machine-to-machine or M2M). This approach eliminates the need for long-lived bearer tokens by using short-lived JSON Web Tokens (JWTs) issued by the recipient's identity provider (IdP). ^[read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws.md]

## Authentication

The client supports Open ID Connect (OIDC) Federation for authentication. In the M2M flow, an OAuth application registered in the recipient's IdP (for example, Microsoft Entra ID) authenticates with Databricks using the OAuth Client Credentials grant. The client reads credentials from an `oauth_config.share` profile file provided by the Databricks data provider. ^[read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws.md]

### Required Profile Fields

The `oauth_config.share` JSON file must contain the following fields:

| Field | Description |
|---|---|
| `shareCredentialsVersion` | Version identifier for the credentials format |
| `endpoint` | The Databricks Delta Sharing REST API endpoint URL |
| `tokenEndpoint` | The recipient IdP's OAuth 2.0 token endpoint |
| `type` | Always `oauth_client_credentials` for M2M flows |
| `clientId` | The client ID of the registered OAuth application |
| `clientSecret` | The client secret of the registered OAuth application |
| `scope` | The OAuth scope, typically `{clientId}/.default` |

^[read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws.md]

## Installation

Install the client using `pip`. A minimum version of 1.3.1 is required for OIDC federation support: ^[read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws.md]

```bash
python3 -m venv .venv
source .venv/bin/activate
pip3 install "delta-sharing>=1.3.1"
```

## Usage

After installing the library and configuring the `oauth_config.share` profile, the `delta_sharing.SharingClient` provides methods to list available tables and load data. ^[read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws.md]

### Creating a Client

```python
import delta_sharing

profile_file = "oauth_config.share"
client = delta_sharing.SharingClient(profile_file)
```

### Listing Shared Tables

```python
tables = client.list_all_tables()
print(tables)
```

### Reading Data as Pandas DataFrame

```python
table_url = profile_file + "#sample_share.sample_db.sample_table"
df = delta_sharing.load_as_pandas(table_url, limit=10)
print(df)
```

The `load_as_pandas()` function can fetch a sample of rows from a shared table that would not fit entirely in memory. ^[read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws.md]

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) — The open protocol for data sharing across platforms
- Open ID Connect (OIDC) Federation — Authentication mechanism using JWT tokens
- SharingClient — The core API object for interacting with shares
- [Unity Catalog](/concepts/unity-catalog.md) — Databricks’ unified governance solution
- M2M OAuth Flow — Machine-to-machine authentication pattern
- [OpenSharing](/concepts/opensharing.md) — The broader open sharing ecosystem

## Sources

- read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws.md

# Citations

1. [read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws.md](/references/read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws-cf8699ed.md)
