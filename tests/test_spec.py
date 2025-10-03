import pytest


@pytest.mark.asyncio
async def test_oas_spec_contains_info_and_paths(http_client):
    resp = await http_client.get("/oas/spec")
    assert resp.status == 200
    spec = await resp.json()

    assert spec.get("openapi", "").startswith("3.")

    info = spec.get("info") or {}
    assert info.get("title") == "Users API"
    assert info.get("version") == "1.0.0"

    paths = spec.get("paths") or {}
    assert "/users" in paths
    assert "/users/{user_id}" in paths
