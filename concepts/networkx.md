---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d9c76ab66f680c2c42351110a8f91538993e7c1c9e5f61695c2fb30d4295b783
  pageDirectory: concepts
  sources:
    - graph-and-network-analysis-on-databricks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - networkx
  citations:
    - file: graph-and-network-analysis-on-databricks-databricks-on-aws.md
title: NetworkX
description: Python library for graph and network analysis suitable for small to medium-sized networks on a single compute node
tags:
  - graph-analysis
  - python
  - network-analysis
timestamp: "2026-06-19T10:46:12.701Z"
---

# NetworkX

**NetworkX** is a Python library for the creation, manipulation, and study of the structure, dynamics, and functions of complex networks. It provides tools for analyzing graphs (also called networks) and is commonly used for tasks ranging from basic network analysis to advanced research in graph theory and network science.

## Overview

[Databricks Runtime ML](/concepts/databricks-runtime-ml.md) includes NetworkX for network analysis at a single-node scale. For relatively small networks that can be processed entirely on one compute node, NetworkX is the recommended choice. For larger networks that require distributed processing across multiple nodes, [GraphFrames](/concepts/graphframes.md) is used instead. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

NetworkX is built into Databricks Runtime for ML, making it straightforward to use within notebooks for graph processing tasks. It can also be used alongside other open source packages or connected to external partners and tools for advanced graph processing and visualization. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

## Core Concepts

NetworkX operates on the fundamental elements of a graph:

- **Nodes (Vertices):** The entities being connected, such as people, cities, or servers. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]
- **Edges (Links):** The connections or relationships between nodes, such as shared borders, co-authorship, or communication links. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

NetworkX supports both [Directed and Undirected Graphs](/concepts/directed-and-undirected-graphs.md). In directed graphs, edges have a one-way relationship; in undirected graphs, edges are bidirectional. Edges can also carry weights, representing quantities like capacity or distance. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

## Analysis Capabilities

NetworkX provides algorithms to compute a wide range of network properties, including:

- **Degree:** The number of edges connected to a node. For directed graphs, in-degree and out-degree are computed separately. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]
- **Shortest Path:** The minimum distance between two nodes, optionally accounting for edge weights and direction. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]
- **Centrality:** Measures of a node's importance, such as degree centrality (fraction of nodes directly connected) and betweenness centrality (fraction of shortest paths passing through a node). ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]
- **Degree Distribution:** The number of nodes of each degree, revealing the structure and organization of the network. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]
- **Diameter:** The maximum shortest path length between any two nodes in the network. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]
- **Density:** The proportion of actual edges to the total possible edges in the graph. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

NetworkX also supports analysis of [Small-world Networks](/concepts/small-world-networks.md), which exhibit closely connected subgroups and short average path lengths — a common pattern in real-world social and communication networks. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

## Use Cases

NetworkX is applied in many domains, including:

- **Social network analysis** – modeling relationships between people.
- **Transportation networks** – analyzing flight, train, or bus connections.
- **Telecommunication networks** – mapping internet traffic between servers.
- Fraud detection and threat detection.
- Product recommendation systems.

Because NetworkX operates on a single node, it is best suited for networks where the entire graph fits in memory. Large-scale distributed graph processing should use [GraphFrames](/concepts/graphframes.md) on Databricks. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

## Example Usage

Databricks provides an example notebook titled "Basic graph analysis using NetworkX" that demonstrates fundamental network analysis concepts with the library. The notebook is available within the Databricks Runtime ML environment. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

## Alternatives

| Tool | Scale | Environment |
|------|-------|-------------|
| NetworkX | Single-node (in-memory) | Databricks Runtime ML |
| [GraphFrames](/concepts/graphframes.md) | Distributed (multi-node) | Databricks (with GraphFrames integration) |

NetworkX is also compatible with other open source packages and external tools for graph processing and visualization. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

## Related Concepts

- Graph theory
- [Graph analytics](/concepts/graph-and-network-analysis.md)
- [Centrality measures](/concepts/centrality-measures-degree-and-betweenness.md)
- [Degree distribution](/concepts/degree-and-degree-distribution.md)
- [Small-world phenomenon](/concepts/small-world-networks.md)
- Fraud detection with graphs

## Sources

- graph-and-network-analysis-on-databricks-databricks-on-aws.md

# Citations

1. [graph-and-network-analysis-on-databricks-databricks-on-aws.md](/references/graph-and-network-analysis-on-databricks-databricks-on-aws-73e6c5fc.md)
