import pathlib

from aiohttp import web
from aiohttp_pydantic.oas.view import generate_oas

from server.routes import UserCollectionView, UserItemView


async def oas_spec(request: web.Request) -> web.Response:
    spec = generate_oas(
        [request.app],
        version_spec="1.0.0",
        title_spec="Users API",
    )
    return web.json_response(spec)


def create_app() -> web.Application:
    app = web.Application()
    app.router.add_view("/users", UserCollectionView)
    app.router.add_view("/users/{user_id}", UserItemView)
    app.router.add_get("/oas/spec", oas_spec)

    async def swagger_ui(_: web.Request) -> web.Response:
        html_path = (
            pathlib.Path(__file__).parent / "templates" / "swagger.html"
        )
        html = html_path.read_text(encoding="utf-8")
        return web.Response(text=html, content_type="text/html")

    app.router.add_get("/docs", swagger_ui)
    return app


if __name__ == "__main__":
    web.run_app(create_app(), host="0.0.0.0", port=8080)
