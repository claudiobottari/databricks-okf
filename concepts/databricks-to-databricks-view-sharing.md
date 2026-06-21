---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f713fa7540d4cf2d9c857dc20ca575e35d0f9d78802927b5d37a72032739b633
  pageDirectory: concepts
  sources:
    - functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-to-databricks-view-sharing
    - DVS
  citations:
    - file: functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md
title: Databricks-to-Databricks View Sharing
description: A Delta Sharing mode that allows sharing views between Databricks workspaces while restricting SQL functions for security
tags:
  - delta-sharing
  - databricks
  - data-sharing
timestamp: "2026-06-19T18:57:33.821Z"
---

# Databricks-to-Databricks View Sharing

**Databricks-to-Databricks view sharing** is a [Delta Sharing](/concepts/delta-sharing.md) feature that enables a provider workspace to share views (SQL-based derived datasets) with a consumer workspace. To protect data security, only a pre-approved subset of Databricks built-in functions and operators is allowed in shared view definitions. If a view uses any function or operator outside this allowed set, the share operation fails. ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

## How It Works

When a provider shares a view with a consumer Databricks workspace, the view's SQL definition is evaluated against an allowlist of supported built-in functions and operators. Any view that references an unsupported function (including user-defined functions (UDFs) or other non-built-in constructs) cannot be shared. The allowlist is periodically reviewed by Databricks and may expand in future releases. ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

The restriction applies at the time the view is created or updated for sharing; existing views that use unsupported functions remain usable inside the provider workspace but cannot be shared across workspaces. ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

## Allowed Functions and Operators

The supported set includes most standard arithmetic operators, [comparison operators](/concepts/ab-comparison-of-agent-configurations.md), bitwise operators, and a broad range of scalar, [aggregate](/concepts/aggregate-metrics.md), array, map, and geospatial (H3) functions. Below is a categorized summary. The complete, authoritative list is in the source document.

### Arithmetic Operators
`-` (unary minus), `!`, `*`, `/`, `%`, `+`, `^`, `~`, `&`, `|`, `<<`, `>>`, `>>>`, `div`, `mod`, `pmod`. ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

### Comparison Operators
`<`, `<=`, `<=>`, `=`, `==`, `>`, `>=`, `between`, `ilike`, `like`, `rlike`, `regexp`. ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

### Logical Operators
`and`, `or`, `not`, `in`, `exists`, `forall`, `some`, `any`, `every`. ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

### String Functions
`ascii`, `base64`, `bit_length`, `btrim`, `char_length`, `character_length`, `charindex`, `chr`, `concat`, `contains`, `decode`, `encode`, `endswith`, `find_in_set`, `format_number`, `format_string`, `initcap`, `instr`, `lcase`, `left`, `len`, `length`, `levenshtein`, `locate`, `lower`, `lpad`, `ltrim`, `octet_length`, `overlay`, `position`, `printf`, `regexp_extract`, `regexp_extract_all`, `regexp_like`, `regexp_replace`, `repeat`, `replace`, `reverse`, `right`, `rpad`, `rtrim`, `sentences`, `soundex`, `space`, `split`, `split_part`, `startswith`, `str_to_map`, `string`, `substr`, `substring`, `substring_index`, `translate`, `trim`, `trunc`, `ucase`, `unbase64`, `unhex`, `upper`, `url_decode`, `url_encode`. ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

### Date and Time Functions
`add_months`, `curdate`, `current_date`, `current_timestamp`, `current_timezone`, `date`, `date_add`, `date_diff`, `date_format`, `date_from_unix_date`, `date_part`, `date_sub`, `date_trunc`, `dateadd`, `datediff`, `datepart`, `day`, `dayofmonth`, `dayofweek`, `dayofyear`, `extract`, `from_unixtime`, `from_utc_timestamp`, `getdate`, `hour`, `last_day`, `localtimestamp`, `make_date`, `make_dt_interval`, `make_interval`, `make_timestamp`, `make_timestamp_ltz`, `make_timestamp_ntz`, `make_ym_interval`, `minute`, `month`, `monthname`, `months_between`, `next_day`, `now`, `quarter`, `second`, `session_window`, `timestamp`, `timestamp_micros`, `timestamp_millis`, `timestamp_seconds`, `to_date`, `to_timestamp`, `to_timestamp_ltz`, `to_timestamp_ntz`, `to_unix_timestamp`, `to_utc_timestamp`, `unix_date`, `unix_micros`, `unix_millis`, `unix_seconds`, `unix_timestamp`, `weekday`, `weekofyear`, `window`, `window_time`, `year`. ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

### Mathematical Functions
`abs`, `acos`, `acosh`, `asin`, `asinh`, `atan`, `atan2`, `atanh`, `bin`, `bround`, `cbrt`, `ceil`, `ceiling`, `conv`, `cos`, `cosh`, `cot`, `csc`, `degrees`, `e`, `exp`, `expm1`, `factorial`, `floor`, `hex`, `hypot`, `ln`, `log`, `log10`, `log1p`, `log2`, `negative`, `pi`, `positive`, `pow`, `power`, `radians`, `rand`, `randn`, `random`, `rint`, `round`, `sec`, `shiftleft`, `shiftright`, `shiftrightunsigned`, `sign`, `signum`, `sin`, `sinh`, `sqrt`, `tan`, `tanh`, `try_add`, `try_divide`, `try_mod`, `try_multiply`, `try_remainder`, `try_subtract`, `width_bucket`. ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

