import importlib
import os
import sys

import pytest


def _generated_client_available():
    return os.path.isdir("client_generated") and os.path.isfile(
        os.path.join("client_generated", "setup.py")
    )


@pytest.mark.skipif(
    not _generated_client_available(),
    reason="generated client not present",
)
@pytest.mark.asyncio
async def test_generated_async_client_end_to_end(test_server):
    sys.path.insert(0, os.path.abspath("client_generated"))
    try:
        users_client = importlib.import_module("users_client")
        default_api_module = importlib.import_module(
            "users_client.api.default_api"
        )
        models_user_create = importlib.import_module(
            "users_client.models.user_create"
        )

        Configuration = getattr(users_client, "Configuration")
        ApiClient = getattr(users_client, "ApiClient")
        DefaultApi = getattr(default_api_module, "DefaultApi")
        UserCreate = getattr(models_user_create, "UserCreate")

        cfg = Configuration(host=test_server)
        async with ApiClient(cfg) as api_client:
            api = DefaultApi(api_client)

            created = await api.users_post(UserCreate(name="Ivan"))
            assert created.id == 1 and created.name == "Ivan"

            users = await api.users_get()
            assert len(users) == 1 and users[0].name == "Ivan"

            user = await api.users_user_id_get(1)
            assert user.id == 1 and user.name == "Ivan"
    finally:
        if sys.path and sys.path[0] == os.path.abspath("client_generated"):
            sys.path.pop(0)
