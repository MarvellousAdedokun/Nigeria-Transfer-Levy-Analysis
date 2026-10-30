create database if not exists emtl_analysis character set utf8mb4 collate utf8mb4_unicode_ci;

use emtl_analysis;

CREATE TABLE IF NOT EXISTS stg_emtl_table1 (
    stg_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    source_file VARCHAR(225) NOT NULL,
    source_path VARCHAR(500) NOT NULL,
    source_container VARCHAR(255) NULL,
    sha256 CHAR(64) NOT NULL,
    archive_sha256 CHAR(64) NULL,
    sheet VARCHAR(100) NULL,
    title_cell VARCHAR(20) NULL,
    title_raw TEXT NULL,
    revenue_period_raw VARCHAR(50) NULL,
    allocation_period_raw VARCHAR(50) NULL,
    allocation_period_source VARCHAR(30) NULL,
    header_row VARCHAR(10) NULL,
    header_cell VARCHAR(20) NULL,
    header_label_raw VARCHAR(255) NULL,
    row_label_cell VARCHAR(20) NULL,
    row_label_raw VARCHAR(255) NULL,
    cell VARCHAR(20) NULL,
    value_raw VARCHAR(64) NULL,
    row_type VARCHAR(30) NOT NULL,
    emtl_found VARCHAR(10) NOT NULL,
    status VARCHAR(60) NULL,
    total_label_cell VARCHAR(20) NULL,
    emtl_total_cell VARCHAR(20) NULL,
    emtl_total_value_raw VARCHAR(64) NULL,
    overall_total_cell VARCHAR(20) NULL,
    overall_total_value_raw VARCHAR(64) NULL,
    detail_sum_raw VARCHAR(64) NULL,
    sum_matches_total VARCHAR(10) NULL,
    warning TEXT NULL,
    loaded_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    KEY idx_stg_source_path (source_path (191))
)  ENGINE=INNODB;   

USE emtl_analysis;
SELECT 
    COUNT(*)
FROM
    stg_emtl_table1;

-- to verify
select count(*) as rows_loaded, count(distinct source_path) as workbooks from stg_emtl_table1;
select row_type, count(*) from stg_emtl_table1 group by row_type;
select revenue_period_raw, allocation_period_raw from stg_emtl_table1 limit 5;
select value_raw from stg_emtl_table1 where value_raw like '%.%.%';

-- the recipient mapping table
create table if not exists recipient_mapping (
	row_label_raw varchar(225) primary key,
    recipient_category varchar(40) not null,
    review_status varchar(20) not null
) ENGINE=INNODB;

SELECT recipient_category, COUNT(*) FROM recipient_mapping GROUP BY recipient_category;

CREATE TABLE IF NOT EXISTS source_files (
    source_file_id   INT AUTO_INCREMENT PRIMARY KEY,
    source_path      VARCHAR(500) NOT NULL,
    file_name        VARCHAR(255) NOT NULL,
    source_container VARCHAR(255) NULL,
    sha256           CHAR(64)     NOT NULL,
    archive_sha256   CHAR(64)     NULL,
    sheet_name       VARCHAR(100) NULL,
    title_cell       VARCHAR(20)  NULL,
    title_raw        TEXT         NULL,
    UNIQUE KEY uq_source_files_path (source_path)
) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS reporting_periods (
    period_id                 INT AUTO_INCREMENT PRIMARY KEY,
    source_file_id            INT         NOT NULL,
    revenue_month             DATE        NOT NULL,
    allocation_month          DATE        NOT NULL,
    allocation_period_source  VARCHAR(30) NULL,
    emtl_line_present         TINYINT(1)  NOT NULL,
    extraction_status         VARCHAR(60) NULL,
    UNIQUE KEY uq_period_source (source_file_id),
    UNIQUE KEY uq_period_revenue_month (revenue_month),
    CONSTRAINT fk_period_source
        FOREIGN KEY (source_file_id) REFERENCES source_files (source_file_id)
) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS emtl_observations (
    observation_id      BIGINT AUTO_INCREMENT PRIMARY KEY,
    period_id           INT           NOT NULL,
    row_label_raw       VARCHAR(255)  NOT NULL,
    recipient_category  VARCHAR(40)   NOT NULL,
    row_type            VARCHAR(10)   NOT NULL,
    source_cell         VARCHAR(20)   NOT NULL,
    amount_ngn          DECIMAL(24,4) NULL,
    UNIQUE KEY uq_obs_period_cell (period_id, source_cell),
    CONSTRAINT fk_obs_period
        FOREIGN KEY (period_id) REFERENCES reporting_periods (period_id)
) ENGINE = InnoDB;

