---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6a61cf1c14cac92e58e9fea2bd5336df0897cf8c4e09b63cc7e0db2eb4db146e
  pageDirectory: concepts
  sources:
    - read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - credential-file-based-access-model
    - CFAM
  citations:
    - file: read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md
title: Credential File-Based Access Model
description: A security model where data providers share a credential file containing endpoints and bearer tokens, which recipients use to gain read access to shared datasets.
tags:
  - security
  - authentication
  - data-sharing
timestamp: "2026-06-19T20:10:49.782Z"
---

# Credential File-Based Access Model

The **Credential File-Based Access Model** is a security mechanism used in [OpenSharing](/concepts/opensharing.md) (Databricks-to-Open sharing) that provides secure read access to shared data through a credential file. In this model, a data provider shares a credential file with authorized recipients, who use it to authenticate and access shared datasets without needing direct access to the provider's underlying storage infrastructure. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

## How It Works

In the Databricks-to-Open sharing model, a member of the recipient team downloads the credential file shared by the data provider and distributes it through a secure channel to other team members who need access. The credential file contains the necessary authentication information, including the endpoint URL and bearer token, that clients use to connect to the shared data. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

Access persists as long as the credential is valid and the provider continues to share the data. Providers manage credential expiration and rotation. Recipients can read and make copies of the shared data but cannot modify the source data. Updates to the data are available in near real time. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

## Credential File Contents

The credential file contains the following key components:

- **Endpoint URL**: The server URL used to connect to the OpenSharing service.
- **Bearer Token**: An authentication token that grants access to the shared data.
- **Iceberg REST Catalog Endpoint**: For Iceberg client access, the credential file includes an `icebergEndpoint` with the format `<workspace-url>/api/2.0/delta-sharing/metastores/<metastore-id>/iceberg`. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

## Access Methods

### Databricks (Unity Catalog)

For workspaces enabled with [Unity Catalog](/concepts/unity-catalog.md), recipients can import the credential file using the Catalog Explorer UI. This creates a provider object without needing to store or specify the credential file directly. Users can then create catalogs from shares, use Unity Catalog access controls to grant permissions, and query shared data using standard Unity Catalog syntax. Rotated credentials can be applied to the existing provider object without recreating the catalog. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

### Apache Spark

For Spark 3.x and above, recipients install the `delta-sharing` Python connector and the Apache Spark connector. The credential file path is specified when loading data using the format `<profile-path>#<share-name>.<schema-name>.<table-name>`. The credential file must be accessible via an absolute path, which can refer to a cloud object or Unity Catalog volume. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

### Pandas

For `pandas` 0.25.3 and above, recipients install the `delta-sharing` Python connector and use the `load_as_pandas()` function with the credential file path to access shared data. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

### Power BI

For Power BI Desktop 2.99.621.0 and above, recipients use the OpenSharing connector available in the **Get Data** menu. The endpoint URL from the credential file is entered as the server URL, and the bearer token is used for authentication. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

### Tableau

For Tableau Desktop and Tableau Server 2024.1 and above, recipients download the OpenSharing Connector from Tableau Exchange and upload the credential file directly through the connector interface. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

### Iceberg Clients

External Iceberg clients such as Snowflake, Trino, Flink, and Spark can access shared data using the [Apache Iceberg REST Catalog API](/concepts/iceberg-rest-catalog-irc-protocol.md). The credential file provides the Iceberg REST Catalog endpoint and bearer token. Recipients configure a catalog integration using these credentials to create databases and query shared tables. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

## Credential Lifecycle

### Expiration and Rotation

Credentials have an expiration date determined by the data provider. When a credential expires or is compromised, the recipient must contact the provider to request a new credential. For Databricks recipients who imported the credential as a provider object in Unity Catalog, the new credential can be applied using the Databricks REST API without recreating the catalog. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

### Security Considerations

- Credential files must be shared through secure channels.
- The storage bucket and credential capabilities (scope, expiration, read vs. read/write) are determined by the provider.
- In Databricks-to-Open sharing, mounting an open share in a Secure Egress Gateway (SEG) workspace automatically allowlists the provider's bucket for outbound access. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

## Related Concepts

- [OpenSharing](/concepts/opensharing.md) — The open protocol for data sharing between Databricks and non-Databricks platforms
- [Delta Sharing](/concepts/delta-sharing.md) — The underlying technology for secure data sharing
- [Bearer Token Authentication](/concepts/bearer-token-authentication-for-delta-sharing.md) — The authentication mechanism used in credential files
- [Unity Catalog](/concepts/unity-catalog.md) — Databricks' governance solution that integrates with credential-based access
- [Apache Iceberg REST Catalog](/concepts/iceberg-rest-catalog-irc-protocol.md) — API standard for Iceberg client access to shared data

## Sources

- read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md

# Citations

1. [read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md](/references/read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws-9252dd38.md)
