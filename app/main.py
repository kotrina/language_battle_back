# app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.battles import router as battles_router

app = FastAPI(
    title="Language Battle API",
    version="1.0.0",
)

ALLOWED_ORIGINS = [
    "https://language-battle.vercel.app",
    "https://e2ffb668-eac0-4bb4-b9b9-4e737c1fc9c2.lovableproject.com",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=False,   # pon True solo si vas a usar cookies/sesiones
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/health", tags=["health"])
def health_check():
    return {"status": "ok"}


# Registrar rutas de la API v1
app.include_router(battles_router)
