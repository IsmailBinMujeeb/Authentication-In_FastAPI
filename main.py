from fastapi import FastAPI
from api.v1 import user_api
from db.db_connect import engine
from models.user_model import Base

app = FastAPI(title="Authenticator")
Base.metadata.create_all(bind=engine)


app.include_router(user_api.router, prefix="/api/v1", tags=["v1", "user"])