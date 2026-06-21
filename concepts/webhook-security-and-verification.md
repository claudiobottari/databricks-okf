---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: dd8a6dfc3c1f7609a81ae322fd0de285337069dfe34916eb9296a99f56cbb0f3
  pageDirectory: concepts
  sources:
    - workspace-model-registry-webhooks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - webhook-security-and-verification
    - Verification and Webhook Security
    - WSAV
    - Webhook Security
  citations:
    - file: workspace-model-registry-webhooks-databricks-on-aws.md
title: Webhook Security and Verification
description: Security measures including HMAC-SHA256 signature (X-Databricks-Signature header), optional Authorization header, and client-side verification to validate webhook origin.
tags:
  - databricks
  - security
  - hmac
  - authentication
timestamp: "2026-06-19T23:27:47.494Z"
---

# Webhook Security and Verification

**Webhook Security and Verification** refers to the mechanisms used to confirm that incoming webhook requests from the [Workspace Model Registry](/concepts/workspace-model-registry.md) are legitimate and originated from Databricks, rather than from a malicious third party. These safeguards protect automated ML pipeline integrations that rely on webhook-triggered actions.

## Shared Secret Verification

The primary verification mechanism is the **shared secret** associated with each webhook. When a shared secret is set during webhook creation, Databricks includes an `X-Databricks-Signature` header in every outgoing HTTP request. This header contains an HMAC (Hash-Based Message Authentication Code) of the request payload, computed using the SHA-256 algorithm with the shared secret as the key. The receiving client must then verify the payload’s integrity by re-computing the HMAC on its side and comparing the result with the value in the `X-Databricks-Signature` header. ^[workspace-model-registry-webhooks-databricks-on-aws.md]

This verification is particularly important when SSL certificate validation is disabled (i.e., when the `enable_ssl_verification` field is set to `false`), because without HTTPS certificate checks the channel is more vulnerable to interception. ^[workspace-model-registry-webhooks-databricks-on-aws.md]

## Client Verification Process

A typical server‑side verification implementation follows these steps:

1.  Extract the shared secret from the webhook configuration.
2.  Read the `X-Databricks-Signature` header from the incoming request.
3.  Encode the raw HTTP request body as UTF‑8 bytes.
4.  Compute an HMAC‑SHA‑256 digest over those bytes using the shared secret.
5.  Compare the computed hex digest with the value in the header using a **constant‑time comparison** (e.g., `hmac.compare_digest`) to prevent timing‑side‑channel attacks.

If the two values do not match, the request is rejected as untrusted. ^[workspace-model-registry-webhooks-databricks-on-aws.md]

The Python reference code provided by Databricks follows this pattern:

```python
import hmac
import hashlib
import json

secret = shared_secret.encode('utf-8')
signature_key = 'X-Databricks-Signature'

def validate_signature(request):
    if not request.headers.has_key(signature_key):
        raise Exception('No X-Signature. Webhook not be trusted.')
    x_sig = request.headers.get(signature_key)
    body = request.body.encode('utf-8')
    h = hmac.new(secret, body, hashlib.sha256)
    computed_sig = h.hexdigest()
    if not hmac.compare_digest(computed_sig, x_sig.encode()):
        raise Exception('X-Signature mismatch. Webhook not be trusted.')
```

^[workspace-model-registry-webhooks-databricks-on-aws.md]

## Authorization Header Verification

In addition to the HMAC‑based signature, webhooks can include a **standard `Authorization` header** in outgoing requests by specifying the `authorization` field in the `HttpUrlSpec` of the webhook. When this header is set, the receiving client should verify the bearer token or other authorization credentials contained in the `Authorization` header to confirm the request’s origin. ^[workspace-model-registry-webhooks-databricks-on-aws.md]

## Payload Content and Limitations

The verification mechanisms protect the authenticity of the request, but the payload itself is **not encrypted**. Sensitive information such as artifact path locations is excluded from the payload; users and principals with appropriate access control lists (ACLs) can retrieve that information separately via the Model Registry REST API. ^[workspace-model-registry-webhooks-databricks-on-aws.md]

## Related Concepts

- [Workspace Model Registry](/concepts/workspace-model-registry.md) — The model registry that emits webhook events.
- [Model Registry Webhooks](/concepts/workspace-model-registry-webhooks.md) — Overview of how webhooks are created, managed, and triggered.
- HMAC — The cryptographic hash function used for signature computation.
- HTTPS — The transport layer that, combined with SSL verification, provides a baseline of security.
- [Audit logging](/concepts/abac-policy-audit-logging.md) — Records of webhook actions that can help with security forensics.

## Sources

- workspace-model-registry-webhooks-databricks-on-aws.md

# Citations

1. [workspace-model-registry-webhooks-databricks-on-aws.md](/references/workspace-model-registry-webhooks-databricks-on-aws-d8277741.md)
