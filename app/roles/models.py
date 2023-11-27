from typing import Optional, List

from sqlalchemy import Column
from sqlmodel import Field, SQLModel, Relationship

from app.core.models import MixinUUID
from app.roles.examples import (
    ex_role_create, 
    ex_role_patch, 
    ex_role_read,
    ex_permission_create,
    ex_permission_patch,
    ex_permission_read
)

prefix = "rol"


class RoleBase(SQLModel):
    name: str = Field(sa_column_kwargs={"unique": True}, index=True)
    description: str
    users: List["User"] = Relationship(back_populates="role", sa_relationship_kwargs={"lazy": "joined"})   
    permissions: List["Permission"] = Relationship(back_populates="role", sa_relationship_kwargs={"lazy": "joined"})
    

class Role(MixinUUID, RoleBase, table=True):
    __tablename__ = f"{prefix}_roles"


class RoleRead(MixinUUID, RoleBase):
    class Config:
        schema_extra = {"example": ex_role_read}
    

class RoleCreate(RoleBase):
    class Config:
        schema_extra = {"example": ex_role_create}


class RolePatch(RoleBase):
    name: Optional[str] = Field(sa_column_kwargs={"unique": True}, index=True)
    description: Optional[str]
    class Config:
        schema_extra = {"example": ex_role_patch}


class PermissionBase(SQLModel):
    name: str = Field(sa_column_kwargs={"unique": True}, index=True)
    description: str
    role_id: Optional[int] = Field(default=None, foreign_key="role.id")
    role: Optional["Role"] = Relationship(back_populates="permissions", sa_relationship_kwargs={"lazy": "joined"})


class Permission(MixinUUID, SQLModel, table=True):
        __tablename__ = f"{prefix}_permissions"


class PermissionRead(MixinUUID, PermissionBase):    
    class Config:
        schema_extra = {"example": ex_permission_read}


class PermissionCreate(PermissionBase):
    class Config:
        schema_extra = {"example": ex_permission_create}


class PermissionPatch(PermissionBase):
    name: Optional[str] = Field(sa_column_kwargs={"unique": True}, index=True)
    description: Optional[str]
    class Config:
        schema_extra = {"example": ex_permission_patch}