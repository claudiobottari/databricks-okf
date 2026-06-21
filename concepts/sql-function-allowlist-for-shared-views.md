---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 572124b8c0a9bc965627960189aa0eec49f9d802b1eda91be62efdbfd23bee50
  pageDirectory: concepts
  sources:
    - functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sql-function-allowlist-for-shared-views
    - SFAFSV
  citations:
    - file: functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md
title: SQL Function Allowlist for Shared Views
description: The restricted subset of Databricks built-in SQL functions and operators permitted in view definitions shared via Databricks-to-Databricks sharing
tags:
  - sql-functions
  - security
  - delta-sharing
timestamp: "2026-06-19T18:57:29.389Z"
---

# SQL Function Allowlist for Shared Views

The **SQL Function Allowlist for Shared Views** is a security measure in [Databricks-to-Databricks View Sharing](/concepts/databricks-to-databricks-view-sharing.md) that restricts which built-in functions and operators can be used when defining a shared view. By limiting the available functions, the provider prevents recipients from executing arbitrary or potentially unsafe SQL operations on the shared data. ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

Only the subset listed below—drawn from the full set of [Databricks SQL built-in functions](/concepts/databricks-built-in-sql-functions-and-operators.md)—is permitted inside a shared view’s definition. Any function or operator not on this list will be rejected when the view is created or queried. ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

## Operators

All standard SQL comparison, arithmetic, bitwise, and logical operators are allowed:

- Arithmetic: `-`, `!`, `/`, `*`, `%`, `+`, `div`
- Comparison: `<`, `<=`, `<=>`, `=`, `==`, `>`, `>=`, `between`, `in`, `like`, `ilike`, `rlike`, `regexp`
- Bitwise: `&`, `^`, `|`, `~`, `<<`, `>>`, `>>>`, `shiftleft`, `shiftright`, `shiftrightunsigned`
- Logical: `and`, `or`, `not`, `some`, `any`, `every`

^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

## Aggregation Functions

Allowed aggregate functions include:

`avg`, `count`, `count_if`, `count_min_sketch`, `approx_count_distinct`, `approx_percentile`, `approx_top_k`, `any_value`, `bit_and`, `bit_or`, `bit_xor`, `bool_and`, `bool_or`, `collect_list`, `collect_set`, `corr`, `covar_pop`, `covar_samp`, `cume_dist`, `dense_rank`, `first`, `first_value`, `grouping`, `grouping_id`, `histogram_numeric`, `hll_sketch_agg`, `hll_union_agg`, `kurtosis`, `last`, `last_value`, `max`, `max_by`, `mean`, `median`, `min`, `min_by`, `mode`, `ntile`, `percent_rank`, `percentile`, `percentile_approx`, `percentile_cont`, `percentile_disc`, `rank`, `regr_avgx`, `regr_avgy`, `regr_count`, `regr_intercept`, `regr_r2`, `regr_slope`, `regr_sxx`, `regr_sxy`, `regr_syy`, `row_number`, `session_window`, `skewness`, `some`, `std`, `stddev`, `stddev_pop`, `stddev_samp`, `sum`, `var_pop`, `var_samp`, `variance`, `width_bucket`, `window`. ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

## Array Functions

Functions for constructing, querying, and transforming arrays:

`array`, `array_agg`, `array_append`, `array_compact`, `array_contains`, `array_distinct`, `array_except`, `array_insert`, `array_intersect`, `array_join`, `array_max`, `array_min`, `array_position`, `array_prepend`, `array_remove`, `array_repeat`, `array_size`, `array_sort`, `array_union`, `arrays_overlap`, `arrays_zip`, `aggregate`, `cardinality`, `element_at`, `exists`, `explode`, `explode_outer`, `filter`, `flatten`, `forall`, `inline`, `inline_outer`, `reduce`, `reverse`, `sequence`, `shuffle`, `size`, `slice`, `sort_array`. ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

## Bitwise & Binary Functions

`bit_count`, `bit_get`, `bit_length`, `bit_reverse`, `bitmap_bit_position`, `bitmap_bucket_number`, `bitmap_construct_agg`, `bitmap_count`, `bitmap_or_agg`, `getbit`, `luhn_check`. ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

## Conversion & Casting Functions

`bigint`, `binary`, `boolean`, `cast`, `char`, `conv`, `date`, `decimal`, `double`, `encode`, `decode`, `float`, `hex`, `int`, `smallint`, `string`, `timestamp`, `tinyint`, `to_binary`, `to_char`, `to_date`, `to_number`, `to_timestamp`, `to_unix_timestamp`, `to_varchar`, `try_to_binary`, `try_to_number`, `try_to_timestamp`, `typeof`, `unbase64`, `unhex`. ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

## Date & Time Functions

