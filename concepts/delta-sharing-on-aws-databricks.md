---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 613b9e9c59ac58ff41a0e2978a01d4927a62cd747374d58a9d0b8788068adb54
  pageDirectory: concepts
  sources:
    - functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-sharing-on-aws-databricks
    - DSOAD
  citations:
    - file: functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md
    - file: abac-grant-policies-for-models-beta-databricks-on-aws.md
title: Delta Sharing on AWS Databricks
description: An open protocol for secure data sharing across Databricks workspaces on AWS, enabling cross-workspace collaboration without copying data.
tags:
  - delta-sharing
  - databricks
  - aws
  - data-sharing
timestamp: "2026-06-18T12:28:58.353Z"
---

# Delta Sharing on AWS Databricks

**Delta Sharing** is an open protocol developed by Databricks for secure data sharing across platforms, clouds, and regions. On AWS Databricks, Delta Sharing enables data providers to share governed data with recipients outside their organization without copying or moving the underlying data, while maintaining fine-grained access controls through [Unity Catalog](/concepts/unity-catalog.md).

## Overview

Delta Sharing allows Databricks workspaces to act as data providers, making tables, views, and other securable objects available to recipients across organizational boundaries. Recipients can be other Databricks workspaces (Databricks-to-Databricks sharing) or external systems using any Delta Sharing-compatible client. ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

## Sharing Models with Delta Sharing

You cannot use [Delta Sharing](/concepts/delta-sharing.md) to share models that have [ABAC GRANT Policy](/concepts/abac-grant-policy.md) defined on them. This is a current limitation of the ABAC GRANT policy feature for models in Unity Catalog. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## View Sharing

Databricks-to-Databricks view sharing allows providers to share not just tables but also views defined in Unity Catalog. When sharing views, certain restrictions apply to ensure data security. ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

### Allowed Functions in Shared Views

To keep data secure, Databricks-to-Databricks view sharing only allows a specific subset of Databricks built-in functions and operators in shared view definitions. The restricted set includes: ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

