from .unit_of_work import CategoriaUnitOfWork
from .schemas import CategoriaCreate, CategoriaUpdate
from .models import Categoria
from datetime import datetime, timezone

def crear(uow: CategoriaUnitOfWork, categoria_in: CategoriaCreate):
    with uow:
        db_categoria = Categoria(**categoria_in.model_dump())
        return uow.categorias.add(db_categoria)

def obtener_todos(uow: CategoriaUnitOfWork, skip: int = 0, limit: int = 50):
    with uow:
        return uow.categorias.get_all(skip, limit)

def obtener_por_id(uow: CategoriaUnitOfWork, id: int):
    with uow:
        return uow.categorias.get_by_id(id)

def actualizar(uow: CategoriaUnitOfWork, id: int, categoria_in: CategoriaUpdate):
    with uow:
        db_categoria = uow.categorias.get_by_id(id)
        if not db_categoria:
            return None
        categoria_data = categoria_in.model_dump(exclude_unset=True)
        for key, value in categoria_data.items():
            setattr(db_categoria, key, value)
        db_categoria.updated_at = datetime.now(timezone.utc)
        return uow.categorias.add(db_categoria)

def eliminar(uow: CategoriaUnitOfWork, id: int):
    with uow:
        db_categoria = uow.categorias.get_by_id(id)
        if not db_categoria:
            return False
        uow.categorias.delete(db_categoria)
        return True