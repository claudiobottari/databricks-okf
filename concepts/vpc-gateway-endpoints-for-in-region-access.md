---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5224e7158efe5748147d96af15264de235a8c675550ade4ad123096e85b677a4
  pageDirectory: concepts
  sources:
    - monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - vpc-gateway-endpoints-for-in-region-access
    - VGEFIA
  citations:
    - file: monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md
title: VPC Gateway Endpoints for In-Region Access
description: Best practice recommendation for recipients to use VPC gateway endpoints or interface endpoints for S3 instead of NAT gateways when accessing shared data in-region to reduce costs and enhance security.
tags:
  - delta-sharing
  - networking
  - aws
  - security
timestamp: "2026-06-19T19:45:46.571Z"
---

# VPC Gateway Endpoints for In-Region Access

**VPC Gateway Endpoints for In-Region Access** are AWS VPC endpoints that provide private connectivity to Amazon S3 and other supported services without traversing a NAT gateway, internet gateway, or VPN connection. In the context of [OpenSharing](/concepts/opensharing.md) (Delta Sharing), using VPC gateway endpoints—or S3 interface endpoints—is a recommended best practice for recipients who access shared data stored in the same AWS region as the provider. ^[monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md]

## Benefits

When OpenSharing recipients use VPC gateway endpoints instead of NAT gateways for in-region storage access, they can:

* **Reduce costs** – Data transfer through a NAT gateway incurs per-GB processing charges. Gateway endpoints are free for data transfer within the same region, eliminating those egress fees. ^[monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md]
* **Enhance security** – Traffic stays within the AWS network and never leaves the VPC, avoiding exposure to the public internet. ^[monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md]

## Recommended Usage

Databricks recommends that recipients of OpenSharing shares always use VPC gateway endpoints or interface endpoints for S3 whenever the storage is in the same region as the recipient’s compute environment. This applies to any in-region read of shared data, such as when a recipient queries a view or table that resides in the provider’s S3 bucket. ^[monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md]

For cross-region or cross-cloud access, egress costs are incurred regardless of endpoint type; in those scenarios, other cost-management strategies (such as data replication or using Cloudflare R2) are more appropriate.

## Related Concepts

- VPC Endpoint – General AWS mechanism for private connectivity.
- S3 Gateway Endpoint – A specific type of VPC endpoint for S3.
- NAT Gateway – The alternative that incurs egress charges.
- OpenSharing Egress Costs – Broader topic of monitoring and managing data transfer costs for Delta Sharing.
- AWS PrivateLink – Underlying technology for interface endpoints.
- In-Region Data Transfer – Zero-cost data movement within an AWS region.

## Sources

- monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md

# Citations

1. [monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws.md](/references/monitor-and-manage-opensharing-egress-costs-for-providers-databricks-on-aws-13b884c0.md)
