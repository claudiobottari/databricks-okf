---
title: "Migrate to MLflow 3 from Agent Evaluation: Quick reference | Databricks on AWS"
source: https://docs.databricks.com/aws/en/mlflow3/genai/agent-eval-migration-reference
ingestedAt: "2026-06-18T08:14:28.686Z"
---

    ### Old imports ###from mlflow import evaluatefrom databricks.agents.evals import metricfrom databricks.agents.evals import judgesfrom databricks.agents import review_app### New imports ###from mlflow.genai import evaluatefrom mlflow.genai.scorers import scorerfrom mlflow.genai import judges# For predefined scorers:from mlflow.genai.scorers import (    Correctness, Guidelines, ExpectationsGuidelines,    RelevanceToQuery, Safety, RetrievalGroundedness,    RetrievalRelevance, RetrievalSufficiency)import mlflow.genai.labeling as labelingimport mlflow.genai.label_schemas as schemas
