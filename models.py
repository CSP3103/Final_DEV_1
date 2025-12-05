from pydantic import BaseModel
from utils.positions import Position
from utils.states import States
from typing import Optional


# ---------------------------
# MODELO JUGADOR
# ---------------------------
class Jugador(BaseModel):
    id: int
    nombre: str
    edad: int
    posicion: Position
    estado: States


# ---------------------------
# MODELO ESTADISTICA
# ---------------------------
class Estadistica(BaseModel):
    id: int
    jugador_id: int
    goles: int = 0
    asistencias: int = 0
    partidos_jugados: int = 0


# ---------------------------
# MODELO PARTIDO
# ---------------------------
class Partido(BaseModel):
    id: int
    equipo_local: str
    equipo_visitante: str
    marcador_local: int = 0
    marcador_visitante: int = 0
    fecha: str

