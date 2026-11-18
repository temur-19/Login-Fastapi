from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import async_session, async_sessionmaker, create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

ASYNC_DATABASE_URL = create_engine('postgres://postgres:postgres@localhost:5432/postgres')

engine = create_async_engine(ASYNC_DATABASE_URL)
Session = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False, autoflush=False)

class Base(declarative_base()):
    pass

async def get_db():
    async with Session() as session:
        yield session
        await session.run_sync(Base.metadata.create_all)

get_async_session = get_db


