from fastapi import FastAPI
from app.routes import router
from app.database import create_db_and_tables

app = FastAPI(title="Invoice API")

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(router)
