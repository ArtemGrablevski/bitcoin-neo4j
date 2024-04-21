import pandas as pd


def get_transactions(inputs_file: bytes, outputs_file: bytes) -> pd.DataFrame:

    inputs = pd.read_csv(inputs_file, sep="\t")
    inputs = inputs[["recipient", "transaction_hash"]]

    outputs = pd.read_csv(outputs_file, sep="\t")
    outputs = outputs[["recipient", "value_usd", "time", "transaction_hash"]]

    transactions = outputs.merge(inputs, on="transaction_hash", suffixes=("_out", "_in"))
    transactions = transactions[transactions["recipient_in"] != transactions["recipient_out"]]
    return transactions
