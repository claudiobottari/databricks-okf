---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 699ef1285a0043154cf939f02298ee4d2d2d22b5726fe926674d3379c33adc2b
  pageDirectory: concepts
  sources:
    - graph-and-network-analysis-on-databricks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - graph-and-network-analysis
    - Network Analysis and Graph
    - GANA
    - Graph analysis
    - Graph analytics
    - Network analysis
  citations:
    - file: graph-and-network-analysis-on-databricks-databricks-on-aws.md
title: Graph and Network Analysis
description: The practice of modeling and analyzing systems using graphs (vertices connected by edges) to understand relationships, structures, and patterns in domains such as social networks, transportation, fraud detection, and recommendations.
tags:
  - graph-analysis
  - networks
  - databricks
timestamp: "2026-06-19T19:02:43.757Z"
---

Here is the wiki page for "Graph and Network Analysis", written based solely on the provided source material.

---

## Graph and Network Analysis

**Graph and Network Analysis** refers to the study of networks, which consist of a set of vertices (also called nodes) connected by edges (also called links or relationships). This field is used to model and analyze the relationships and structures within complex systems, such as social networks, transportation networks, and telecommunication networks. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

### Basic Concepts

#### Nodes and Edges
A network, or graph, is composed of a set of **nodes** representing the entities being connected (e.g., people, cities) and a set of **edges** representing the connections or relationships between them (e.g., friendships, train routes). Nodes are also known as vertices, points, or entities, while edges are also called lines, relationships, or links. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

#### Directed and Undirected Networks
Edges can represent a one-way relationship, such as a fan following a celebrity, creating a **directed** network. If edges do not have an associated direction and represent a two-way relationship, such as coworkers, the network is called **undirected**. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

#### Weighted Edges
Edges can have **weights** to represent properties like the carrying capacity of a highway or a cable. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

#### Degree
The **degree** of a node is the number of edges that link to it. In directed graphs, **in-degree** is the number of edges coming into the node, and **out-degree** is the number of edges pointing away from it. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

### Network and Node Properties

#### Shortest Path
The **shortest path** is the minimum distance between two nodes, accounting for directional links and optionally edge weights. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

#### Centrality
**Centrality** measures the importance of a node in a network. **Degree centrality** is based on the fraction of nodes it is directly connected to. **Betweenness centrality** is the fraction of all shortest paths that pass through the node. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

#### Degree Distribution
The **degree distribution** of a network describes the number of nodes having each degree, providing information about the network's structure. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

#### Diameter
The **diameter** of a network is the maximum of the shortest paths between any two nodes. It is equivalent to the maximum eccentricity of nodes in the network. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

#### Density
The **density** of a graph is the number of edges divided by the total number of possible edges. For an undirected graph, the total possible edges are `n(n-1)/2`; for a directed graph, it is `n(n-1)`. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

#### Small-World Networks
Most real-world networks are not randomly connected and exhibit patterns like the "small-world phenomenon," where closely linked subgroups exist alongside a short average path length between any two nodes. This can lead to common issues in graph processing at scale, such as data skew. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

### Tools and Implementation

Databricks Runtime ML includes network analysis packages for different scales. For smaller networks that fit on a single compute node, use [NetworkX](/concepts/networkx.md). For large networks requiring distributed processing, use [GraphFrames](/concepts/graphframes.md). Custom open-source packages or external partners can also be integrated for specialized graph processing and visualization. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

### Applications

Graph processing is commonly used in fraud detection, threat detection, product recommendation, and analyzing social, transportation, and telecommunication networks. Its power is enhanced when combined with other analytics techniques, including [Machine Learning](/concepts/cicd-for-machine-learning.md). ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

## Sources

- graph-and-network-analysis-on-databricks-databricks-on-aws.md

# Citations

1. [graph-and-network-analysis-on-databricks-databricks-on-aws.md](/references/graph-and-network-analysis-on-databricks-databricks-on-aws-73e6c5fc.md)
