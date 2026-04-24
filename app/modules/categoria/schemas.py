from pydantic import BaseModel, Field
from typing import Optional, Generic, TypeVar
from datetime import datetime

T = TypeVar("T")

class RespuestaEstandar(BaseModel, Generic[T]):
    message: str
    data: T

class CategoriaBase(BaseModel):
    nombre: str = Field(..., max_length=100)
    descripcion: Optional[str] = None
    imagen_url: Optional[str] = None

class CategoriaCreate(CategoriaBase):
    pass

class CategoriaUpdate(BaseModel):
    nombre: Optional[str] = Field(None, max_length=100)
    descripcion: Optional[str] = None
    imagen_url: Optional[str] = None

class CategoriaRead(CategoriaBase):
    id: int
    created_at: datetime
    updated_at: datetime
    class Config:
        from_attributes = True