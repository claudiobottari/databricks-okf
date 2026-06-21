---
title: OpenSharing recipient firewall configuration for SecureConnect | Databricks on AWS
source: https://docs.databricks.com/aws/en/delta-sharing/secureconnect-recipient
ingestedAt: "2026-06-18T08:05:48.741Z"
---

This page describes how Databricks recipients access shares from a provider who has enabled OpenSharing SecureConnect.

If your provider has enabled SecureConnect and you have an egress firewall, you must allowlist Databricks inbound IP addresses to access SecureConnect. You allowlist IPs for the provider's cloud and region, regardless of the cloud you are on.

important

Databricks recipients on classic compute and open recipients must allowlist Databricks inbound IP addresses.

Databricks recipients on serverless compute do not need to configure their egress firewall to access SecureConnect. Databricks routes serverless traffic to SecureConnect internally.

For an overview of SecureConnect and provider-side setup, see [Share data behind a firewall with SecureConnect](https://docs.databricks.com/aws/en/delta-sharing/secureconnect-provider).

## Allowlist Databricks inbound IPs[​](#allowlist-databricks-inbound-ips "Direct link to allowlist-databricks-inbound-ips")

Select the cloud your provider is on, then allowlist the listed Databricks inbound IP addresses for the provider's region.

*   AWS
*   Azure
*   GCP

## Limitations[​](#limitations "Direct link to limitations")

The following limitations apply to Databricks recipients accessing SecureConnect-enabled shares:

*   mTLS is not enabled for recipients using classic compute.
*   mTLS is not enabled for OIDC recipients.
*   Serverless Databricks recipients using a Databricks-to-Open credential in the same region as the provider are not supported.
