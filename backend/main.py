from fastapi import FastAPI
from core.config import settingobject
from db.session import engine
from db.base import Base
from apis.base import api_router
from webapps.base import api_router as webapprouter  # two api_router may clash,hence renaming one 

def create_tables():
    Base.metadata.create_all(bind=engine) # connects fastapi with the database engine

def include_router(app):
    app.include_router(api_router)
    app.include_router(webapprouter)

def start_application():
    app=FastAPI(title=settingobject.PROJECT_TITLE,version=settingobject.PROJECT_VERSION)
    create_tables() 
    include_router(app)
    return app

app = start_application()

