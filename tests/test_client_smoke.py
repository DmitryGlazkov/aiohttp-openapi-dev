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
async def test_generated_client_import_and_basic_usage(http_client):
    sys.path.insert(0, os.path.abspath("client_generated"))
    try:
        pkg = importlib.import_module("users_client")
    finally:
        if sys.path[0] == os.path.abspath("client_generated"):
            sys.path.pop(0)

    assert hasattr(pkg, "__version__")

    resp = await http_client.get("/users")
    assert resp.status == 200
