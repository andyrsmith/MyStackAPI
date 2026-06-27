from pydantic import BaseModel, HttpUrl
from typing import Optional


class CatalogBase(BaseModel):
    title: str
    type: str
    category: str
    notes: Optional[str] = None
    link: Optional[str] = None


class Catalog(CatalogBase):
    class Config:
        from_attributes = True


class RandomPickResponse(BaseModel):
    category: str
    catalog: Catalog
