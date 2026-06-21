---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2fe41b11d2e51102f0c8ec1abb9d66e881b0e2bb495ff7e8bdb7de002acf3fd4
  pageDirectory: concepts
  sources:
    - functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - supported-sql-functions-for-shared-views
    - SSFFSV
  citations:
    - file: functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md
title: Supported SQL Functions for Shared Views
description: The comprehensive list of SQL operators, mathematical functions, string functions, date/time functions, array/map functions, aggregation functions, window functions, encryption functions, geospatial (H3) functions, and type conversion functions allowed in Databricks-to-Databricks view sharing.
tags:
  - sql
  - functions
  - databricks
  - delta-sharing
timestamp: "2026-06-18T12:28:54.063Z"
---

# Supported SQL Functions for Shared Views

**Supported SQL Functions for Shared Views** refers to the restricted subset of Databricks built-in SQL functions and operators that are allowed in Databricks-to-Databricks view sharing. To maintain data security, only explicit functions and operators are permitted in view definitions that are shared between Databricks workspaces. ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

## Overview

Databricks-to-Databricks view sharing enforces a security boundary by allowing only a specific subset of Databricks built-in functions and operators in shared views. Any function not on the allowed list cannot be used in a view that is shared between Databricks workspaces. This approach protects data by preventing the execution of arbitrary or potentially unsafe operations on the recipient side. ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

Supported functions are drawn from the full Databricks [built-in functions and operators](/concepts/databricks-built-in-sql-functions-and-operators.md) documentation. The allowed list includes operators, mathematical functions, string functions, date/time functions, array and map functions, aggregate functions, window functions, and more. ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

## Categorized Function List

### Arithmetic and Bitwise Operators

- `-` (minus), `!` (factorial/not), `*` (multiply), `/` (divide), `&` (bitwise AND), `%` (modulo), `^` (bitwise XOR), `+` (plus), `~` (bitwise NOT)
- `<<` (bitwise left shift), `>>` (bitwise right shift), `>>>` (bitwise unsigned right shift), `|` (bitwise OR) ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

### Comparison Operators

- `<` (less than), `<=` (less than or equal), `<=>` (null-safe equal), `=` (equal), `==` (equal), `>` (greater than), `>=` (greater than or equal) ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

### Logical Operators

- `and`, `between`, `ilike`, `in`, `isnan`, `isnotnull`, `isnull`, `like`, `not`, `or`, `regexp`, `rlike`, `when` ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

### Mathematical Functions

- `abs`, `acos`, `acosh`, `asin`, `asinh`, `atan`, `atan2`, `atanh`, `bin`, `bround`, `cbrt`, `ceil`, `ceiling`, `conv`, `cos`, `cosh`, `cot`, `csc`, `degrees`, `div`, `e`, `exp`, `expm1`, `factorial`, `floor`, `hex`, `hypot`, `ln`, `log`, `log10`, `log1p`, `log2`, `mod`, `negative`, `pi`, `pmod`, `positive`, `pow`, `power`, `radians`, `rand`, `randn`, `random`, `rint`, `round`, `sec`, `sign`, `signum`, `sin`, `sinh`, `sqrt`, `tan`, `tanh`, `trunc`, `unhex`, `width_bucket` ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

### String Functions

- `ascii`, `base64`, `btrim`, `char`, `char_length`, `character_length`, `charindex`, `chr`, `coalesce`, `collate`, `collation`, `concat`, `contains`, `decode`, `encode`, `endswith`, `find_in_set`, `format_number`, `format_string`, `ifnull`, `left`, `len`, `length`, `levenshtein`, `lower`, `luhn_check`, `nullif`, `octet_length`, `overlay`, `position`, `printf`, `regexp_extract`, `regexp_extract_all`, `regexp_like`, `regexp_replace`, `repeat`, `replace`, `reverse`, `right`, `rpad`, `rtrim`, `sha`, `sha1`, `sha2`, `space`, `split`, `split_part`, `startswith`, `str_to_map`, `string`, `stringdecode`, `substr`, `substring`, `substring_index`, `to_binary`, `to_char`, `to_number`, `to_varchar`, `translate`, `trim`, `try_to_binary`, `try_to_number`, `typeof`, `ucase`, `unbase64`, `unhex`, `upper`, `url_decode`, `url_encode` ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

### Date and Time Functions

- `add_months`, `curdate`, `current_catalog`, `current_database`, `current_date`, `current_metastore`, `current_recipient`, `current_schema`, `current_timestamp`, `current_timezone`, `current_version`, `convert_timezone`, `date`, `date_add`, `date_diff`, `date_format`, `date_from_unix_date`, `date_part`, `date_sub`, `date_trunc`, `dateadd`, `datediff`, `datepart`, `day`, `dayofmonth`, `dayofweek`, `dayofyear`, `extract`, `from_unixtime`, `from_utc_timestamp`, `getdate`, `hour`, `last_day`, `localtimestamp`, `make_date`, `make_dt_interval`, `make_interval`, `make_timestamp`, `make_timestamp_ltz`, `make_timestamp_ntz`, `make_ym_interval`, `minute`, `month`, `monthname`, `months_between`, `next_day`, `now`, `quarter`, `second`, `session_window`, `timestamp`, `timestamp_micros`, `timestamp_millis`, `timestamp_seconds`, `to_date`, `to_timestamp`, `to_timestamp_ltz`, `to_timestamp_ntz`, `to_unix_timestamp`, `to_utc_timestamp`, `try_add`, `try_subtract`, `try_to_timestamp`, `unix_date`, `unix_micros`, `unix_millis`, `unix_seconds`, `unix_timestamp`, `weekday`, `weekofyear`, `window`, `window_time`, `year` ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

### Array and Map Functions

