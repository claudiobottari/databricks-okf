---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7d666cdf5a60529a2c80563568a17953b26258748f7311d7710793a6546fce5a
  pageDirectory: concepts
  sources:
    - functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - restricted-sql-function-allowlist
    - RSFA
  citations:
    - file: functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md
title: Restricted SQL Function Allowlist
description: A security mechanism in Databricks-to-Databricks view sharing that limits shared views to only use a predefined subset of built-in SQL functions and operators, preventing arbitrary code execution.
tags:
  - delta-sharing
  - security
  - sql
  - databricks
timestamp: "2026-06-18T12:28:13.432Z"
---

# Restricted SQL Function Allowlist

**Restricted SQL Function Allowlist** refers to the subset of Databricks built-in SQL functions and operators that are permitted in [Databricks-to-Databricks View Sharing](/concepts/databricks-to-databricks-view-sharing.md). This allowlist is enforced to maintain data security when sharing views across Databricks workspaces.

## Overview

To keep data secure, Databricks-to-Databricks view sharing only allows a specific subset of Databricks built-in functions and operators in shared views. Any function or operator not included in this allowlist cannot be used in view definitions that are shared between Databricks workspaces. ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

## Allowed Functions and Operators

The allowlist includes a comprehensive set of functions and operators across multiple categories:

### Arithmetic Operators
`-`, `!`, `*`, `/`, `&`, `%`, `^`, `+`, `<`, `<<`, `<=`, `<=>`, `=`, `==`, `>`, `>=`, `>>`, `>>>`, `|`, `~` ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

### Mathematical Functions
`abs`, `acos`, `acosh`, `asin`, `asinh`, `atan`, `atan2`, `atanh`, `bin`, `bround`, `cbrt`, `ceil`, `ceiling`, `conv`, `cos`, `cosh`, `cot`, `csc`, `degrees`, `div`, `e`, `exp`, `expm1`, `factorial`, `floor`, `greatest`, `hex`, `hypot`, `least`, `ln`, `log`, `log10`, `log1p`, `log2`, `mod`, `negative`, `pi`, `pmod`, `positive`, `pow`, `power`, `radians`, `rand`, `randn`, `random`, `rint`, `round`, `sec`, `sign`, `signum`, `sin`, `sinh`, `sqrt`, `tan`, `tanh`, `try_add`, `try_divide`, `try_mod`, `try_multiply`, `try_subtract`, `unhex`, `width_bucket` ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

### String Functions
`ascii`, `base64`, `btrim`, `char`, `char_length`, `character_length`, `charindex`, `chr`, `concat`, `contains`, `decode`, `encode`, `endswith`, `find_in_set`, `format_number`, `format_string`, `initcap`, `instr`, `lcase`, `left`, `len`, `length`, `levenshtein`, `locate`, `lower`, `lpad`, `ltrim`, `luhn_check`, `octet_length`, `overlay`, `position`, `printf`, `regexp_extract`, `regexp_extract_all`, `regexp_like`, `regexp_replace`, `repeat`, `replace`, `reverse`, `right`, `rlike`, `rpad`, `rtrim`, `soundex`, `space`, `split`, `split_part`, `startswith`, `str_to_map`, `substr`, `substring`, `substring_index`, `to_binary`, `to_char`, `to_number`, `to_varchar`, `translate`, `trim`, `try_to_binary`, `try_to_number`, `ucase`, `unbase64`, `upper`, `url_decode`, `url_encode` ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

### Date and Time Functions
`add_months`, `convert_timezone`, `curdate`, `current_date`, `current_timestamp`, `current_timezone`, `date`, `date_add`, `date_diff`, `date_format`, `date_from_unix_date`, `date_part`, `date_sub`, `date_trunc`, `dateadd`, `datediff`, `day`, `dayofmonth`, `dayofweek`, `dayofyear`, `extract`, `from_unixtime`, `from_utc_timestamp`, `getdate`, `hour`, `last_day`, `make_date`, `make_dt_interval`, `make_interval`, `make_timestamp`, `make_ym_interval`, `minute`, `month`, `months_between`, `next_day`, `now`, `quarter`, `second`, `session_window`, `timestamp`, `timestamp_micros`, `timestamp_millis`, `timestamp_seconds`, `to_date`, `to_timestamp`, `to_unix_timestamp`, `to_utc_timestamp`, `trunc`, `try_to_timestamp`, `unix_date`, `unix_micros`, `unix_millis`, `unix_seconds`, `unix_timestamp`, `weekday`, `weekofyear`, `window`, `window_time`, `year` ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

