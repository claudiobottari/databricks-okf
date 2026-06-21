---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 38467098aa5bbe35e62dc990d77dca36b9dcf3a8a8689ec2e849f32764bb1b0d
  pageDirectory: concepts
  sources:
    - databricks-connect-for-python-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-troubleshooting-and-limitations
    - limitations and Databricks Connect troubleshooting
    - DCTAL
  citations:
    - file: databricks-connect-for-python-databricks-on-aws.md
title: Databricks Connect troubleshooting and limitations
description: Known troubleshooting guidance and limitations when using Databricks Connect.
tags:
  - databricks
  - troubleshooting
  - limitations
timestamp: "2026-06-19T18:09:45.244Z"
---

# Databricks Connect Troubleshooting and Limitations

**Databricks Connect** enables you to connect popular IDEs such as PyCharm, notebook servers, and other custom applications to Databricks compute. This page covers common troubleshooting scenarios and known limitations when using Databricks Connect for Python (Databricks Runtime 13.3 LTS and above). ^[databricks-connect-for-python-databricks-on-aws.md]

## Troubleshooting

When encountering issues with Databricks Connect, refer to the official [troubleshooting documentation](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/python/troubleshooting) for detailed guidance. Common problem areas include:

- **Connection failures**: Verify that your workspace and local development environment meet the [Databricks Connect usage requirements](/concepts/databricks-connect-usage-requirements.md) and that the Databricks Connect package version is compatible with your configuration. ^[databricks-connect-for-python-databricks-on-aws.md]
- **Compute configuration issues**: Ensure your compute is properly configured for Databricks Connect. See [Compute configuration for Databricks Connect](/concepts/compute-configuration-for-databricks-connect.md) for details. ^[databricks-connect-for-python-databricks-on-aws.md]
- **Authentication problems**: Check that your authentication credentials are correctly set up and have the necessary permissions to access the target cluster or serverless compute. ^[databricks-connect-for-python-databricks-on-aws.md]

## Known Limitations

Databricks Connect for Python (Databricks Runtime 13.3 LTS and above) has the following known limitations. For the most current and comprehensive list, refer to the official [limitations documentation](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/python/limitations). ^[databricks-connect-for-python-databricks-on-aws.md]

### General Limitations

- Not all Spark features and APIs may be available through Databricks Connect. Some operations that work directly on a cluster may behave differently when executed through the remote connection. ^[databricks-connect-for-python-databricks-on-aws.md]
- Performance may differ from running code directly on a cluster due to network latency and serialization overhead. ^[databricks-connect-for-python-databricks-on-aws.md]

### Version Compatibility

- Databricks Connect requires that the client-side package version is compatible with the Databricks Runtime version running on the target compute. Mismatched versions can cause unexpected errors or feature unavailability. ^[databricks-connect-for-python-databricks-on-aws.md]

### Migration Considerations

- If you are migrating from Databricks Connect for Databricks Runtime 12.2 LTS and below to Databricks Connect for Databricks Runtime 13.3 LTS and above, see [Migrate to Databricks Connect for Python](/concepts/databricks-connect-for-python.md) for important changes and migration steps. ^[databricks-connect-for-python-databricks-on-aws.md]

## Best Practices

To minimize issues when using Databricks Connect:

- Always use a compatible version of the Databricks Connect package for your target Databricks Runtime. ^[databricks-connect-for-python-databricks-on-aws.md]
- Test your code on a small dataset first to verify connectivity and behavior before scaling up. ^[databricks-connect-for-python-databricks-on-aws.md]
- Review the [Code examples for Databricks Connect for Python](/concepts/databricks-connect-for-python.md) and the [example applications repository](https://github.com/databricks-demos/dbconnect-examples) for patterns that work well with remote execution. ^[databricks-connect-for-python-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect for Scala](/concepts/databricks-connect-for-scala.md)
- [Databricks Connect for R](/concepts/databricks-connect-for-r.md)
- [Databricks Utilities with Databricks Connect for Python](/concepts/databricks-utilities-with-databricks-connect.md)
- [Serverless compute](/concepts/serverless-gpu-compute.md)
- Classic compute

## Sources

- databricks-connect-for-python-databricks-on-aws.md

# Citations

1. [databricks-connect-for-python-databricks-on-aws.md](/references/databricks-connect-for-python-databricks-on-aws-669513ea.md)
