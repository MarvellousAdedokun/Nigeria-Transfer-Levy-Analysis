create database if not exists emtl_analysis character set utf8mb4 collate utf8mb4_unicode_ci;

use emtl_analysis;

create table if not exists stg_emtl_table1 (
	stg_id bigint auto_increment primary key,
    source_file varchar(225) not null,
    source_path varchar(500) not null,
    source_container varchar(255) null,
	sha256                    CHAR(64)     NOT NULL,
    archive_sha256            CHAR(64)     NULL,
    sheet                     VARCHAR(100) NULL,
    title_cell                VARCHAR(20)  NULL,
    title_raw                 TEXT         NULL,
    revenue_period_raw        VARCHAR(50)  NULL,
    allocation_period_raw     VARCHAR(50)  NULL,
    allocation_period_source  VARCHAR(30)  NULL,
    header_row                VARCHAR(10)  NULL,
    header_cell               VARCHAR(20)  NULL,
    header_label_raw          VARCHAR(255) NULL,
    row_label_cell            VARCHAR(20)  NULL,
    row_label_raw             VARCHAR(255) NULL,
    cell                      VARCHAR(20)  NULL,
    value_raw                 VARCHAR(64)  NULL,
    row_type                  VARCHAR(30)  NOT NULL,
    emtl_found                VARCHAR(10)  NOT NULL,
    status                    VARCHAR(60)  NULL,
    total_label_cell          VARCHAR(20)  NULL,
    emtl_total_cell           VARCHAR(20)  NULL,
    emtl_total_value_raw      VARCHAR(64)  NULL,
    overall_total_cell        VARCHAR(20)  NULL,
    overall_total_value_raw   VARCHAR(64)  NULL,
    detail_sum_raw            VARCHAR(64)  NULL,
    sum_matches_total         VARCHAR(10)  NULL,
    warning                   TEXT         NULL,
    loaded_at                 TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP,
    KEY idx_stg_source_path (source_path(191))
) ENGINE = InnoDB;   
    