import pandas as pd
import time, json
from kafka import KafkaProducer
from config.enviroment import reclamacoes_parquet, bootstrap_servers

def main():

    parquet_file = reclamacoes_parquet

    producer = KafkaProducer(
        bootstrap_servers=[bootstrap_servers],
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    df = pd.read_parquet(parquet_file)
    batch_size = 10
    for start in range(0, len(df), batch_size):
        end = min(start + batch_size, len(df))
        print(f"Inserindo da linha {start} até {end}")
        batch = df.iloc[start:end]
        # Convert the batch to JSON format
        batch_dict = batch.to_dict(orient='records')
        for dict in batch_dict: 
            producer.send('reclamacoes', dict)
        producer.flush()
        time.sleep(2)
        
if __name__ == "__main__":
    main()