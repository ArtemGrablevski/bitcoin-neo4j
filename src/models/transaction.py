from pydantic import BaseModel


class Transaction(BaseModel):
    address_from: str
    address_to: str
    value_usd: float
    timestamp: str
