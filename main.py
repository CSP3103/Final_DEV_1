from fastapi import FastAPI, HTTPException
from models import Jugador, Estadistica, Partido

app = FastAPI(title="sigmotoa FC")

# “Base de datos” temporal
jugadores_db = []
estadisticas_db = []
partidos_db = []


# ---------------------------
# HOME
# ---------------------------
@app.get("/")
async def root():
    return {"message": "sigmotoa FC data"}


# ---------------------------
# CRUD JUGADORES
# ---------------------------

@app.post("/jugadores/")
async def crear_jugador(jugador: Jugador):
    jugadores_db.append(jugador)
    return jugador


@app.get("/jugadores/")
async def obtener_jugadores():
    return jugadores_db


@app.get("/jugadores/{jugador_id}")
async def obtener_jugador(jugador_id: int):
    for j in jugadores_db:
        if j.id == jugador_id:
            return j
    raise HTTPException(status_code=404, detail="Jugador no encontrado")


@app.put("/jugadores/{jugador_id}")
async def actualizar_jugador(jugador_id: int, jugador: Jugador):
    for i, j in enumerate(jugadores_db):
        if j.id == jugador_id:
            jugadores_db[i] = jugador
            return jugador
    raise HTTPException(status_code=404, detail="Jugador no encontrado")


@app.delete("/jugadores/{jugador_id}")
async def eliminar_jugador(jugador_id: int):
    for j in jugadores_db:
        if j.id == jugador_id:
            jugadores_db.remove(j)
            return {"message": "Jugador eliminado"}
    raise HTTPException(status_code=404, detail="Jugador no encontrado")


# ---------------------------
# CRUD ESTADISTICAS
# ---------------------------

@app.post("/estadisticas/")
async def crear_estadistica(est: Estadistica):
    estadisticas_db.append(est)
    return est


@app.get("/estadisticas/")
async def obtener_estadisticas():
    return estadisticas_db


# ---------------------------
# CRUD PARTIDOS
# ---------------------------

@app.post("/partidos/")
async def crear_partido(partido: Partido):
    partidos_db.append(partido)
    return partido


@app.get("/partidos/")
async def obtener_partidos():
    return partidos_db

