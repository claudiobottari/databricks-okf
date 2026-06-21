---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bd8f2d5fee79de669058840d1e77027227cd6498c96b76a865a1b6689c00bdcb
  pageDirectory: concepts
  sources:
    - read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - oidc-profile-generation-portal
    - OPGP
  citations:
    - file: read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws.md
title: OIDC Profile Generation Portal
description: Portal URL provided by Databricks providers that recipients use to obtain profile files or OAuth sign-in endpoints for U2M access
tags:
  - delta-sharing
  - oidc
  - portal
  - configuration
timestamp: "2026-06-19T20:09:06.092Z"
---

# OIDC Profile Generation Portal

The **OIDC Profile Generation Portal** is a web-based interface provided by Databricks that enables data recipients in the Open ID Connect (OIDC) Federation user-to-machine (U2M) flow to obtain the credentials needed to access shared data. The portal is accessed via a URL shared by the Databricks provider. ^[read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws.md]

## Overview

In the [Delta Sharing](/concepts/delta-sharing.md) OIDC U2M flow, the provider sends the recipient a link to the OIDC Profile Generation Portal. This link does not contain sensitive information and can be opened from anywhere and accessed multiple times. The portal serves as the bridge between the recipient’s identity provider (IdP) and the Databricks sharing infrastructure, delivering the configuration needed by client applications such as Microsoft Power BI and Tableau. ^[read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws.md]

## Usage

### For Power BI

On the portal page, the recipient selects the **U2M** tile and, under **To use on Power BI**, copies the serving endpoint URL. In Power BI, the recipient uses **Get data** → **OpenSharing**, pastes this endpoint, and authenticates via OAuth. The recipient is redirected to their IdP login page, and after successful authentication, the shared data appears in the Navigator. ^[read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws.md]

### For Tableau

The recipient selects the **U2M** tile on the portal and, under **To use on Tableau**, downloads the profile file. The profile file contains the bearer token and other metadata. The recipient then opens the Tableau OpenSharing OAuth connector, pastes the OpenSharing endpoint URL (also provided on the portal), and the bearer token is prepopulated. This completes the authentication. ^[read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws.md]

## Security

The portal itself does not expose sensitive information; the shared URL is non‑sensitive and reusable. All authentication is handled by the recipient’s IdP through JSON Web Tokens (JWT) that are validated by Databricks according to the recipient’s OIDC federation policy. The portal acts only as a distribution point for the serving endpoint and profile file, which are specific to the recipient’s share and IdP configuration. ^[read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws.md]

## Related Concepts

- [User-to-Machine (U2M) Flow](/concepts/user-to-machine-u2m-authentication-flow.md)
- Open ID Connect (OIDC) Federation
- [Delta Sharing](/concepts/delta-sharing.md)
- [Identity Provider (IdP)](/concepts/internal-vs-external-identity-providers.md)
- Microsoft Power BI
- Tableau
- [Bearer Token Authentication](/concepts/bearer-token-authentication-for-delta-sharing.md)
- [Delta Sharing Recipient](/concepts/delta-sharing-recipient-object.md)

## Sources

- read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws.md

# Citations

1. [read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws.md](/references/read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws-89402a4e.md)
