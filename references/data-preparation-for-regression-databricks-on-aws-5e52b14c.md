---
title: Data preparation for regression | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/automl/regression-data-prep
ingestedAt: "2026-06-18T08:09:38.733Z"
---

This article describes how AutoML prepares data for regression training and describes configurable data settings. You can adjust these options during experiment setup in the AutoML UI.

For configuring these settings using the [AutoML API](https://docs.databricks.com/aws/en/machine-learning/automl/regression-train-api)), refer to the [AutoML Python API reference](https://docs.databricks.com/aws/en/machine-learning/automl/automl-api-reference).

## Supported data feature types[​](#supported-data-feature-types "Direct link to Supported data feature types")

Only the feature types listed below are supported. For example, images are _not_ supported.

The following feature types are supported:

*   Numeric (`ByteType`, `ShortType`, `IntegerType`, `LongType`, `FloatType`, and `DoubleType`)
*   Boolean
*   String (categorical or English text)
*   Timestamps (`TimestampType`, `DateType`)
*   ArrayType\[Numeric\] (Databricks Runtime 10.4 LTS ML and above)
*   DecimalType (Databricks Runtime 11.3 LTS ML and above)

## Impute missing values[​](#impute-missing-values "Direct link to impute-missing-values")

In Databricks Runtime 10.4 LTS ML and above, you can specify how null values are imputed. In the UI, select a method from the drop-down in the **Impute with** column in the table schema. In the API, use the `imputers` parameter. For more information, see [AutoML Python API reference](https://docs.databricks.com/aws/en/machine-learning/automl/automl-api-reference).

By default, AutoML selects an imputation method based on the column type and content.

note

If you specify a non-default imputation method, AutoML does not perform semantic type detection.

## Column selection[​](#column-selection "Direct link to column-selection")

In Databricks Runtime 10.3 ML and above, you can specify which columns AutoML should use for training. To exclude a column in the UI, uncheck it in the **Include** column. In the API, use the `exclude_cols` parameter. For more information, see [AutoML Python API reference](https://docs.databricks.com/aws/en/machine-learning/automl/automl-api-reference).

You cannot drop the column selected as the prediction target or as the [time column](#control-automl-split) to split the data.

By default, all columns are included.

## Split data into train, validation, and test sets[​](#split-data-into-train-validation-and-test-sets "Direct link to split-data-into-train-validation-and-test-sets")

AutoML splits your data into three splits for training, validation, and testing. Depending on the type of ML problem, you have different options for splitting the data.

Use the following methods to divide data into training, validation, and test sets:

(**Default**) **Random split**: If a data split strategy isn't specified, the dataset is randomly split into 60% train split, 20% validate split, and 20% test split. For classification, a stratified random split ensures that each class is adequately represented in the training, validation, and test sets.

**Chronological split**: In Databricks Runtime 10.4 LTS ML and above, you can select a time column to create chronological train, validate, and test splits. Chronological splits use the earliest data points for training, the next earliest for validation, and the latest points for testing. The time column can be a timestamp, integer, or string column.

**Manual split**: In Databricks Runtime 15.3 ML and above, you can use the API to set up a manual split. Specify a split column and use the values `train`, `validate`, or `test` to identify rows you want to use for training, validation, and testing datasets. Any rows with split column values other than `train`, `test`, or `validate` are ignored and a corresponding alert is raised.

## Sampling large datasets[​](#sampling-large-datasets "Direct link to sampling-large-datasets")

Although AutoML distributes hyperparameter tuning trials across the worker nodes of a cluster, each model is trained on a single worker node.

AutoML automatically estimates the memory required to load and train your dataset and samples the dataset if necessary.

For classification problems, AutoML uses the PySpark `sampleBy` [method](https://api-docs.databricks.com/python/pyspark/latest/pyspark.sql/api/pyspark.sql.DataFrameStatFunctions.sampleBy.html) for stratified sampling to preserve the target label distribution.

For regression problems, AutoML uses the PySpark `sample` [method](https://api-docs.databricks.com/python/pyspark/latest/pyspark.sql/api/pyspark.sql.DataFrame.sample.html).

## Semantic type detection[​](#semantic-type-detection "Direct link to semantic-type-detection")

note

*   AutoML does not perform semantic type detection for columns that have [custom imputation](#impute-missing-values) methods specified.

With Databricks Runtime 9.1 LTS ML and above, AutoML tries to detect whether columns have a semantic type different from the Spark or pandas data type in the table schema. AutoML treats these columns as the detected semantic type. These detections are best effort and might sometimes miss the existence of semantic types. You can also manually set the semantic type of a column or tell AutoML not to apply semantic type detection to a column [using annotations](#semantic-type-annotations).

Specifically, AutoML makes these adjustments:

*   String and integer columns representing date or timestamp data are treated as a timestamp type.
*   String columns that represent numeric data are treated as a numeric type.

With Databricks Runtime 10.1 ML and above, AutoML also makes these adjustments:

*   Numeric columns that contain categorical IDs are treated as a categorical feature.
*   String columns that contain English text are treated as a text feature.

### Semantic type annotations[​](#semantic-type-annotations "Direct link to Semantic type annotations")

With Databricks Runtime 10.1 ML and above, you can manually control the assigned semantic type by placing a semantic type annotation on a column. To manually annotate the semantic type of column `<column-name>` as `<semantic-type>`, use the following syntax:

Python

    metadata_dict = df.schema["<column-name>"].metadatametadata_dict["spark.contentAnnotation.semanticType"] = "<semantic-type>"df = df.withMetadata("<column-name>", metadata_dict)

`<semantic-type>` can be one of the following:

*   `categorical`: The column contains categorical values (for example, numerical values that should be treated as IDs).
*   `numeric`: The column contains numeric values (for example, string values that can be parsed into numbers).
*   `datetime`: The column contains timestamp values (string, numerical, or date values that can be converted into timestamps).
*   `text`: The string column contains English text.

To disable semantic type detection on a column, use the special keyword annotation `native`.
