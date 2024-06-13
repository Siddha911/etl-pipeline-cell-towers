--- Создание базы данных
CREATE DATABASE IF NOT EXISTS ct_database;

--- DDL для schema таблицы
CREATE TABLE IF NOT EXISTS ct_database.cell_towers 
(
    radio Enum8('' = 0, 'CDMA' = 1, 'GSM' = 2, 'LTE' = 3, 'NR' = 4, 'UMTS' = 5),
    mcc UInt16,
    net UInt16,
    area UInt16,
    cell UInt64,
    unit UInt16,
    lon Float64,
    lat Float64,
    range UInt32,
    samples UInt32,
    changeable UInt8,
    created DateTime,
    updated DateTime,
    averageSignal UInt8
) 
ENGINE = MergeTree() ORDER BY (radio, mcc, net, created)
SETTINGS non_replicated_deduplication_window = 100;