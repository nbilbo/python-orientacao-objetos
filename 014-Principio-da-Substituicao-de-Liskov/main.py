from typing import Type


class Animal:
    def comer(self) -> str:
        print('Comendo')

    def andar(self) -> str:
        print('Andando')

    def dormir(self) -> str:
        print('Dormir')

    def __repr__(self) -> str:
        return '<Animal>'


class Lobos(Animal):
    def uivar(self) -> str:
        print('Uivando')


class Aves(Animal):
    def voar(self) -> str:
        print('Voando')


class Penguim(Aves):
    def deslizar(self) -> None:
        print('Deslizando')


class Falcao(Aves):
    def voar(self) -> None:
        print('Voando')


class Pessoa:
    def __init__(self, nome: str) -> str:
        self.nome = nome

    def obeservar(self, animal: Type[Animal]) -> None:
        print('{} oberseva {}'.format(self.nome, animal))


if __name__ == '__main__':
    ana = Pessoa('Ana')
    penguim = Penguim()
    ana.obeservar(penguim)

