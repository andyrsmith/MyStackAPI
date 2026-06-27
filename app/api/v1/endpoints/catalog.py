from fastapi import APIRouter, Depends
from typing import List

from app.dependencies import get_session
from app.db.session import CSVSession
from app.schemas.resource import Catalog, RandomPickResponse
from app.crud import catalog as crud

router = APIRouter()


@router.get(
    "/",
    response_model=List[Catalog],
    summary="List all items in the catalog",
    description="Returns every item from the data store.",
)
def list_resources(session: CSVSession = Depends(get_session)):
    return crud.get_all_items(session)


@router.get(
    "/random",
    response_model=List[RandomPickResponse],
    summary="Random pick per category",
    description="Returns one randomly selected resource for each category.",
)
def random_by_category(session: CSVSession = Depends(get_session)):
    return crud.get_random_by_category(session)
