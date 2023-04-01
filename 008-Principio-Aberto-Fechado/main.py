class Circo:
    def apresentar(self, apresentador: any) -> None:
        apresentador.apresentar_show()


class Malabarista:
    def apresentar_show(self) -> None:
        print('Malabarista apresenta seu show.')


class Palhaco:
    def apresentar_show(self) -> None:
        print('Palhaço apresenta seu show.')


if __name__ == '__main__':
    circo = Circo()
    malabarista = Malabarista()
    palhaco = Palhaco()
    circo.apresentar(malabarista)
    circo.apresentar(palhaco)
