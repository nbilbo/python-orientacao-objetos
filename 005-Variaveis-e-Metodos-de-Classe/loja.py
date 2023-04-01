class Loja:
    tarifa: float = 1.03

    def __init__(self, endereco: str) -> None:
        self.__endereco = endereco

    def apresentar_endereco(self) -> None:
        print('Endereço: {}'.format(self.__endereco))
    
    @classmethod
    def vender(cls) -> float:
        return 40 * cls.tarifa
    
    @classmethod
    def alterar_tarifa(cls, nova_tarifa: float) -> None:
        print('tarifa alterada para: {}'.format(nova_tarifa))
        cls.tarifa = nova_tarifa


if __name__ == '__main__':
    loja_praia = Loja('Praia')
    loja_centro = Loja('Centro')

    loja_praia.apresentar_endereco()
    loja_centro.apresentar_endereco()

    print('Loja da praia vendeu: {}'.format(loja_praia.vender()))
    print('Loja do centro vendeu: {}'.format(loja_centro.vender()))

    loja_centro.alterar_tarifa(1.50)

    print('Loja da praia vendeu: {}'.format(loja_praia.vender()))
    print('Loja do centro vendeu: {}'.format(loja_centro.vender()))

