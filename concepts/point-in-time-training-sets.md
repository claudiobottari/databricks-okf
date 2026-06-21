---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 80830681feccad256f42d237a53ba334ea728e308549eb97d362183bcfb066e7
  pageDirectory: concepts
  sources:
    - declarative-features-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - point-in-time-training-sets
    - PTS
    - create_training_set()
  citations:
    - file: declarative-features-databricks-on-aws.md
title: Point-in-Time Training Sets
description: Using create_training_set to compute point-in-time aggregated features for ML model training by joining labeled data with feature definitions across entity keys and time.
tags:
  - machine-learning
  - training
  - feature-engineering
timestamp: "2026-06-18T11:45:38.540Z"
---

#Point-in-Time Training Sets

**Point-in-Time Training Sets** are training datasets created by computing feature values as they existed at a specific historical moment, avoiding look-ahead bias. In the [Databricks Feature Store](/concepts/databricks-feature-store.md) declarative feature engineering workflow, `create_training_set` calculates point-in-time aggregated features from defined `Feature` objects and a labeled dataset. ^[declarative-features-databricks-on-aws.md]

## Overview

When training machine learning models, features must reflect the information available at the time of prediction. Point-in-time training sets ensure that only historical data (and no future data) is used to compute each row's feature values. The Declarative Feature Engineering APIs provide a `create_training_set` function that automatically performs this point-in-time join by aligning the labeled dataset's timestamps with the feature definitions' time-series columns. ^[declarative-features-databricks-on-aws.md]

## Creating a Point-in-Time Training Set

The `create_training_set` method accepts a labeled DataFrame (`df`), a list of `Feature` objects (which can be local or registered in Unity Catalog), and a `label` column. It returns a `TrainingSet` object whose `load_df()` method materializes the point-in-time aggregated features. ^[declarative-features-databricks-on-aws.md]

```python
from databricks.feature_engineering import FeatureEngineeringClient

fe = FeatureEngineeringClient()

training_set = fe.create_training_set(
    df=labeled_df,         # must contain entity key and timestamp columns
    features=[avg_feature, sum_feature],
    label="target",
)

training_df = training_set.load_df()
```

## Requirements

- The labeled dataset must contain entity columns and a timestamp column whose names match those used in the feature definitions. ^[declarative-features-databricks-on-aws.md]
- The `label` column name must not exist in the source tables used for defining the features. ^[declarative-features-databricks-on-aws.md]
- A classic compute cluster running Databricks Runtime 17.0 ML or above and the `databricks-feature-engineering>=0.15.0` package are required. ^[declarative-features-databricks-on-aws.md]

## Best Practices

- Use declarative features with time-windowed aggregations (rolling windows, sliding windows, or [tumbling windows](/concepts/time-windows.md)) to capture temporal patterns without leaking future information. ^[declarative-features-databricks-on-aws.md]
- Align window boundaries with business cycles (daily, weekly) to ensure training and inference consistency. ^[declarative-features-databricks-on-aws.md]

## Related Concepts

- [Declarative Feature Engineering APIs](/concepts/declarative-feature-engineering-apis.md)
- create_training_set
- [FeatureEngineeringClient](/concepts/featureengineeringclient-api.md)
- [Point-in-time correctness](/concepts/point-in-time-correctness.md)
- [Feature Materialization](/concepts/feature-materialization.md)
- Train Models with Declarative Features

## Sources

- declarative-features-databricks-on-aws.md

# Citations

1. [declarative-features-databricks-on-aws.md](/references/declarative-features-databricks-on-aws-681d2599.md)
