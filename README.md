# Cell towers data ETL pipeline
## **Project introduction** 
This repository contains the ETL-pipeline project which is designed to extract, transform, and load data from a public dataset of [cell towers](https://datasets.clickhouse.com/cell_towers.csv.xz) into a ClickHouse database.
## **Problem statement**
Our goal is to download data from an open source, filter the data by the required Mobile Country Code (MCC), partition the downloaded data into smaller chunks for faster and more efficient data processing, and upload the data to ClickHouse for further analysis.
## **Technologies**
- **Workflow orchestration** - [Apache Airflow](https://airflow.apache.org/)
- **Data load and transformation** - [PySpark](https://spark.apache.org/docs/latest/api/python/index.html)
- **Data warehouse** - [ClickHouse](https://clickhouse.com/)