- `aggregate`, `array`, `array_append`, `array_compact`, `array_contains`, `array_distinct`, `array_except`, `array_insert`, `array_intersect`, `array_join`, `array_max`, `array_min`, `array_position`, `array_prepend`, `array_remove`, `array_repeat`, `array_size`, `array_sort`, `array_union`, `arrays_overlap`, `arrays_zip`, `cardinality`, `element_at`, `exists`, `explode`, `explode_outer`, `filter`, `flatten`, `forall`, `get`, `inline`, `inline_outer`, `map`, `map_concat`, `map_contains_key`, `map_entries`, `map_filter`, `map_from_arrays`, `map_from_entries`, `map_keys`, `map_values`, `map_zip_with`, `named_struct`, `reduce`, `sequence`, `shuffle`, `size`, `slice`, `sort_array`, `stack`, `struct`, `transform`, `transform_keys`, `transform_values`, `zip_with` ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

### Aggregate Functions

- `any`, `any_value`, `approx_count_distinct`, `approx_percentile`, `approx_top_k`, `array_agg`, `avg`, `bit_and`, `bit_or`, `bit_xor`, `bitmap_construct_agg`, `bitmap_or_agg`, `bool_and`, `bool_or`, `collect_list`, `collect_set`, `corr`, `count`, `count_if`, `count_min_sketch`, `covar_pop`, `covar_samp`, `every`, `first`, `histogram_numeric`, `hll_sketch_agg`, `hll_union_agg`, `kurtosis`, `last`, `max`, `max_by`, `mean`, `median`, `min`, `min_by`, `mode`, `percentile`, `percentile_approx`, `percentile_cont`, `percentile_disc`, `regr_avgx`, `regr_avgy`, `regr_count`, `regr_intercept`, `regr_r2`, `regr_slope`, `regr_sxx`, `regr_sxy`, `regr_syy`, `skewness`, `some`, `std`, `stddev`, `stddev_pop`, `stddev_samp`, `sum`, `try_avg`, `try_sum`, `var_pop`, `var_samp`, `variance` ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

### Window Functions

- `cume_dist`, `dense_rank`, `first_value`, `grouping`, `grouping_id`, `lag`, `last_value`, `lead`, `nth_value`, `ntile`, `percent_rank`, `rank`, `row_number` ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

### H3 (Geospatial) Functions

- `h3_boundaryasgeojson`, `h3_boundaryaswkb`, `h3_boundaryaswkt`, `h3_centerasgeojson`, `h3_centeraswkb`, `h3_centeraswkt`, `h3_compact`, `h3_coverash3`, `h3_coverash3string`, `h3_distance`, `h3_h3tostring`, `h3_hexring`, `h3_ischildof`, `h3_ispentagon`, `h3_isvalid`, `h3_kring`, `h3_kringdistances`, `h3_longlatash3`, `h3_longlatash3string`, `h3_maxchild`, `h3_minchild`, `h3_pointash3`, `h3_pointash3string`, `h3_polyfillash3`, `h3_polyfillash3string`, `h3_resolution`, `h3_stringtoh3`, `h3_tessellateaswkb`, `h3_tochildren`, `h3_toparent`, `h3_try_coverash3`, `h3_try_coverash3string`, `h3_try_distance`, `h3_try_polyfillash3`, `h3_try_polyfillash3string`, `h3_try_tessellateaswkb`, `h3_try_validate`, `h3_uncompact`, `h3_validate` ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

### Security and Hash Functions

- `aes_decrypt`, `aes_encrypt`, `crc32`, `hash`, `md5`, `sha`, `sha1`, `sha2` ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

### Type Conversion and Casting Functions

- `bigint`, `binary`, `boolean`, `cast`, `date`, `decimal`, `double`, `float`, `int`, `smallint`, `string`, `timestamp`, `tinyint`, `to_binary`, `to_char`, `to_date`, `to_number`, `to_timestamp`, `to_varchar`, `try_to_binary`, `try_to_number`, `try_to_timestamp` ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

### Miscellaneous Functions

- `assert_true`, `bit_count`, `bit_get`, `bit_length`, `bit_reverse`, `bitmap_bit_position`, `bitmap_bucket_number`, `bitmap_count`, `current_catalog`, `current_database`, `current_metastore`, `current_recipient`, `current_schema`, `current_timezone`, `current_version`, `getbit`, `greatest`, `hash`, `if`, `iff`, `least`, `nanvl`, `random`, `shiftleft`, `shiftright`, `shiftrightunsigned`, `try_divide`, `try_mod`, `try_multiply`, `try_remainder`, `uuid`, `version` ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

### Unsupported Geography/Geometry Functions (Experimental)

The following functions are listed as supported but are marked as experimental: `to_geography`, `to_geometry`, `try_to_geography`, `try_to_geometry`. These should be used with caution as they may have different stability guarantees. ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

## Usage Notes

- The supported function list includes all standard SQL functions commonly used in data transformations, including mathematical operations, string manipulation, date/time arithmetic, array and map processing, and windowing operations. ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]
- Functions not listed on this page cannot be used in view definitions for Databricks-to-Databricks sharing. Attempting to use unsupported functions will result in errors. ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]
- For the complete reference on each supported function's syntax and behavior, consult the Databricks SQL language manual for built-in functions and operators. ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) — The underlying technology for Databricks-to-Databricks sharing
- [Databricks-to-Databricks View Sharing](/concepts/databricks-to-databricks-view-sharing.md) — How views are shared between workspaces
- [Built-in Functions](/concepts/abac-built-in-tag-functions.md) — The full set of Databricks SQL functions
- [Shared View Security](/concepts/delta-sharing-security-model.md) — Security considerations for shared views

## Sources

- functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md

# Citations

1. [functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md](/references/functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws-c0b6a2ae.md)
