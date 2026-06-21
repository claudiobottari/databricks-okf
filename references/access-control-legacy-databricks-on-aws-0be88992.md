---
title: Access control (legacy) | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/feature-store/workspace-feature-store/access-control
ingestedAt: "2026-06-18T08:10:53.984Z"
---

This article describes how to control access to feature tables in workspaces that are not enabled for Unity Catalog. If your workspace is enabled for Unity Catalog, use [Unity Catalog privileges](https://docs.databricks.com/aws/en/data-governance/unity-catalog/manage-privileges/) instead.

You can configure Feature Store access control to grant fine-grained permissions on feature table metadata. You can control a user's ability to view a feature table in the UI, edit its description, manage other users' permissions on the table, and delete the table.

You can assign three permission levels to feature table metadata: CAN VIEW METADATA, CAN EDIT METADATA, and CAN MANAGE. Any user can create a new feature table. The table lists the abilities for each permission.

By default, when a feature table is created:

*   The creator has CAN MANAGE permission
*   Workspace admins have CAN MANAGE permission
*   Other users have NO PERMISSIONS

## Configure permissions for a feature table[​](#configure-permissions-for-a-feature-table "Direct link to Configure permissions for a feature table")

1.  On the feature table page, click the arrow to the right of the name of the feature table and select **Permissions**. If you do not have CAN MANAGE permission for the feature table, you will not see this option.
    
    ![Select permissions from drop-down menu](https://docs.databricks.com/aws/en/assets/images/feature-store-permissions-840e0dfb9dce73d02e7e520219a4b652.png)
    
2.  Edit the permissions and click **Save**.
    

## Configure permissions for all feature tables in Feature Store[​](#configure-permissions-for-all-feature-tables-in-feature-store "Direct link to Configure permissions for all feature tables in Feature Store")

Workspace administrators can use the Feature Store UI to set permission levels on all feature tables for specific users or groups.

note

*   A user with CAN MANAGE permission for the Feature Store can change Feature Store permissions for all other users.
*   Permissions set from the feature store page also apply to all future feature tables.

1.  On the feature store page, click **Permissions**. This button is only available for workspace administrators and users with CAN MANAGE permission for the Feature Store.
    
    ![Drop-down menu where you select permissions](https://docs.databricks.com/aws/en/assets/images/feature-store-wide-permissions-65c0edf83a192ef0b3b1adf7395003e8.png)
    
2.  Edit the permissions and click **Save**.
    
    Permissions set on the Feature Store page can only be removed from that page. On the feature table page, you can override settings from the Feature Store page to add permissions, but you cannot set more restrictive permissions.
    
    When you navigate to a specific feature table page, permissions set from the feature store page are marked “Some permissions cannot be removed because they are inherited”.
