from sqlmodel import SQLModel, create_engine, Session

# Base de datos SQLite
DATABASE_URL = "sqlite:///database.db"

engine = create_engine(DATABASE_URL, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


## antes de crear el database.py, en la terminal se tuvo que haber instalado el sqlmodel (pip install sqlmodel fastapi uvicorn)