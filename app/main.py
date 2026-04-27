from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
 
# Importamos los routers
from app.modules.producto.router import router as producto_router
from app.modules.categoria.router import router as categoria_router
from app.modules.ingrediente.router import router as ingrediente_router
 
# Importamos la configuración de DB
from app.core.database import create_db_and_tables
 
# Importamos los modelos (Esencial para que create_db_and_tables detecte todo)
from app.modules.categoria.models import Categoria
from app.modules.ingrediente.models import Ingrediente
from app.modules.producto.models import Producto, ProductoCategoriaLink, ProductoIngredienteLink
 
 
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Código que corre al iniciar la app
    create_db_and_tables()
    yield
    # Código que corre al apagar la app (cleanup, cerrar conexiones, etc.)
 
 
def create_app() -> FastAPI:
    app = FastAPI(
        title="Parcial 1 - API Integradora",
        description="Backend FastAPI con UoW, Repository y Relaciones Complejas",
        version="1.0.0",
        lifespan=lifespan,
    )
 
    # CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:5173"],
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
