# Bitcoin transactions

## Run with Docker
Don't forget to create `.env` file before. Use `.env.example` as an example.
```
docker compose up --build
```

## How to use
- Run the app
- Open `http://127.0.0.1:8000/docs` in your browser
- Upload tsv files from folder `input_files_examples` or from [blockchair.com](https://blockchair.com) (inputs and outputs archives) to the endpoint `/api/transactions/upload`
- use `/api/transactions/{address}` endpoint to view address stats
![swagger](https://raw.githubusercontent.com/ArtemGrablevski/bitcoin-neo4j/main/images/swagger.png)

## Visualisation example:
![graph](https://raw.githubusercontent.com/ArtemGrablevski/bitcoin-neo4j/main/images/graph_example.png)

## How can the project be improved:
- Use Kafka/RabbitMQ
- Read large input TSV files in batches
- Set up logging and monitoring
- Set up authentication
