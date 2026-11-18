from fastapi import FastAPI
from api.login import  auth_router, signup_router
from api import login
app = FastAPI()


app.include_router(auth_router)
app.include_router(signup_router)