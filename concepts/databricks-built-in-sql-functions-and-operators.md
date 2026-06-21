---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 56d9c8155b7c1fd51e19957e808634f1c477edf62007c46f33c09a72d9a522da
  pageDirectory: concepts
  sources:
    - functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-built-in-sql-functions-and-operators
    - Operators and Databricks Built-in SQL Functions
    - DBSFAO
    - Databricks SQL built-in functions
    - built-in functions and operators
  citations:
    - file: functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md
title: Databricks Built-in SQL Functions and Operators
description: The comprehensive reference of SQL functions and operators available in Databricks, from which a security-restricted subset is chosen for use in Databricks-to-Databricks view sharing.
tags:
  - databricks
  - sql-functions
  - reference
timestamp: "2026-06-19T10:42:38.048Z"
---

# Databricks Built-in SQL Functions and Operators

**Databricks Built-in SQL Functions and Operators** refers to the extensive library of SQL expressions and functions available in Databricks for transforming, querying, and analyzing data. When used in **[Databricks-to-Databricks View Sharing](/concepts/databricks-to-databricks-view-sharing.md)**, only a specific subset of these built-in functions and operators is permitted, in order to protect data security and prevent unintended information disclosure. ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

---

## Allowed Subset in View Sharing

To keep shared views secure, Databricks restricts view sharing to the following categories of functions and operators. Any function not in this list is blocked during view creation or query execution in a shared context. ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

### Operators

| Category | Operators |
|----------|-----------|
| **Arithmetic** | `-` (negation), `+`, `-` (subtraction), `*`, `/`, `%`, `div`, `mod` |
| **Comparison** | `<`, `<=`, `<=>` (null-safe equal), `=`, `==`, `>`, `>=`, `between`, `in`, `isnotnull`, `isnull`, `isnan` |
| **Logical** | `!`, `and`, `not`, `or`, `some`, `every`, `any` |
| **Bitwise** | `&`, `^`, `\|`, `~`, `<<`, `>>`, `>>>` |
| **String/Pattern** | `like`, `ilike`, `rlike`, `regexp`, `contains`, `startswith`, `endswith` |

### Aggregate Functions

`avg`, `count`, `count_if`, `sum`, `min`, `max`, `mean`, `std`, `stddev`, `stddev_pop`, `stddev_samp`, `var_pop`, `var_samp`, `variance`, `collect_list`, `collect_set`, `any_value`, `approx_count_distinct`, `approx_percentile`, `approx_top_k`, `bit_and`, `bit_or`, `bit_xor`, `bool_and`, `bool_or`, `corr`, `covar_pop`, `covar_samp`, `cume_dist`, `dense_rank`, `first`, `first_value`, `grouping`, `grouping_id`, `kurtosis`, `lag`, `last`, `last_value`, `lead`, `max_by`, `min_by`, `median`, `mode`, `nth_value`, `ntile`, `percent_rank`, `percentile`, `percentile_approx`, `percentile_cont`, `percentile_disc`, `rank`, `regr_avgx`, `regr_avgy`, `regr_count`, `regr_intercept`, `regr_r2`, `regr_slope`, `regr_sxx`, `regr_sxy`, `regr_syy`, `row_number`, `skewness`, `spark_partition_id` (not listed but not needed), `width_bucket`, `session_window`, `window`, `window_time`, `histogram_numeric`, `hll_sketch_agg`, `hll_union_agg`, `bitmap_construct_agg`, `bitmap_or_agg`, `bitmap_count`, `bitmap_bit_position`, `bitmap_bucket_number`, `count_min_sketch`

### Array Functions

`array`, `array_agg`, `array_append`, `array_compact`, `array_contains`, `array_distinct`, `array_except`, `array_insert`, `array_intersect`, `array_join`, `array_max`, `array_min`, `array_position`, `array_prepend`, `array_remove`, `array_repeat`, `array_size`, `array_sort`, `array_union`, `arrays_overlap`, `arrays_zip`, `cardinality`, `element_at`, `exists`, `filter`, `flatten`, `forall`, `get`, `reverse`, `shuffle`, `size`, `slice`, `sort_array`, `zip_with`, `transform`

### Map Functions

`map`, `map_concat`, `map_contains_key`, `map_entries`, `map_filter`, `map_from_arrays`, `map_from_entries`, `map_keys`, `map_values`, `map_zip_with`, `str_to_map`, `transform_keys`, `transform_values`

### Bitmap Functions

`bitmap_bit_position`, `bitmap_bucket_number`, `bitmap_construct_agg`, `bitmap_count`, `bitmap_or_agg`

### Conversion Functions

`cast`, `bigint`, `binary`, `boolean`, `date`, `decimal`, `double`, `float`, `int`, `smallint`, `string`, `timestamp`, `tinyint`, `to_binary`, `to_char`, `to_date`, `to_number`, `to_timestamp`, `to_unix_timestamp`, `to_varchar`, `try_to_binary`, `try_to_number`, `try_to_timestamp`, `unix_timestamp`, `from_unixtime`, `from_utc_timestamp`, `to_utc_timestamp`

### Date / Time Functions

