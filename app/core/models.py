import uuid as uuid_pkg
from datetime import datetime

from pydantic import BaseModel
from sqlalchemy import text
from sqlmodel import Field, SQLModel


class HealthCheck(BaseModel):
    name: str
    version: str
    description: str


class StatusMessage(BaseModel):
    status: bool
    message: str


class UUIDModel(SQLModel):
    uuid: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4,
        primary_key=True,
        index=True,
        nullable=False,
        sa_column_kwargs={
            "server_default": text("gen_random_uuid()"),
            "unique": True
        }
    )


class IdModel(SQLModel):
    id: int = Field(
        primary_key=True,
        index=True,
        nullable=False,
        sa_column_kwargs={
            "autoincrement": True,
            "unique": True
        }
    )

class TimestampModel(SQLModel):
    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        nullable=False,
        sa_column_kwargs={
            "server_default": text("current_timestamp(0)")
        }
    )

    updated_at: datetime = Field(
        default_factory=datetime.utcnow,
        nullable=False,
        sa_column_kwargs={
            "server_default": text("current_timestamp(0)"),
            "onupdate": text("current_timestamp(0)")
        }
    )


class Mixin(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: Optional[datetime] = Field(default=datetime.now())
    updated_at: Optional[datetime] = Field(default=datetime.now())


class MixinUUID(SQLModel):
    uuid: Optional[uuid_pkg.UUID] = Field(
        default_factory=uuid_pkg.uuid4,
        primary_key=True,
        nullable=False,
        sa_column_kwargs={
            "server_default": text("gen_random_uuid()"),
            "unique": True
        }
    )
    created_at: Optional[datetime] = Field(
        default=datetime.utcnow,
        nullable=False,
        sa_column_kwargs={
            "server_default": text("current_timestamp(0)")
        }
    )
    updated_at: Optional[datetime] = Field(
        default=datetime.utcnow,
        nullable=False,
        sa_column_kwargs={
            "server_default": text("current_timestamp(0)"),
            "onupdate": text("current_timestamp(0)")
        }
    )