### Aggregate Functions
`any_value`, `approx_count_distinct`, `approx_percentile`, `approx_top_k`, `array_agg`, `avg`, `bit_and`, `bit_or`, `bit_xor`, `bitmap_construct_agg`, `bitmap_or_agg`, `bool_and`, `bool_or`, `collect_list`, `collect_set`, `corr`, `count`, `count_if`, `count_min_sketch`, `covar_pop`, `covar_samp`, `cume_dist`, `dense_rank`, `every`, `first`, `first_value`, `grouping`, `grouping_id`, `histogram_numeric`, `hll_sketch_agg`, `hll_union_agg`, `kurtosis`, `lag`, `last`, `last_value`, `lead`, `max`, `max_by`, `mean`, `median`, `min`, `min_by`, `mode`, `nth_value`, `ntile`, `percent_rank`, `percentile`, `percentile_approx`, `percentile_cont`, `percentile_disc`, `rank`, `regr_avgx`, `regr_avgy`, `regr_count`, `regr_intercept`, `regr_r2`, `regr_slope`, `regr_sxx`, `regr_sxy`, `regr_syy`, `row_number`, `skewness`, `some`, `std`, `stddev`, `stddev_pop`, `stddev_samp`, `sum`, `try_avg`, `try_sum`, `var_pop`, `var_samp`, `variance` ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

### Array Functions
`aggregate`, `array`, `array_append`, `array_compact`, `array_contains`, `array_distinct`, `array_except`, `array_insert`, `array_intersect`, `array_join`, `array_max`, `array_min`, `array_position`, `array_prepend`, `array_remove`, `array_repeat`, `array_size`, `array_sort`, `array_union`, `arrays_overlap`, `arrays_zip`, `cardinality`, `element_at`, `exists`, `explode`, `explode_outer`, `filter`, `flatten`, `forall`, `inline`, `inline_outer`, `reduce`, `reverse`, `sequence`, `shuffle`, `size`, `slice`, `sort_array`, `transform`, `zip_with` ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

### Map Functions
`map`, `map_concat`, `map_contains_key`, `map_entries`, `map_filter`, `map_from_arrays`, `map_from_entries`, `map_keys`, `map_values`, `map_zip_with`, `str_to_map`, `transform_keys`, `transform_values` ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

### Type Conversion and Casting
`bigint`, `binary`, `boolean`, `cast`, `date`, `decimal`, `double`, `float`, `int`, `smallint`, `string`, `timestamp`, `tinyint`, `typeof` ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

### Conditional and Logical Functions
`and`, `assert_true`, `between`, `case`, `coalesce`, `if`, `iff`, `ifnull`, `ilike`, `in`, `isnan`, `isnotnull`, `isnull`, `like`, `nanvl`, `not`, `nullif`, `or`, `when` ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

### Cryptographic and Hash Functions
`aes_decrypt`, `aes_encrypt`, `crc32`, `hash`, `md5`, `sha`, `sha1`, `sha2` ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

### H3 Geospatial Functions
`h3_boundaryasgeojson`, `h3_boundaryaswkb`, `h3_boundaryaswkt`, `h3_centerasgeojson`, `h3_centeraswkb`, `h3_centeraswkt`, `h3_compact`, `h3_coverash3`, `h3_coverash3string`, `h3_distance`, `h3_h3tostring`, `h3_hexring`, `h3_ischildof`, `h3_ispentagon`, `h3_isvalid`, `h3_kring`, `h3_kringdistances`, `h3_longlatash3`, `h3_longlatash3string`, `h3_maxchild`, `h3_minchild`, `h3_pointash3`, `h3_pointash3string`, `h3_polyfillash3`, `h3_polyfillash3string`, `h3_resolution`, `h3_stringtoh3`, `h3_tessellateaswkb`, `h3_tochildren`, `h3_toparent`, `h3_try_coverash3`, `h3_try_coverash3string`, `h3_try_distance`, `h3_try_polyfillash3`, `h3_try_polyfillash3string`, `h3_try_tessellateaswkb`, `h3_try_validate`, `h3_uncompact`, `h3_validate` ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

### Miscellaneous Functions
`any`, `bit_count`, `bit_get`, `bit_length`, `bit_reverse`, `bitmap_bit_position`, `bitmap_bucket_number`, `bitmap_count`, `collate`, `collation`, `current_catalog`, `current_database`, `current_metastore`, `current_recipient`, `current_schema`, `current_version`, `get`, `getbit`, `named_struct`, `shiftleft`, `shiftright`, `shiftrightunsigned`, `stack`, `struct`, `try_remainder`, `uuid`, `version` ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

## Functions Not in the Allowlist

Some functions are explicitly excluded from the allowlist. These include geospatial functions such as `to_geography`, `to_geometry`, `try_to_geography`, and `try_to_geometry`, as well as timestamp-related functions like `localtimestamp`, `make_timestamp_ltz`, `make_timestamp_ntz`, `monthname`, `stringdecode`, `to_timestamp_ltz`, and `to_timestamp_ntz`. ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) — The underlying protocol for sharing data across Databricks workspaces
- [Databricks-to-Databricks View Sharing](/concepts/databricks-to-databricks-view-sharing.md) — The specific sharing mechanism that enforces this allowlist
- SQL Language Reference — The full set of Databricks SQL functions and operators
- Data Security — The security considerations that motivate the restricted allowlist

## Sources

- functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md

# Citations

1. [functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md](/references/functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws-c0b6a2ae.md)
