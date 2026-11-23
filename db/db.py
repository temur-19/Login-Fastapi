from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession
from sqlalchemy.orm import DeclarativeBase
from dotenv import load_dotenv
import os
load_dotenv()

ASYNC_DATABASE_URL = os.getenv("ASYNC_DATABASE_URL")
if not ASYNC_DATABASE_URL:
    raise ValueError("DATABASE URL topilmadi!")

engine = create_async_engine(ASYNC_DATABASE_URL, echo=True)
Session = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False, autoflush=False)

class Base(DeclarativeBase):
    pass

async def get_db():
    async with Session() as session:
        yield session

get_async_session = get_db