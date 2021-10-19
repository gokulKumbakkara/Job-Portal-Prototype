from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends,HTTPException,status

from db.session import get_db
from db.models.jobs import Job
from schemas.jobs import JobCreate,ShowJob
from db.repository.jobs import create_new_job,retrieve_job,list_jobs,update_job_by_id,delete_job_by_id
from schemas.jobs import ShowJob
from typing import List

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

@router.get("/all",response_model=List[ShowJob])
def retrieve_all_jobs(db:Session = Depends(get_db)):
    jobs=list_jobs(db=db)  #passing the db
    return jobs

@router.put("/update/{id}")
def update_job(id:int,job:JobCreate,db:Session=Depends(get_db)):
    owner_id=1
    message=update_job_by_id(id=id,job=job,db=db,owner_id=owner_id)
    if not message:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Job with id {id} doesn't exist")
    return {"detail":"Successfully updated data"}

@router.delete("/delete/{id}")
def delete_job(id:int,db:Session=Depends(get_db)):
    owner_id=1
    message=delete_job_by_id(id=id,db=db,owner_id=owner_id)
    if not message:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Job with id {id} doesnt exist")
    return {"detail":"Successfully deleted data"}
