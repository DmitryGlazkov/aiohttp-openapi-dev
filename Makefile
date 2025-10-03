.PHONY: install server spec client test clean

install:
	pip install -r requirements.txt

server:
	python -m server.app

spec:
	python -m server.generate_spec

client: spec
	openapi-generator-cli generate -i openapi.yaml -g python -o client_generated --package-name users_client --library asyncio
test:
	pytest -q

clean:
	rm -rf client_generated