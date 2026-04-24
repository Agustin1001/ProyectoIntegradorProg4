from typing import TYPE_CHECKING, List, Optional
from sqlmodel import Field, Relationship, SQLModel
from datetime import datetime, timezone

# Importamos el Link desde producto para que no haya ciclo
from app.modules.producto.models import ProductoCategoriaLink

if TYPE_CHECKING:
    from app.modules.producto.models import Producto

class Categoria(SQLModel, table=True):
    __tablename__ = "categorias" # type: ignore

    id: Optional[int] = Field(default=None, primary_key=True)
    parent_id: Optional[int] = Field(default=None, foreign_key="categorias.id")
    nombre: str = Field(index=True, max_length=100)
    descripcion: Optional[str] = Field(default=None)
    imagen_url: Optional[str] = Field(default=None)

    # --- Auditoría ---
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    deleted_at: Optional[datetime] = Field(default=None)

    # ── Relación N:M via ProductoCategoriaLink ────────────────────────────
    productos: List["Producto"] = Relationship(
        back_populates="categorias",
        link_model=ProductoCategoriaLink,
    )
    
    # ── Auto-referencia para subcategorías ────────────────────────────────
    subcategorias: List["Categoria"] = Relationship(
        sa_relationship_kwargs={"remote_side": "Categoria.id"}
    )