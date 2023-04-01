class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade

    def conversar(self, mensagem: str) -> None:
        print('-'*10)
        print(mensagem)
        print('-'*10)

if __name__ == '__main__':
    pessoa = Pessoa('Samuel', 40)
    print(f'Nome da pessoa:', pessoa.nome)
    print(f'Idade da pessoa:', pessoa.idade)
    pessoa.conversar('Olá, Mundo.')

