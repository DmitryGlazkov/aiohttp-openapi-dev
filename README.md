# aiohttp-openapi-dev

Мини-проект на aiohttp, включающий в себя:
- реализацию сервера на aiohttp;
- генерацию контрактов OpenAPI;
- генерацию клиента из контрактов;
- тесты.

## Стек
- python
- aiohttp
- aiohttp-pydantic
- pydantic v2
- pytest + pytest-asyncio
- openapi-generator-cli

## Установка
```bash
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
```

## Запуск сервера
```bash
python -m server.app
```

## Эндпоинты
- `POST /users` — создать пользователя
- `GET /users` — список пользователей
- `GET /users/{user_id}` — получить пользователя по id

## OpenAPI спецификация и Swagger UI
- Swagger UI: `http://localhost:8080/docs`
- JSON спецификация на запущенном сервере: `GET http://localhost:8080/oas/spec`
- Генерация и сохранение `openapi.yaml` в корне проекта:
```bash
python -m server.generate_spec
```

## Генерация клиента из OpenAPI
```bash
openapi-generator-cli generate \
  -i openapi.yaml -g python \
  -o client_generated \
  --package-name users_client \
  --library asyncio
```


## Тесты
```bash
pytest -q
```


## Автор

[Дмитрий Глазков](https://github.com/DmitryGlazkov)