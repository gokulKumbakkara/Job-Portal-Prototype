from fastapi import FastAPI
from core.config import settingobject
from db.session import engine
from db.base_class import Base

def create_tables():
    Base.metadata.create_all(bind=engine) # connects fastapi with the database engine
def start_application():
    app=FastAPI(title=settingobject.PROJECT_TITLE,version=settingobject.PROJECT_VERSION)
    create_tables() 
    return app

app = start_application()

@app.get("/")
def hello_api():
    return {"hello world"}