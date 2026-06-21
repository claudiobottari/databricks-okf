---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ca5d2b6fbcb9279fee9e92338012accc916786cd2eb885de9402fd988ab61c87
  pageDirectory: concepts
  sources:
    - best-practices-for-abac-policies-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - auditing-direct-grants-and-abac-grant-policies
    - ABAC GRANT Policies and Auditing Direct Grants
    - ADGAAGP
    - ABAC GRANT policies for models|ABAC GRANT policies
  citations:
    - file: best-practices-for-abac-policies-databricks-on-aws.md
title: Auditing Direct Grants and ABAC GRANT Policies
description: The need to audit both direct grants and ABAC GRANT policies together since effective privileges are the union of both
tags:
  - abac
  - auditing
  - unity-catalog
  - access-control
timestamp: "2026-06-19T14:09:19.062Z"
---

---

title: Auditing Direct Grants and ABAC GRANT Policies
summary: Why you must review both direct grants and ABAC GRANT policies together to avoid hidden unintended permissions.
sources:
  - best-practices-for-abac-policies-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T12:26:53.977Z"
updatedAt: "2026-06-18T12:26:53.977Z"
tags:
  - databricks
  - unity-catalog
  - abac
  - access-control
  - audit
aliases:
  - auditing-direct-grants-and-abac-grant-policies
  - ADGAGP
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Auditing Direct Grants and ABAC GRANT Policies

## Overview

Auditing **direct grants** and **ABAC GRANT policies** together is a critical governance practice in [Unity Catalog](/concepts/unity-catalog.md). A user's effective privileges on a data object are the **union** of both mechanisms. Reviewing only one surface can lead to overlooking permissions that were granted through the other, potentially exposing data unintentionally. ^[best-practices-for-abac-policies-databricks-on-aws.md]

## The Union of Privileges

Direct grants — the traditional assignment of privileges to a user or group — and [ABAC GRANT Policies](/concepts/abac-grant-policies.md) (currently in Beta) both contribute to the final set of permissions a principal holds on a Unity Catalog object. Because the system computes effective access as the combination of these two sources, neither can be ignored during an access review. ^[best-practices-for-abac-policies-databricks-on-aws.md]

## The Risk of One-Sided Auditing

If an auditor checks only direct grants, they might miss permissions that were added through a tag-based ABAC GRANT policy. Conversely, checking only ABAC GRANT policies could hide direct grant permissions that were assigned explicitly. In either case, unintended permissions can remain undetected. ^[best-practices-for-abac-policies-databricks-on-aws.md]

## Best Practices

- **Always review both surfaces** when performing a security audit or recertification.
- Use the `SHOW EFFECTIVE POLICIES` command (see Dynamic policy evaluation) to see the combined effect of direct grants and ABAC policies on a specific object.
- Document the tag taxonomy and policy scopes so that auditors understand which ABAC GRANT policies might apply.

For detailed guidance on creating and managing ABAC GRANT policies, see [ABAC GRANT policies for models (Beta)](/concepts/abac-grant-policies.md). ^[best-practices-for-abac-policies-databricks-on-aws.md]

## Related Concepts

- Direct grants
- [ABAC GRANT Policies](/concepts/abac-grant-policies.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- Dynamic policy evaluation
- Access control auditing
- Tag-based governance

## Sources

- best-practices-for-abac-policies-databricks-on-aws.md

# Citations

1. [best-practices-for-abac-policies-databricks-on-aws.md](/references/best-practices-for-abac-policies-databricks-on-aws-716fb4af.md)
