# Cell towers data ETL pipeline
## **Project introduction** 
This repository contains the ETL pipeline project which is designed to extract, transform, and load data from a public [dataset](https://datasets.clickhouse.com/cell_towers.csv.xz) of cell towers into a ClickHouse database.
## **Problem statement**
Our goal is to download data from an open source, filter the data by the required Mobile Country Code (MCC), partition the downloaded data into smaller chunks for faster and more efficient data processing, and upload the data to ClickHouse for further analysis.
## **Technologies**
- **Workflow orchestration** - [Apache Airflow](https://airflow.apache.org/)
- **Data load and transformation** - [PySpark](https://spark.apache.org/docs/latest/api/python/index.html)
- **Data warehouse** - [ClickHouse](https://clickhouse.com/)
## **Data pipeline**
The pipeline consists of three main tasks:
- **Extract**: The extract task uses the [requests](https://requests.readthedocs.io/en/latest/) library to download the cell towers dataset from a public URL in CSV format. The file is then saved to a local directory.
- **Transform**: The transform task uses PySpark to read the CSV file, filter the data based on a list of MCC, and repartition the data into 10 smaller chunks. The transformed data is then saved to a different local directory.
- **Load**: The load task uses PySpark and the ClickHouse JDBC driver to load the transformed data into a ClickHouse database. The task creates a connection to the database using the [ClickhouseHook](https://github.com/bryzgaloff/airflow-clickhouse-plugin) and then writes the data to a specified table. The task also includes an option to ignore duplicates during a reload in case of a failure. \

The PythonOperator is used to execute the **extract task**, which is a simple Python function. The SparkSubmitOperator is used to execute the **transform** and **load tasks**, which are defined as PySpark functions using the task.pyspark decorator. The SparkSubmitOperator allows the pipeline to submit Spark applications to a remote Spark cluster.
## **Conclusion**
In summary, this ETL pipeline provides an efficient and scalable way to extract, transform, and load large datasets into a ClickHouse database using Apache Airflow and Apache Spark. The pipeline's modular design and configuration options also make it easy to customize and adapt to different data sources and use cases.
