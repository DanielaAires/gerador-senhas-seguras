# Projeto: Gerador de Senhas Seguras
# Objetivo: gerar senhas fortes com letras maiúsculas, minúsculas, números e símbolos.
# Autora: Dani

import secrets
import string


def gerar_senha(tamanho):
    """
    Gera uma senha segura com o tamanho informado.

    A senha sempre terá pelo menos:
    - 1 letra maiúscula
    - 1 letra minúscula
    - 1 número
    - 1 símbolo

    Parâmetro:
        tamanho (int): quantidade de caracteres da senha.

    Retorno:
        str: senha gerada.
    """

    if tamanho < 4:
        raise ValueError("Tamanho mínimo para garantir os tipos de caracteres é 4.")

    # Define os grupos de caracteres que serão usados na senha
    maiusculas = string.ascii_uppercase
    minusculas = string.ascii_lowercase
    digitos = string.digits
    simbolos = string.punctuation

    # Garante que a senha tenha pelo menos um caractere de cada tipo
    senha_chars = [
        secrets.choice(maiusculas),
        secrets.choice(minusculas),
        secrets.choice(digitos),
        secrets.choice(simbolos),
    ]

    # Junta todos os caracteres possíveis
    todos = maiusculas + minusculas + digitos + simbolos

    # Completa o restante da senha até atingir o tamanho solicitado
    for _ in range(tamanho - 4):
        senha_chars.append(secrets.choice(todos))

    # Embaralha os caracteres para não deixar a ordem previsível
    secrets.SystemRandom().shuffle(senha_chars)

    # Junta a lista de caracteres em uma única string
    return ''.join(senha_chars)


def validar_tamanho(tamanho, minimo=8):
    """
    Valida se o tamanho informado atende ao tamanho mínimo definido.

    Parâmetros:
        tamanho (int): tamanho escolhido pelo usuário.
        minimo (int): tamanho mínimo permitido.

    Retorno:
        bool: True se o tamanho for válido, False caso contrário.
    """

    return tamanho >= minimo


def solicitar_tamanho(minimo=8):
    """
    Solicita ao usuário o tamanho da senha.

    A função continua perguntando até o usuário informar:
    - um número válido
    - ou a palavra 'sair'

    Parâmetro:
        minimo (int): tamanho mínimo permitido para a senha.

    Retorno:
        int: tamanho escolhido pelo usuário.
        None: caso o usuário escolha sair.
    """

    while True:
        entrada = input(
            f"Digite o tamanho da senha desejada (mínimo {minimo}) ou 'sair' para encerrar: "
        ).strip()

        # Permite encerrar o programa
        if entrada.lower() == 'sair':
            return None

        # Valida se o usuário digitou um número inteiro
        if not entrada.isdigit():
            print("Por favor, digite um número inteiro ou 'sair'.")
            continue

        tamanho = int(entrada)

        # Valida se o tamanho atende ao mínimo definido
        if not validar_tamanho(tamanho, minimo):
            print(f"A senha deve ter pelo menos {minimo} caracteres.")
            continue

        return tamanho


if __name__ == "__main__":
    print("=== Gerador de Senhas Seguras ===")

    # Mantém o programa rodando até o usuário digitar 'sair'
    while True:
        tamanho = solicitar_tamanho(minimo=8)

        if tamanho is None:
            print("Encerrando. Até logo!")
            break

        senha = gerar_senha(tamanho)

        print("\nSenha gerada com sucesso!")
        print("Senha:", senha)
        print()