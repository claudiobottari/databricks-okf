---
title: RESTORE | Databricks on AWS
source: https://docs.databricks.com/aws/en/sql/language-manual/delta-restore
ingestedAt: "2026-06-18T08:19:00.672Z"
---

    -- Restore the employee table to a specific timestamp> RESTORE TABLE employee TO TIMESTAMP AS OF '2022-08-02 00:00:00'; table_size_after_restore num_of_files_after_restore num_removed_files num_restored_files removed_files_size restored_files_size                      100                          3                 1                  0                574                   0-- Restore the employee table to a specific version number retrieved from DESCRIBE HISTORY employee> RESTORE TABLE employee TO VERSION AS OF 1; table_size_after_restore num_of_files_after_restore num_removed_files num_restored_files removed_files_size restored_files_size                      100                          3                 1                  0                574                   0-- Restore the employee table to the state it was in an hour ago> RESTORE TABLE employee TO TIMESTAMP AS OF current_timestamp() - INTERVAL '1' HOUR; table_size_after_restore num_of_files_after_restore num_removed_files num_restored_files removed_files_size restored_files_size                      100                          3                 1                  0                574                   0
