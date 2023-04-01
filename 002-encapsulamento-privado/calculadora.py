class OperacaoInvalida(Exception):
    pass


class Calculadora:
    def calcular(self, op: str, num1: int, num2: int) -> None:
        if op == '+':
            return self.__adicionar(num1, num2)

        elif op == '-':
            return self.__subtrair(num1, num2)

        else:
            raise OperacaoInvalida(f'A operacao \"{op}\" é invalida.')
    
    # metodos privados.
    def __adicionar(self, num1: int, num2: int) -> None:
        return num1+num2

    def __subtrair(self, num1: int, num2: int) -> None:
        return num1-num2


if __name__ == '__main__':
    calculadora = Calculadora()
    print('{}+{}={}'.format(1, 2, calculadora.calcular('+', 1, 2)))
    print('{}-{}={}'.format(10, 20, calculadora.calcular('-', 10, 20)))
