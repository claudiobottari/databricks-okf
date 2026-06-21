---
title: Read data shared using Open ID Connect (OIDC) federation in a U2M flow | Databricks on AWS
source: https://docs.databricks.com/aws/en/delta-sharing/sharing-over-oidc-u2m
ingestedAt: "2026-06-18T08:06:02.171Z"
---

This page describes how data recipients can use a 'user-to-machine' (U2M) application (e.g, Power BI) to establish access to OpenSharing shares created in Databricks using Open ID Connect (OIDC) federation. The "user-to-machine" (U2M) authentication flow uses OIDC federation, allowing JSON Web Tokens (JWTs) issued by the recipient's IdP to be used as short-lived OAuth tokens that are authenticated by Databricks. This [Databricks-to-open sharing](https://docs.databricks.com/aws/en/delta-sharing/share-data-databricks) authentication method is designed for recipients who do not have access to a Unity Catalog\-enabled Databricks workspace.

In OIDC Federation, the recipient's IdP is responsible for issuing JWT tokens and enforcing security policies, such as Multi-Factor Authentication (MFA). Likewise, the lifetime of the JWT token is governed by the recipient's IdP. Databricks does not generate or manage these tokens. It only federates authentication to the recipient's IdP and validates the JWT against the recipient's configured federation policy. Data providers can also choose to federate authentication to their own IdP when sharing data internally with other users or departments within their organization.

