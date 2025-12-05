from fastapi import FastAPI
from database import init_db
from jugador import router as jugador_router


app = FastAPI(title="sigmotoa FC")
app.include_router(jugador_router)


@app.on_event("startup")
def startup():
    init_db()


@app.get("/")
def home():
    return {"message": "sigmotoa"}



