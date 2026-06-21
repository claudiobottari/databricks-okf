---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7250ac449e8008a1bd1c27076607f568422502def320e43f3542a2bc089c7aab
  pageDirectory: concepts
  sources:
    - graph-and-network-analysis-on-databricks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - graph-processing-on-databricks
    - GPOD
  citations:
    - file: graph-and-network-analysis-on-databricks-databricks-on-aws.md
title: Graph Processing on Databricks
description: "Databricks provides capabilities for graph analysis at any scale: NetworkX for single-node processing of small networks, GraphFrames for distributed processing of large networks, and the ability to install additional open-source or third-party tools."
tags:
  - databricks
  - graph-analysis
  - tools
timestamp: "2026-06-19T19:02:24.458Z"
---

# Graph Processing on Databricks

**Graph Processing on Databricks** refers to the capabilities and tools available on the Databricks platform for analyzing graph-structured data, also commonly called network analysis. Graphs consist of vertices (nodes) connected by edges (links), and are used to model relationships in domains such as social networks, transportation systems, telecommunications, fraud detection, threat detection, and product recommendation. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

## Overview

A graph is a set of vertices connected by edges. Vertices are also known as nodes, while edges may be called links, relationships, or arcs. Real-world examples include social networks representing connections between people, transportation networks showing flight or train routes between cities, and telecommunication networks mapping cables that carry internet traffic between servers. Graph processing is especially powerful when combined with other analytics techniques, including Machine Learning on Databricks. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

## Supported Tools and Libraries

Databricks Runtime ML includes network analysis packages for problems at any scale. The choice of tool depends on the size of the graph and the processing requirements. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

### NetworkX

For relatively small networks that can be processed on a single compute node, Databricks provides [NetworkX](/concepts/networkx.md), a Python library for the creation, manipulation, and study of complex networks. NetworkX is built into Databricks Runtime ML and is suitable for graphs that fit in memory on a single machine. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

### GraphFrames

For large networks that require distributed processing across a cluster, Databricks supports [GraphFrames](/concepts/graphframes.md), a library that provides graph algorithms and queries on top of Apache Spark DataFrames. GraphFrames enables scalable graph processing using the distributed computing power of a Databricks cluster. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

## Core Graph Concepts

### Nodes and Edges

In network analysis, a network (graph) consists of a set of nodes and a set of edges that connect them. Nodes represent the entities being connected, such as people or cities. Edges represent the connections or relationships between them. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

### Directed and Undirected Networks

Edges can represent one-way relationships (directed networks), such as a social media follower, or two-way relationships (undirected networks), such as coworkers. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

### Weighted Edges

Edges can have weights associated with them, representing properties such as the carrying capacity of a highway or cable. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

### Degree

The degree of a node is the number of edges that connect to it. In directed graphs, in-degree and out-degree are distinguished as the number of edges coming into and pointing away from the node, respectively. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

## Network and Node Properties

### Shortest Path

The shortest path is the minimum distance between two nodes, considering directional links and optionally edge weights. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

### Centrality

Centrality measures the importance of a node within a network. Different centrality measures exist:

- **Degree centrality**: Based on the fraction of nodes a given node is directly connected to.
- **Betweenness centrality**: The fraction of shortest paths in a network that pass through a given node.

^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

### Degree Distribution

The degree distribution of a network describes the number of nodes of each degree, providing information about the network's structure and organization. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

### Diameter

The diameter of a network is the maximum shortest path between any two nodes, equivalent to the maximum eccentricity of nodes in the network. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

### Density

Graph density is the number of edges in the graph divided by the total number of possible edges. For undirected graphs, total possible edges are n(n-1)/2; for directed graphs, total possible edges are n(n-1), where n is the number of nodes. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

### Small-World Networks

Most real-world networks exhibit structured patterns rather than random connections. The small-world phenomenon describes networks with closely linked subgroups and short average path lengths between nodes. These patterns often lead to data skew challenges when processing large graphs. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

## Extensibility

Beyond the built-in tools, users can install additional open-source graph processing packages as needed or connect to external partners and tools for graph processing and visualization. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

## Related Concepts

- [GraphFrames](/concepts/graphframes.md) — Distributed graph processing library for Apache Spark
- [NetworkX](/concepts/networkx.md) — Single-node graph analysis library
- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) — ML-optimized runtime that includes graph packages
- Apache Spark — Distributed computing framework underlying GraphFrames
- Fraud Detection — Common graph processing application on Databricks
- Recommendation Systems — Application leveraging graph analysis

## Example Notebook

Databricks provides example notebooks that use the NetworkX package to illustrate basic network analysis concepts. These notebooks can be run directly in a Databricks workspace. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

## Sources

- graph-and-network-analysis-on-databricks-databricks-on-aws.md

# Citations

1. [graph-and-network-analysis-on-databricks-databricks-on-aws.md](/references/graph-and-network-analysis-on-databricks-databricks-on-aws-73e6c5fc.md)
