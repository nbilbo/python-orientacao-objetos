from abc import ABC
from abc import abstractmethod
from typing import Type


class FormasInterface(ABC):

    @abstractmethod
    def get_perimetro(self) -> int:
        pass
    
    @abstractmethod
    def get_area(self) -> int:
        pass


class Quadrado(FormasInterface):
    def __init__(self, lado: int) -> None:
        self.lado = lado

    def get_perimetro(self) -> int:
        return self.lado * 4

    def get_area(self) -> int:
        return self.lado * self.lado


class Retangulo(FormasInterface):
    def __init__(self, comprimento: int, largura: int) -> None:
        self.comprimento = comprimento
        self.largura = largura

    def get_perimetro(self) -> int:
        return (self.comprimento * 2) + (self.largura * 2)

    def get_area(self) -> int:
        return eelf.comprimento * self.largura


class Engenheiro:
    def __init__(self, nome: str) -> None:
        self.nome = nome

    def calcular_perimetro(self, terreno: Type[FormasInterface]) -> None:
        print(terreno.get_perimetro())


if __name__ == '__main__':
    terreno = Retangulo(100, 50)
    engenheiro = Engenheiro('Ana')
    engenheiro.calcular_perimetro(terreno)
