from fastapi import APIRouter
from app.api.v1.endpoints import catalog

router = APIRouter()

router.include_router(catalog.router, prefix="/catalog", tags=["catalog"])
