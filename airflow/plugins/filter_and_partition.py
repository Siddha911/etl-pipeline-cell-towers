from airflow.decorators import task
from pyspark.sql.functions import col


@task.pyspark(conn_id='spark-local')
def filter_and_partition(tmp_file, path, **kwargs):
    """Функция с ипользование декоратора PySpark Decorator. 
    SparkSession и SparkContext созданы используя Spark Connect.
    Функция читает записанный файл, затем фильтрует данные по требуемым МСС,
    далее разбивает файл на 10 блоков меньшего размера"""
    
    df = spark.read.options(header=True, inferSchema=True).csv(tmp_file)

    mcc_list = [262, 460, 310, 208, 510,404, 250, 724, 234, 311] 
    filtered_df = df.filter(col('mcc').isin(mcc_list))

    partitioned_df = filtered_df.repartition(10)
    partitioned_df.write.csv(path) 
