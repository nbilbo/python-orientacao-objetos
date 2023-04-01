class DatabaseConn:
    def __init__(self) -> None:
        self.__database = 'Postgres'
        self._conn = '///connection_string'
        self.user = 'admin'

    def get_database(self) -> str:
        return self.__database

    def _testing_connection(self) -> None:
        print('Testing connection')


class Repository(DatabaseConn):
    def select(self) -> None:
        self._testing_connection()
        print('Select * from ...')


if __name__ == '__main__':
    db = DatabaseConn()
    print(db.user)
    # print(db.__database) # levanta um erro.
    print(db._conn) 

    repo = Repository()
    print(repo.user)
    repo.select()

