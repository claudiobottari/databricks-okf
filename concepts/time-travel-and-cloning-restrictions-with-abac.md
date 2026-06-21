---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a2bae07669eb4b8fd9839d33f874997a97a48bb8eb7d92bf24bd2a22c3d86624
  pageDirectory: concepts
  sources:
    - requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - time-travel-and-cloning-restrictions-with-abac
    - Cloning Restrictions with ABAC and Time Travel
    - TTACRWA
  citations:
    - file: requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md
title: Time Travel and Cloning Restrictions with ABAC
description: Time travel queries and clone operations fail on tables with ABAC policies unless the principal is exempted via the EXCEPT clause
tags:
  - access-control
  - unity-catalog
  - time-travel
  - cloning
  - databricks
timestamp: "2026-06-19T20:13:48.169Z"
---

# Time Travel and Cloning Restrictions with ABAC

**Time Travel and Cloning Restrictions with ABAC** refers to the limitations that prevent time travel queries and clone operations on tables protected by [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) row filter or column mask policies in [Unity Catalog](/concepts/unity-catalog.md).

## Overview

ABAC policies cannot be evaluated against historical table snapshots. As a result, time travel queries fail on tables with active row filters or column masks. Additionally, both deep and shallow clones are not supported on tables with ABAC policies. ^[requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Workaround: Exempting Principals

To enable time travel and cloning operations on ABAC-secured tables, create a service principal or group and add it to the policy's `EXCEPT` clause. When a principal is listed in the `EXCEPT` clause, the policy is not evaluated for that identity, allowing these operations to run. ^[requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

### Important Security Consideration

Exempted principals see unfiltered, unmasked data. Only exempt trusted identities such as service principals used for ETL or pipeline workloads. ^[requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

### Example

The following SQL policy masks PII columns for all users except the `etl_service_principal`, which can run time travel queries and clone operations:

```sql
CREATE POLICY mask_pii
ON CATALOG prod
COLUMN MASK prod.governance.mask_value
TO `account users`
EXCEPT `etl_service_principal`
FOR TABLES
MATCH COLUMNS has_tag_value('pii', 'ssn') AS ssn
ON COLUMN ssn;
```

^[requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Related Concepts

- ABAC Limitations — Comprehensive list of all ABAC restrictions
- [Row Filters and Column Masks](/concepts/row-filters-and-column-masks.md) — The underlying access control mechanisms
- [Delta Time Travel](/concepts/delta-lake-time-travel.md) — Feature for querying historical table snapshots
- Clone Operations — Deep and shallow cloning in Delta Lake
- Service Principals — Identity type suitable for exemption
- [Policy Evaluation](/concepts/dynamic-abac-policy-evaluation.md) — How ABAC policies are resolved at runtime

## Sources

- requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md

# Citations

1. [requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws.md](/references/requirements-quotas-and-limitations-for-row-filter-and-column-mask-policies-databricks-on-aws-43ef91f3.md)
