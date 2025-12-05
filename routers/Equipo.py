from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from database import get_session
from models import Jugador, Estadisticageneral
from crud import create, get_all, update, delete, get_by_id


router = APIRouter(prefix="/equipo", tags=["Equipo"])

@router.post("/")
def crear_jugador (jugador: Jugador, session: Session = Depends(get_session)):
    return create(session, Jugador, jugador)

@router.get("/")
def listar_Jugador(session: Session = Depends(get_session)):
    return get_all(session, Jugador)

@router.put("/{id}")
def actualizar_jugador(id: int, jugador: Jugador, session: Session = Depends(get_session)):
    return update(session, Jugador, id, jugador)

@router.delete("/{id}")
def desactivar_jugador(id: int, session: Session = Depends(get_session)):
    return delete(session, Jugador, id)

