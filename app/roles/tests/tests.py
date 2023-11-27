import pytest
from httpx import AsyncClient
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.roles.models import Role, Permission


@pytest.mark.asyncio
async def test_create_role(
        async_client: AsyncClient,
        async_session: AsyncSession,
        test_data: dict
):
    payload = test_data["case_create"]["payload"]
    response = await async_client.post("/roles", json=payload,)

    assert response.status_code == 201

    got = response.json()
    want = test_data["case_create"]["want"]

    for k, v in want.items():
        assert got[k] == v

    statement = select(Role).where(Role.uuid == got["uuid"])
    results = await async_session.execute(statement=statement)
    role = results.scalar_one()

    for k, v in want.items():
        assert getattr(role, k) == v


@pytest.mark.asyncio
async def test_get_role(
        async_client: AsyncClient,
        async_session: AsyncSession,
        test_data: dict
):
    role_data = test_data["initial_data"]["role"]
    statement = insert(Role).values(role_data)
    await async_session.execute(statement=statement)
    await async_session.commit()

    response = await async_client.get(f"/roles/{role_data['uuid']}")
    assert response.status_code == 200

    got = response.json()
    want = test_data["case_get"]["want"]

    for k, v in want.items():
        assert got[k] == v


@pytest.mark.asyncio
async def test_patch_role(
        async_client: AsyncClient,
        async_session: AsyncSession,
        test_data: dict
):
    role_data = test_data["initial_data"]["role"]
    statement = insert(Role).values(role_data)
    await async_session.execute(statement=statement)
    await async_session.commit()

    payload = test_data["case_patch"]["payload"]
    response = await async_client.patch(
        f"/roles/{role_data['uuid']}",
        json=payload
    )
    assert response.status_code == 200

    got = response.json()
    want = test_data["case_patch"]["want"]

    for k, v in want.items():
        assert got[k] == v


@pytest.mark.asyncio
async def test_delete_role(
        async_client: AsyncClient,
        async_session: AsyncSession,
        test_data: dict
):
    role_data = test_data["initial_data"]["role"]
    statement = insert(Role).values(role_data)
    await async_session.execute(statement=statement)
    await async_session.commit()

    response = await async_client.delete(f"/roles/{role_data['uuid']}")
    assert response.status_code == 200

    got = response.json()
    want = test_data["case_delete"]["want"]

    for k, v in want.items():
        assert got[k] == v

    statement = select(
        Role
    ).where(
        Role.uuid == role_data["uuid"]
    )
    results = await async_session.execute(statement=statement)
    role = results.scalar_one_or_none()

    assert role is None


@pytest.mark.asyncio
async def test_create_permission(
        async_client: AsyncClient,
        async_session: AsyncSession,
        test_data: dict
):
    payload = test_data["case_create"]["payload"]
    response = await async_client.post("/roles", json=payload,)

    assert response.status_code == 201

    got = response.json()
    want = test_data["case_create"]["want"]

    for k, v in want.items():
        assert got[k] == v

    statement = select(Permission).where(Permission.uuid == got["uuid"])
    results = await async_session.execute(statement=statement)
    permission = results.scalar_one()

    for k, v in want.items():
        assert getattr(permission, k) == v


@pytest.mark.asyncio
async def test_get_permission(
        async_client: AsyncClient,
        async_session: AsyncSession,
        test_data: dict
):
    permission_data = test_data["initial_data"]["permission"]
    statement = insert(Permission).values(permission_data)
    await async_session.execute(statement=statement)
    await async_session.commit()

    response = await async_client.get(f"/roles/{permission_data['uuid']}")
    assert response.status_code == 200

    got = response.json()
    want = test_data["case_get"]["want"]

    for k, v in want.items():
        assert got[k] == v


@pytest.mark.asyncio
async def test_patch_permission(
        async_client: AsyncClient,
        async_session: AsyncSession,
        test_data: dict
):
    permission_data = test_data["initial_data"]["permission"]
    statement = insert(Permission).values(permission_data)
    await async_session.execute(statement=statement)
    await async_session.commit()

    payload = test_data["case_patch"]["payload"]
    response = await async_client.patch(
        f"/roles/{permission_data['uuid']}",
        json=payload
    )
    assert response.status_code == 200

    got = response.json()
    want = test_data["case_patch"]["want"]

    for k, v in want.items():
        assert got[k] == v


@pytest.mark.asyncio
async def test_delete_permission(
        async_client: AsyncClient,
        async_session: AsyncSession,
        test_data: dict
):
    permission_data = test_data["initial_data"]["permission"]
    statement = insert(Permission).values(permission_data)
    await async_session.execute(statement=statement)
    await async_session.commit()

    response = await async_client.delete(f"/roles/{permission_data['uuid']}")
    assert response.status_code == 200

    got = response.json()
    want = test_data["case_delete"]["want"]

    for k, v in want.items():
        assert got[k] == v

    statement = select(
        Permission
    ).where(
        Permission.uuid == permission_data["uuid"]
    )
    results = await async_session.execute(statement=statement)
    permission = results.scalar_one_or_none()

    assert permission is None
