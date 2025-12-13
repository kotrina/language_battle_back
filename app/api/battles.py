# app/api/battles.py

from fastapi import APIRouter, HTTPException

from app.models.battle import BattleCreate, BattleOut
from app.services.battles import save_battle, get_battle_by_id

router = APIRouter(
    prefix="/api/battles",  # <-- aquí decides el prefijo base
    tags=["battles"],
)


@router.post("/", response_model=BattleOut)
@router.post("", response_model=BattleOut)
def create_or_update_battle(battle: BattleCreate) -> BattleOut:
    """
    Crea o actualiza una batalla.

    - Si el id no existe, la crea.
    - Si el id ya existe, actualiza la configuración.
    """
    save_battle(battle)

    db_battle = get_battle_by_id(battle.id)
    if db_battle is None:
        # Esto no debería pasar salvo error interno
        raise HTTPException(status_code=500, detail="Battle could not be retrieved after save")

    return BattleOut(**db_battle.model_dump())


@router.get("/{battle_id}", response_model=BattleOut)
def get_battle(battle_id: str) -> BattleOut:
    """
    Devuelve una batalla por su id.
    """
    db_battle = get_battle_by_id(battle_id)

    if db_battle is None:
        raise HTTPException(status_code=404, detail="Battle not found")

    return BattleOut(**db_battle.model_dump())
