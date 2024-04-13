import asyncio

from sqlalchemy.ext.asyncio import (
    async_sessionmaker,
    create_async_engine,
)

from app.models import Base

url = "postgresql+asyncpg://user:password@db:5432/db"

engine = create_async_engine(
    url,
    echo=True,
)


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async_session = async_sessionmaker(engine, expire_on_commit=False)


if __name__ == "__main__":
    asyncio.run(init_db())
