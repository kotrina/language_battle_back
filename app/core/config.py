# app/core/config.py

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import AnyUrl


class Settings(BaseSettings):
    # Configuración de pydantic-settings v2
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )

    # URL completa de conexión a Postgres (Neon / Vercel Postgres)
    database_url: AnyUrl

    # Entorno actual: local, production, etc.
    env: str = "local"


settings = Settings()
