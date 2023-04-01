from abc import ABC
from abc import abstractmethod


class ClasseAbstrata(ABC):

    @abstractmethod
    def metodo_abstrato(self) -> None:
        pass


class Filha(ClasseAbstrata):
    def metodo_abstrato(self) -> None:
        print('meu metodo abstrato')

