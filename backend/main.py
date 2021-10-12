from fastapi import FastAPI
from core.config import settingobject
from db.session import engine
from db.base import Base
from apis.base import api_router

def create_tables():
    Base.metadata.create_all(bind=engine) # connects fastapi with the database engine

def include_router(app):
    app.include_router(api_router)

def start_application():
    app=FastAPI(title=settingobject.PROJECT_TITLE,version=settingobject.PROJECT_VERSION)
    create_tables() 
    include_router(app)
    return app

app = start_application()

@app.get("/")
def hello_api():
    return {"hello world"}