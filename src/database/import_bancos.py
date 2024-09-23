import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from sqlalchemy import create_engine
import pandas as pd
from config.enviroment import database_url, data_folder, database_db, database_bancos_table

def main():
    engine = create_engine(f"{database_url}{database_db}")
    df = pd.read_parquet(f"{data_folder}/trusted/bancos/bancos_trusted.parquet")
    df.to_sql(database_bancos_table, engine, if_exists="append", index=False)
    
if __name__ == "__main__":
    main()