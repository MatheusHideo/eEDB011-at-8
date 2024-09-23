import os
from dotenv import load_dotenv

load_dotenv()

data_folder = os.getenv('DATA_FOLDER')
bootstrap_servers = os.getenv('BOOTSTRAP_SERVERS')
database_user = os.getenv('POSTGRES_USER')
database_password = os.getenv('POSTGRES_PASSWORD')
database_host = os.getenv('POSTGRES_HOST')
database_port = os.getenv('POSTGRES_PORT')
database_db = os.getenv('POSTGRES_DATABASE')
database_bancos_table = os.getenv('BANCOS_TABLE_NAME')
database_url = f"postgresql://{database_user}:{database_password}@{database_host}:{database_port}/"
reclamacoes_parquet = f"{data_folder}/trusted/reclamacoes/reclamacoes.parquet"
checkpoints_path = f"{data_folder}/checkpoints"
