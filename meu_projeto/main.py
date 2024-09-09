import os
from models.pessoa import Pessoa
from models.enum.sexo import Sexo
from models.endereco import Endereco

os.system("cls || clear")

# Instanciando classe.
pessoa_1 = Pessoa("Caio", 18,Sexo.MASCULINO
                  , Endereco("\nRua 123", 801))

print(pessoa_1)