---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ef9686892684f828530dae3acd1bd713b6cbb8b05d4ac4a62c45e691f5c28bc6
  pageDirectory: concepts
  sources:
    - restrict-opensharing-recipient-access-using-ip-access-lists-databricks-to-open-sharing-databricks-on-aws.md
    - what-is-opensharing-databricks-on-aws.md
    - what-is-the-opensharing-databricks-to-open-sharing-protocol-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - databricks-to-open-sharing-protocol
    - DSP
  citations:
    - file: what-is-the-opensharing-databricks-to-open-sharing-protocol-databricks-on-aws.md
    - file: what-is-opensharing-databricks-on-aws.md
    - file: restrict-opensharing-recipient-access-using-ip-access-lists-databricks-to-open-sharing-databricks-on-aws.md
title: Databricks-to-Open Sharing Protocol
description: Delta Sharing protocol variant on Databricks that enables data providers to share data with recipients using the open-source Delta Sharing standard, supporting features like IP access lists and SecureConnect.
tags:
  - delta-sharing
  - databricks
  - protocol
timestamp: "2026-06-19T20:14:46.985Z"
---

# Databricks-to-Open Sharing Protocol

The **Databricks-to-Open Sharing Protocol** is one of the three sharing models in [OpenSharing](/concepts/opensharing.md) that allows a data provider using a [Unity Catalog](/concepts/unity-catalog.md)-enabled Databricks workspace to share tabular data with any user on any computing platform, regardless of whether the recipient uses Databricks. It is designed for providers who manage data in Unity Catalog and want to share with external organizations that do not have access to a Unity Catalog–enabled Databricks workspace. ^[what-is-the-opensharing-databricks-to-open-sharing-protocol-databricks-on-aws.md] ^[what-is-opensharing-databricks-on-aws.md]

## Comparison with Other Sharing Models

OpenSharing offers three distinct sharing approaches. The Databricks-to-Open protocol is the recommended choice when the recipient is not a Databricks user or does not have a Unity Catalog–enabled workspace. It uses the built-in OpenSharing server on the provider side, simplifying setup and governance for the provider. The other two approaches are the [Databricks-to-Databricks Sharing Protocol](/concepts/databricks-to-databricks-sharing.md) (for sharing with other Unity Catalog–enabled Databricks workspaces) and a customer-managed open-source OpenSharing server (for sharing from any platform to any platform). ^[what-is-opensharing-databricks-on-aws.md] ^[what-is-the-opensharing-databricks-to-open-sharing-protocol-databricks-on-aws.md]

## Workflow

The Databricks-to-Open sharing workflow follows these high-level steps:

1. **Create a recipient**: The provider creates a recipient object that represents the external user or group. This step sets up authentication, either via a long-lived bearer token or OpenID Connect (OIDC) federation. ^[what-is-the-opensharing-databricks-to-open-sharing-protocol-databricks-on-aws.md]
2. **Create a share**: The provider creates a share, a named collection of tables (in Delta format) registered in the Unity Catalog [Metastore](/concepts/metastore.md). ^[what-is-the-opensharing-databricks-to-open-sharing-protocol-databricks-on-aws.md]
   - Only tabular data in [Delta Lake](/concepts/delta-lake.md) or managed Iceberg tables can be shared. Assets such as notebooks, volumes, and models are not supported in the Databricks-to-Open protocol; they require the Databricks-to-Databricks protocol. ^[what-is-opensharing-databricks-on-aws.md]
3. **Grant access**: The provider grants the recipient access to the share. ^[what-is-the-opensharing-databricks-to-open-sharing-protocol-databricks-on-aws.md]
4. **Send connection information**:
   - In the bearer token flow, the provider sends an activation link over a secure channel. The recipient uses the link to download a credential file containing the bearer token and endpoint details. ^[what-is-the-opensharing-databricks-to-open-sharing-protocol-databricks-on-aws.md]
   - In the OIDC federation flow, the provider sends a portal URL; the recipient authenticates through their own identity provider. ^[what-is-opensharing-databricks-on-aws.md]
5. **Access the data**: The recipient uses the credential file (bearer token) or IdP (OIDC) to read the shared data using any compatible tool (e.g., Apache Spark, pandas, Power BI). Data is read-only and updates from the provider appear in near real time. ^[what-is-opensharing-databricks-on-aws.md] ^[what-is-the-opensharing-databricks-to-open-sharing-protocol-databricks-on-aws.md]

## Authentication Methods

### Bearer Token Authentication

The provider generates a long-lived bearer token and shares it via an activation link. The link allows the recipient to download a credential file (e.g., a `.json` configuration file) that contains the token and the OpenSharing server endpoint. Providers can configure a default token lifetime when enabling OpenSharing on their [Metastore](/concepts/metastore.md) and can modify it later. Tokens should be managed securely; they can be rotated or revoked on demand. ^[what-is-the-opensharing-databricks-to-open-sharing-protocol-databricks-on-aws.md] ^[what-is-opensharing-databricks-on-aws.md]

