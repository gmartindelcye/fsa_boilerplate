from uuid import UUID

from fastapi import HTTPException
from fastapi import status as http_status
from sqlalchemy import delete, select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.roles.models import (
    Role, 
    RoleCreate, 
    RolePatch, 
    Permission, 
    PermissionCreate, 
    PermissionPatch
)

class RolesCRUD:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, data: RoleCreate) -> Role:
        values = data.dict()

        role = Role(**values)
        self.session.add(role)
        await self.session.commit()
        await self.session.refresh(role)

        return role

    async def get(self, role_id: str | UUID) -> Role:
        statement = select(
            Role
        ).where(
            Role.uuid == role_id
        )
        results = await self.session.execute(statement=statement)
        role = results.scalar_one_or_none()  # type: Role | None

        if role is None:
            raise HTTPException(
                status_code=http_status.HTTP_404_NOT_FOUND,
                detail="The role hasn't been found!"
            )

        return role

    async def patch(self, role_id: str | UUID, data: RolePatch) -> Role:
        role = await self.get(role_id=role_id)
        values = data.dict(exclude_unset=True)

        for k, v in values.items():
            setattr(role, k, v)

        self.session.add(role)
        await self.session.commit()
        await self.session.refresh(role)

        return role

    async def delete(self, role_id: str | UUID) -> bool:
        statement = delete(
            Role
        ).where(
            Role.uuid == role_id
        )

        await self.session.execute(statement=statement)
        await self.session.commit()

        return True


    async def get_all(self) -> list[Role]:
        statement = select(Role)
        results = await self.session.execute(statement=statement)
        roles = results.scalars().all()

        return roles


class PermissionsCRUD:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, data: PermissionCreate) -> Permission:
        values = data.dict()

        permission = Permission(**values)
        self.session.add(permission)
        await self.session.commit()
        await self.session.refresh(permission)

        return permission

    async def get(self, permission_id: str | UUID) -> Permission:
        statement = select(
            Permission
        ).where(
            Permission.uuid == permission_id
        )
        results = await self.session.execute(statement=statement)
        permission = results.scalar_one_or_none()  # type: Permission | None

        if permission is None:
            raise HTTPException(
                status_code=http_status.HTTP_404_NOT_FOUND,
                detail="The permission hasn't been found!"
            )

        return role

    async def patch(self, permission_id: str | UUID, data: PermissionPatch) -> Permission:
        permission = await self.get(role_id=role_id)
        values = data.dict(exclude_unset=True)

        for k, v in values.items():
            setattr(role, k, v)

        self.session.add(permission)
        await self.session.commit()
        await self.session.refresh(rpermission)

        return permission

    async def delete(self, permission_id: str | UUID) -> bool:
        statement = delete(
            Permission
        ).where(
            Permission.uuid == permission_id
        )

        await self.session.execute(statement=statement)
        await self.session.commit()

        return True


    async def get_all(self) -> list[Permission]:
        statement = select(Permission)
        results = await self.session.execute(statement=statement)
        permission = results.scalars().all()

        return permission
