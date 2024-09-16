import pytest
from ..models.pessoa import Pessoa
from meu_projeto.models.endereco import Endereco # Caminho relativo
from meu_projeto.models.enum.sexo import Sexo # Caminho Absoluto
from meu_projeto.models.enum.unidade_federativa import UnidadeFederativa

# Modelo.
@pytest.fixture
def criar_pessoa():
    pessoa_1 = Pessoa("Caio", 18, Sexo.MASCULINO,
                    Endereco("Rua A.", UnidadeFederativa.BAHIA, 123))
    return pessoa_1

def test_pessoa_atributo_nome(criar_pessoa):
    assert criar_pessoa.nome == "Caio"


def test_pessoa_atributo_idade(criar_pessoa):
    assert criar_pessoa.idade == 18