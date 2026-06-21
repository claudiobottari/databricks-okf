---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cc77520f975598a00c9e1598d2fccc7938166d9b0c2700f89e08a0d5b33d5ce9
  pageDirectory: concepts
  sources:
    - express-deployments-for-model-serving-endpoints-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - non-express-deployments-databricks
    - ND(
  citations:
    - file: express-deployments-for-model-serving-endpoints-databricks-on-aws.md
title: Non-Express Deployments (Databricks)
description: The traditional model serving deployment approach where model artifacts and environments are packaged into containers at deployment time, which may result in environment mismatches with training.
tags:
  - databricks
  - model-serving
  - deployment
  - machine-learning
timestamp: "2026-06-19T10:28:28.110Z"
---

# Non-Express Deployments (Databricks)

**Non-express deployments** are the traditional method for deploying custom models to Databricks Model Serving endpoints. In contrast to [Express Deployments (Databricks)](/concepts/express-deployments-databricks.md), non-express deployments package model artifacts and their environments into containers at deployment time rather than during model registration.^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

## Characteristics

### Deployment Time

Because the container build happens during endpoint creation or update, non-express deployments take longer to be ready than express deployments. The endpoint event logs for a non-express deployment explicitly show the container build phase.^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

### Environment Consistency

The serving environment in a non-express deployment may not exactly match the environment used during model training. This is because the container is assembled from the model's declared dependencies and the environment of the deployment process, which can differ from the training environment — especially if the model was trained in a [Serverless Notebooks|serverless notebook](/concepts/serverless-notebook-environments.md) environment or with a different runtime.^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

## Requirements vs. Express Deployments

Non-express deployments do not require the model to be logged and registered from a serverless notebook, nor do they require a specific MLflow version or `env_pack` configuration. They support any custom model that meets the general [Model Serving Endpoint Requirements|model serving endpoint requirements](/concepts/model-serving-endpoint-deployment-timeouts.md), regardless of where it was trained.^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

| Requirement | Express Deployments | Non-Express Deployments |
|-------------|---------------------|-------------------------|
| Model type | Custom model only | Custom model only (FMAPI not supported) |
| Training environment | Must be a serverless notebook (client version 3 or 4) | No restriction |
| MLflow version | `mlflow>=3.1` | Any supported version |
| `env_pack` parameter | Required | Not used |
| Container build | Done at registration time | Done at deployment time |
| Max environment size | 1 GB | No specific limit |

## Use Cases

Non-express deployments remain the standard choice when:

- The model was not trained in a serverless notebook environment.
- The model's dependencies or artifacts exceed the 1 GB size limit for express deployments.
- Inference requires GPU resources (express deployments currently support CPU only).
- The team has existing CI/CD pipelines that package models into containers at deployment time.

## Limitations

- The deployment process takes longer because the container is built from scratch each time the endpoint is created or updated.
- The environment mismatch risk is higher than with express deployments, especially when the training and serving runtimes differ (e.g., different Python versions, different operating system packages).^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- [Express Deployments (Databricks)](/concepts/express-deployments-databricks.md) — The faster, environment-consistent alternative for models trained in serverless notebooks
- [Model Serving Endpoints](/concepts/model-serving-endpoint.md) — The Databricks service that hosts custom models for inference
- [Serverless Notebooks](/concepts/serverless-notebook-environments.md) — The compute environment that enables express deployment packaging
- MLflow Model Registration — The step where `env_pack` can be specified for express deployments
- [Foundational Model APIs (FMAPI)](/concepts/foundation-model-apis.md) — Model types not supported by express or non-express deployments

## Sources

- express-deployments-for-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [express-deployments-for-model-serving-endpoints-databricks-on-aws.md](/references/express-deployments-for-model-serving-endpoints-databricks-on-aws-00f4ae5c.md)
