# app/core/config.py

from pydantic_settings import BaseSettings
from pydantic import AnyUrl


class Settings(BaseSettings):
    # URL completa de conexión a Postgres (Neon / Vercel Postgres)
    database_url: AnyUrl

    # Entorno actual: local, production, etc.
    env: str = "local"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


# Instancia global que usarán el resto de módulos
settings = Settings()
