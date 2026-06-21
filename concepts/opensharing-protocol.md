---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 72c6b4b8af0610552c4d8d7600897eaf12d113b612ec1dbb9c7aa52f1bd1931d
  pageDirectory: concepts
  sources:
    - read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws.md
    - what-is-unity-catalog-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - opensharing-protocol
    - Open Sharing Protocol
    - OpenSharing OSS Protocol
  citations:
    - file: read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws.md
    - file: what-is-unity-catalog-databricks-on-aws.md
title: OpenSharing Protocol
description: Databricks protocol for sharing data with recipients who don't have a Unity Catalog-enabled Databricks workspace
tags:
  - delta-sharing
  - protocol
  - data-sharing
timestamp: "2026-06-19T20:10:43.808Z"
---

# OpenSharing Protocol

**OpenSharing Protocol** is a vendor-agnostic, standardized method for securely sharing tabular and other data assets across platforms using bearer token authentication or Open ID Connect (OIDC) federation. It powers Databricks's Delta Sharing implementation, enabling a **Databricks-to-Open sharing** model where a data provider grants read access to a recipient without requiring the recipient to have a Databricks account. ^[read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws.md] ^[what-is-unity-catalog-databricks-on-aws.md]

## How It Works

In the Databricks-to-Open sharing model, the provider creates a [Delta Share](/concepts/delta-sharing.md) and configures authentication for recipients. Two authentication methods are supported:

- **Bearer tokens**: The provider distributes a credential file containing an endpoint URL and a long-lived bearer token. The recipient uses this file to connect to the provider's OpenSharing server and list available shares, namespaces, and tables. ^[read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws.md]
- **OIDC federation**: Recipients use JSON Web Tokens (JWTs) issued by their own identity provider (IdP) as short-lived OAuth tokens. This enables fine-grained access control, supports Multi-Factor Authentication (MFA), and eliminates the need for managing shared credentials. ^[read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws.md]

Access persists as long as the credential remains valid or the JWT can be refreshed, and the provider continues to share the data. Providers manage credential expiration and rotation. Updates to the data are available in near real time. Recipients can read and make copies of shared data but cannot modify the source data. ^[read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws.md]

## Authentication Flows

### Bearer Token Authentication

Bearer token authentication uses long-lived tokens issued by Databricks. The provider creates a recipient object for non-Databricks users and distributes a credential file. This method is simpler to set up but carries security risks from managing shared credentials. ^[read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws.md]

### OIDC Federation

OIDC federation supports two authentication flows:

- **User-to-Machine (U2M)**: Designed for applications like Power BI and Tableau where an individual user authenticates. The recipient's IdP issues JWTs, and Databricks federates authentication to validate the token against the configured federation policy. The `audience` claim must use the Databricks multi-tenant app ID `64978f70-f6a6-4204-a29e-87d74bfea138`. ^[read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws.md]
- **Machine-to-Machine (M2M)**: Uses the OAuth Client Credentials flow for automated, non-interactive access.

For U2M authentication, the provider shares an OIDC profile generation portal URL. Recipients access the portal to obtain a profile file (Tableau) or an OAuth sign-in page (Power BI) without handling sensitive credentials directly. ^[read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws.md]

## Integration with Unity Catalog

The OpenSharing Protocol is a fundamental capability of [Unity Catalog](/concepts/unity-catalog.md), serving as the open data sharing mechanism for the platform. When sharing a securable object (e.g., a table or view) via OpenSharing, the object cannot be deleted while it is still shared. Attempting to delete it raises the `DELTA_SHARING_SECURABLE_DELETE_BLOCKED` error, which includes the name of the share(s) and, if applicable, any clean room IDs through which the object is shared. ^[what-is-unity-catalog-databricks-on-aws.md]

## Supported Connectors

OpenSharing provides connectors for a wide range of tools and platforms. Recipients can read shared data using:

- Databricks (via Catalog Explorer or Python notebooks with Unity Catalog integration)
- Apache Spark (via the `delta-sharing-spark` connector)
- Pandas (via the `delta-sharing` Python connector)
- Power BI (via the OpenSharing connector in Power BI Desktop, version 2.141.1253.0 or later)
- Tableau (via the OpenSharing connector on Tableau Exchange)
- External Iceberg clients such as Snowflake, Trino, Apache Flink, and Apache Spark (via the [Apache Iceberg REST Catalog API](/concepts/iceberg-rest-catalog-irc-protocol.md))

### OIDC Authentication for Power BI and Tableau

For U2M applications like Power BI and Tableau, OIDC authentication works as follows:

**Power BI:**
1. Access the OIDC profile portal URL from the provider.
2. Select the **U2M** tile and copy the serving endpoint.
3. In Power BI, search for **Delta Sharing** and select **OpenSharing**.
4. Paste the serving endpoint as the server URL.
5. Authenticate using OAuth sign-in, which redirects to the IdP login page.
6. The Entra ID tenant admin must grant admin consent for the Databricks multi-tenant app using `https://login.microsoftonline.com/{organization}/adminconsent?client_id=64978f70-f6a6-4204-a29e-87d74bfea138`. ^[read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws.md]

**Tableau:**
1. Access the OIDC profile portal URL from the provider.
2. Select the **U2M** tile and download the profile file.
3. Open the Tableau OpenSharing OAuth connector for automatic IdP authentication.
4. Paste the OpenSharing endpoint; the bearer token is prepopulated. ^[read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws.md]

## Iceberg Client Support

To access shared data through Iceberg clients, the recipient obtains the Iceberg REST Catalog endpoint (`icebergEndpoint`) and bearer token from the credential file. The endpoint follows the format `<workspace-url>/api/2.0/delta-sharing/metastores/<metastore-id>/iceberg`. Recipients can then list shares, namespaces, and tables programmatically and configure their Iceberg client to create a catalog integration.

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- Credential File
- [Bearer Token](/concepts/oidc-vs-bearer-token-authentication.md)
- OpenSharing Connectors
- Open ID Connect (OIDC)
- [User-to-Machine (U2M) Authentication](/concepts/user-to-machine-u2m-authentication.md)
- [Machine-to-Machine (M2M) Authentication](/concepts/machine-to-machine-m2m-authentication.md)
- Power BI OpenSharing Connector
- [Tableau OpenSharing Connector](/concepts/opensharing-bi-tool-connectors-power-bi-and-tableau.md)
- [Apache Iceberg REST Catalog API](/concepts/iceberg-rest-catalog-irc-protocol.md)

## Sources

- read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws.md
- what-is-unity-catalog-databricks-on-aws.md

# Citations

1. [read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws.md](/references/read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws-89402a4e.md)
2. [what-is-unity-catalog-databricks-on-aws.md](/references/what-is-unity-catalog-databricks-on-aws-ea58b0e9.md)
