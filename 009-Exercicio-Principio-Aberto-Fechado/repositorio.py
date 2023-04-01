class Repositorio:
    def select(self, db_connection: any) -> None:
        connection = db_connection.conectar()
        print('conectei ao banco {}'.format(connection))
        print('fazendo um select...')
        db_connection.desconectar()

    def insert(self, db_connection: any) -> None:
        connection = db_connection.conectar()
        print('conectei ao banco {}'.format(connection))
        print('fazendo um insert...')
        db_connection.desconectar()