### OpenID Connect (OIDC) Federation

With OIDC federation, no bearer token is issued. Instead, the recipient’s identity provider (IdP) issues JWT tokens that Databricks exchanges for short-lived Databricks OAuth tokens. The provider creates a policy that dictates which IdP claims are accepted. This approach avoids long-lived secrets and is suitable for user-to-machine (U2M) and machine-to-machine (M2M) flows. ^[what-is-opensharing-databricks-on-aws.md] ^[what-is-the-opensharing-databricks-to-open-sharing-protocol-databricks-on-aws.md]

## Security and Access Control

### IP Access Lists

Providers can assign an IP access list to a recipient, restricting access to a predefined set of IP addresses or CIDR ranges. The list is independent of workspace-level IP access lists and only supports allow‑list entries. It controls access to the OpenSharing OSS Protocol REST API, the activation URL, and the credential file download. If the provider has [SecureConnect](/concepts/secureconnect.md) enabled, the IP access list also enforces access to shared data storage; without SecureConnect, storage URLs are reachable from any client IP regardless of the list. Each recipient can have a maximum of 100 IP/CIDR values (IPv4 only). ^[restrict-opensharing-recipient-access-using-ip-access-lists-databricks-to-open-sharing-databricks-on-aws.md]

Audit logs are generated for recipient management operations (create, update) and for any denied access to the OpenSharing REST API, activation URL, or credential file download. ^[restrict-opensharing-recipient-access-using-ip-access-lists-databricks-to-open-sharing-databricks-on-aws.md]

### Cloud Tokens and Directory-Based Access

When sharing eligible Delta tables, Databricks can return temporary cloud credentials (cloud tokens) that allow recipients to read data directly from cloud storage using directory-based access. This is enabled by default for newly shared assets that meet eligibility criteria. If a table does not meet all requirements, the fallback is pre‑signed URL access. ^[what-is-the-opensharing-databricks-to-open-sharing-protocol-databricks-on-aws.md]

### Token Security Considerations

Because the Databricks-to-Open protocol relies on tokens that must be exchanged outside the Databricks platform, providers should:
- Configure tokens to expire and set an appropriate lifetime.
- Encourage recipients to store credential files securely.
- Rotate tokens regularly and revoke them immediately if compromised.
- Use [Databricks-to-Databricks Sharing](/concepts/databricks-to-databricks-sharing.md) if token-based authentication is undesirable. ^[what-is-the-opensharing-databricks-to-open-sharing-protocol-databricks-on-aws.md] ^[what-is-opensharing-databricks-on-aws.md]

## Limitations

- Only tabular data in Delta or managed Iceberg format can be shared; notebooks, volumes, and models are not supported.
- Some Delta features (e.g., liquid clustering with partition filtering, collations, row filters, column masks, `SHALLOW CLONE` tables) are not supported.
- Recipients using pre‑signed URLs have direct cloud storage access during the URL’s short lifetime.
- Providers cannot share managed Iceberg tables to external Iceberg clients. ^[what-is-opensharing-databricks-on-aws.md]

## Cost and Egress

OpenSharing does not require data replication, so egress costs may apply when sharing across clouds or regions. Databricks supports sharing from Cloudflare R2 (no egress fees) and provides monitoring tools. Compute costs for materializing views or streaming tables are charged by Databricks, and storage/network egress costs are charged by the cloud vendor (or by Databricks if [SecureConnect](/concepts/secureconnect.md) is used). ^[what-is-opensharing-databricks-on-aws.md]

## Related Concepts

- [OpenSharing](/concepts/opensharing.md)
- [Databricks-to-Databricks Sharing Protocol](/concepts/databricks-to-databricks-sharing.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Delta Sharing](/concepts/delta-sharing.md)
- [SecureConnect](/concepts/secureconnect.md)
- [Bearer Token Authentication](/concepts/bearer-token-authentication-for-open-sharing.md)
- OpenID Connect (OIDC) Federation
- IP Access Lists
- [Directory-Based Access](/concepts/cloud-token-access-directory-based-access.md)
- [Delta Lake](/concepts/delta-lake.md)
- Iceberg Tables

## Sources

- restrict-opensharing-recipient-access-using-ip-access-lists-databricks-to-open-sharing-databricks-on-aws.md
- what-is-opensharing-databricks-on-aws.md
- what-is-the-opensharing-databricks-to-open-sharing-protocol-databricks-on-aws.md

# Citations

1. [what-is-the-opensharing-databricks-to-open-sharing-protocol-databricks-on-aws.md](/references/what-is-the-opensharing-databricks-to-open-sharing-protocol-databricks-on-aws-e4f6895b.md)
2. [what-is-opensharing-databricks-on-aws.md](/references/what-is-opensharing-databricks-on-aws-adff4826.md)
3. [restrict-opensharing-recipient-access-using-ip-access-lists-databricks-to-open-sharing-databricks-on-aws.md](/references/restrict-opensharing-recipient-access-using-ip-access-lists-databricks-to-open-sharing-databricks-on-aws-665da518.md)
