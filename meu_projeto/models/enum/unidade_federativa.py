from enum import Enum

class UnidadeFederativa(Enum):
    BAHIA = ("Bahia", "BA")
    SAO_PAULO = ("São Paulo", "SP")

    def __init__(self, nome: str, sigla: str) -> None:
        self.nome = nome
        self.sigla = sigla

