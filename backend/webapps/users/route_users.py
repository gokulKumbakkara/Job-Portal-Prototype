from fastapi import APIRouter
from fastapi.params import Depends
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi import responses
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.session import Session
from fastapi import status,HTTPException

from db.session import get_db
from webapps.users.forms import UserCreateForm
from schemas.users import Usercreate
from db.repository.users import create_new_user

router=APIRouter(include_in_schema=False)
templates=Jinja2Templates(directory="Templates")

@router.get("/register/")
def register(request:Request):
    return templates.TemplateResponse("users/register.html",{"request":request})

@router.post("/register/")
async def register(request:Request,db:Session=Depends(get_db)):
    form=UserCreateForm(request)
    await form.load_data()
    if await form.is_valid():
        user=Usercreate(username=form.username,email=form.email,password=form.password)
        try:
            user=create_new_user(user=user,db=db)
            return responses.RedirectResponse("/",status_code=status.HTTP_302_FOUND)
        except IntegrityError:
            form.__dict__.get("errors").append("Duplicate username or email")
            return templates.TemplateResponse("users/register.html",form.__dict__)
        
