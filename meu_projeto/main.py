import os
from models.pessoa import Pessoa
from models.enum.sexo import Sexo
from models.endereco import Endereco
from models.enum.unidade_federativa import UnidadeFederativa

os.system("cls || clear")

# Instanciando classe.
pessoa_1 = Pessoa("Caio", 18,Sexo.MASCULINO
                  , Endereco("Rua 123",UnidadeFederativa.BAHIA, 801))

print(pessoa_1)