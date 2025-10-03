from typing import Annotated, List, Union

from aiohttp import web
from aiohttp_pydantic import PydanticView
from aiohttp_pydantic.oas.typing import r200, r404
from pydantic import Field

from server.models import User, UserCreate

_DB: dict[int, User] = {}
_last_id: int = 0


class UserCollectionView(PydanticView):
    """/users"""
    async def post(self, user: UserCreate) -> r200[User]:  # type: ignore[misc]
        """Создать пользователя"""
        global _last_id
        _last_id += 1
        new_user = User(id=_last_id, name=user.name)
        _DB[new_user.id] = new_user
        return web.json_response(new_user.model_dump())

    async def get(self) -> r200[List[User]]:  # type: ignore[misc]
        """Список пользователей"""
        return web.json_response([u.model_dump() for u in _DB.values()])


class UserItemView(PydanticView):
    """/users/{user_id}"""
    async def get(
        self,
        user_id: Annotated[
            int,
            Field(
                ge=1,
                description="Идентификатор пользователя",
            ),
        ],
        /,
    ) -> Union[r200[User], r404]:  # type: ignore[misc]
        """Получить пользователя"""
        user = _DB.get(user_id)
        if not user:
            raise web.HTTPNotFound
        return web.json_response(user.model_dump())
