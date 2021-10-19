from fastapi import FastAPI
from fastapi.routing import APIRoute, APIRouter

from apis.version1 import route_users
from apis.version1 import route_jobs
from apis.version1 import route_login

api_router=APIRouter()

api_router.include_router(route_users.router,prefix="/user",tags=["users"])
api_router.include_router(route_jobs.router,prefix="/job",tags=["Jobs"])
api_router.include_router(route_login.router,prefix="/login",tags=["Login"])