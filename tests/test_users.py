import pytest


@pytest.mark.asyncio
async def test_create_user(http_client):
    resp = await http_client.post("/users", json={"name": "Ivan"})
    assert resp.status == 200
    data = await resp.json()
    assert data["id"] == 1
    assert data["name"] == "Ivan"


@pytest.mark.asyncio
async def test_list_users_after_create(http_client):
    await http_client.post("/users", json={"name": "Ivan"})
    await http_client.post("/users", json={"name": "Masha"})

    resp = await http_client.get("/users")
    assert resp.status == 200
    data = await resp.json()
    names = [u["name"] for u in data]
    assert names == ["Ivan", "Masha"]


@pytest.mark.asyncio
async def test_get_user_by_id(http_client):
    await http_client.post("/users", json={"name": "Ivan"})

    resp = await http_client.get("/users/1")
    assert resp.status == 200
    data = await resp.json()
    assert data["id"] == 1
    assert data["name"] == "Ivan"


@pytest.mark.asyncio
async def test_get_user_not_found(http_client):
    resp = await http_client.get("/users/999")
    assert resp.status == 404
