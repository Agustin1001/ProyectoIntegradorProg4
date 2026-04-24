# TP Integrador 4 - Backend FastAPI (Catálogo) 🚀

Este proyecto corresponde a la **Parte A** del Trabajo Práctico Integrador 4. Consiste en una evolución del backend desarrollado anteriormente, implementando un **Módulo de Catálogo de Productos** robusto con **FastAPI** y **SQLModel**, conectado a **MySQL**. 

[cite_start]Se ha optimizado la arquitectura para soportar auditoría temporal, respuestas estandarizadas y relaciones complejas entre productos, categorías e ingredientes[cite: 11, 13, 34].

## 🛠️ Tecnologías Utilizadas

* **Framework:** [FastAPI](https://fastapi.tiangolo.com/)
* **ORM:** [SQLModel](https://sqlmodel.tiangolo.com/)
* **Base de Datos:** MySQL
* **Validación:** Pydantic v2
* **Auditoría:** Manejo de zonas horarias con `datetime` y `timezone`

## ⚙️ Características Principales

* [cite_start]**CRUD Completo con Auditoría:** Gestión de `Categorías`, `Productos` e `Ingredientes` con registro automático de `created_at` y `updated_at`[cite: 32, 33, 118].
* **Borrado Lógico (Soft Delete):** Implementación de `deleted_at` para preservar la integridad de los datos y el historial de auditoría.
* **Relaciones N:M Avanzadas:** * `Producto` ↔ `Categoría` (con atributo `es_principal`).
    * `Producto` ↔ `Ingrediente` (con atributo `es_removible`).
* [cite_start]**Respuestas Estandarizadas:** Todos los endpoints devuelven un formato consistente con mensajes de éxito y datos encapsulados[cite: 37].
* [cite_start]**CORS Habilitado:** Configurado para la integración nativa con el frontend en React[cite: 36, 119].

## 🚀 Requisitos Previos

* Python 3.10 o superior.
* Servidor MySQL ejecutándose.
* Base de Datos: Se recomienda crear una base limpia (ej. `tp4_db`) para evitar conflictos con esquemas anteriores debido a los nuevos campos de auditoría.

## 🔧 Instalación y Configuración

1. **Entorno Virtual:**
   ```bash
   python -m venv .venv
   # Activar en Windows:
   .venv\Scripts\activate
2. Dependencias:

pip install -r requirements.txt

Base de Datos:
Actualiza la URL de conexión en app/db.py según tus credenciales de MySQL local.

▶️ Ejecución del Servidor
Levanta la API con el comando de desarrollo de FastAPI:

python -m fastapi dev main.py

La documentación interactiva estará disponible en: http://localhost:8000/docs

🧪 Pruebas de la API (REST Client)
Para cumplir con la entrega, se incluye el archivo catalogo.http. Este permite probar:

El CRUD completo de Categorías.

La creación de Productos con sus relaciones N:M.

El funcionamiento del borrado lógico y la persistencia de datos.

📂 Estructura Modular

TP4/
├── .venv/                    # Entorno virtual
├── app/
│   ├── __init__.py
│   ├── db.py                 # Engine y Session de MySQL
│   ├── main.py               # Configuración de CORS y Routers principales
│   └── modules/
│       ├── __init__.py
│       ├── categoria/        # Dominio de Categorías
│       ├── cliente/          # Dominio de Clientes
│       └── producto/         # Dominio de Productos e Ingredientes
│           ├── __init__.py
│           ├── models.py     # Entidades y Tablas Intermedias N:M
│           ├── routers.py    # Endpoints de la API
│           ├── schemas.py    # Validaciones Pydantic
│           └── services.py   # Lógica de negocio y Soft Delete
├── tests/
│   ├── catalogo.http         # Cliente de pruebas para la Parte A (TP4)
│   └── productos.http        # Cliente de pruebas (TP3)
├── README.md                 # Documentación
└── requirements.txt          # Dependencias del proyecto