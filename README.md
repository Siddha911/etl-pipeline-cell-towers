# Cell Towers data ETL processing pipeline
## **Project introduction** 
This repository contains the ETL-pipeline project which is designed to extract, transform, and load data from a public dataset of cell towers into a [ClickHouse](https://clickhouse.com/) database.
## **Problem statement**
Our goal is to download data from an open source, filter the data by the required Mobile Country Code (MCC), partition the downloaded data into smaller chunks, and upload the data to ClickHouse for further analysis.
