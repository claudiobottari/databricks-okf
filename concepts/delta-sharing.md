---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f0b3984a5ee3c403eefc18bad4634aacd407d17ef7d612a8ca4d0acd3e7fa98c
  pageDirectory: concepts
  sources:
    - functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-sharing
    - Data Sharing
    - Data sharing
    - Delta Sharing view
    - VIEW (Delta Sharing)
    - Audit Logs for Data Sharing
    - Delta Share
    - Delta Sharing Protocol
    - Delta Sharing Providers
    - Delta Sharing Shares
    - Provider (Data Sharing)
    - Share (Delta Sharing)
    - Table Sharing
    - Update shares
    - View Sharing
    - View sharing
  citations:
    - file: functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md
title: Delta Sharing
description: An open protocol for secure real-time data sharing across platforms, foundational to Databricks-to-Databricks view sharing
tags:
  - delta-sharing
  - data-sharing
  - open-protocol
timestamp: "2026-06-19T18:57:27.463Z"
---

# Delta Sharing

**Delta Sharing** is an open protocol for secure data sharing across platforms. On Databricks, Delta Sharing supports **Databricks-to-Databricks view sharing**, which allows a provider to share a view (a saved SQL query) from their Databricks environment with a recipient’s Databricks workspace. ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

## Allowed Functions and Operators in View Sharing

To maintain data security when using Databricks-to-Databricks view sharing, only a limited subset of Databricks built-in functions and operators is permitted in the view definition. All other functions are blocked. The following categories are allowed:

