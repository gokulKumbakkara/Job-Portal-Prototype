from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends,HTTPException,status

from db.session import get_db
from db.models.jobs import Job
from schemas.jobs import JobCreate,ShowJob
from db.repository.jobs import create_new_job,retrieve_job,list_jobs
from schemas.jobs import ShowJob

router = APIRouter()


@router.post("/create-job/",response_model=ShowJob)
def create_job(job: JobCreate,db: Session = Depends(get_db)):
    current_user = 1
    jobss = create_new_job(job=job,db=db,owner_id=current_user)
    return jobss

@router.get("/get/{id}",response_model=ShowJob)
def retrieve_job_by_id(id:int,db:Session = Depends(get_db)):
    jobss=retrieve_job(id=id,db=db)
    if not jobss:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Job with id {id} does not exist")
    return jobss

@router.get("/get/all")
def retrieve_all_jobs(db:Session=Depends(get_db)):
    jobss=list_jobs(db=db)  #passing the db
    return jobss