from fastapi import FastAPI
from core.config import settingobject

app=FastAPI(title=settingobject.PROJECT_TITLE,version=settingobject.PROJECT_VERSION)

@app.get("/")
def hello_api():
    return {"hello world"}