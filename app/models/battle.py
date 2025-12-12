# app/models/battle.py

from datetime import datetime
from typing import Any, Dict, Optional
from pydantic import ConfigDict

from pydantic import BaseModel, Field


class BattleBase(BaseModel):
    """
    Campos comunes de una configuración de batalla.
    """

    config: Dict[str, Any] = Field(
        ...,
        description="JSON con la configuración de la batalla (lenguajes, rondas, reglas, etc.)",
    )


class BattleCreate(BattleBase):
    """
    Modelo para crear/guardar una batalla.

    - Si quieres permitir que el backend genere el ID, puedes hacer que 'id'
      sea opcional.
    - Si prefieres que el front mande siempre el ID, déjalo obligatorio.
    """

    id: str = Field(
        ...,
        description="Identificador único de la batalla (se usará en la URL para compartirla).",
        example="abc123xy",
    )


class BattleDB(BattleBase):
    """
    Representa una batalla tal y como se guarda en la base de datos.
    """

    id: str
    created_at: datetime


class BattleOut(BattleBase):
    """
    Modelo de salida para el endpoint que devuelve una batalla.
    """

    id: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
