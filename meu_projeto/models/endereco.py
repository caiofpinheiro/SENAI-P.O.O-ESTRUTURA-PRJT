from models.enum.unidade_federativa import UnidadeFederativa
class Endereco:
    def __init__(self, logradouro: str, numero: int, uf: UnidadeFederativa) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.uf = UnidadeFederativa
    
    def __str__(self) -> str:
        return (
            f"\nLogradouro: {self.logradouro}"
            f"\nEstado: {self.uf.sigla}"
            f"\nEstado: {self.uf.nome}"
            f"\nNumero: {self.numero}"
        )