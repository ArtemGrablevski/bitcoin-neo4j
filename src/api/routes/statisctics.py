from fastapi import APIRouter, Depends
from starlette import status

from api.dependencies.db import get_neo4j_sevice
from services.db import Neo4jService


router = APIRouter(
    tags=["Statisctics"],
    prefix="/api/statisctics"
)


@router.get("/{address}", status_code=status.HTTP_200_OK)
def get_address_statistics(
    address: str,
    neo4j_sevice: Neo4jService = Depends(get_neo4j_sevice)
):
    return neo4j_sevice.get_address_info(
        address=address
    )