- **Arithmetic and bitwise operators:** `-`, `!`, `*`, `/`, `&`, `%`, `^`, `+`, `<`, `<<`, `<=`, `<=>`, `=`, `==`, `>`, `>=`, `>>`, `>>>`, `|`, `~`
- **Comparison and logical operators:** `<`, `<=`, `<=>`, `=`, `==`, `>`, `>=`, `AND`, `OR`, `NOT`, `BETWEEN`, `IN`, `LIKE`, `ILIKE`, `RLIKE`, `IS NULL`, `IS NOT NULL`
- **Mathematical functions:** `abs`, `acos`, `acosh`, `asin`, `asinh`, `atan`, `atan2`, `atanh`, `cbrt`, `ceil`, `ceiling`, `cos`, `cosh`, `cot`, `csc`, `degrees`, `div`, `e`, `exp`, `expm1`, `factorial`, `floor`, `hypot`, `ln`, `log`, `log10`, `log1p`, `log2`, `mod`, `negative`, `pi`, `pmod`, `positive`, `pow`, `power`, `radians`, `rand`, `randn`, `random`, `rint`, `round`, `sec`, `sign`, `signum`, `sin`, `sinh`, `sqrt`, `tan`, `tanh`, `try_divide`, `try_mod`, `try_multiply`, `try_subtract`
- **String functions:** `ascii`, `base64`, `bin`, `bit_length`, `btrim`, `char`, `char_length`, `character_length`, `charindex`, `chr`, `concat`, `contains`, `decode`, `encode`, `endswith`, `find_in_set`, `format_number`, `format_string`, `hex`, `initcap`, `instr`, `left`, `len`, `length`, `levenshtein`, `locate`, `lower`, `lpad`, `ltrim`, `mask`, `octet_length`, `overlay`, `position`, `printf`, `repeat`, `replace`, `reverse`, `right`, `rpad`, `rtrim`, `sha`, `sha1`, `sha2`, `soundex`, `space`, `split`, `split_part`, `startswith`, `str_to_map`, `string`, `substr`, `substring`, `substring_index`, `to_binary`, `to_char`, `to_number`, `to_varchar`, `translate`, `trim`, `try_to_binary`, `try_to_number`, `ucase`, `unbase64`, `unhex`, `upper`, `url_decode`, `url_encode`
- **Date/time functions:** `add_months`, `convert_timezone`, `curdate`, `current_date`, `current_timestamp`, `current_timezone`, `date`, `date_add`, `date_diff`, `date_format`, `date_from_unix_date`, `date_part`, `date_sub`, `date_trunc`, `dateadd`, `datediff`, `day`, `dayofmonth`, `dayofweek`, `dayofyear`, `extract`, `from_unixtime`, `from_utc_timestamp`, `getdate`, `hour`, `last_day`, `make_date`, `make_dt_interval`, `make_interval`, `make_timestamp`, `make_ym_interval`, `minute`, `month`, `months_between`, `next_day`, `now`, `quarter`, `second`, `timestamp`, `timestamp_micros`, `timestamp_millis`, `timestamp_seconds`, `to_date`, `to_timestamp`, `to_unix_timestamp`, `to_utc_timestamp`, `trunc`, `try_add`, `try_to_timestamp`, `unix_date`, `unix_micros`, `unix_millis`, `unix_seconds`, `unix_timestamp`, `weekday`, `weekofyear`, `year`
- **Array functions:** `array`, `array_agg`, `array_append`, `array_compact`, `array_contains`, `array_distinct`, `array_except`, `array_insert`, `array_intersect`, `array_join`, `array_max`, `array_min`, `array_position`, `array_prepend`, `array_remove`, `array_repeat`, `array_size`, `array_sort`, `array_union`, `arrays_overlap`, `arrays_zip`, `cardinality`, `element_at`, `flatten`, `slice`, `sort_array`
- **Map functions:** `map`, `map_concat`, `map_contains_key`, `map_entries`, `map_filter`, `map_from_arrays`, `map_from_entries`, `map_keys`, `map_values`, `map_zip_with`, `str_to_map`
- **Aggregate functions:** `any`, `any_value`, `approx_count_distinct`, `approx_percentile`, `approx_top_k`, `avg`, `bit_and`, `bit_or`, `bit_xor`, `bitmap_construct_agg`, `bitmap_count`, `bitmap_or_agg`, `bool_and`, `bool_or`, `collect_list`, `collect_set`, `corr`, `count`, `count_if`, `count_min_sketch`, `covar_pop`, `covar_samp`, `cume_dist`, `dense_rank`, `every`, `first`, `first_value`, `grouping`, `grouping_id`, `histogram_numeric`, `hll_sketch_agg`, `hll_union_agg`, `kurtosis`, `lag`, `last`, `last_value`, `lead`, `max`, `max_by`, `mean`, `median`, `min`, `min_by`, `mode`, `nth_value`, `ntile`, `percent_rank`, `percentile`, `percentile_approx`, `percentile_cont`, `percentile_disc`, `rank`, `regr_avgx`, `regr_avgy`, `regr_count`, `regr_intercept`, `regr_r2`, `regr_slope`, `regr_sxx`, `regr_sxy`, `regr_syy`, `row_number`, `skewness`, `some`, `std`, `stddev`, `stddev_pop`, `stddev_samp`, `sum`, `try_avg`, `try_sum`, `var_pop`, `var_samp`, `variance`
- **H3 geospatial functions** (a large family starting with `h3_`)
- **Miscellaneous functions:** `aes_decrypt`, `aes_encrypt`, `assert_true`, `bit_get`, `bitmap_bit_position`, `bitmap_bucket_number`, `bitmap_count`, `cast`, `coalesce`, `collate`, `collation`, `contains`, `conv`, `crc32`, `current_catalog`, `current_database`, `current_metastore`, `current_recipient`, `current_schema`, `current_version`, `exists`, `get`, `getbit`, `hash`, `if`, `iff`, `ifnull`, `isnan`, `isnotnull`, `isnull`, `nanvl`, `named_struct`, `nullif`, `nvl`, `nvl2`, `random`, `regexp`, `regexp_extract`, `regexp_extract_all`, `regexp_like`, `regexp_replace`, `session_window`, `shiftleft`, `shiftright`, `shiftrightunsigned`, `spark_partition_id`, `struct`, `try_divide`, `try_mod`, `try_multiply`, `try_remainder`, `try_subtract`, `typeof`, `uuid`, `version`, `when`, `width_bucket`, `window`, `window_time`, `zip_with`

> **Note:** The list above is a summary. Refer to the official Databricks documentation for the complete and up‑to‑date list of allowed functions.

## Purpose of the Restriction

The function subset is enforced to protect the provider’s data. By limiting view definitions to a curated set of deterministic, safe functions, Databricks prevents view recipients from executing arbitrary SQL that could expose or manipulate data outside the shared view definition. ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

## Related Concepts

- Databricks — The unified analytics platform that hosts Delta Sharing.
- Delta Sharing protocol — The underlying open protocol for secure data sharing.
- [View sharing](/concepts/delta-sharing.md) — Sharing a query result rather than a table.
- [Databricks-to-Databricks Sharing](/concepts/databricks-to-databricks-sharing.md) — A specific Delta Sharing scenario where both parties are on Databricks.

## Sources

- functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md

# Citations

1. [functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md](/references/functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws-c0b6a2ae.md)
