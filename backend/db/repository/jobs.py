from sqlalchemy.orm import Session

from schemas.jobs import JobCreate
from db.models.jobs import Job

def create_new_job(job: JobCreate,db: Session,owner_id:int):
    job_object = Job(**job.dict(),owner_id=owner_id)
    db.add(job_object)
    db.commit()
    db.refresh(job_object)
    return job_object

def retrieve_job(id:int,db:Session):
    print("first line works")
    job=db.query(Job).filter(Job.id==id).first()
    return job
#Job is the table
def list_jobs(db:Session):
    
    jobs=db.query(Job)
    print(jobs).filter(Job.is_active==True)
    return jobs