---
title: Share a Genie Space using OpenSharing | Databricks on AWS
source: https://docs.databricks.com/aws/en/delta-sharing/share-genie-space
ingestedAt: "2026-06-18T08:05:56.840Z"
---

Beta

Genie Space sharing using OpenSharing is in [Beta](https://docs.databricks.com/aws/en/release-notes/release-types).

Use OpenSharing to share a Genie Space with users outside your organization. When you share a Genie Space, Databricks creates a point-in-time snapshot of the space's data assets and instructions and makes it available to your selected recipients. Recipients can mount the share to create a local Genie Space pre-loaded with your data and instructions. See [Mount a shared Genie Space](https://docs.databricks.com/aws/en/delta-sharing/mount-genie-space).

## Requirements[​](#requirements "Direct link to Requirements")

To share a Genie Space, you must have the following:

*   The **Genie Agent Sharing** preview enabled at the account level. See [Manage Databricks previews](https://docs.databricks.com/aws/en/admin/workspace-settings/manage-previews).
*   [Set up OpenSharing](https://docs.databricks.com/aws/en/delta-sharing/set-up) for your account.
*   `CREATE SHARE` privilege on the Unity Catalog metastore where the Genie Space's data is registered.
*   `CAN EDIT` or higher on the Genie Space. See [Access control lists](https://docs.databricks.com/aws/en/security/auth/access-control/).
*   `SELECT` on all data assets in the space. You must retain this privilege. If you lose it, recipients cannot access the shared data.
*   At least one recipient. See [Create data recipients for OpenSharing (Databricks-to-Databricks sharing)](https://docs.databricks.com/aws/en/delta-sharing/create-recipient).

1.  In your Databricks workspace, go to the Genie Space you want to share.
    
2.  In the upper-right corner, click **Share**, then click the **External** tab.
    
3.  In the **Select recipients to share with** field, search for and select the recipients with whom you want to share the space.
    
    If no recipients exist yet, click **Create new recipient**. See [Create data recipients for OpenSharing (Databricks-to-Databricks sharing)](https://docs.databricks.com/aws/en/delta-sharing/create-recipient).
    
4.  Click **Share**.
    

Databricks exports a snapshot of the Genie Space, creates a share containing all of the space's tables, instructions, curated SQL examples, SQL functions, and other configuration, and grants the selected recipients access. The snapshot is captured at the time you click **Share**.

## Add more recipients[​](#add-more-recipients "Direct link to Add more recipients")

After the initial share is created, you can share the same snapshot with additional recipients:

1.  Go to the Genie Space and in the upper-right corner, click **Share**, then click the **External** tab.
2.  Search for and select the additional recipients with whom you want to share the space, then click **Add recipients**.

You cannot modify the data assets in the share after you create it.

The share appears in the **Shared by me** list. The share's asset list is read-only. You can manage recipients and delete the share, but you cannot add or remove data assets manually. See [Manage shares for OpenSharing](https://docs.databricks.com/aws/en/delta-sharing/manage-share).

## Limitations[​](#limitations "Direct link to Limitations")

*   **Snapshot only:** The share captures the Genie Space at the time you click **Share** and does not update when you change the space. All recipients see the same snapshot.
*   **Size limit:** The Genie Space configuration must be less than 256 KB when compressed. Spaces that exceed this limit return an error when you attempt to share them. To reduce the size, shorten instructions or descriptions, then try again.
*   **Metric views:** Genie Spaces that include metric views cannot be shared.

## Next steps[​](#next-steps "Direct link to Next steps")

*   [Mount a shared Genie Space](https://docs.databricks.com/aws/en/delta-sharing/mount-genie-space)
*   [Manage shares](https://docs.databricks.com/aws/en/delta-sharing/manage-share)
*   [Grant and manage share access](https://docs.databricks.com/aws/en/delta-sharing/grant-access)
