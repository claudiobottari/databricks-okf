---
title: What is the OpenSharing Databricks-to-Databricks protocol? | Databricks on AWS
source: https://docs.databricks.com/aws/en/delta-sharing/share-data-databricks
ingestedAt: "2026-06-18T08:05:51.680Z"
---

This page gives an overview of how to use Databricks-to-Databricks OpenSharing to share data securely with any Databricks user, regardless of account or cloud host, as long as that user has access to a workspace enabled for [Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/).

## Who should use Databricks-to-Databricks OpenSharing?[​](#who-should-use-databricks-to-databricks-opensharing "Direct link to who-should-use-databricks-to-databricks-opensharing")

There are three ways to share data using OpenSharing.

1.  **The Databricks-to-Databricks sharing protocol**, covered in this article, lets you share data from your Unity Catalog\-enabled workspace with users who also have access to a Unity Catalog\-enabled Databricks workspace.
    
    This approach uses the OpenSharing server that is built into Databricks and provides support for notebook sharing, Unity Catalog data governance, auditing, and usage tracking for both providers and recipients. The integration with Unity Catalog simplifies setup and governance for both providers and recipients and improves performance.
    
2.  **The Databricks-to-Open sharing protocol** lets you share data that you manage in a Unity Catalog\-enabled Databricks workspace with users on any computing platform.
    
    See [What is the OpenSharing Databricks-to-Open sharing protocol?](https://docs.databricks.com/aws/en/delta-sharing/share-data-open).
    
3.  **A customer-managed implementation of the open-source OpenSharing server** lets you share from any platform to any platform, whether Databricks or not.
    
    See [the open source project](https://go.delta.io/sharing).
    

For an introduction to OpenSharing and more information about these three approaches, see [What is OpenSharing?](https://docs.databricks.com/aws/en/delta-sharing/).

## Databricks-to-Databricks OpenSharing workflow[​](#databricks-to-databricks-opensharing-workflow "Direct link to databricks-to-databricks-opensharing-workflow")

This section provides a high-level overview of the Databricks-to-Databricks sharing workflow, with links to detailed documentation for each step.

In the Databricks-to-Databricks OpenSharing model:

1.  A data _recipient_ gives a data _provider_ the unique _sharing identifier_ for the Databricks Unity Catalog metastore that is attached to the Databricks workspace that the recipient (which represents a user or group of users) will use to access the data that the data provider is sharing.
    
    For details, see [Step 1: Request the recipient's sharing identifier](https://docs.databricks.com/aws/en/delta-sharing/create-recipient#request-uuid).
    
2.  The data provider creates a _share_ in the provider's Unity Catalog metastore. This named object contains a collection of tables, views, volumes, and notebooks registered in the metastore.
    
    For details, see [Create shares for OpenSharing](https://docs.databricks.com/aws/en/delta-sharing/create-share).
    
3.  The data provider creates a recipient object in the provider's Unity Catalog metastore. This named object represents the user or group of users who will access the data included in the share, along with the sharing identifier of the Unity Catalog metastore that is attached to the workspace that the user or group of users will use to access the share. The sharing identifier is the key identifier that enables the secure connection.
    
    For details, see [Step 2: Create the recipient](https://docs.databricks.com/aws/en/delta-sharing/create-recipient#create-recipient-db-to-db).
    
4.  The data provider grants the recipient access to the share.
    
    For details, see [Manage access to OpenSharing data shares (for providers)](https://docs.databricks.com/aws/en/delta-sharing/grant-access).
    
5.  The share becomes available in the recipient's Databricks workspace, and recipients can access it using Catalog Explorer, the Databricks CLI, or SQL commands in a Databricks notebook or the Databricks SQL query editor.
    
    To access the tables, views, volumes, and notebooks in a share, a metastore admin or [privileged user](https://docs.databricks.com/aws/en/delta-sharing/read-data-databricks#access-data) must create a catalog from the share. Then that user or another user who is granted the appropriate privilege can give other users access to the catalog and objects in the catalog. Granting permissions on shared catalogs and data assets works just like it does with any other assets registered in Unity Catalog, with the important distinction being that users can be granted only read access on objects in catalogs that are created from OpenSharing shares.
    
    Shared notebooks live at the catalog level, and any user with the `USE CATALOG` privilege on the catalog can access them.
    
    For details, see [Read data shared using Databricks-to-Databricks OpenSharing (for recipients)](https://docs.databricks.com/aws/en/delta-sharing/read-data-databricks).
    

## Improve table read performance with history sharing[​](#improve-table-read-performance-with-history-sharing "Direct link to improve-table-read-performance-with-history-sharing")

Databricks-to-Databricks table shares can improve performance by enabling history sharing. Sharing history improves performance by leveraging temporary security credentials from your cloud storage, scoped-down to the root directory of the provider's shared Delta table, resulting in performance that is comparable to direct access to source tables.

*   For new table shares, specify `WITH HISTORY` when creating the table share. See [Add tables to a share](https://docs.databricks.com/aws/en/delta-sharing/create-share#add-tables). When you share a table using compute on Databricks Runtime 16.2 and above, `WITH HISTORY` is the default.
*   For existing table shares, you must alter the share to share table history. See [Update shares](https://docs.databricks.com/aws/en/delta-sharing/manage-share#update). When you share a table using compute on Databricks Runtime 16.2 and above, `WITH HISTORY` is the default.

When you share an entire schema, all tables in the schema are shared with history by default.

For cloud token eligibility requirements and data privacy considerations, see [Cloud token eligibility](https://docs.databricks.com/aws/en/delta-sharing/create-share#cloud-token-eligibility).

## Databricks-to-Databricks OpenSharing support matrix for cloud environments[​](#databricks-to-databricks-opensharing-support-matrix-for-cloud-environments "Direct link to databricks-to-databricks-opensharing-support-matrix-for-cloud-environments")

Databricks-to-Databricks OpenSharing supports sharing within the same environment type. Commercial clouds include workspaces with compliance controls enabled, such as FedRAMP Moderate. Sharing with Azure Government environments is not supported.

Preview

Sharing across regulatory domains is in gated [Public Preview](https://docs.databricks.com/aws/en/release-notes/release-types). Contact your Databricks account team to get started.

In this matrix, each row represents the provider environment (the metastore sharing data), and each column represents the recipient environment (the metastore receiving shared data).

### Limitations[​](#limitations "Direct link to Limitations")

The following limitations apply to cross-regulatory domain sharing:

*   [Cloud tokens](https://docs.databricks.com/aws/en/delta-sharing/create-share#cloud-token-eligibility) are used unless a share crosses into or out of AWS GovCloud or AWS GovCloud DoD. In these following cases, tables are shared using pre-signed URLs instead:
    *   A commercial cloud shares to or receives shares from either AWS GovCloud or AWS GovCloud DoD.
    *   AWS GovCloud and AWS GovCloud DoD share with each other.

*   GCP commercial workspaces cannot share with or receive shares from AWS GovCloud DoD.
