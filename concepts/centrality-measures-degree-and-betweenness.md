---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 12eea82813779024e8da73fdc193e08557f2c8f47b6e6b3a5fbfd0b4962ed4e1
  pageDirectory: concepts
  sources:
    - graph-and-network-analysis-on-databricks-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - centrality-measures-degree-and-betweenness
    - Betweenness) and Centrality Measures (Degree
    - CM(AB
    - Centrality measures
  citations:
    - file: graph-and-network-analysis-on-databricks-databricks-on-aws.md
title: Centrality Measures (Degree and Betweenness)
description: Metrics for measuring the importance of a node within a network, including degree centrality and betweenness centrality
tags:
  - graph-analysis
  - network-science
  - centrality
timestamp: "2026-06-19T10:46:18.766Z"
---

# Centrality Measures (Degree and Betweenness)

**Centrality measures** are quantitative metrics used in [Graph and Network Analysis](/concepts/graph-and-network-analysis.md) to determine the importance or influence of individual nodes within a network. The two most fundamental centrality measures are **degree centrality** and **betweenness centrality**, each capturing a different aspect of a node's role in the network structure.

## Overview

Centrality is a way to measure the importance of a node in a network. Different centrality measures capture different aspects of what makes a node important — for example, how well-connected it is, or how critical it is for information flow between other nodes.^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

## Degree Centrality

**Degree centrality** is based on the fraction of nodes in a network that a given node is directly connected to. It reflects how well-connected a node is within its immediate neighborhood.^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

The degree of a node is the number of edges that link to it. For example, in a simple graph of six European countries, the node representing "France" has a degree of 4.^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

### Directed Graphs

For [directed networks](/concepts/directed-vs-undirected-networks.md), degree centrality can be further broken down into:
- **In-degree**: the number of edges coming into the node
- **Out-degree**: the number of edges pointing away from the node

^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

Degree centrality identifies nodes that have the most direct connections, making them potentially influential as hubs in the network.

## Betweenness Centrality

**Betweenness centrality** measures the fraction of shortest paths in a network that pass through a given node.^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

A node with high betweenness centrality acts as a bridge or bottleneck — many of the shortest paths between other pairs of nodes must go through it. Such nodes are critical for efficient communication and information flow across the network.

Betweenness centrality is particularly important in:
- social network analysis, where certain individuals connect different communities
- transportation networks, where certain hubs or chokepoints control traffic flow
- fraud detection and threat detection, where intermediaries may be points of vulnerability

## Relationship Between Measures

Degree centrality and betweenness centrality capture different aspects of node importance:
- A node may have high degree centrality (many direct connections) but low betweenness centrality (not on many shortest paths between other nodes).
- Conversely, a node may have few connections (low degree) but sit on critical paths between major network clusters (high betweenness), making it a crucial bridge.

## Applications

Centrality measures are commonly used in:
- Social networks representing connections between people
- Communication networks, such as the cables that carry internet traffic between servers
- Transportation networks, such as flight, train, or bus connections between cities
- Product recommendation systems
- Fraud or threat detection

These analyses are especially powerful when combined with other analytics techniques, including machine learning.^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

## Implementation on Databricks

For computing centrality measures, Databricks recommends:
- [NetworkX](/concepts/networkx.md) for relatively small networks that can be processed on a single compute node
- [GraphFrames](/concepts/graphframes.md) for large networks that require distributed processing

Databricks Runtime ML includes both of these network analysis packages.^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

## Related Concepts

- [Nodes and Edges](/concepts/nodes-and-edges.md)
- [Directed and Undirected Networks](/concepts/directed-vs-undirected-networks.md)
- [Weighted Edges](/concepts/weighted-edges.md)
- Shortest Path
- [Degree Distribution](/concepts/degree-and-degree-distribution.md)
- Diameter
- Density
- [Small-world Networks](/concepts/small-world-networks.md)

## Sources

- graph-and-network-analysis-on-databricks-databricks-on-aws.md

# Citations

1. [graph-and-network-analysis-on-databricks-databricks-on-aws.md](/references/graph-and-network-analysis-on-databricks-databricks-on-aws-73e6c5fc.md)
