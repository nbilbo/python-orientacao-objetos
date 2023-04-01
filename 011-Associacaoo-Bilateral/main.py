from modulos import Casa
from modulos import Pessoa


if __name__ == '__main__':
    casa_ana = Casa('Rua do limoeiro')
    ana = Pessoa('Ana')

    ana.set_local(casa_ana)
    casa_ana.set_proprietario(ana)
    ana.se_apresentar()
    ana.apresentar_local()

    casa_pedro = Casa('Rua arvore grande')
    pedro = Pessoa('Pedro')

    pedro.set_local(casa_pedro)
    casa_pedro.set_proprietario(pedro)
    pedro.se_apresentar()
    pedro.apresentar_local()


