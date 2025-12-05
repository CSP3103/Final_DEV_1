from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from database import get_session
from models import Jugador
from crud import create, get_all, update, delete, get_by_id


router = APIRouter(prefix="/jugador", tags=["Jugador"])

@router.post("/")
def crear_jugador(jugador: Jugador, session: Session = Depends(get_session)):
    return create(session, Jugador, jugador)

@router.get("/")
def listar_jugadores(session: Session = Depends(get_session)):
    return get_all(session, Jugador)

@router.get("/{id}")
def obtener_jugador(id: int, session: Session = Depends(get_session)):
    return get_by_id(session, Jugador, id)

@router.put("/{id}")
def actualizar_jugadores(id: int, jugador: Jugador, session: Session = Depends(get_session)):
    return update(session, Jugador, id, jugador)

@router.delete("/{id}")
def eliminar_jugador(id: int, session: Session = Depends(get_session)):
    return delete(session, Jugador, id)
