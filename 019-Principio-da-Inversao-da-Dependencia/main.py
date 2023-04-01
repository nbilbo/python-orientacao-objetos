from abc import ABC
from abc import abstractmethod
from typing import Type


class InterfaceRepositorio(ABC):

    @abstractmethod
    def inserir(self) -> None:
        raise NotImplementedError('Should implement inserir method.')
    
    @abstractmethod
    def deletar(self) -> None:
        raise NotImplementedError('Should implement deletar method.')


class MySqlRepositorio(InterfaceRepositorio):

    def inserir(self) -> None:
        print('inserindo no repositorio mysql.') 
    
    def deletar(self) -> None:
        print('deletando no repositorio mysql.') 


class MongoRepositorio(InterfaceRepositorio):

    def inserir(self) -> None:
        print('inserindo no repositorio mongo.') 
    
    def deletar(self) -> None:
        print('deletando no repositorio mongo.') 


class Usuario:
    def __init__(self, repositorio: Type[InterfaceRepositorio]) -> None:
        self.__repositorio = repositorio

    def armazenar_dado(self) -> None:
        self.__repositorio.inserir()

    def remover_dado(self) -> None:
        self.__repositorio.deletar()


if __name__ == '__main__':
    repo = MySqlRepositorio()
    usu = Usuario(repo)
    usu.armazenar_dado()
    usu.remover_dado()
    
