from typing import Type


class Casa:
    def __init__(self, endereco: str) -> None:
        self.__endereco = endereco

    def acender_luzes(self) -> None:
        print('Luzes foram acendidas.')

    def get_endereco(self) -> str:
        return self.__endereco


class Pessoa:
    def __init__(self, nome: str, local: Type[Casa]) -> None:
        self.__nome = nome
        self.__local = local
    
    def entrar_ao_local(self) -> None:
        self.__local.acender_luzes()

    def apresentar_local(self) -> None:
        endereco = self.__local.get_endereco()
        print('Endereço: {}'.format(endereco))


if __name__ == '__main__':
    casa_de_amigo = Casa('Rua dos limoeiros')
    ana = Pessoa('Ana', casa_de_amigo)
    ana.entrar_ao_local()
    ana.apresentar_local()
