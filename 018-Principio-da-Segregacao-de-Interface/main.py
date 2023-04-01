from abc import ABC
from abc import abstractmethod
from typing import Type


class Aves(ABC):

    @abstractmethod
    def comer(self) -> None:
        raise NotImplementedError('Should implement comer method.')
    
    @abstractmethod
    def voar(self) -> None:
        raise NotImplementedError('Should implement voar method.')
    
    @abstractmethod
    def cantar(self) -> None:
        raise NotImplementedError('Should implement cantar method.')


class Canario(Aves):

    def comer(self) -> None:
        print('Canario começou a comer uma fruta.')
    
    def voar(self) -> None:
        print('Canario começou a voar para seu ninho.')

    def cantar(self) -> None:
        print('Canario começou a cantar bem alto.')
        self.__acasalar()

    def __acasalar(self) -> None:
        print('Canario começou a acasalar.')


class Agente:
    def observar(self, ave: Type[Aves]) -> None:
        ave.gritar()


if __name__ == '__main__':
    canario = Canario()
    agente = Agente()
    agente.observar(canario)

