from sys import modules

from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel.ext.asyncio.session import AsyncSession

from app import settings

db_connection_str = settings.DB_ASYNC_CONNECTION_STR
if "pytest" in modules:
    db_connection_str = settings.DB_ASYNC_TEST_CONNECTION_STR


async_engine = create_async_engine(
    db_connection_str,
    echo=True,
    future=True
)


async def get_async_session() -> AsyncSession:
    async_session = sessionmaker(
        bind=async_engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        yield session