### Aggregate Functions
`any_value`, `approx_count_distinct`, `approx_percentile`, `approx_top_k`, `avg`, `bit_and`, `bit_or`, `bit_xor`, `bitmap_construct_agg`, `bitmap_or_agg`, `bool_and`, `bool_or`, `collect_list`, `collect_set`, `corr`, `count`, `count_if`, `count_min_sketch`, `covar_pop`, `covar_samp`, `cume_dist`, `dense_rank`, `first`, `first_value`, `grouping`, `grouping_id`, `histogram_numeric`, `hll_sketch_agg`, `hll_union_agg`, `kurtosis`, `lag`, `last`, `last_value`, `lead`, `max`, `max_by`, `mean`, `median`, `min`, `min_by`, `mode`, `nth_value`, `ntile`, `percent_rank`, `percentile`, `percentile_approx`, `percentile_cont`, `percentile_disc`, `rank`, `regr_avgx`, `regr_avgy`, `regr_count`, `regr_intercept`, `regr_r2`, `regr_slope`, `regr_sxx`, `regr_sxy`, `regr_syy`, `row_number`, `skewness`, `some`, `std`, `stddev`, `stddev_pop`, `stddev_samp`, `sum`, `try_avg`, `try_sum`, `var_pop`, `var_samp`, `variance`. ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

### Array Functions
`array`, `array_agg`, `array_append`, `array_compact`, `array_contains`, `array_distinct`, `array_except`, `array_insert`, `array_intersect`, `array_join`, `array_max`, `array_min`, `array_position`, `array_prepend`, `array_remove`, `array_repeat`, `array_size`, `array_sort`, `array_union`, `arrays_overlap`, `arrays_zip`, `cardinality`, `element_at`, `explode`, `explode_outer`, `filter`, `flatten`, `forall`, `inline`, `inline_outer`, `slice`, `sort_array`, `zip_with`. ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

### Map Functions
`map`, `map_concat`, `map_contains_key`, `map_entries`, `map_filter`, `map_from_arrays`, `map_from_entries`, `map_keys`, `map_values`, `map_zip_with`, `str_to_map`. ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

### Conditional and Conversion Functions
`assert_true`, `cast`, `coalesce`, `decode`, `if`, `iff`, `ifnull`, `isnan`, `isnotnull`, `isnull`, `nanvl`, `nullif`, `nvl`, `nvl2`, `try_cast`, `typeof`. Also all standard type conversions: `bigint`, `binary`, `boolean`, `date`, `decimal`, `double`, `float`, `int`, `smallint`, `string`, `timestamp`, `tinyint`, `to_binary`, `to_char`, `to_number`, `to_varchar`, `try_to_binary`, `try_to_number`, `try_to_timestamp`. ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

### Geospatial Functions (H3)
`h3_boundaryasgeojson`, `h3_boundaryaswkb`, `h3_boundaryaswkt`, `h3_centerasgeojson`, `h3_centeraswkb`, `h3_centeraswkt`, `h3_compact`, `h3_coverash3`, `h3_coverash3string`, `h3_distance`, `h3_h3tostring`, `h3_hexring`, `h3_ischildof`, `h3_ispentagon`, `h3_isvalid`, `h3_kring`, `h3_kringdistances`, `h3_longlatash3`, `h3_longlatash3string`, `h3_maxchild`, `h3_minchild`, `h3_pointash3`, `h3_pointash3string`, `h3_polyfillash3`, `h3_polyfillash3string`, `h3_resolution`, `h3_stringtoh3`, `h3_tessellateaswkb`, `h3_tochildren`, `h3_toparent`, `h3_try_coverash3`, `h3_try_coverash3string`, `h3_try_distance`, `h3_try_polyfillash3`, `h3_try_polyfillash3string`, `h3_try_tessellateaswkb`, `h3_try_validate`, `h3_uncompact`, `h3_validate`. ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

### Other Functions
`aes_decrypt`, `aes_encrypt`, `aggregate`, `collate`, `collation`, `crc32`, `current_catalog`, `current_database`, `current_metastore`, `current_recipient`, `current_schema`, `current_version`, `get`, `getbit`, `hash`, `luhn_check`, `md5`, `named_struct`, `reduce`, `sha`, `sha1`, `sha2`, `shuffle`, `spark_partition_id`, `stack`, `struct`, `transform`, `transform_keys`, `transform_values`, `try_divide`, `try_mod`, `typeof`, `uuid`, `version`, `when`. ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

## Restrictions

Views that use any built-in function or operator not listed above cannot be shared via Databricks-to-Databricks view sharing. User-defined functions (UDFs) and other non-standard constructs are also excluded. The allowed set is periodically reviewed and may change in future releases. ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) – The open protocol for data sharing across platforms
- Views – Logical tables defined by SQL queries
- [Unity Catalog](/concepts/unity-catalog.md) – The governance layer that manages shared views
- [Built-in Functions](/concepts/abac-built-in-tag-functions.md) – Full reference of Databricks SQL functions
- [User-defined functions (UDFs)](/concepts/abac-user-defined-functions-udfs.md) – Custom functions not allowed in shared views
- [Databricks-to-Databricks Sharing](/concepts/databricks-to-databricks-sharing.md) – Broader sharing capabilities for tables and other objects

## Sources

- functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md

# Citations

1. [functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md](/references/functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws-c0b6a2ae.md)
