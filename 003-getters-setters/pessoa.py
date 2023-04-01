class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade

    def dirigir(self, veiculo: str) -> None:
        print('Dirigindo um(a) {}'.format(veiculo))

    def cantar(self) -> None:
        print('Cantando 🎤')

    def apresentar_idade(self) -> int:
        return self.idade


if __name__ == '__main__':
    pessoa = Pessoa('Amanda', 40)
    pessoa.dirigir('motocicleta')
    pessoa.cantar()
    print('Idade: {}'.format(pessoa.apresentar_idade()))

