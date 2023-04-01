class MinhaClasse:
    estatico = 'hello, world.'
    
    @classmethod
    def print_estatico(cls) -> None:
        print(cls.estatico)
    
    @classmethod
    def mudar_estatico(cls) -> None:
        cls.estatico = 'Programador'


if __name__ == '__main__':
    obj1 = MinhaClasse()
    obj1.print_estatico()
    obj1.mudar_estatico()
    obj1.print_estatico()
