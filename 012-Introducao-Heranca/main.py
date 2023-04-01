class Mae:
    def __init__(self, endereco: str, sobrenome: str) -> None:
        self.endereco = endereco
        self.sobrenome = sobrenome

    def comer(self) -> None:
        print('Comendo.')

    def estudar(self) -> None:
        print('Estudando.')


class Filha(Mae):
    def __init__(self, endereco: str, sobrenome: str, idade: int) -> None:
        # referenciando o método inicializador da classe super.
        super().__init__(endereco, sobrenome)
        self.idade = idade


if __name__ == '__main__':
    mae = Mae('Rua do balão', 'Almeida')
    filha = Filha('Rua do balão', 'Almeida', 10)

    filha.comer()
    filha.estudar()
    print('Idade: {}'.format(filha.idade))
