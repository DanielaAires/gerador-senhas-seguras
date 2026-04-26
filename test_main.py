import string
import pytest

from main import gerar_senha, validar_tamanho


# Valida se a senha gerada possui exatamente o tamanho solicitado
def test_gerar_senha_com_tamanho_correto():
    senha = gerar_senha(12)

    assert len(senha) == 12


# Valida se a senha contém pelo menos uma letra maiúscula
def test_senha_contem_maiuscula():
    senha = gerar_senha(12)

    assert any(caractere in string.ascii_uppercase for caractere in senha)


# Valida se a senha contém pelo menos uma letra minúscula
def test_senha_contem_minuscula():
    senha = gerar_senha(12)

    assert any(caractere in string.ascii_lowercase for caractere in senha)


# Valida se a senha contém pelo menos um número
def test_senha_contem_numero():
    senha = gerar_senha(12)

    assert any(caractere in string.digits for caractere in senha)


# Valida se a senha contém pelo menos um símbolo
def test_senha_contem_simbolo():
    senha = gerar_senha(12)

    assert any(caractere in string.punctuation for caractere in senha)


# Valida se tamanhos iguais ou maiores que o mínimo são aceitos
def test_validar_tamanho_valido():
    assert validar_tamanho(8) is True
    assert validar_tamanho(12) is True


# Valida se tamanho menor que o mínimo é recusado
def test_validar_tamanho_invalido():
    assert validar_tamanho(7) is False


# Valida se a função gera erro quando o tamanho é menor que 4
# Isso acontece porque não seria possível garantir:
# 1 maiúscula, 1 minúscula, 1 número e 1 símbolo
def test_gerar_senha_menor_que_4_deve_gerar_erro():
    with pytest.raises(ValueError):
        gerar_senha(3)