from typing import Type


class Produto:
    def __init__(self, nome: str, preco: float) -> None:
        self.nome = nome
        self.preco = preco


class CarrinhoCompra:
    def __init__(self) -> None:
        self.__produtos = []

    def adidicionar_produto(self, produto: Type[Produto]) -> None:
        self.__produtos.append(produto)


if __name__ == '__main__':
    monitor = Produto('monitor', 1000)
    cadeira = Produto('cadeira', 500)

    carrinho = CarrinhoCompra()
    carrinho.adidicionar_produto(monitor)
    carrinho.adidicionar_produto(cadeira)
