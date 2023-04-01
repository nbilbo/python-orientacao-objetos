class Casa:
    def __init__(self, endereco: str) -> None:
        self.__endereco = endereco
        self.__proprietario = None

    def acender_luzes(self) -> None:
        print('Estou acendendo as luzes.')

    def get_endereco(self) -> str:
        return self.__endereco

    def set_proprietario(self, proprietario: any) -> None:
        self.__proprietario = proprietario

    def ge_proprietario(self) -> None:
        return self.__proprietario

