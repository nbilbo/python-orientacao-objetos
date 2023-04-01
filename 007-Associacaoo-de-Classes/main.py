class Interruptor:
    def __init__(self, comodo: str) -> None:
        self.__comodo = comodo

    def acender(self) -> None:
        print(f'luzes do comodo {self.__comodo} acendidas.')

    def apagar(self) -> None:
        print(f'luzes do comodo {self.__comodo} apagadas.')


class Pessoa:
    def acender_luzes(self, interruptor: 'Interruptor') -> None:
        interruptor.acender()

    def apagar_luzes(self, interruptor: 'Interruptor') -> None:
        interruptor.apagar()

    def dormir(self) -> None:
        print('indo dormir.')


if __name__ == '__main__':
    pessoa = Pessoa()
    interruptor_sala = Interruptor('sala')
    interruptor_quarto = Interruptor('quarto')

    pessoa.acender_luzes(interruptor_quarto)
    pessoa.apagar_luzes(interruptor_quarto)
    pessoa.dormir()

