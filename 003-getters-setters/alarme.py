class ValorInvalido(Exception):
    pass


class Alarme:
    def __init__(self, estado: bool) -> None:
        self.set_estado(estado)

    def get_estado(self) -> bool:
        return self.__estado

    def set_estado(self, valor: bool) -> None:
        if isinstance(valor, bool):
            self.__estado = valor
        else:
            raise ValorInvalido('O valor \"{}\" é invalido.'.format(valor))


if __name__ == '__main__':
    meu_alarme = Alarme(False)
    print('Estado: {}'.format(meu_alarme.get_estado()))
    # meu_alarme.set_estado('True') # levanta uma exception.
