from datetime import datetime, timezone
from typing import Optional
from .unit_of_work import ProductoUnitOfWork
from .schemas import ProductoCreate, ProductoUpdate
from .models import Producto

def crear(uow: ProductoUnitOfWork, producto_in: ProductoCreate):
    with uow:
        prod_data = producto_in.model_dump(exclude={"categoria_ids", "ingrediente_ids"})
        db_producto = Producto(**prod_data)
        
        if producto_in.categoria_ids:
            for c_id in producto_in.categoria_ids:
                cat = uow.categorias.get_by_id(c_id)
                if cat: db_producto.categorias.append(cat)  # noqa: E701
                
        if producto_in.ingrediente_ids:
            for i_id in producto_in.ingrediente_ids:
                ing = uow.ingredientes.get_by_id(i_id)
                if ing: db_producto.ingredientes.append(ing)  # noqa: E701

        return uow.productos.add(db_producto)

def obtener_todos(uow: ProductoUnitOfWork, skip: int, limit: int, nombre: Optional[str] = None):
    with uow:
        return uow.productos.get_all_active(skip, limit, nombre)

def obtener_por_id(uow: ProductoUnitOfWork, id: int):
    with uow:
        # Aquí podrías sumar el chequeo deleted_at == None
        return uow.productos.get_by_id(id)

def eliminar(uow: ProductoUnitOfWork, id: int):
    with uow:
        db_producto = uow.productos.get_by_id(id)
        if not db_producto or db_producto.deleted_at is not None:
            return False
        # Soft Delete (Baja lógica)
        db_producto.deleted_at = datetime.now(timezone.utc)
        uow.productos.add(db_producto)
        return True

def actualizar(uow: ProductoUnitOfWork, id: int, producto_in: ProductoUpdate):
    with uow:
        db_producto = uow.productos.get_by_id(id)
        if not db_producto or db_producto.deleted_at is not None:
            return None
        
        prod_data = producto_in.model_dump(exclude={"categoria_ids", "ingrediente_ids"}, exclude_unset=True)
        for key, value in prod_data.items():
            setattr(db_producto, key, value)
        
        # Actualizar relaciones si se enviaron (borramos las anteriores y agregamos las nuevas)
        if producto_in.categoria_ids is not None:
            db_producto.categorias.clear()
            for c_id in producto_in.categoria_ids:
                cat = uow.categorias.get_by_id(c_id)
                if cat: db_producto.categorias.append(cat)  # noqa: E701
                
        if producto_in.ingrediente_ids is not None:
            db_producto.ingredientes.clear()
            for i_id in producto_in.ingrediente_ids:
                ing = uow.ingredientes.get_by_id(i_id)
                if ing: db_producto.ingredientes.append(ing)  # noqa: E701

        db_producto.updated_at = datetime.now(timezone.utc)
        return uow.productos.add(db_producto)