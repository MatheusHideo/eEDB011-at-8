
# Exercício 8 - Pipeline Streaming com PySpark e Kafka

Este repositório contém o código e a documentação para o **Exercício 8** da disciplina de Ingestão de Dados do curso de Engenharia de Dados.

## Objetivo

O objetivo deste exercício é desenvolver uma pipeline de ingestão de dados utilizando linguagem de programação Python e Pyspark para ingestão e tratamento de dados e para processo de enquecimento utilizando kafka e postgres.

## Estrutura do Repositório

- **`config/`**: Contém script de configuração.
- **`data/`**: Contém os arquivos de dados utilizados para o exercício (raw/, trusted/, delivert/, checkpoint/).
- **`init_postgres_pos/`**: Contém scripts para inciação do banco de dados.
- **`src/`**: Contém scripts do consumidor e produtor.
- **`postgres`**: Pasta padrão para volume de persistencia do Postgres.
- **`kafka_logs`**: Pasta padrão para volume de persistencia do Postgres.

## Tecnologias Utilizadas

- **`Python Pyspark`**: Linguagem de programação utilizada para desenvolvimento dos scripts.
- **`PostgresSQL`**: Utilizado criação do banco de dados e análise de dados estruturados.
- **KAFKA**: Plataforma de streaming de eventos distribuídos de código aberto 

## Como Executar

1. Clone este repositório para sua máquina local:

   ```bash
   git clone https://github.com/MatheusHideo/eEDB011-at-8
   cd eEDB011-at-8
   ```
2. Execute o comando abaixo para instalar os requirimentos:

   ```bash
      pip install -r ./requirements.txt
   ```

3. Crie um .env com as seguintes opções customize se preciso:
   ```
      POSTGRES_DATA_VOLUME="./postgres" ## Ou outro path
      POSTGRES_INIT_VOLUME="./init_postgres_pos"
      KAFKA_DATA_VOLUME="./kafka_logs" ## Ou outro path


      POSTGRES_PASSWORD={Database Password}
      POSTGRES_USER={Database User}
      POSTGRES_PORT="5432"
      POSTGRES_HOST="0.0.0.0"
      POSTGRES_DATABASE = "ingestao"
      BANCOS_TABLE_NAME ={Database Name}

      KAFKA_NODE_ID = 1
      KAFKA_LISTENERS = "DOCKER://0.0.0.0:29092,CONTROLLER://0.0.0.0:9093,PLAINTEXT://0.0.0.0:9092"
      KAFKA_LISTENER_SECURITY_PROTOCOL_MAP = "DOCKER:PLAINTEXT,CONTROLLER:PLAINTEXT,PLAINTEXT:PLAINTEXT"
      KAFKA_CONTROLLER_QUORUM_VOTERS = "1@localhost:9093" 
      KAFKA_PROCESS_ROLES = "broker,controller"
      KAFKA_CONTROLLER_LISTENER_NAMES = "CONTROLLER"
      KAFKA_AUTO_CREATE_TOPICS_ENABLE = "true"
      KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR = 1
      KAFKA_TRANSACTION_STATE_LOG_REPLICATION_FACTOR = 1
      KAFKA_TRANSACTION_STATE_LOG_MIN_ISR = 1
      KAFKA_INTER_BROKER_LISTENER_NAME = "DOCKER"
      KAFKA_PLAINTEXT_PORT = "9092"
      KAFKA_CONTROLLER_PORT = "9093"
      KAFKA_LOG_DIRS = "/var/lib/kafka/data"
      DATA_FOLDER = "./data" ## Ou outro path
      BOOTSTRAP_SERVERS = "0.0.0.0:9092"
   ```

4. Configure seus caminhos e conexões no arquivo config/define se necessario


5. Você terá duas opções para rodar o projeto pelo script principal ou por script:

6. Script principal:
   ```bash
      python src/main.py
   ```

7. Por scripts:
   ```bash
      src/producer/producer.py
      src/consumer/consumer.py
   ```

## Contribuições

Sinta-se à vontade para abrir issues ou enviar pull requests para contribuir com melhorias ou correções.

