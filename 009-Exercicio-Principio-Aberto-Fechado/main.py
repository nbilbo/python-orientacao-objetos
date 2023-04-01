from repositorio import Repositorio
from databases import PostgresDB


if __name__ == '__main__':
    repo = Repositorio()
    db = PostgresDB()

    repo.select(db)
    repo.insert(db)
