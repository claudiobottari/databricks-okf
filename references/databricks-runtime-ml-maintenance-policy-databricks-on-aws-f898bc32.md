---
title: Databricks Runtime ML maintenance policy | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/databricks-runtime-ml-maintenance
ingestedAt: "2026-06-18T08:10:01.655Z"
---

Databricks Runtime ML includes a variety of popular ML and DL libraries. The libraries are updated with each release to include new features and fixes. This article describes the supported top-tier libraries, their update cadence and the scenarios for when libraries are deprecated.

## Library support policy[​](#library-support-policy "Direct link to Library support policy")

Databricks has designated a subset of the supported libraries as top-tier libraries. For these libraries, Databricks provides a faster update cadence, updating to the latest package releases with each runtime release (barring dependency conflicts). Databricks also provides advanced support, testing, and embedded optimizations for top-tier libraries. Top-tier libraries are added or removed only with major releases.

The full list of the top-tier libraries is:

*   [datasets](https://docs.databricks.com/aws/en/machine-learning/train-model/huggingface/load-data)
*   [GraphFrames](https://docs.databricks.com/aws/en/integrations/graphframes/)
*   [MLflow](https://docs.databricks.com/aws/en/mlflow/)
*   [PyTorch](https://docs.databricks.com/aws/en/machine-learning/train-model/pytorch)
*   [Scikit-learn](https://docs.databricks.com/aws/en/machine-learning/train-model/scikit-learn)
*   [streaming](https://docs.databricks.com/aws/en/machine-learning/load-data/streaming)
*   [TensorBoard](https://docs.databricks.com/aws/en/machine-learning/train-model/tensorboard)
*   [transformers](https://docs.databricks.com/aws/en/machine-learning/train-model/huggingface/)

For a list of all libraries included in each runtime version, see the [release notes](https://docs.databricks.com/aws/en/release-notes/runtime/) for Databricks Runtime ML.

note

Starting with Databricks Runtime 18.0 ML, TensorFlow and spark-tensorflow-connector are no longer top-tier libraries.

## Library deprecation policy[​](#library-deprecation-policy "Direct link to Library deprecation policy")

Databricks might remove a library from the top-tier list in the following situations:

*   If the library has no new commits in two months and no new releases in more than six months. Databricks might add back the removed library when active maintenance resumes.
*   If usage of the library drops significantly.
*   Libraries are replaced if new packages have been added to fill major gaps.

Databricks will remove a pre-installed library when the library reaches any of the following conditions:

*   The library is no longer actively maintained. A library is considered not actively maintained when any of the following conditions are met:
    *   No new commits in three months and no new releases in more than nine months.
    *   The library's repository is archived.
    *   An announced stop in maintenance for that library.
*   No stable release is found to be functional for the new runtime.

When a library is planned for removal, Databricks takes the following steps to notify customers:

*   A deprecation warning is added in the runtime release notes, indicating that the library will be removed in the next major Databricks Runtime ML release.
*   A notification is displayed when importing the library, indicating that the library will be removed in the next major Databricks Runtime ML release.
*   Databricks documentation that references the library is updated to indicate that the library is planned for removal.

To continue to use a library after it has been removed, you can either install the library manually or use an earlier version of Databricks Runtime ML.
