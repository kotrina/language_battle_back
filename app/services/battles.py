# app/services/battles.py

from typing import Optional

from app.core.db import get_connection
from app.models.battle import BattleCreate, BattleDB
from psycopg.types.json import Jsonb


TABLE_NAME = "language_battle.battles"


def _row_to_battle_db(row: dict) -> BattleDB:
    """
    Convierte un dict devuelto por psycopg (dict_row) en un modelo BattleDB.
    """
    return BattleDB(
        id=row["id"],
        config=row["config"],
        created_at=row["created_at"],
    )


def save_battle(battle: BattleCreate) -> None:
    """
    Guarda una batalla en la base de datos.

    - Si el id ya existe, actualiza la configuración.
    - Si no existe, la crea.
    """
    query = f"""
        INSERT INTO {TABLE_NAME} (id, config)
        VALUES (%s, %s)
        ON CONFLICT (id) DO UPDATE
        SET config = EXCLUDED.config
    """
    print(query)
    print(battle.id, '---', battle.config)
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query, (battle.id, Jsonb(battle.config)))
        conn.commit()


def get_battle_by_id(battle_id: str) -> Optional[BattleDB]:
    """
    Devuelve una batalla por su id o None si no existe.
    """
    query = f"""
        SELECT id, config, created_at
        FROM {TABLE_NAME}
        WHERE id = %s
    """

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query, (battle_id,))
            row = cur.fetchone()

    if row is None:
        return None

    return _row_to_battle_db(row)
