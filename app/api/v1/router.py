from fastapi import APIRouter
from app.api.v1.endpoints import resources

router = APIRouter()

router.include_router(resources.router, prefix="/resources", tags=["resources"])
