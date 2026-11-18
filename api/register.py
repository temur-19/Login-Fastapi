from argon2 import hash_password_raw
import security
from sqlalchemy import select
from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from pwdlib import PasswordHash


from models.models import User
from db.db import get_db
from routers.routers import signup_router
from schemas.schemas import RegisterSchema


@signup_router.post("/")
async def signup(user_in: RegisterSchema, db:AsyncSession = Depends(get_db)):
    stmt = select(User).where(User.username == user_in.username)
    result = await db.execute(stmt)
    user_exists = result.scalar_one_or_none()
    if user_exists:
        raise HTTPException(status_code=400, detail="Username already exists")
    else:
        user = User(username = user_in.user,
                    password = PasswordHash.recommended().hash(user_in.password))

    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user

