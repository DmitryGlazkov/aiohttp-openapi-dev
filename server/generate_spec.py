import asyncio
import pathlib

import aiohttp
import aiohttp.web
import yaml

from server.app import create_app


async def main():
    app = create_app()
    runner = aiohttp.web.AppRunner(app)
    await runner.setup()
    site = aiohttp.web.TCPSite(runner, "127.0.0.1", 8080)
    await site.start()

    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(
                "http://127.0.0.1:8080/oas/spec",
                headers={"Host": "127.0.0.1"},
            ) as resp:
                resp.raise_for_status()
                spec = await resp.json()
        except Exception as e:
            print(f"Ошибка при получении спецификации: {e}")
            await runner.cleanup()
            return

    await runner.cleanup()

    pathlib.Path("openapi.yaml").write_text(
        yaml.dump(spec, sort_keys=False, allow_unicode=True),
        encoding="utf-8",
    )
    print("openapi.yaml сохранён в корень проекта")

if __name__ == "__main__":
    asyncio.run(main())
