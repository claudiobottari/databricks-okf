---
title: Foundation model Unity Catalog permissions | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/model-uc-permissions
ingestedAt: "2026-06-18T08:11:07.478Z"
---

important

Foundation model Unity Catalog permissions is [generally available](https://docs.databricks.com/aws/en/release-notes/release-types) but requires enablement. Reach out to your Databricks account team to enable this feature. After enablement, see [Manage account-level previews](https://docs.databricks.com/aws/en/admin/workspace-settings/manage-previews#account) for how account admins can control access to this feature.

This page describes when and how account admins use foundation model Unity Catalog permissions to restrict which Databricks-hosted foundation models your organization can access. Admins can block specific models account-wide or grant model access to specific groups or users. The enforcement applies consistently across pay-per-token, provisioned throughput, and batch inference (AI Functions) workloads.

## When to use foundation model Unity Catalog permissions[​](#when-to-use-foundation-model-unity-catalog-permissions "Direct link to when-to-use-foundation-model-unity-catalog-permissions")

Use this feature only when legally required to restrict which specific models are open, such as:

*   Export-controlled model families
*   Vendor-restricted or region-restricted models
*   Corporate policies prohibiting specific foundation models

For day-to-day governance, use:

*   `system.billing` for cost tracking and attribution
*   [AI Gateway](https://docs.databricks.com/aws/en/ai-gateway/) for rate limits and request-level usage tracking
*   Private Link or private networking for secure connectivity
*   Egress and network controls for restricting outbound traffic

## How foundation model Unity Catalog permissions work[​](#how-foundation-model-unity-catalog-permissions-work "Direct link to how-foundation-model-unity-catalog-permissions-work")

Foundation model Unity Catalog permissions use Unity Catalog permissions on the `system.ai` schema and individual model objects. By default, all users have `EXECUTE` permission on the `system.ai` schema, which opens all Databricks-hosted foundation models to users.

To restrict which models are open to users, admins remove the default `EXECUTE` permission from the schema and then selectively grant it on approved individual models. The system enforces permissions consistently across:

*   **Pay-per-token** endpoints — automatically enforced
*   **Batch inference (AI Functions)** — automatically enforced
*   **Provisioned throughput** endpoints — require manual deletion of disallowed endpoints

The following sections provide step-by-step instructions for how to enforce model restrictions.

## Requirements[​](#requirements "Direct link to Requirements")

*   Unity Catalog must be enabled for your account.
*   Account admin or Unity Catalog admin privileges.
*   The feature must be enabled for your account. Reach out to your Databricks account team to enable it.

## Step 1: Remove EXECUTE permission from the schema[​](#step-1-remove-execute-permission-from-the-schema "Direct link to step-1-remove-execute-permission-from-the-schema")

Removing `EXECUTE` from the `system.ai` schema clears all default access to models. No user can invoke any model until permissions are explicitly re-granted.

1.  Go to **Catalog**. Select the **system** catalog, then the **ai** schema. Click the **Permissions** tab.
2.  Revoke `EXECUTE` from **All Users** (or from all groups).

important

After you remove `EXECUTE` from the schema, pay-per-token and batch inference (AI Functions) calls to all models stop immediately. Provisioned throughput endpoints continue serving until manually deleted.

## Step 2: Grant `EXECUTE` on approved models[​](#step-2-grant-execute-on-approved-models "Direct link to step-2-grant-execute-on-approved-models")

For each model your organization approves, selectively grant `EXECUTE` privilege.

1.  In Catalog Explorer, under the **system** catalog, select **ai** > **models**, then your target model.
2.  Click the **Permissions** tab.
3.  Grant `EXECUTE` to **All Users**, or to specific groups.

Repeat for each approved model. This creates an allow-list of permitted models.

## Step 3: Remove disallowed provisioned throughput endpoints[​](#step-3-remove-disallowed-provisioned-throughput-endpoints "Direct link to Step 3: Remove disallowed provisioned throughput endpoints")

Delete all provisioned throughput endpoints that serve a disallowed model. Active endpoints continue serving until removed.

Pay-per-token and batch inference (AI Functions) endpoints automatically enforce the new permissions. Provisioned throughput endpoints do not, so you must manually delete the disallowed endpoints.

## Limitations[​](#limitations "Direct link to Limitations")

*   **Agent Bricks Knowledge Assistant**: Knowledge Assistant does not support foundation model Unity Catalog permissions. Contact your Databricks account team before enabling this feature if you actively use Knowledge Assistant.

## Additional resources[​](#additional-resources "Direct link to Additional resources")

*   [Databricks Foundation Model APIs](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/)
*   [Foundation Model APIs compliance and security](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/compliance)
*   [Unity AI Gateway](https://docs.databricks.com/aws/en/ai-gateway/)
