from apache.airflow.providers.clickhouse.hooks import ClickhouseHook
from airflow.decorators import task
from pyspark.sql.functions import col


@task.pyspark(conn_id='spark-local')
def load_to_clickhouse(path, **kwargs):
    """Создаем подключение и загружаем данные в ClickHouse"""
    
    clickhouse_conn = ClickhouseHook.get_conn('clickhouse_connection')

    df = spark.read.options(header=True, inferSchema=True).csv(path)

    df.write.format('jdbc').options(
        url=f'jdbc:clickhouse://{clickhouse_conn.host}:{clickhouse_conn.port}/{clickhouse_conn.database}',
        driver='com.clickhouse.jdbc.ClickHouseDriver',
        dtable='ct_database.cell_towers',
        user=clickhouse_conn.user,
        password=clickhouse_conn.password,
        #  Игнорируем дубликаты при повторной загрузке в случае сбоя,
        #  используя идентичный insert_deduplication_token
        properties={'insert_deduplication_token': 'cell_towers_dag_token'}
    ).mode('append').save()

