from fastapi import APIRouter, HTTPException, Path, Query, status, Depends
from sqlmodel import Session
from typing import List

from . import schemas, service
from .unit_of_work import CategoriaUnitOfWork
from app.core.database import get_session

router = APIRouter(prefix="/categorias", tags=["Categorías"])

def get_categoria_uow(session: Session = Depends(get_session)) -> CategoriaUnitOfWork:
    return CategoriaUnitOfWork(session)

@router.post("/", response_model=schemas.RespuestaEstandar[schemas.CategoriaRead], status_code=status.HTTP_201_CREATED)
def alta_categoria(categoria: schemas.CategoriaCreate, uow: CategoriaUnitOfWork = Depends(get_categoria_uow)):
    nuevo = service.crear(uow, categoria)
    return {"message": "Categoría creada", "data": nuevo}




@router.get("/", response_model=schemas.RespuestaEstandar[List[schemas.CategoriaRead]])
def listar_categorias(skip: int = Query(0, ge=0), limit: int = Query(50, le=100), uow: CategoriaUnitOfWork = Depends(get_categoria_uow)):
    categorias = service.obtener_todos(uow, skip, limit)
    return {"message": "Lista de categorías", "data": categorias}



@router.get("/{id}", response_model=schemas.RespuestaEstandar[schemas.CategoriaRead], status_code=status.HTTP_200_OK)
def detalle_categoria(id: int = Path(..., gt=0), uow: CategoriaUnitOfWork = Depends(get_categoria_uow)):
    categoria = service.obtener_por_id(uow, id)
    if not categoria:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Categoría no encontrada")
    return {"message": "Categoría encontrada", "data": categoria}


@router.put("/{id}", response_model=schemas.RespuestaEstandar[schemas.CategoriaRead], status_code=status.HTTP_200_OK)
def actualizar_categoria(categoria: schemas.CategoriaUpdate, id: int = Path(..., gt=0), uow: CategoriaUnitOfWork = Depends(get_categoria_uow)):
    actualizado = service.actualizar(uow, id, categoria)
    if not actualizado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Categoría no encontrada")
    return {"message": "Categoría actualizada con éxito", "data": actualizado}

@router.delete("/{id}", response_model=schemas.RespuestaEstandar[None], status_code=status.HTTP_200_OK)
def borrar_categoria(id: int = Path(..., gt=0), uow: CategoriaUnitOfWork = Depends(get_categoria_uow)):
    eliminado = service.eliminar(uow, id)
    if not eliminado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Categoría no encontrada")
    return {"message": "Categoría eliminada con éxito", "data": None}