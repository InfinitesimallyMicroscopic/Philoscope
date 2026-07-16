from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from dotenv import load_dotenv

import os
from pathlib import Path
load_dotenv()
BASE_DIR = Path(__file__).resolve().parent
#use env variable
SQLALCHEMY_DATABASE_URL = os.getenv('DATABASE_URL')

if SQLALCHEMY_DATABASE_URL is None:
    raise RuntimeError("DATABASE_URL is not set")
engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL,
)

AsyncSessionLocal = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


class Base(DeclarativeBase):
    pass




async def get_db():
    async with AsyncSessionLocal() as session:
        yield session