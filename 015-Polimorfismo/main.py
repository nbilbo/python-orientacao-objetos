class Pessoa:
    def __init__(self, nome: str) -> None:
        self.nome = nome

    def __repr__(self) -> str:
        return '<Pessoa {}>'.format(self.nome)


class Funcionario(Pessoa):
    def __init__(self, nome: str, cpf: str) -> None:
        super().__init__(nome)
        self.cpf = cpf

    def __repr__(self) -> str:
        return '<Funcionario {} {}>'.format(self.nome, self.cpf)


if __name__ == '__main__':
    pessoa = Pessoa('Ana')
    funcionario = Funcionario('Clara', 'AAA-111-BBB-01')
    print(pessoa)
    print(funcionario)
