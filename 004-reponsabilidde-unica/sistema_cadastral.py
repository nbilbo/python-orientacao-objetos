class SistemaCadastral:
    def cadastrar(self, nome: str, idade: int) -> None:
        if self.__verificar_dados_cadastrar(nome, idade):
            self.__armazenar_usuario(nome, idade)
        else:
            self.__indicar_erros_cadastrar(nome, idade)
    
    def __verificar_dados_cadastrar(self, nome: str, idade: int) -> bool:
        return isinstance(nome, str) and isinstance(idade, int)
    
    def __armazenar_usuario(self, nome: str, idade: int) -> None:
        print('Acessando o banco de dados...')
        print('Cadastrado o usuario {} com {} anos.'.format(nome, idade))
    
    def __indicar_erros_cadastrar(self, nome:str, idade: int) -> None:
            print('dados invalidos.')


if __name__ == '__main__':
    sistema = SistemaCadastral()
    sistema.cadastrar('Andre', 40)
    sistema.cadastrar('Andrea', '40')