`add_months`, `convert_timezone`, `curdate`, `current_date`, `current_timestamp`, `current_timezone`, `date_add`, `date_diff`, `date_format`, `date_from_unix_date`, `date_part`, `date_sub`, `date_trunc`, `dateadd`, `datediff`, `datepart`, `day`, `dayofmonth`, `dayofweek`, `dayofyear`, `extract`, `from_unixtime`, `from_utc_timestamp`, `getdate`, `hour`, `last_day`, `make_date`, `make_dt_interval`, `make_interval`, `make_timestamp`, `make_ym_interval`, `minute`, `month`, `months_between`, `next_day`, `now`, `quarter`, `second`, `timestamp_micros`, `timestamp_millis`, `timestamp_seconds`, `to_utc_timestamp`, `trunc`, `unix_date`, `unix_micros`, `unix_millis`, `unix_seconds`, `unix_timestamp`, `weekday`, `weekofyear`, `window_time`, `year`. ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

## H3 Geospatial Functions

`h3_boundaryasgeojson`, `h3_boundaryaswkb`, `h3_boundaryaswkt`, `h3_centerasgeojson`, `h3_centeraswkb`, `h3_centeraswkt`, `h3_compact`, `h3_coverash3`, `h3_coverash3string`, `h3_distance`, `h3_h3tostring`, `h3_hexring`, `h3_ischildof`, `h3_ispentagon`, `h3_isvalid`, `h3_kring`, `h3_kringdistances`, `h3_longlatash3`, `h3_longlatash3string`, `h3_maxchild`, `h3_minchild`, `h3_pointash3`, `h3_pointash3string`, `h3_polyfillash3`, `h3_polyfillash3string`, `h3_resolution`, `h3_stringtoh3`, `h3_tessellateaswkb`, `h3_tochildren`, `h3_toparent`, `h3_try_coverash3`, `h3_try_coverash3string`, `h3_try_distance`, `h3_try_polyfillash3`, `h3_try_polyfillash3string`, `h3_try_tessellateaswkb`, `h3_try_validate`, `h3_uncompact`, `h3_validate`. ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

## Map Functions

`map`, `map_concat`, `map_contains_key`, `map_entries`, `map_filter`, `map_from_arrays`, `map_from_entries`, `map_keys`, `map_values`, `map_zip_with`, `str_to_map`, `transform_keys`, `transform_values`. ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

## Math & Trigonometric Functions

`abs`, `acos`, `acosh`, `asin`, `asinh`, `atan`, `atan2`, `atanh`, `bround`, `cbrt`, `ceil`, `ceiling`, `cos`, `cosh`, `cot`, `csc`, `degrees`, `e`, `exp`, `expm1`, `factorial`, `floor`, `greatest`, `hypot`, `least`, `ln`, `log`, `log10`, `log1p`, `log2`, `mod`, `negative`, `pi`, `pmod`, `positive`, `pow`, `power`, `radians`, `rand`, `randn`, `random`, `rint`, `round`, `sec`, `sign`, `signum`, `sin`, `sinh`, `sqrt`, `tan`, `tanh`, `try_divide`, `try_mod`, `try_multiply`, `try_subtract`. ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

## String Functions

`ascii`, `base64`, `bin`, `btrim`, `char`, `char_length`, `character_length`, `charindex`, `chr`, `concat`, `contains`, `endswith`, `find_in_set`, `format_number`, `format_string`, `initcap`, `instr`, `left`, `len`, `length`, `levenshtein`, `locate`, `lower`, `lpad`, `ltrim`, `octet_length`, `overlay`, `position`, `printf`, `regexp_extract`, `regexp_extract_all`, `regexp_like`, `regexp_replace`, `repeat`, `replace`, `right`, `rpad`, `rtrim`, `space`, `split`, `split_part`, `startswith`, `substr`, `substring`, `substring_index`, `trim`, `ucase`, `upper`, `url_decode`, `url_encode`. ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

## Struct & Miscellaneous Functions

`coalesce`, `collate`, `collation`, `current_catalog`, `current_database`, `current_metastore`, `current_recipient`, `current_schema`, `current_version`, `hash`, `if`, `iff`, `ifnull`, `isnan`, `isnotnull`, `isnull`, `named_struct`, `nanvl`, `nullif`, `struct`, `try_add`, `try_avg`, `try_sum`, `uuid`, `version`. ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

## Security Context

The allowlist exists to prevent shared view recipients from executing functions that could expose sensitive data or perform arbitrary computation outside the scope of the shared dataset. For example, functions that access external systems or perform implicit file I/O are excluded. This restriction applies only to **Databricks-to-Databricks** view sharing; other sharing protocols may have different rules. ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md)
- [Databricks-to-Databricks View Sharing](/concepts/databricks-to-databricks-view-sharing.md)
- [Databricks SQL built-in functions](/concepts/databricks-built-in-sql-functions-and-operators.md)
- Shared view security

## Sources

- functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md

# Citations

1. [functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md](/references/functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws-c0b6a2ae.md)
