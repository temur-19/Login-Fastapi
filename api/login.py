from sqlalchemy import select
from sqlalchemy.sql.functions import user
from routers.routers import  auth_router
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from schemas.schemas import LoginSchema
from models.models import User
from security.security import hash_password, create_access_token, verify_password
from db.db import get_db




async def authenticate_user(username: str, password: str, db:AsyncSession = Depends(get_db)):
    stmt = select(User).where(User.username == username)
    person = await db.execute(stmt)
    res = person.scalar_one_or_none()
    if not res:
        return None
    if not verify_password(password, res.password):
        return None
    return res


@auth_router.post('/login')
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db)):
    stmt = await authenticate_user(form_data.username, form_data.password, db)
    if not stmt:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = create_access_token({"sub": stmt.username})
    return {"access_token": access_token, "token_type": "bearer"}

