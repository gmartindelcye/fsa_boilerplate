from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.roles.crud import RolesCRUD, PermissionsCRUD


async def get_heroes_crud(
        session: AsyncSession = Depends(get_async_session)
) -> RolesCRUD:
    return RolesCRUD(session=session)

async def get_permissions_crud(
        session: AsyncSession = Depends(get_async_session)
) -> PermissionsCRUD:
    return PermissionsCRUD(session=session)

