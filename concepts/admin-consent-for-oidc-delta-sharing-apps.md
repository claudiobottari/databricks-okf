---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 460251b5f812424605a23ab5077798d07fd658dbbf0d4fe5d2263492f4cf3e91
  pageDirectory: concepts
  sources:
    - read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - admin-consent-for-oidc-delta-sharing-apps
    - ACFODSA
  citations:
    - file: read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws.md
title: Admin Consent for OIDC Delta Sharing Apps
description: One-time admin approval required in Entra ID tenant to authorize the Databricks multi-tenant app for OIDC federation
tags:
  - delta-sharing
  - admin-consent
  - entra-id
  - security
timestamp: "2026-06-19T20:09:28.999Z"
---

#Admin Consent for OIDC Delta Sharing Apps

**Admin Consent for OIDC Delta Sharing Apps** is a prerequisite for using the Databricks published multi-tenant application (DeltaSharing) in a [U2M Flow|user-to-machine (U2M) OIDC flow](/concepts/u2m-user-to-machine-authentication-flow.md). The consent must be granted by an Entra ID tenant administrator before users in that tenant can authenticate to Delta Sharing shares via applications such as Power BI or Tableau. ^[read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws.md]

## How to grant admin consent

The tenant admin navigates to the following URL in a browser, replacing `{organization}` with the Azure tenant ID:

```
https://login.microsoftonline.com/{organization}/adminconsent?client_id=64978f70-f6a6-4204-a29e-87d74bfea138
```

The `client_id` is the fixed identifier of the Databricks published multi-tenant app registered in Entra ID. After signing in with an admin identity and approving the application, the consent takes effect. ^[read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws.md]

## Important notes

- This is a **one‑time action**. Once granted, subsequent U2M authentication flows for Delta Sharing within that tenant do not require re‑consent. ^[read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws.md]
- For detailed instructions on granting admin consent in the Entra ID portal, see the [Microsoft Entra documentation](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/grant-admin-consent?pivots=portal). ^[read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws.md]

## Related concepts

- OIDC Federation
- U2M Flow
- Multi-tenant App
- [Delta Sharing](/concepts/delta-sharing.md)
- Power BI
- Tableau
- Entra ID

## Sources

- read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws.md

# Citations

1. [read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws.md](/references/read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws-89402a4e.md)