`add_months`, `convert_timezone`, `curdate`, `current_date`, `current_timestamp`, `current_timezone`, `date`, `date_add`, `date_diff`, `date_format`, `date_from_unix_date`, `date_part`, `date_sub`, `date_trunc`, `dateadd`, `datediff`, `datepart`, `day`, `dayofmonth`, `dayofweek`, `dayofyear`, `extract`, `from_unixtime`, `from_utc_timestamp`, `getdate`, `hour`, `last_day`, `make_date`, `make_dt_interval`, `make_interval`, `make_timestamp`, `make_timestamp_ltz`, `make_timestamp_ntz`, `make_ym_interval`, `minute`, `month`, `monthname`, `months_between`, `next_day`, `now`, `quarter`, `second`, `timestamp`, `timestamp_micros`, `timestamp_millis`, `timestamp_seconds`, `to_date`, `to_timestamp`, `to_timestamp_ltz`, `to_timestamp_ntz`, `to_unix_timestamp`, `to_utc_timestamp`, `trunc`, `unix_date`, `unix_micros`, `unix_millis`, `unix_seconds`, `unix_timestamp`, `weekday`, `weekofyear`, `year`, `localtimestamp`, `current_catalog`, `current_database`, `current_metastore`, `current_recipient`, `current_schema`

### H3 Geospatial Functions

`h3_boundaryasgeojson`, `h3_boundaryaswkb`, `h3_boundaryaswkt`, `h3_centerasgeojson`, `h3_centeraswkb`, `h3_centeraswkt`, `h3_compact`, `h3_coverash3`, `h3_coverash3string`, `h3_distance`, `h3_h3tostring`, `h3_hexring`, `h3_ischildof`, `h3_ispentagon`, `h3_isvalid`, `h3_kring`, `h3_kringdistances`, `h3_longlatash3`, `h3_longlatash3string`, `h3_maxchild`, `h3_minchild`, `h3_pointash3`, `h3_pointash3string`, `h3_polyfillash3`, `h3_polyfillash3string`, `h3_resolution`, `h3_stringtoh3`, `h3_tessellateaswkb`, `h3_tochildren`, `h3_toparent`, `h3_try_coverash3`, `h3_try_coverash3string`, `h3_try_distance`, `h3_try_polyfillash3`, `h3_try_polyfillash3string`, `h3_try_tessellateaswkb`, `h3_try_validate`, `h3_uncompact`, `h3_validate`

### Hash & Encoding Functions

`hash`, `md5`, `sha`, `sha1`, `sha2`, `crc32`, `base64`, `unbase64`, `hex`, `unhex`, `encode`, `decode`

### Math Functions

`abs`, `acos`, `acosh`, `asin`, `asinh`, `atan`, `atan2`, `atanh`, `bin`, `bround`, `cbrt`, `ceil`, `ceiling`, `conv`, `cos`, `cosh`, `cot`, `csc`, `degrees`, `e`, `exp`, `expm1`, `factorial`, `floor`, `greatest`, `hypot`, `least`, `ln`, `log`, `log10`, `log1p`, `log2`, `negative`, `pi`, `pmod`, `positive`, `pow`, `power`, `printf`, `radians`, `rand`, `randn`, `random`, `rint`, `round`, `sec`, `sign`, `signum`, `sin`, `sinh`, `sqrt`, `tan`, `tanh`, `try_add`, `try_avg`, `try_divide`, `try_mod`, `try_multiply`, `try_remainder`, `try_subtract`, `try_sum`

### String Functions

`ascii`, `btrim`, `char`, `char_length`, `character_length`, `charindex`, `chr`, `concat`, `contains`, `endswith`, `find_in_set`, `format_number`, `format_string`, `initcap` (not listed), `instr` (not listed), `left`, `len`, `length`, `levenshtein`, `locate` (not listed), `lower`, `lpad` (not listed), `ltrim` (not listed), `overlay`, `position`, `repeat`, `replace`, `right`, `rpad`, `rtrim`, `split`, `split_part`, `startswith`, `substr`, `substring`, `substring_index`, `trim`, `ucase`, `upper`, `url_decode`, `url_encode`, `luhn_check`

### Utility & Misc Functions

`assert_true`, `coalesce`, `collate`, `collation`, `current_version`, `if`, `iff`, `ifnull`, `inline`, `inline_outer`, `named_struct`, `nanvl`, `nullif`, `stack`, `struct`, `typeof`, `uuid`, `version`, `when`, `explode`, `explode_outer`, `posexplode` (not listed), `posexplode_outer` (not listed), `aggregate`, `reduce`, `sequence`

### Geospatial (WKB/WKT) Functions

`to_geography`, `to_geometry`, `try_to_geography`, `try_to_geometry`

> **Note:** Functions `stringdecode` and `try_remainder` also appear in the allowed list, but are not documented separately in the provided source.

^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

---

## Usage in View Sharing

When creating a view that will be shared using [Delta Sharing](/concepts/delta-sharing.md) between two Databricks workspaces, the view definition **must only use** functions from the list above. If a view references an unsupported function, the sharing operation fails with an error. ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

For the complete, authoritative list of all built-in functions and operators available in Databricks SQL, see the official [Databricks SQL language manual](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-functions-builtin-alpha). ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

---

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md)
- [Databricks-to-Databricks View Sharing](/concepts/databricks-to-databricks-view-sharing.md)
- Databricks SQL language manual
- [Unity Catalog](/concepts/unity-catalog.md)

## Sources

- functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md

# Citations

1. [functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md](/references/functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws-c0b6a2ae.md)
