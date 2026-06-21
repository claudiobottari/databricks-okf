---
title: What is the OpenSharing Databricks-to-Open sharing protocol? | Databricks on AWS
source: https://docs.databricks.com/aws/en/delta-sharing/share-data-open
ingestedAt: "2026-06-18T08:05:53.082Z"
---

This page gives an overview of how providers can use the OpenSharing Databricks-to-Open sharing protocol to share data from your Unity Catalog\-enabled Databricks workspace with any user on any computing platform, anywhere. If you are a data recipient (a user or group of users with whom data is being shared), see instead [Access data shared with you using OpenSharing (for recipients)](https://docs.databricks.com/aws/en/delta-sharing/recipient).

## Who should use the OpenSharing Databricks-to-Open sharing protocol?[​](#who-should-use-the-opensharing-databricks-to-open-sharing-protocol "Direct link to who-should-use-the-opensharing-databricks-to-open-sharing-protocol")

There are three ways to share data using OpenSharing:

1.  **The Databricks-to-Open sharing protocol**, covered in this article, lets you share data that you manage in a Unity Catalog\-enabled Databricks workspace with users on any computing platform.
    
    This approach uses the OpenSharing server that is built into Databricks and is useful when you manage data using Unity Catalog and want to share it with users who don't use Databricks or don't have access to a Unity Catalog\-enabled Databricks workspace. The integration with Unity Catalog on the provider side simplifies setup and governance for providers.
    
2.  **A customer-managed implementation of the open-source OpenSharing server** lets you share from any platform to any platform, whether Databricks or not.
    
    See [the open source project](https://go.delta.io/sharing).
    
3.  **The Databricks-to-Databricks sharing protocol** lets you share data from your Unity Catalog\-enabled workspace with users who also have access to a Unity Catalog\-enabled Databricks workspace.
    
    See [What is the OpenSharing Databricks-to-Databricks protocol?](https://docs.databricks.com/aws/en/delta-sharing/share-data-databricks).
    

For an introduction to OpenSharing and more information about these three approaches, see [What is OpenSharing?](https://docs.databricks.com/aws/en/delta-sharing/).

## OpenSharing Databricks-to-Open sharing workflow[​](#opensharing-databricks-to-open-sharing-workflow "Direct link to opensharing-databricks-to-open-sharing-workflow")

This section provides a high-level overview of the Databricks-to-Open sharing workflow, with links to detailed documentation for each step.

In the OpenSharing Databricks-to-Open sharing model:

1.  The data provider creates a _recipient_, which is a named object that represents a user or group of users that the data provider wants to share data with.
    
    When the data provider creates the recipient, the provider sets up authentication using either a long-lived bearer token or Open ID Connect (OIDC) federation. If the provider uses a bearer token, Databricks generates a credential file and an activation link that the data provider can send to the recipient to access the credential file. In the OIDC federation flow, the recipient's IdP manages authentication, based on a policy created by the provider.
    
    For details, see [Create a recipient object for non-Databricks users using bearer tokens (Databricks-to-Open sharing)](https://docs.databricks.com/aws/en/delta-sharing/create-recipient-token) or [Enable Open ID Connect (OIDC) federation for OpenSharing recipients](https://docs.databricks.com/aws/en/delta-sharing/create-recipient-oidc-fed).
    
2.  The data provider creates a _share_, which is a named object that contains a collection of tables registered in a Unity Catalog metastore in the provider's account.
    
    For details, see [Create shares for OpenSharing](https://docs.databricks.com/aws/en/delta-sharing/create-share).
    
3.  The data provider grants the recipient access to the share.
    
    For details, see [Manage access to OpenSharing data shares (for providers)](https://docs.databricks.com/aws/en/delta-sharing/grant-access).
    
4.  In the bearer token flow, the data provider sends the activation link to the recipient over a secure channel, along with instructions for using the activation link to download the credential file that the recipient will use to establish a secure connection with the data provider to receive the shared data.
    
    For details, see [Get the activation link](https://docs.databricks.com/aws/en/delta-sharing/create-recipient-token#get-activation-link).
    
    In the OIDC federation flow, recipients authenticate through their IdP. See [Enable Open ID Connect (OIDC) federation for OpenSharing recipients](https://docs.databricks.com/aws/en/delta-sharing/create-recipient-oidc-fed).
    
5.  In the bearer token flow, the data recipient follows the activation link to download the credential file, and then uses the credential file to access the shared data.
    
    Shared data is available to read only. Users can access data using their platform or tools of choice. For details, see [Read data shared using OpenSharing Databricks-to-Open sharing with bearer tokens](https://docs.databricks.com/aws/en/delta-sharing/read-data-open).
    
    In the OIDC federation flow, recipients authenticate through their IdP. See [Enable Open ID Connect (OIDC) federation for OpenSharing recipients](https://docs.databricks.com/aws/en/delta-sharing/create-recipient-oidc-fed).
    

## Provider-specific configurations[​](#provider-specific-configurations "Direct link to provider-specific-configurations")

Many providers have their own OpenSharing networks for sharing. For specific sharing instructions, see, for example:

*   [Amperity](https://docs.amperity.com/datagrid/bridge_databricks.html)
*   [Atlassian](https://support.atlassian.com/analytics/docs/create-a-data-share/)
*   [Oracle](https://docs.oracle.com/en/database/data-integration/data-transforms/using/create-delta-share-connection.html)

## Cloud tokens and directory-based access[​](#cloud-tokens-and-directory-based-access "Direct link to cloud-tokens-and-directory-based-access")

When you share eligible Delta tables using Databricks-to-Open sharing, Databricks returns the table's cloud storage location alongside temporary cloud credentials (cloud tokens) that recipients can use to read data directly from cloud storage. This is called _directory-based access mode_ and is part of the [Databricks-to-Open sharing protocol](https://github.com/delta-io/delta-sharing/blob/main/PROTOCOL.md#generate-temporary-table-credential). It is enabled by default for newly shared assets that meet eligibility requirements. If a shared table does not meet all requirements, recipients use pre-signed URL access as normal.

For eligibility requirements and data privacy considerations, see [Cloud token eligibility](https://docs.databricks.com/aws/en/delta-sharing/create-share#cloud-token-eligibility).

## Provider setup and security considerations for Databricks-to-Open sharing[​](#provider-setup-and-security-considerations-for-databricks-to-open-sharing "Direct link to provider-setup-and-security-considerations-for-databricks-to-open-sharing")

Good token management is key to sharing data securely when you use the Databricks-to-Open sharing model:

*   Data providers on Databricks who intend to use Databricks-to-Open sharing when they provide shares must configure the default recipient token lifetime when they enable OpenSharing for their Unity Catalog metastore. Databricks recommends that you configure tokens to expire. See [Enable OpenSharing on a metastore](https://docs.databricks.com/aws/en/delta-sharing/set-up#enable).
*   If you need to modify the default token lifetime, see [Modify the recipient token lifetime](https://docs.databricks.com/aws/en/delta-sharing/create-recipient-token#modify-recipient-token-lifetime).
*   Encourage recipients to manage their downloaded credential file securely.
*   For more information about token management and Databricks-to-Open sharing security, see [Manage recipient tokens](https://docs.databricks.com/aws/en/delta-sharing/create-recipient-token#rotate-credential).
*   Databricks-to-Open sharing is supported between all cloud environment types.

Data providers can provide additional security by assigning IP access lists to restrict recipient access to specific network locations. See [Restrict OpenSharing recipient access using IP access lists (Databricks-to-Open sharing)](https://docs.databricks.com/aws/en/delta-sharing/access-list).
