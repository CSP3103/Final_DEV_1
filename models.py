from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime
from enum import Enum

class EstadoJugador(str, Enum):
    activo = "Activo"
    inactivo = "Inactivo"
    lesionado = "Lesionado"
    suspendido = "Suspendido"


class Jugador(SQLModel, ):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    edad: int
    numeroUnico: int = Field(ge=1, le=99)  # Limitar a 1-99
    fechaNacimiento: datetime
    nacionalidad: str
    altura: float
    peso: float
    pieDominante: str
    posicion: str
    estado: bool | None = Field(description="Estados jugador", default=True)
    #estadisticas: Optional[str] = None
    #partidos: List["Partido"] = Relationship(back_populates="jugador")


class estadisticas(SQLModel, ):
    id: Optional[int] = Field(default=None, primary_key=True)
    goles: int
    promedio_gol:int
    asistencias: int
    partidos_jugados: int
    tarjetas_amarillas: int
    suspensiones: int
    vallas_invictas: int

class Partido (SQLModel, ):
    id: Optional[int] = Field(default=None, primary_key=True)
    local: str
    visitante: str
    goles: str
    victoria: bool

class Historial(SQLModel, ):
    idHistorial: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    edad: int
    numeroUnico: int
    fechaNacimiento: datetime
    nacionalidad: str
    altura: float
    peso: float
    pieDominante: str
    posicion: str
    estado: str