OIDC federation is an alternative to using long-lived Databricks\-issued bearer tokens to connect non-Databricks recipients to providers. It enables fine-grained access control, supports MFA, and reduces security risks by eliminating the need for recipients to manage and secure shared credentials. For information about using bearer tokens to manage authentication to shares instead, see [Create a recipient object for non-Databricks users using bearer tokens (Databricks-to-Open sharing)](https://docs.databricks.com/aws/en/delta-sharing/create-recipient-token).

This page is for recipients using "user-to-machine" (U2M) applications (e.g., Power BI or Tableau). For information about how providers can enable OIDC federation for recipients in Databricks, see [Enable Open ID Connect (OIDC) federation for OpenSharing recipients](https://docs.databricks.com/aws/en/delta-sharing/create-recipient-oidc-fed). For information about the "machine-to-machine" (M2M) OAuth Client Credentials flow, see [Read data shared using Open ID Connect (OIDC) federation in an M2M flow](https://docs.databricks.com/aws/en/delta-sharing/sharing-over-oidc-m2m).

This page explains how data recipients can use their own identity provider (IdP) to access OpenSharing shares created in Databricks.

## Overview of the user-to-machine (U2M) authentication flow using OIDC token federation[​](#overview-of-the-user-to-machine-u2m-authentication-flow-using-oidc-token-federation "Direct link to Overview of the user-to-machine (U2M) authentication flow using OIDC token federation")

To use OIDC token federation for access to data shared by a Databricks provider, you do the following:

1.  Give the Databricks provider the IdP and user information that they request.
2.  Use the OIDC profile generation portal URL that the provider sends you to access a profile file (Tableau) or OAuth sign-in page (Power BI).

## Get the OIDC policy field values from Entra ID[​](#-get-the-oidc-policy-field-values-from-entra-id "Direct link to -get-the-oidc-policy-field-values-from-entra-id")

If you, as a recipient, use Microsoft Entra ID as your Identity Provider, you can get the information requested by the provider by following these instructions. For other IdPs, refer to their documentation.

*   **Issuer URL**: This is the token issuer, specified in the `iss` claim of OIDC JWT tokens. For Entra ID it is `https://login.microsoftonline.com/{tenantId}/v2.0`, replace `{tenantId}` with your Entra tenant ID. To learn how to find your tenant ID, see the [Microsoft Entra ID documentation](https://learn.microsoft.com/entra/fundamentals/how-to-find-tenant).
    
*   **Subject Claim**: Refers to the field in the JWT payload that identifies the entity (e.g., user or group) accessing the data. The specific field used depends on your Identity Provider (IdP) and your use case. For example, in Microsoft Entra ID, you might use the following values for U2M scenarios:
    
    *   **`oid` (Object ID)**: Select when a single user requires access.
    *   **`groups`**: Select when a group of users requires access.
    
    For other IdPs, refer to their documentation to determine the appropriate subject claim for your specific requirements.
    
*   **Subject**: the Unique identifier of the identity which can access the shared data.
    
    *   If you intend to share with a single user and choose `oid` for the subject claim, then you should find the Object ID of the user according to [Microsoft Entra ID documentation](https://learn.microsoft.com/partner-center/account-settings/find-ids-and-domain-names#find-the-user-object-id) and use that as subject.
    *   If you choose groups as the subject-claim then you must find the group object Id Group object ID: In the Entra ID console, select groups, and search for the group. The object ID is displayed on the group row in the list. For groups claim, in the Entra Console, select groups, and find the object ID of your group.
*   **Audience**: For U2M authentication, the recipient doesn't need this value. The Databricks provider always uses the following ID:
    
    `64978f70-f6a6-4204-a29e-87d74bfea138`
    
    This is the ID for the `Databricks published multi-tenant App(DeltaSharing)` OAuth-registered client app that recipients use to access Databricks shares using Power BI and Tableau.
    

### Example values for Entra ID[​](#example-values-for-entra-id "Direct link to Example values for Entra ID")

These are example configuration for sharing with a specific user with Object ID `11111111-2222-3333-4444-555555555555` in Entra ID tenant `aaaaaaaa-bbbb-4ccc-dddd-eeeeeeeeeeee`.

*   Issuer: `https://login.microsoftonline.com/aaaaaaaa-bbbb-4ccc-dddd-eeeeeeeeeeee/v2.0`
*   subject claim: `oid` (Object ID of a user)
*   Subject: `11111111-2222-3333-4444-555555555555` [Microsoft Entra ID documentation](https://learn.microsoft.com/partner-center/account-settings/find-ids-and-domain-names#find-the-user-object-id)
*   Audiences: `64978f70-f6a6-4204-a29e-87d74bfea138` (This is the client ID of the multi-tenant app registered by Databricks in Entra ID)

These are example configurations for sharing with a specific group with Object ID `66666666-2222-3333-4444-555555555555` in Entra ID tenant `aaaaaaaa-bbbb-4ccc-dddd-eeeeeeeeeeee`

*   Issuer: `https://login.microsoftonline.com/aaaaaaaa-bbbb-4ccc-dddd-eeeeeeeeeeee/v2.0`
*   subject claim: `groups`
*   Subject: `66666666-2222-3333-4444-555555555555` (This is the object ID of the group, which can be found in the Entra ID console. You can select a group and find the object id of your group)
*   Audiences: `64978f70-f6a6-4204-a29e-87d74bfea138` (This is the client ID of the multi-tenant app registered by Databricks in Entra ID)

note

For U2M applications like Power BI and Tableau, the audience should be the multi-tenant app ID registered by Databricks in Entra ID, which is `64978f70-f6a6-4204-a29e-87d74bfea138`.

For more information about U2M applications and their OIDC Federation policies see [Read data shared using Open ID Connect (OIDC) federation in a U2M flow](https://docs.databricks.com/aws/en/delta-sharing/sharing-over-oidc-u2m).

After the provider creates the policy for you, they will share a link to the Databricks OIDC Portal, which can be opened from anywhere and accessed multiple times. This link does not contain any sensitive information.

### Requirements[​](#requirements "Direct link to Requirements")

The Power BI Desktop must be version 2.141.1253.0 (released on March 31, 2025) or later.

1.  Go to the OIDC profile portal URL that the Databricks provider shared with you.
    
    Request the URL if you haven't yet received it.
    
2.  On the portal page, select the **U2M** tile and, under **To use on Power BI**, copy the serving endpoint.
    
3.  In Power BI, go to **Get data** and search for _Delta Sharing_, select **OpenSharing**, and click **Connect**.
    
4.  On the **OpenSharing** dialog, paste the serving endpoint URL in the **OpenSharing Server URL** field and click **OK**.
    
5.  On the **OpenSharing** authentication dialog, make sure that **OAuth** is selected in the sidebar, and click **Sign in**.
    
    You are taken to your IdP login page. Log in as you usually do.
    
6.  Return to the **OpenSharing** authentication dialog and click **Connect**.
    
7.  In the Navigator, the shared data is listed under the OpenSharing URL.
    

### Approve of Multi-Tenant App[​](#approve-of-multi-tenant-app "Direct link to Approve of Multi-Tenant App")

To be able to use the Databricks published multi-tenant app(DeltaSharing), the Entra ID tenant admin needs to open this URL in their browser and sign in with admin identity to approve usage: [https://login.microsoftonline.com/{organization}/adminconsent?client\_id=64978f70-f6a6-4204-a29e-87d74bfea138](https://login.microsoftonline.com/%7Borganization%7D/adminconsent?client_id=64978f70-f6a6-4204-a29e-87d74bfea138). Please replace `{organization}` with your Azure tenant ID. This is a one time action, more info here: [https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/grant-admin-consent?pivots=portal](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/grant-admin-consent?pivots=portal).

To access the share using Tableau:

1.  Go to the OIDC profile portal URL that the Databricks provider shared with you.
    
    Request the URL if you haven't yet received it.
    
2.  On the portal page, select the **U2M** tile and, under **To use on Tableau**, download the profile file.
    
3.  Find and copy the OpenSharing endpoint.
    
4.  Open the Tableau OpenSharing OAuth connector to authenticate automatically with your IdP and launch the connector page.
    
5.  On the connector page, paste the OpenSharing endpoint URL. The bearer token is prepopulated.
    

For more information, see the [Tableau OpenSharing connector readme in Databricks Labs](https://github.com/databrickslabs/sandbox/tree/main/tableau-delta-sharing-connector-oauth).
