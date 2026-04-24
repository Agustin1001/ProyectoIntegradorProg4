from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class ProductoBase(BaseModel):
    nombre: str = Field(..., max_length=150)
    descripcion: Optional[str] = None
    precio_base: float = Field(gt=0)
    imagen_url: List[str] = Field(default=[])
    stock_cantidad: int = Field(default=0, ge=0)
    disponible: bool = True

class ProductoCreate(ProductoBase):
    categoria_ids: List[int] = []
    ingrediente_ids: List[int] = []

class ProductoUpdate(BaseModel):
    nombre: Optional[str] = Field(None, max_length=150)
    descripcion: Optional[str] = None
    precio_base: Optional[float] = Field(None, gt=0)
    stock_cantidad: Optional[int] = Field(None, ge=0)
    disponible: Optional[bool] = None
    categoria_ids: Optional[List[int]] = None
    ingrediente_ids: Optional[List[int]] = None

class ProductoRead(ProductoBase):
    id: int
    created_at: datetime
    updated_at: datetime
    class Config: from_attributes = True  # noqa: E701
