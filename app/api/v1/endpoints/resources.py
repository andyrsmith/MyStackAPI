from fastapi import APIRouter, Depends
from typing import List

from app.dependencies import get_session
from app.db.session import CSVSession
from app.schemas.resource import Resource, RandomPickResponse
from app.crud import resource as crud

router = APIRouter()


@router.get(
    "/",
    response_model=List[Resource],
    summary="List all resources",
    description="Returns every resource from the data store.",
)
def list_resources(session: CSVSession = Depends(get_session)):
    return crud.get_all_resources(session)


@router.get(
    "/random",
    response_model=List[RandomPickResponse],
    summary="Random pick per category",
    description="Returns one randomly selected resource for each category.",
)
def random_by_category(session: CSVSession = Depends(get_session)):
    return crud.get_random_by_category(session)
