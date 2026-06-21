---
title: Custom classifiers | Databricks on AWS
source: https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-classification-custom-classifiers
ingestedAt: "2026-06-18T08:04:00.680Z"
---

This page describes how to create and manage custom classifiers for Databricks Data Classification in Unity Catalog. Custom classifiers extend the [built-in classification system](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-classification) so you can detect sensitive data that is specific to your organization, such as internal employee IDs, proprietary product codes, vendor identifiers, or partner account numbers.

To create a custom classifier, you select a [governed tag](https://docs.databricks.com/aws/en/admin/governed-tags/) and provide example columns that contain representative values for the class. Data Classification then detects this class during its regular scans.

Using custom classifiers, you can:

*   **Tag organization-specific data**: Detect and configure auto-tagging for data types that are unique to your organization, such as employee IDs, partner codes, or internal account numbers.
*   **Extend governance controls**: Apply [ABAC column-level masks](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/core-concepts#policy-types) to sensitive data.

note

Custom classifier configuration and the detection metadata that Databricks generates from your example columns are encrypted at rest. You can use a [customer-managed key (CMK)](https://docs.databricks.com/aws/en/security/keys/cmek-unity-catalog) on your system catalog to manage the encryption key. Configuring a CMK on the system catalog encrypts all data in the system catalog, not just custom classifier data.

![Configure a customer-managed key on the system catalog in Catalog Explorer.](https://docs.databricks.com/aws/en/assets/images/data-classification-custom-classifier-system-catalog-cmk-3b363fbf9188461e0bc8bf3f9e93f2ce.png)

## Requirements[​](#requirements "Direct link to Requirements")

*   Data Classification must be enabled on at least one catalog in the metastore. See [Use data classification](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-classification#use-data-classification).
*   Your workspace must have [serverless compute](https://docs.databricks.com/aws/en/compute/serverless/) available (enabled by default in workspaces with Unity Catalog).
*   To create, edit, or delete a custom classifier, you must be a metastore admin.
*   To create or edit a custom classifier, you must have `ASSIGN` privileges on the governed tag the classifier uses. See [Manage permissions on governed tags](https://docs.databricks.com/aws/en/admin/governed-tags/manage-permissions).
*   To select a column for the classifier, you must have `SELECT` on the table that contains it.

## Create a custom classifier[​](#create-a-custom-classifier "Direct link to Create a custom classifier")

1.  From the Data Classification results page, click **Manage custom classifiers**.
    
    ![Manage custom classifiers button on the Data Classification results page.](https://docs.databricks.com/aws/en/assets/images/data-classification-custom-classifier-manage-button-27dea39992ed593d73cac1fbf16c8f27.png)
    
2.  In the **Manage custom classifiers** side panel, click **Create custom classifier**.
    
3.  **Select a tag**. Choose an existing governed tag, or click **Create new tag** to define one inline. If the tag has allowed values, choose the specific value you want to detect.
    
    ![Create custom classifier wizard step 1: select a governed tag.](https://docs.databricks.com/aws/en/assets/images/data-classification-custom-classifier-create-step1-a468e72999b15db556d3fb12809f5da7.png)
    
4.  **Select example columns**. Browse the catalog tree and select columns that contain representative values for the class. Choose columns whose values are typical of what you want detected — broader and more varied examples produce more accurate detection rules.
    
    ![Create custom classifier wizard step 2: select example columns.](https://docs.databricks.com/aws/en/assets/images/data-classification-custom-classifier-create-step2-c79e11ae55a3e1ba8853e642143dd6fe.png)
    
5.  Click **Create**.
    

Detections from the custom classifier typically appear on the results page within a few hours.

note

A custom classifier applies to **all** catalogs in the metastore that have Data Classification enabled. Per-catalog or per-schema scoping is not supported.

## Manage custom classifiers[​](#manage-custom-classifiers "Direct link to Manage custom classifiers")

The **Manage custom classifiers** side panel lists all custom classifiers configured for the metastore. From this panel, you can search by tag name, edit the example columns of an existing classifier, or delete a classifier.

![Custom classifier list in the Manage custom classifiers side panel.](https://docs.databricks.com/aws/en/assets/images/data-classification-custom-classifier-list-5e8f907147c97130c46ac5146980dc02.png)

### Edit a custom classifier[​](#edit-a-custom-classifier "Direct link to Edit a custom classifier")

To update the example columns for an existing custom classifier:

1.  In the **Manage custom classifiers** side panel, select the custom classifier you want to edit.
2.  Click **Edit** next to the example columns list.
3.  Add or remove columns. The example column limit still applies.
4.  Click **Save**.

Updates take effect within a few hours. Existing detections from the previous configuration remain in place.

The governed tag and tag value cannot be changed after a custom classifier is created. To switch to a different tag, delete the custom classifier and create a new one.

### Delete a custom classifier[​](#delete-a-custom-classifier "Direct link to Delete a custom classifier")

1.  In the **Manage custom classifiers** side panel, select the custom classifier you want to delete.
2.  Click **Delete**.
3.  Confirm the deletion.
4.  Confirm that the classifier is removed from the **Manage custom classifiers** side panel.

When you delete a custom classifier:

*   No new detections are produced for that classifier.
*   Existing detections are removed from the Data Classification results page.
*   Tags that were already auto-applied to columns are not removed automatically.

### Suspended custom classifiers[​](#suspended-custom-classifiers "Direct link to Suspended custom classifiers")

If rule generation or validation fails, Databricks suspends the custom classifier and shows a warning on the Data Classification results page. A suspended custom classifier produces no new detections.

![Warning showing that one or more custom classifiers are suspended.](https://docs.databricks.com/aws/en/assets/images/data-classification-custom-classifier-suspended-warning-265378e7bb46e77fe26396a365144920.png)

To resolve a suspension, edit the custom classifier and replace example columns that are inaccessible or not representative enough. If the governed tag or tag value is no longer valid, delete the custom classifier and create a new one with a valid tag.

## View custom classifier detections[​](#view-custom-classifier-detections "Direct link to View custom classifier detections")

To view custom classifier detections, follow the same steps as for built-in classifications. See [View classification results](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-classification#view-classification-results).

## Limitations[​](#limitations "Direct link to Limitations")

*   You can create a maximum of 50 custom classifiers per metastore.
*   Each custom classifier must reference between 1 and 10 example columns to provide sufficient data for classification.
*   Governed tag naming is subject to [Tag Policy rules](https://docs.databricks.com/aws/en/admin/governed-tags/).
*   Custom classifiers apply to all Data Classification-enabled catalogs in the metastore. Per-catalog or per-schema scoping is not supported.
*   The governed tag used by a custom classifier cannot be changed after creation. To use a different tag, delete and recreate the custom classifier.
*   New and updated custom classifiers apply only to subsequent Data Classification scans. Existing scan results are not automatically reclassified, so detections for previously scanned data appear after the next scan completes.
*   All Data Classification limitations apply to custom classifiers as well, including supported table types. See [Limitations](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-classification#limitations).

## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

The following topics help you troubleshoot common issues with custom classifiers.

### A custom classifier is suspended[​](#a-custom-classifier-is-suspended "Direct link to A custom classifier is suspended")

Common causes include:

*   One or more example columns reference tables that have been deleted or renamed since the classifier was created.
*   The example columns are not representative enough for the system to learn a stable detection.
*   The governed tag is no longer a governed tag, or the tag value is no longer valid.

To resolve, edit the custom classifier with a different set of example columns and wait for the next scan. If the suspension is caused by an invalid governed tag or tag value, delete the custom classifier and create a new one with a valid tag.

### Permission denied when creating or listing custom classifiers[​](#permission-denied-when-creating-or-listing-custom-classifiers "Direct link to Permission denied when creating or listing custom classifiers")

You must be a metastore admin. Creating or editing a custom classifier additionally requires `ASSIGN` privileges on the governed tag. See [Requirements](#requirements).

### Cannot select an example column[​](#cannot-select-an-example-column "Direct link to Cannot select an example column")

You must have `SELECT` on the table that contains the column. If you do not have `SELECT` on the table, ask the table owner to grant it, or choose a different example column.

*   [Data Classification](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-classification)
*   [Supported classification tags](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-classification-tags)
*   [Governed tags](https://docs.databricks.com/aws/en/admin/governed-tags/)
*   [Attribute-based access control in Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/)
*   [Data classification system table reference](https://docs.databricks.com/aws/en/admin/system-tables/data-classification)
