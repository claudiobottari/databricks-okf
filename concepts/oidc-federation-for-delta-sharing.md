---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b6c6aa20e849f7bd6358889da1617d2c5ab9ec53f9a2a3660ba3db830572a543
  pageDirectory: concepts
  sources:
    - read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - oidc-federation-for-delta-sharing
    - OFFDS
  citations:
    - file: read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws.md
title: OIDC Federation for Delta Sharing
description: Authentication method using Open ID Connect federation to allow recipients without a Databricks workspace to access OpenSharing shares
tags:
  - delta-sharing
  - authentication
  - oidc
  - federation
timestamp: "2026-06-19T20:08:35.392Z"
---

---
title: OIDC Federation for Delta Sharing
summary: An authentication method for OpenSharing that uses OpenID Connect tokens issued by the recipient's identity provider, supporting both User-to-Machine (U2M) and Machine-to-Machine (M2M) flows.
sources:
  - read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T15:36:09.765Z"
updatedAt: "2026-06-19T16:00:00.000Z"
tags:
  - authentication
  - delta-sharing
  - opensharing
  - oidc
  - federation
aliases:
  - oidc-federation-for-delta-sharing
  - OFDS
confidence: 1.0
provenanceState: extracted
inferredParagraphs: 0
---

## OIDC Federation for Delta Sharing

**OIDC Federation for Delta Sharing** is an authentication mechanism used in the [OpenSharing](/concepts/opensharing.md) (Databricks-to-Open sharing) protocol. Instead of using long-lived bearer tokens, the recipient authenticates with JSON Web Tokens (JWTs) issued by their own identity provider (IdP). The data provider configures an OIDC policy and shares a URL to a dedicated portal; the recipient uses that URL to authenticate and obtain access to the shared data. ^[read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws.md]

### Overview

In OIDC federation, the recipient's IdP is responsible for issuing JWTs and enforcing security policies such as multi-factor authentication (MFA). The token lifetime is governed by the recipient's IdP; Databricks only federates authentication to the IdP and validates the JWT against the configured federation policy. Data providers can also federate to their own IdP for internal sharing across departments. ^[read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws.md]

OIDC federation eliminates the need for recipients to manage and secure shared credentials, reduces security risks, and enables fine-grained access control with MFA support. It is an alternative to using Databricks-issued bearer tokens for connecting non-Databricks recipients to providers. ^[read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws.md]

### How it works

1. The recipient provides their IdP and user information (e.g., issuer URL, subject claim, subject identifier) to the data provider.
2. The provider creates an OIDC policy in Databricks and sends the recipient a secure URL to the OIDC profile generation portal.
3. The recipient visits the portal and selects the appropriate flow (U2M or M2M). For U2M, they either copy a serving endpoint (for Power BI) or download a profile file (for Tableau). For M2M, they obtain tokens programmatically.
4. The recipient uses the endpoint or profile to authenticate with their IdP and access the shared data.

Access persists as long as the provider continues to share the data. Updates appear in near real time. The recipient can read and copy the data but cannot modify the source. ^[read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws.md]

### User-to-Machine (U2M) flow

The U2M flow is designed for interactive analytic tools such as Power BI and Tableau. The recipient authenticates through an OAuth sign-in page presented by the OIDC portal. For Power BI, the recipient pastes the serving endpoint URL into the Delta Sharing connector and signs in via OAuth. For Tableau, the recipient downloads a profile file and uses it with the Tableau OpenSharing OAuth connector. ^[read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws.md]

**Requirements:** Power BI Desktop must be version 2.141.1253.0 (released March 31, 2025) or later. For Microsoft Entra ID, the tenant admin must grant admin consent to the Databricks multi-tenant app (client ID `64978f70-f6a6-4204-a29e-87d74bfea138`) before users can authenticate. ^[read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws.md]

### Machine-to-Machine (M2M) flow

The M2M flow uses the OAuth Client Credentials grant for automated applications (e.g., Python scripts). The recipient obtains tokens from their IdP without interactive user sign-in. For detailed instructions, see the separate documentation on reading data shared using OIDC federation in an M2M flow. ^[read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws.md]

### Related concepts

- [OpenSharing Protocol](/concepts/opensharing-protocol.md)
- [Bearer Token Authentication for Delta Sharing](/concepts/bearer-token-authentication-for-open-sharing.md)
- [Delta Sharing](/concepts/delta-sharing.md)
- [Identity Provider (IdP)](/concepts/internal-vs-external-identity-providers.md)
- OpenID Connect (OIDC)
- [User-to-Machine (U2M) Authentication](/concepts/user-to-machine-u2m-authentication.md)
- [Machine-to-Machine (M2M) Authentication](/concepts/machine-to-machine-m2m-authentication.md)

### Sources

- read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws.md

# Citations

1. [read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws.md](/references/read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws-89402a4e.md)
