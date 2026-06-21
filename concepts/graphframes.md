---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e4ff03f54c90cb4ef2b3f5ebbd39e56e46fe8a5203fe5f76309919fa31171561
  pageDirectory: concepts
  sources:
    - graph-and-network-analysis-on-databricks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - graphframes
  citations:
    - file: graph-and-network-analysis-on-databricks-databricks-on-aws.md
title: GraphFrames
description: Distributed graph processing library for Apache Spark used on Databricks for large-scale network analysis
tags:
  - graph-analysis
  - distributed-computing
  - apache-spark
timestamp: "2026-06-19T10:46:00.933Z"
---

# GraphFrames

**GraphFrames** is an open-source library for graph processing on distributed clusters, built on top of Apache Spark. It provides a DataFrame-based API for representing and analyzing large-scale graphs. Databricks includes GraphFrames in [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) as the recommended solution for graph workloads that require distributed processing across multiple nodes. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

## Overview

GraphFrames is designed for networks that are too large to be processed on a single machine. It supports common graph algorithms such as PageRank, shortest paths, connected components, and triangle counting, all executed in a distributed fashion using Spark’s engine. Graphs are represented as two DataFrames: a **vertex DataFrame** containing node identifiers and optional attributes, and an **edge DataFrame** containing source, destination, and optional edge properties. This integration with Spark DataFrames allows users to combine graph analysis with other data processing and machine learning workflows.

## Comparison with NetworkX

For smaller networks that can fit in memory on a single node, Databricks recommends using [NetworkX](/concepts/networkx.md), which is also included in Databricks Runtime ML. For large networks that require distributed processing, GraphFrames is the appropriate choice. The selection depends on the scale of the data and the need for parallelism. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

## Availability

GraphFrames is available as part of Databricks Runtime ML. Users can also install additional open-source graph packages as needed or connect to external tools for visualization. Documentation for integrating GraphFrames with Databricks is provided in the official [integration guide](https://docs.databricks.com/aws/en/integrations/graphframes/). ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

## Related Concepts

- [NetworkX](/concepts/networkx.md) – Single-node graph analysis library
- Distributed computing – Foundation for GraphFrames’ scalability
- [Graph analysis](/concepts/graph-and-network-analysis.md) – Broader domain of graph and network analysis
- Apache Spark – Underlying distributed processing engine
- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) – Environment that includes GraphFrames

## Sources

- graph-and-network-analysis-on-databricks-databricks-on-aws.md

# Citations

1. [graph-and-network-analysis-on-databricks-databricks-on-aws.md](/references/graph-and-network-analysis-on-databricks-databricks-on-aws-73e6c5fc.md)
