---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7282e444b0cfb667c491b452d83a72ac82bbefc2b5c0196292ce5601de77ba3b
  pageDirectory: concepts
  sources:
    - graph-and-network-analysis-on-databricks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - graph-properties-centrality-shortest-path-diameter-density
    - GP(SPDD
  citations:
    - file: graph-and-network-analysis-on-databricks-databricks-on-aws.md
title: Graph Properties (Centrality, Shortest Path, Diameter, Density)
description: "Key analytical metrics for graphs: shortest path (minimum distance between nodes), centrality (node importance measures like degree centrality and betweenness centrality), diameter (maximum shortest path across the network), and density (actual edges vs possible edges)."
tags:
  - graph-analysis
  - metrics
timestamp: "2026-06-19T19:02:47.834Z"
---

# Graph Properties (Centrality, Shortest Path, Diameter, Density)

**Graph properties** are quantitative measures that describe the structure, organization, and characteristics of a Graph (Network Theory)|graph or network. These properties are essential for understanding the behavior of complex systems represented as networks, including Social Networks, Transportation Networks, and Telecommunication Networks.

## Key Graph Properties

### Centrality

**Centrality** is a measure of the importance of a node within a network. Multiple definitions exist, each capturing a different aspect of importance. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

- **Degree Centrality**: Based on the fraction of nodes in a network that a given node is directly connected to. A node with high degree centrality has many direct connections. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]
- **Betweenness Centrality**: The fraction of Shortest Path|shortest paths in the network that pass through a given node. Nodes with high betweenness centrality act as bridges or critical connectors within the network. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

Centrality measures are widely used in applications such as Fraud Detection, Threat Detection, and Product Recommendation systems. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

### Shortest Path

The **shortest path** is the minimum distance between two nodes in a network. The calculation takes into account directional links (for [Directed and Undirected Networks|directed graphs](/concepts/directed-vs-undirected-networks.md)) and, optionally, edge weights. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

For example, in a graph of European countries where edges represent shared borders, the shortest path between Germany and Spain passes through France, yielding a path distance of 2 (Germany→France→Spain). ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

Shortest path algorithms are fundamental to many graph analysis tasks and form the basis for computing other graph properties.

### Diameter

The **diameter** of a network is the maximum of all shortest paths between any two nodes in the network. It is equivalent to the maximum eccentricity of all nodes. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

The diameter provides a measure of the overall size or "spread" of a network. In the context of [Small-world Networks](/concepts/small-world-networks.md), the diameter tends to be small relative to the number of nodes, reflecting the "six degrees of separation" phenomenon observed in many real-world networks. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

### Density

**Density** measures how many edges exist in a graph compared to the total number of possible edges. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

- For an **undirected graph**, the total number of possible edges is n(n-1)/2, where n is the number of nodes.
- For a **directed graph**, each edge has two possible directions, so the total number of possible edges is n(n-1).

^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

Density values range from 0 (no edges) to 1 (complete graph). Sparse graphs have low density, while dense graphs have high density. Most real-world networks, such as social networks and biological networks, are sparse.

## Related Concepts

- Degree — The number of edges incident to a node; the foundation for degree centrality
- [Degree Distribution](/concepts/degree-and-degree-distribution.md) — The frequency distribution of node degrees in a network
- [Weighted Edges](/concepts/weighted-edges.md) — Edges with associated values representing capacity, distance, or cost
- [GraphFrames](/concepts/graphframes.md) — A distributed graph processing library for large-scale graph analysis on Databricks
- [NetworkX](/concepts/networkx.md) — A Python package for analyzing small to medium-sized graphs on a single node
- Data Skew in Graph Processing — A common challenge when processing large-scale real-world networks

## Applications

These graph properties are particularly powerful when combined with other analytics techniques, including [Machine Learning](/concepts/cicd-for-machine-learning.md). Common applications include: ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

- Fraud and threat detection
- Product recommendation systems
- Social network analysis
- Transportation and logistics optimization
- Communication network analysis

## Sources

- graph-and-network-analysis-on-databricks-databricks-on-aws.md

# Citations

1. [graph-and-network-analysis-on-databricks-databricks-on-aws.md](/references/graph-and-network-analysis-on-databricks-databricks-on-aws-73e6c5fc.md)
