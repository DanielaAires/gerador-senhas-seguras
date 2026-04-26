# Gerador de Senhas Seguras

Este é um mini projeto desenvolvido em Python com o objetivo de gerar senhas seguras de forma simples e prática.

O projeto foi criado como parte de um estudo inicial de desenvolvimento, versionamento com GitHub, testes automatizados e boas práticas de documentação.

## Objetivo do projeto

Gerar senhas aleatórias e seguras, garantindo que cada senha tenha pelo menos:

- 1 letra maiúscula
- 1 letra minúscula
- 1 número
- 1 símbolo

## Tecnologias utilizadas

- Python
- VS Code
- GitHub
- Pytest

## Como funciona

O programa solicita ao usuário o tamanho desejado para a senha.

Caso o tamanho informado seja menor que o mínimo permitido, o sistema exibe uma mensagem de validação.

O usuário também pode digitar `sair` para encerrar o programa.

## Regras de validação

- O tamanho mínimo da senha é 8 caracteres.
- O usuário deve informar apenas números inteiros.
- A opção `sair` encerra a aplicação.
- A senha gerada sempre contém letras maiúsculas, letras minúsculas, números e símbolos.
- Caso a função de geração receba um tamanho menor que 4, o sistema gera um erro, pois não seria possível garantir todos os tipos de caracteres obrigatórios.

## Estrutura do projeto

```text
gerador-senhas-seguras/
│
├── main.py
├── test_main.py
└── README.md
````

## Como executar o projeto

1. Abra o projeto no VS Code.

2. Abra o terminal.

3. Execute o comando:

```bash
python main.py
```

4. Informe o tamanho desejado para a senha.

Exemplo:

```text
Digite o tamanho da senha desejada (mínimo 8) ou 'sair' para encerrar: 12
```

O sistema irá gerar uma senha segura com o tamanho informado.

## Como executar os testes

Para rodar os testes automatizados, execute no terminal:

```bash
pytest
```

Os testes validam se:

* A senha gerada possui o tamanho correto.
* A senha contém letra maiúscula.
* A senha contém letra minúscula.
* A senha contém número.
* A senha contém símbolo.
* O tamanho mínimo é validado corretamente.
* A função gera erro quando recebe tamanho menor que 4.
* Os testes foram comentados para facilitar manutenção e aprendizado futuro.

## Exemplo de uso

```text
=== Gerador de Senhas Seguras ===
Digite o tamanho da senha desejada (mínimo 8) ou 'sair' para encerrar: 12

Senha gerada com sucesso!
Senha: A7#kLm2@pQx!
```

> Observação: a senha gerada será diferente a cada execução.

## Aprendizados

Com este projeto, foram praticados conceitos como:

* Criação de funções em Python
* Uso de bibliotecas nativas
* Geração segura de senhas com `secrets`
* Validação de entrada do usuário
* Escrita de docstrings
* Testes automatizados com Pytest
* Organização de projeto no GitHub
* Documentação com README

## Autora

Daniela Santos