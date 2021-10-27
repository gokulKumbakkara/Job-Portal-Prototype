from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm.session import Session
from db.repository.jobs import list_jobs,retrieve_job
from db.session import get_db
from fastapi import Depends


templates=Jinja2Templates(directory="templates")
router=APIRouter(include_in_schema=False)

@router.get("/")
def home(request:Request,db:Session = Depends(get_db),msg:str=None):
    jobs=list_jobs(db=db)
    return templates.TemplateResponse("jobs/homepage.html",{"request":request,"jobs":jobs,"msg":msg})

@router.get("/details/{id}")
def home(id:int,request:Request,db:Session = Depends(get_db)):
    job=retrieve_job(id=id,db=db)
    return templates.TemplateResponse("jobs/details.html",{"request":request,"jobs":job})