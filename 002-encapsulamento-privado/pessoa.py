class Pessoa:
    def __init__(self, nome: str, idade: int, cpf: str) -> None:
        self.nome = nome
        self.idade = idade

        # attrbituto privado.
        self.__cpf = cpf

    def correr(self) -> None:
        print('correndo')

    def beber(self, bebida: str) -> None:
        if bebida == 'cerveja':
            self.__apresentar_documento()
        print(f'bebendo {bebida}')

    def __apresentar_documento(self) -> None:
        print(f'Documento: {self.__cpf}')


if __name__ == '__main__':
    ronaldo = Pessoa('Ronaldo', 40, '123-abc-456')
    print(ronaldo.nome)
    print(ronaldo.idade)
    ronaldo.beber('agua')
    ronaldo.beber('cerveja')
