from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime
from enum import Enum

# Definir los posibles estados del jugador
class EstadoJugador(str, Enum):
    activo = "Activo"
    inactivo = "Inactivo"
    lesionado = "Lesionado"
    suspendido = "Suspendido"

# Modelo del jugador
class Jugador(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    edad: int
    numeroUnico: int = Field(ge=1, le=99)  # Limitar a 1-99
    fechaNacimiento: datetime
    nacionalidad: str
    altura: float
    peso: float
    pieDominante: str
    posicion: str  # Cambiar si usas un enum o clase para posición
    estado: EstadoJugador = EstadoJugador.activo
    estadisticas: Optional[str] = None  # Aquí puedes poner estadísticas adicionales si es necesario.
    partidos: List["Partido"] = Relationship(back_populates="jugador")


class estadisticas(SQLModel, table=True):
    goles: int
    promedio_gol:int
    asistencias: int
    partidos_jugados: int
    tarjetas_amarillas: int
    suspensiones: int
    vallas_invictas: int

