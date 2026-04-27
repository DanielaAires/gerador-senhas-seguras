.PHONY: install run test help

install:
	pip install -r requirements.txt

run:
	python main.py

test:
	pytest -v

help:
	@echo "Comandos disponíveis:"
	@echo "  make install  - Instala as dependências"
	@echo "  make run      - Executa o projeto"
	@echo "  make test     - Executa os testes"
	@echo "  make help     - Mostra os comandos disponíveis"