- **Arithmetic operators**: `-`, `!`, `/`, `*`, `%`, `^`, `+`, `<`, `<<`, `<=`, `<=>`, `=`, `==`, `>`, `>=`, `>>`, `>>>`, `|`, `~`
- **Aggregate functions**: `avg`, `count`, `count_if`, `max`, `min`, `sum`, `collect_list`, `collect_set`, `approx_count_distinct`, `approx_percentile`, `approx_top_k`, `bit_and`, `bit_or`, `bit_xor`, `bool_and`, `bool_or`, `corr`, `covar_pop`, `covar_samp`, `cume_dist`, `dense_rank`, `first`, `first_value`, `kurtosis`, `last`, `last_value`, `lag`, `lead`, `max_by`, `mean`, `median`, `min_by`, `mode`, `nth_value`, `ntile`, `percent_rank`, `percentile`, `percentile_approx`, `percentile_cont`, `percentile_disc`, `rank`, `regr_avgx`, `regr_avgy`, `regr_count`, `regr_intercept`, `regr_r2`, `regr_slope`, `regr_sxx`, `regr_sxy`, `regr_syy`, `row_number`, `skewness`, `some`, `std`, `stddev`, `stddev_pop`, `stddev_samp`, `var_pop`, `var_samp`, `variance`, `histogram_numeric`, `hll_sketch_agg`, `hll_union_agg`, `bitmap_construct_agg`, `bitmap_or_agg`, `count_min_sketch`, `session_window`
- **String functions**: `ascii`, `base64`, `bin`, `btrim`, `char`, `char_length`, `character_length`, `charindex`, `chr`, `concat`, `contains`, `decode`, `encode`, `endswith`, `find_in_set`, `format_number`, `format_string`, `hex`, `initcap`, `instr`, `lcase`, `left`, `len`, `length`, `levenshtein`, `like`, `ilike`, `locate`, `lower`, `lpad`, `ltrim`, `luhn_check`, `octet_length`, `overlay`, `position`, `printf`, `regexp`, `regexp_extract`, `regexp_extract_all`, `regexp_like`, `regexp_replace`, `repeat`, `replace`, `reverse`, `right`, `rlike`, `rpad`, `rtrim`, `sha`, `sha1`, `sha2`, `space`, `split`, `split_part`, `startswith`, `str_to_map`, `string`, `substr`, `substring`, `substring_index`, `to_binary`, `to_char`, `to_number`, `to_varchar`, `translate`, `trim`, `try_to_binary`, `try_to_number`, `ucase`, `unbase64`, `unhex`, `upper`, `url_decode`, `url_encode`, `uuid`
- **Date/time functions**: `add_months`, `convert_timezone`, `curdate`, `current_date`, `current_timestamp`, `current_timezone`, `date`, `date_add`, `date_diff`, `date_format`, `date_from_unix_date`, `date_part`, `date_sub`, `date_trunc`, `dateadd`, `datediff`, `day`, `dayofmonth`, `dayofweek`, `dayofyear`, `extract`, `from_unixtime`, `from_utc_timestamp`, `getdate`, `hour`, `last_day`, `make_date`, `make_dt_interval`, `make_interval`, `make_timestamp`, `minute`, `month`, `months_between`, `next_day`, `now`, `quarter`, `second`, `to_date`, `to_timestamp`, `to_unix_timestamp`, `to_utc_timestamp`, `trunc`, `try_add`, `try_divide`, `try_mod`, `try_multiply`, `try_subtract`, `unix_date`, `unix_micros`, `unix_millis`, `unix_seconds`, `unix_timestamp`, `weekday`, `weekofyear`, `window`, `window_time`, `year`
- **Math functions**: `abs`, `acos`, `acosh`, `asin`, `asinh`, `atan`, `atan2`, `atanh`, `bround`, `cbrt`, `ceil`, `ceiling`, `conv`, `cos`, `cosh`, `cot`, `crc32`, `csc`, `degrees`, `div`, `e`, `exp`, `expm1`, `factorial`, `floor`, `greatest`, `hypot`, `least`, `ln`, `log`, `log10`, `log1p`, `log2`, `mod`, `negative`, `pi`, `pmod`, `positive`, `pow`, `power`, `radians`, `rand`, `randn`, `random`, `rint`, `round`, `sec`, `sign`, `signum`, `sin`, `sinh`, `sqrt`, `tan`, `tanh`, `try_sum`, `width_bucket`
- **Type casting**: `bigint`, `binary`, `boolean`, `cast`, `date`, `decimal`, `double`, `float`, `int`, `smallint`, `string`, `timestamp`, `tinyint`
- **Array functions**: `array`, `array_agg`, `array_append`, `array_compact`, `array_contains`, `array_distinct`, `array_except`, `array_insert`, `array_intersect`, `array_join`, `array_max`, `array_min`, `array_position`, `array_prepend`, `array_remove`, `array_repeat`, `array_size`, `array_sort`, `array_union`, `arrays_overlap`, `arrays_zip`, `cardinality`, `element_at`, `explode`, `explode_outer`, `filter`, `flatten`, `forall`, `inline`, `inline_outer`, `reverse`, `sequence`, `shuffle`, `size`, `slice`, `sort_array`, `transform`, `zip_with`
- **Map functions**: `map`, `map_concat`, `map_contains_key`, `map_entries`, `map_filter`, `map_from_arrays`, `map_from_entries`, `map_keys`, `map_values`, `map_zip_with`, `str_to_map`
- **Struct/named struct**: `named_struct`, `struct`
- **Conditional functions**: `coalesce`, `if`, `iff`, `ifnull`, `in`, `isnan`, `isnotnull`, `isnull`, `nanvl`, `not`, `nullif`, `when`
- **Cryptographic and hash functions**: `aes_decrypt`, `aes_encrypt`, `hash`, `md5`, `sha`, `sha1`, `sha2`, `crc32`
- **H3 geospatial functions**: All H3 functions are supported
- **Window functions**: `cume_dist`, `dense_rank`, `lag`, `last_value`, `lead`, `nth_value`, `ntile`, `percent_rank`, `rank`, `row_number`
- **Other**: `aggregate`, `any`, `any_value`, `assert_true`, `between`, `bit_count`, `bit_get`, `bit_length`, `bit_reverse`, `bitmap_bit_position`, `bitmap_bucket_number`, `bitmap_count`, `collate`, `collation`, `current_catalog`, `current_database`, `current_metastore`, `current_recipient`, `current_schema`, `current_version`, `every`, `exists`, `get`, `getbit`, `grouping`, `grouping_id`, `hash`, `if`, `reduce`, `shiftleft`, `shiftright`, `shiftrightunsigned`, `spark_partition_id`, `stack`, `try_avg`, `try_divide`, `try_mod`, `try_multiply`, `try_subtract`, `try_sum`, `typeof`, `version`

### Restricted Functions

Functions that are **not** in the allowed list cannot be used in shared view definitions. Notably, `to_geography`, `to_geometry`, `try_to_geography`, `try_to_geometry`, `localtimestamp`, `make_timestamp_ltz`, `make_timestamp_ntz`, `monthname`, `stringdecode`, `to_timestamp_ltz`, `to_timestamp_ntz`, `try_remainder`, and `try_to_geometry` are among those not supported in shared views. ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

## Configuration

Setting up Delta Sharing on AWS Databricks involves:

1. **Enabling Delta Sharing** in the Databricks workspace settings
2. **Creating a share** in Unity Catalog that includes the tables, views, or models to share
3. **Adding recipients** who will receive access to the share
4. **Recipients activating** the share using the credential file provided by the data provider

Recipients can access shared data from any Delta Sharing-compatible client, including Apache Spark, pandas, or other Databricks workspaces.

## Access Control

Delta Sharing integrates with [Unity Catalog](/concepts/unity-catalog.md) access controls. Data providers use Unity Catalog's permission model to control which tables and views are included in a share. Recipients access the data according to the permissions defined in the share. ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer that manages Delta Sharing
- [ABAC GRANT Policy](/concepts/abac-grant-policy.md) — Attribute-based access control policies for models (not compatible with Delta Sharing)
- [Databricks-to-Databricks Sharing](/concepts/databricks-to-databricks-sharing.md) — Sharing data between Databricks workspaces
- [Open Sharing Protocol](/concepts/opensharing-protocol.md) — The open standard underlying Delta Sharing
- [Recipients](/concepts/data-recipient.md) — Consumers of shared data

## Sources

- abac-grant-policies-for-models-beta-databricks-on-aws.md
- functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md

# Citations

1. [functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md](/references/functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws-c0b6a2ae.md)
2. [abac-grant-policies-for-models-beta-databricks-on-aws.md](/references/abac-grant-policies-for-models-beta-databricks-on-aws-49466796.md)