-- tun the period text into dates, we need to test different things first
SELECT DISTINCT revenue_period_raw FROM stg_emtl_table1;

SELECT revenue_period_raw, REPLACE(revenue_period_raw,',','')FROM stg_emtl_table1 LIMIT 5;

SELECT SUBSTRING_INDEX(TRIM(REPLACE('July , 2025', ',', ' ')), ' ', 1),
       SUBSTRING_INDEX(TRIM(REPLACE('July , 2025', ',', ' ')), ' ', -1);
       
SELECT STR_TO_DATE('1 July 2025', '%e %M %Y');

CREATE OR REPLACE VIEW v_stg_periods AS
SELECT
    source_path,
    MAX(revenue_period_raw)        AS revenue_period_raw,
    MAX(allocation_period_raw)     AS allocation_period_raw,
    MAX(allocation_period_source)  AS allocation_period_source,
    STR_TO_DATE(CONCAT('1 ',
        SUBSTRING_INDEX(TRIM(REPLACE(MAX(revenue_period_raw), ',', ' ')), ' ', 1), ' ',
        SUBSTRING_INDEX(TRIM(REPLACE(MAX(revenue_period_raw), ',', ' ')), ' ', -1)), '%e %M %Y') AS revenue_month,
    STR_TO_DATE(CONCAT('1 ',
        SUBSTRING_INDEX(TRIM(REPLACE(MAX(allocation_period_raw), ',', ' ')), ' ', 1), ' ',
        SUBSTRING_INDEX(TRIM(REPLACE(MAX(allocation_period_raw), ',', ' ')), ' ', -1)), '%e %M %Y')
                                   AS allocation_month,
    MAX(emtl_found = 'True')       AS emtl_line_present,
    MAX(status)                    AS extraction_status
FROM stg_emtl_table1
GROUP BY source_path;

-- 1. Source files
INSERT INTO source_files
    (source_path, file_name, source_container, sha256, archive_sha256, sheet_name, title_cell, title_raw)
SELECT source_path, MAX(source_file), MAX(source_container), MAX(sha256), MAX(archive_sha256),
       MAX(sheet), MAX(title_cell), MAX(title_raw)
FROM stg_emtl_table1
GROUP BY source_path
ON DUPLICATE KEY UPDATE
    file_name        = VALUES(file_name),
    source_container = VALUES(source_container),
    sha256           = VALUES(sha256),
    archive_sha256   = VALUES(archive_sha256),
    sheet_name       = VALUES(sheet_name),
    title_cell       = VALUES(title_cell),
    title_raw        = VALUES(title_raw);

-- 2. Reporting periods (a failed date parse violates NOT NULL and stops the load)
INSERT INTO reporting_periods
    (source_file_id, revenue_month, allocation_month, allocation_period_source, emtl_line_present, extraction_status)
SELECT sf.source_file_id, p.revenue_month, p.allocation_month,
       p.allocation_period_source, p.emtl_line_present, p.extraction_status
FROM v_stg_periods p
JOIN source_files sf ON sf.source_path = p.source_path
ON DUPLICATE KEY UPDATE
    revenue_month            = VALUES(revenue_month),
    allocation_month         = VALUES(allocation_month),
    allocation_period_source = VALUES(allocation_period_source),
    emtl_line_present        = VALUES(emtl_line_present),
    extraction_status        = VALUES(extraction_status);

-- 3. Observations: Table I detail and total rows of the EMTL column
INSERT INTO emtl_observations
    (period_id, row_label_raw, recipient_category, row_type, source_cell, amount_ngn)
SELECT rp.period_id,
       TRIM(s.row_label_raw),
       COALESCE(m.recipient_category, 'UNMAPPED'),
       s.row_type,
       s.cell,
       CAST(NULLIF(TRIM(s.value_raw), '') AS DECIMAL(24,4))
FROM stg_emtl_table1 s
JOIN source_files sf      ON sf.source_path = s.source_path
JOIN reporting_periods rp ON rp.source_file_id = sf.source_file_id
LEFT JOIN recipient_mapping m ON m.row_label_raw = TRIM(s.row_label_raw)
WHERE s.emtl_found = 'True'
  AND s.row_type IN ('detail', 'total')
  AND s.cell IS NOT NULL
ON DUPLICATE KEY UPDATE
    row_label_raw      = VALUES(row_label_raw),
    recipient_category = VALUES(recipient_category),
    row_type           = VALUES(row_type),
    amount_ngn         = VALUES(amount_ngn);