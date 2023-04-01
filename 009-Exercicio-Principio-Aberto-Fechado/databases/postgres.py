class PostgresDB:
    def __init__(self) -> None:
        self.__conexao = 'Postgres'

    def conectar(self) -> str:
        print('conectando ao banco de dados postgres.')
        return self.__conexao

    def desconectar(self) -> None:
        print('desconectando do banco de dados postgres.')

