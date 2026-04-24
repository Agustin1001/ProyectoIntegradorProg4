from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Importamos los routers
from app.modules.producto.router import router as producto_router
from app.modules.categoria.router import router as categoria_router
from app.modules.ingrediente.router import router as ingrediente_router

# Importamos la configuración de DB
from app.core.database import create_db_and_tables

# Importamos los modelos (Esencial para que create_db_and_tables detecte todo)
from app.modules.categoria.models import Categoria  # noqa: F401
from app.modules.ingrediente.models import Ingrediente  # noqa: F401
from app.modules.producto.models import Producto, ProductoCategoriaLink, ProductoIngredienteLink  # noqa: F401

def create_app() -> FastAPI:
    app = FastAPI(
        title="Parcial 1 - API Integradora",
        description="Backend FastAPI con UoW, Repository y Relaciones Complejas",
        version="1.0.0"
    )
    
    # CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=['http://localhost:5173'], 
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    # Registramos las rutas
    app.include_router(producto_router)
    app.include_router(categoria_router)
    app.include_router(ingrediente_router)
    
    return app

app = create_app()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()