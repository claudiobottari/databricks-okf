---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7c188fbd3628bb8edd77cf7ed4065d05a5ca14fdfcc0528464928c7ba7a1d279
  pageDirectory: concepts
  sources:
    - monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - secureconnect-billing-for-data-transfer
    - SBFDT
  citations:
    - file: monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md
title: SecureConnect Billing for Data Transfer
description: Databricks SecureConnect feature that bills data transfer through Databricks rather than the cloud vendor, providing an alternative billing model for egress costs.
tags:
  - delta-sharing
  - secure-connect
  - billing
  - cost-management
timestamp: "2026-06-19T19:45:43.588Z"
---

---
title: SecureConnect Billing for Data Transfer
summary: When using SecureConnect, Databricks bills the data transfer costs directly, instead of the cloud vendor charging egress fees.
sources:
  - monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T21:00:00.000Z"
updatedAt: "2026-06-19T21:00:00.000Z"
tags:
  - databricks
  - delta-sharing
  - billing
  - egress
aliases:
  - secureconnect-billing-for-data-transfer
  - scbdt
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# SecureConnect Billing for Data Transfer

**SecureConnect Billing for Data Transfer** refers to the billing model applied when sharing data through OpenSharing with [SecureConnect](https://docs.databricks.com/aws/en/delta-sharing/secureconnect-provider#billing). Instead of the cloud vendor charging data egress fees (which are common when data crosses cloud boundaries or regions), Databricks directly bills the data transfer. ^[monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md]

This billing arrangement is part of the tools Databricks provides to help providers monitor and manage egress costs. When SecureConnect is used, providers no longer incur cloud vendor egress charges for data shared via OpenSharing; costs appear on the Databricks bill rather than on the infrastructure provider's invoice. ^[monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md]

## Related Concepts

- [OpenSharing](/concepts/opensharing.md) – The Delta Sharing protocol under which data is shared.
- Egress cost management – Broader strategies for controlling cross‑cloud data transfer expenses.
- [SecureConnect](/concepts/secureconnect.md) – The Databricks feature that enables private connectivity for sharing.
- [OpenSharing Egress Pipeline Notebooks](/concepts/opensharing-egress-pipeline-notebooks.md) – Tools that monitor egress usage patterns and costs.

## Sources

- monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md

# Citations

1. [monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md](/references/monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws-13b884c0.md)
