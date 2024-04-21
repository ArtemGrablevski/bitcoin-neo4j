import pandas as pd
from neo4j import Session

from models.transaction import Transaction
from services.csv_processor import get_transactions


class Neo4jService:

    def __init__(self, session: Session) -> None:
        self.session = session

    def _create_nodes_and_relationships(self, transactions: pd.DataFrame) -> None:
        query = """
        UNWIND $batch AS transaction
        MERGE (a:Address {address: transaction.recipient_out})
        MERGE (b:Address {address: transaction.recipient_in})
        MERGE (a)-[t:TRANSACTION {hash: transaction.transaction_hash}]->(b)
        SET t.value_usd = transaction.value_usd, t.time = transaction.time
        """
        batch_size = 1500
        total = len(transactions)
        for i in range(0, total, batch_size):
            batch = transactions.iloc[i:i + batch_size]
            self.session.run(query, batch=batch.to_dict("records"))

    def create_transaction_graph(self, inputs_csv_file: bytes, outputs_csv_file: bytes) -> None:
        transactions = get_transactions(
            inputs_file=inputs_csv_file,
            outputs_file=outputs_csv_file
        )
        self._create_nodes_and_relationships(transactions)

    def get_address_info(self, address: str) -> list[Transaction]:
        query = """
        MATCH (a:Address)-[t:TRANSACTION]->(b:Address)
        WHERE a.address = $address OR b.address = $address
        RETURN a.address AS from, b.address AS to, t.value_usd AS value, t.time AS timestamp
        ORDER BY t.time DESC
        """
        result = self.session.run(query, address=address)
        return [
            Transaction(
                address_from=record.get("from"),
                address_to=record.get("to"),
                value_usd=record.get("value"),
                timestamp=record.get("timestamp")
            ) for record in result
        ]
