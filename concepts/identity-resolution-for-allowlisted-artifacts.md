---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4d13ac3694148e8606a873db46afb8478d3b9fc4fab1d53e4f9a77745b0d8e59
  pageDirectory: concepts
  sources:
    - allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md
  confidence: 0.85
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - identity-resolution-for-allowlisted-artifacts
    - IRFAA
  citations:
    - file: allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md
title: Identity Resolution for Allowlisted Artifacts
description: The rule by which the identity used for allowlisted libraries and init scripts is determined — the library installer's identity in standard mode and the assigned principal's identity in dedicated access mode.
tags:
  - unity-catalog
  - identity
  - access-control
timestamp: "2026-06-19T14:00:04.882Z"
---

# Identity Resolution for Allowlisted Artifacts

**Identity Resolution for Allowlisted Artifacts** refers to the process by which Databricks determines the principal (user or service principal) that is checked for data access permissions when an allowlisted library or init script runs on compute with [Standard Access Mode](/concepts/standard-access-mode.md) or dedicated access mode. The identity used affects whether the artifact can read from its storage location (e.g., a Unity Catalog volume or object storage bucket). ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Identity by Access Mode

### Dedicated Access Mode

In dedicated access mode (formerly single user access mode), the identity used for permission checks is the **assigned principal** of the compute resource – either a user or a group. This means that all allowlisted artifacts running on that compute will use that principal’s identity to access data. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

### Standard Access Mode

In standard access mode (formerly shared access mode), the identity used differs depending on the type of artifact:

- **Libraries**: The identity of the **library installer** (the user who installs the library on the cluster) is used when accessing the artifact’s storage location.
- **Init scripts**: The identity of the **cluster owner** (the user who owns the cluster) is used. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

### No-Isolation Shared Access Mode

No-isolation shared access mode does not support Unity Catalog volumes, but the identity assignment for allowlisted artifacts follows the same rules as standard access mode: libraries use the installer’s identity and init scripts use the cluster owner’s identity. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Permission Requirements

Beyond the allowlist itself, the principal whose identity is resolved must have the necessary data permissions to read the artifact’s location. For artifacts stored in Unity Catalog volumes, the principal must have the `READ VOLUME` privilege on the volume. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

Databricks enforces **two independent checks**: the path must be on the allowlist, *and* the resolved identity must have the relevant data access permissions (e.g., `READ VOLUME` for volumes, or appropriate instance profile permissions for S3). ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Best Practices

- **Use read‑only permissions** on storage locations for allowlisted artifacts. Users with write access could modify library or init script code, bypassing governance controls. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]
- **Plan for identity resolution** when designing workflows. For example, if different users install libraries on a standard‑access cluster, each user’s identity must have the necessary permissions to the artifact’s location.
- **Use instance profiles** for S3‑stored artifacts to manage access more granularly, combined with the appropriate IAM roles. ^[allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md]

## Related Concepts

- [Allowlist for Libraries and Init Scripts](/concepts/init-script-and-jar-allowlisting.md) – The mechanism that controls which artifacts can run on standard access mode compute.
- [Standard Access Mode](/concepts/standard-access-mode.md) – A compute access mode that shares resources but requires allowlisting for custom artifacts.
- [Dedicated Access Mode](/concepts/dedicated-access-mode-for-ml-compute.md) – A single‑user compute mode where the assigned principal’s identity is used for all artifact access.
- Unity Catalog Volumes – Storage locations that require `READ VOLUME` permissions for artifact access.
- [MANAGE ALLOWLIST Privilege](/concepts/manage-allowlist-privilege.md) – The privilege required to add or remove items from the allowlist.
- Attribute Usage with Serverless Usage Policies – Related identity model for serverless compute.

## Sources

- allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md

# Citations

1. [allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws.md](/references/allowlist-libraries-and-init-scripts-on-compute-with-standard-access-mode-formerly-shared-access-mode-databricks-on-aws-75a9dfbb.md)
