---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 01f708dc19830b062718225952b70d4ac8040d9fdeebb318eea0805364c88869
  pageDirectory: concepts
  sources:
    - graph-and-network-analysis-on-databricks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - degree-and-degree-distribution
    - Degree Distribution and Degree
    - DADD
    - Degree Distribution
    - Degree distribution
    - Node Degree|Degree
  citations:
    - file: graph-and-network-analysis-on-databricks-databricks-on-aws.md
title: Degree and Degree Distribution
description: Degree is the number of edges incident to a node (with in-degree and out-degree for directed graphs); degree distribution describes the count of nodes at each degree level, revealing network structure and organization.
tags:
  - graph-analysis
  - fundamentals
  - metrics
timestamp: "2026-06-19T19:02:14.709Z"
---

# Degree and Degree Distribution

**Degree** and **Degree Distribution** are fundamental concepts in [Graph and Network Analysis](/concepts/graph-and-network-analysis.md) that describe the connectivity of nodes within a network. The degree measures how many connections a node has, while the degree distribution characterizes the overall structure and organization of the network.

## Degree

The **degree** of a node is the number of edges that link to it. For example, in a simple graph representing six European countries connected by shared borders, the node representing "France" has a degree of 4, meaning it shares a border with four other countries in the network. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

For directed graphs, where edges represent one-way relationships, degree is further divided into two measures:

- **In-degree**: The number of edges coming into the node.
- **Out-degree**: The number of edges pointing away from the node.

^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

## Degree Distribution

The **degree distribution** of a network is the count of nodes of each degree value. It describes how connectivity is spread across all nodes in the network. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

The degree distribution provides information about the structure and organization of the network. For example, some networks may have many nodes with low degree and a few nodes with very high degree (often called "hub" nodes), while other networks may have a more uniform distribution of connections. Understanding the degree distribution is essential for analyzing network properties such as robustness, information flow, and clustering behavior. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

## Related Concepts

- [Graph and Network Analysis](/concepts/graph-and-network-analysis.md)
- [Nodes and Edges](/concepts/nodes-and-edges.md)
- [Directed and Undirected Networks](/concepts/directed-vs-undirected-networks.md)
- [Weighted Edges](/concepts/weighted-edges.md)
- Centrality
- [NetworkX](/concepts/networkx.md) — A Python package for analyzing small to medium-sized networks on a single compute node
- [GraphFrames](/concepts/graphframes.md) — A distributed graph processing library for large-scale networks

## Sources

- graph-and-network-analysis-on-databricks-databricks-on-aws.md

# Citations

1. [graph-and-network-analysis-on-databricks-databricks-on-aws.md](/references/graph-and-network-analysis-on-databricks-databricks-on-aws-73e6c5fc.md)
