from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends,HTTPException,status

from db.session import get_db
from db.models.jobs import Job
from db.models.users import User
from schemas.jobs import JobCreate,ShowJob
from db.repository.jobs import create_new_job,retrieve_job,list_jobs,update_job_by_id,delete_job_by_id
from schemas.jobs import ShowJob
from typing import List
from apis.version1.route_login import get_current_user_from_token
from db.models.users import User

router = APIRouter()


@router.post("/create-job/",response_model=ShowJob)
def create_job(job: JobCreate,db: Session = Depends(get_db),current_user:User = Depends(get_current_user_from_token)):
    current_user = current_user.id
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
def update_job(id:int,job:JobCreate,db:Session=Depends(get_db),current_user: User = Depends(get_current_user_from_token)):
    
    job_retrieved = retrieve_job(id =id,db=db)
    if not job_retrieved:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Job with id {id} doesn't exist")
    if job_retrieved.owner_id == current_user.id or current_user.is_superuser:
        update_job_by_id(id=id,job=job,db=db,owner_id=current_user.id)
        return {"detail":"Successfully updated data"}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f"You are not permitted!!!!")

@router.delete("/delete/{id}")
def delete_job(id: int,db: Session = Depends(get_db),current_user: User = Depends(get_current_user_from_token)):
    job = retrieve_job(id =id,db=db)
    if not job:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Job with {id} does not exist")
    print(job.owner_id,current_user.id,current_user.is_superuser)
    if job.owner_id == current_user.id or current_user.is_superuser:
        delete_job_by_id(id=id,db=db,owner_id=current_user.id)
        return {"msg":"Successfully deleted."}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f"You are not permitted!!!!")