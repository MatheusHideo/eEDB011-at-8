import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json
from pyspark.sql.types import StructType, StringType, IntegerType
from config.enviroment import (
    data_folder,
    bootstrap_servers,
    checkpoints_path,
    database_host,
    database_port,
    database_db,
    database_user,
    database_password,
    database_bancos_table)


packages = [
    "org.postgresql:postgresql:42.7.4",
    "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.2"
]


spark = SparkSession.builder.appName("atividade8") \
    .config("spark.jars.packages", ",".join(packages)) \
    .getOrCreate()


def line_execution(df, epoch_id):
    """Function that run every line"""
    df_renamed = df.withColumnRenamed("cnpj_if", "cnpj")
    cnpj = df_renamed.select("cnpj").first()[0]
    bancos_df = read_sql(cnpj)
    if not bancos_df.isEmpty():
        rich = df_renamed.join(bancos_df, on=["cnpj"], how="inner")
        save_json(rich, epoch_id)

def save_json(df, epoch):
    """Function to save json"""
    df = df.toPandas()
    df.to_json(f'{data_folder}/delivery/{epoch}.json', orient="records")

def read_sql(cnpj_if: str):
    """Funtion to select a bank with the provided cnpj"""
    query = f"(SELECT * FROM {database_bancos_table} WHERE cnpj = '{
        cnpj_if}') AS subquery"
    df_bancos = spark.read \
        .format("jdbc") \
        .option("url", f"jdbc:postgresql://{database_host}:{database_port}/{database_db}") \
        .option("dbtable", query) \
        .option("user", database_user) \
        .option("password", database_password) \
        .option("driver", "org.postgresql.Driver") \
        .load()
    return df_bancos

def get_kafka_message(max_offsets_per_trigger: int):
    """Function to read message from kafka"""

    json_schema = StructType() \
        .add("ano", IntegerType()) \
        .add("trimestre", StringType()) \
        .add("Categoria", StringType()) \
        .add("tipo", StringType()) \
        .add("cnpj_if", StringType()) \
        .add("instituicao_financeira", StringType()) \
        .add("indice", StringType()) \
        .add("quantidade_de_reclamacoes_reguladas_procedentes", IntegerType()) \
        .add("quantidade_de_reclamacoes_reguladas_outras", IntegerType()) \
        .add("quantidade_de_reclamacoes_nao_reguladas", IntegerType()) \
        .add("quantidade_total_de_reclamacoes", IntegerType()) \
        .add("quantidade_total_de_clientes_ccs_e_scr", IntegerType()) \
        .add("quantidade_de_clientes_ccs", IntegerType()) \
        .add("quantidade_de_clientes_scr", IntegerType())

    kafka_df = spark.readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", bootstrap_servers) \
        .option("subscribe", "reclamacoes") \
        .option("startingOffsets", "earliest") \
        .option("maxOffsetsPerTrigger", max_offsets_per_trigger) \
        .load()

    message_df = kafka_df.selectExpr("CAST(value AS STRING) as message") \
        .select(from_json(col("message"), json_schema).alias("message")) \
        .select("message.*")

    return message_df


def main():
    parsed_df = get_kafka_message(1)

    query = parsed_df.writeStream \
        .outputMode("append") \
        .foreachBatch(line_execution) \
        .option("checkpointLocation", checkpoints_path) \
        .start()

    query.awaitTermination()
    
if __name__ == "__main__":
    main()
