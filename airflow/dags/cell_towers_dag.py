from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from datetime import datetime
import requests


def download_and_extract(url, path, **kwargs):
    """Функция для загрузки данных с использование библиотеки requests"""
    
    response = requests.get(url, params={'downloadformat': 'csv.xz'})
    response.raise_for_status()

    with open(path, mode='wb') as file:
        file.write(response.content)


default_args = {
    'owner': 'airflow',
    'start_date': datetime.today(),
    'depends_on_past': False,
    'retries': 1,
}

dag = DAG(
    dag_id='cell_towers_dag',
    default_args=default_args,
    schedule_interval='@once'
)

extract_task = PythonOperator(
    task_id='extract',
    python_callable=download_and_extract,
    op_kwargs={'url': 'https://datasets.clickhouse.com/cell_towers.csv.xz', 
               'path': '~/airflow_workspace/downloads/cell_towers.csv.xz'},
    dag=dag
)

transform_task = SparkSubmitOperator(
    name='transform',
    application='~/airflow_workspace/airflow/plugins/filter_and_partition.py',
    application_args=['~/airflow_workspace/downloads/cell_towers.csv.xz',
                      '~/airflow_workspace/airflow/files'],
    dag=dag
)

load_task = SparkSubmitOperator(
    name='load',
    application='~/airflow_workspace/airflow/plugins/load_to_clickhouse.py',
    application_args=['~/airflow_workspace/airflow/files'],
    dag=dag
)

extract_task >> transform_task >> load_task 
