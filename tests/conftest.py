import contextlib
import os
import socket
import sys
from typing import AsyncIterator

import aiohttp
import pytest
import pytest_asyncio
from aiohttp import web

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..")),
)
from server.app import create_app  # noqa: E402


def _get_free_port() -> int:
    with contextlib.closing(
        socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ) as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


@pytest_asyncio.fixture
async def test_server() -> AsyncIterator[str]:
    app: web.Application = create_app()
    runner = web.AppRunner(app)
    await runner.setup()
    port = _get_free_port()
    site = web.TCPSite(runner, "127.0.0.1", port)
    await site.start()
    try:
        yield f"http://127.0.0.1:{port}"
    finally:
        await runner.cleanup()


@pytest_asyncio.fixture
async def http_client(test_server) -> AsyncIterator[aiohttp.ClientSession]:
    async with aiohttp.ClientSession(base_url=test_server) as session:
        yield session


@pytest.fixture(autouse=True)
def reset_db():
    from server import routes as routes_module

    routes_module._DB.clear()
    routes_module._last_id = 0
    yield
