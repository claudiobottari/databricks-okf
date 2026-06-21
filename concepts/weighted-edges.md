---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5b5c89073f59c9e3acd9a14bef00fa2ce801fb0f7ee916efe44cbfece3a3bfb9
  pageDirectory: concepts
  sources:
    - graph-and-network-analysis-on-databricks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - weighted-edges
  citations:
    - file: graph-and-network-analysis-on-databricks-databricks-on-aws.md
title: Weighted Edges
description: Edges in a graph can carry weights representing properties such as capacity, distance, or strength of a relationship, enabling richer analysis like shortest-path with costs.
tags:
  - graph-analysis
  - fundamentals
timestamp: "2026-06-19T19:02:04.471Z"
---

# Weighted Edges

**Weighted edges** are edges in a graph that have an associated numerical value, known as a **weight**, which quantifies some property of the connection between two vertices (nodes). Weights add a dimension of magnitude or cost to the relationship represented by an edge, enabling more nuanced graph analysis than unweighted (binary) edges. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

## Definition and Examples

A weighted edge can represent any measurable attribute of a link between nodes. Common examples include:

- **Carrying capacity** of a highway or cable – e.g., the bandwidth of a network cable or the traffic capacity of a road. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]
- **Distance** between cities in a transportation network.
- **Strength of a relationship** in a social network, such as frequency of communication.

Weights are optional; an unweighted edge simply indicates the presence of a connection without any quantitative measure. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]

## Role in Network Analysis

Edge weights play a critical role in many graph algorithms:

- **Shortest path** – The shortest path between two nodes is defined as the minimum cumulative weight of edges along the path, optionally taking directional links into account. Weights allow the algorithm to find the cheapest or fastest route, not just the fewest hops. ^[graph-and-network-analysis-on-databricks-databricks-on-aws.md]
- **Centrality** – Some centrality measures (e.g., weighted degree centrality) incorporate edge weights to reflect the importance of a node based on total connection strength.
- **Community detection** – Weights can help cluster nodes with stronger ties.

## Weighted Edges in Databricks

On Databricks, weighted edges are supported in both single‑node and distributed graph processing libraries:

- **[NetworkX](/concepts/networkx.md)** (built into Databricks Runtime ML) – Represents weighted edges by adding a `weight` attribute to the edge dictionary.
- **[GraphFrames](/concepts/graphframes.md)** (for distributed processing) – Weights are stored as a column in the edge DataFrame.

## Related Concepts

- [Graph and Network Analysis on Databricks](/concepts/graph-and-network-analysis-on-databricks.md)
- Vertex
- Edge
- [Directed and undirected networks](/concepts/directed-vs-undirected-networks.md)
- Degree (in‑degree and out‑degree)
- Diameter
- Density

## Sources

- graph-and-network-analysis-on-databricks-databricks-on-aws.md

# Citations

1. [graph-and-network-analysis-on-databricks-databricks-on-aws.md](/references/graph-and-network-analysis-on-databricks-databricks-on-aws-73e6c5fc.md)
