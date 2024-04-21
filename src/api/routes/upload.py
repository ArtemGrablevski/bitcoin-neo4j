from fastapi import APIRouter, Depends, File, UploadFile
from starlette import status

from api.dependencies.db import get_neo4j_sevice
from services.db import Neo4jService


router = APIRouter(
    tags=["Transactions"],
    prefix="/api/transactions"
)


@router.post("/upload", status_code=status.HTTP_201_CREATED)
def upload_csv(
    inputs_csv_file: UploadFile = File(...),
    outputs_csv_file: UploadFile = File(...),
    neo4j_sevice: Neo4jService = Depends(get_neo4j_sevice)
):
    # TODO: Use Kafka/RabbitMQ here
    neo4j_sevice.create_transaction_graph(
        inputs_csv_file=inputs_csv_file.file,
        outputs_csv_file=outputs_csv_file.file
    )
    return {"success": True}
