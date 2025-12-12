# app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.battles import router as battles_router

app = FastAPI(
    title="Language Battle API",
    version="1.0.0",
)

# CORS: ajusta origins cuando sepas la URL del frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],            # en producción mejor poner la URL concreta del frontend    
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health", tags=["health"])
def health_check():
    return {"status": "ok"}


# Registrar rutas de la API v1
app.include_router(battles_router)
