class Select:

    def select_many(self):
        pass

    def select_one(self):
        pass


class Insert:
    
    def insert_many(self):
        pass

    def insert_one(self):
        pass


class Repositorio:
    def __init__(self) -> None:
        self.__insert = Insert()
        self.__select = Select()

    def select_by_id(self):
        pass

    def insert_single(self):
        pass

