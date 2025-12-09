# app/core/db.py

import psycopg
from psycopg.rows import dict_row

from app.core.config import settings


def get_connection():
    """
    Devuelve una nueva conexión a la base de datos.

    Uso típico:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT 1")
    """
    return psycopg.connect(
        str(settings.database_url),
        row_factory=dict_row,  # para que cur.fetchall() devuelva dicts
    )


def ping_db() -> bool:
    """
    Comprueba si la conexión a la base de datos funciona.
    Útil para tests o endpoints de healthcheck.
    """
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT 1")
                _ = cur.fetchone()
        return True
    except Exception:
        return False
