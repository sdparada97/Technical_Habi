NAME := Technical_Habi

.PHONY: build run stop clean

build:
	docker build -t habi-test .

run:
	docker run -p 5000:5000 habi-test

stop:
	docker stop habi-test

clean:
	docker rm habi-test

test:
	docker run --rm habi-test python -m pytest tests

help:
	@echo "Makefile para $(NAME)"
	@echo "Comandos:"
	@echo "  make build       - Construir a imagem Docker"
	@echo "  make run         - Executar o container"
	@echo "  make stop        - Parar o container"
	@echo "  make clean       - Remover o container"
	@echo "  make help        - Mostrar esta mensagem de ajuda"
