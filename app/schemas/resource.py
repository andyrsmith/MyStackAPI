from pydantic import BaseModel, HttpUrl
from typing import Optional


class ResourceBase(BaseModel):
    title: str
    type: str
    category: str
    notes: Optional[str] = None
    link: Optional[str] = None


class Resource(ResourceBase):
    class Config:
        from_attributes = True


class RandomPickResponse(BaseModel):
    category: str
    resource: Resource
