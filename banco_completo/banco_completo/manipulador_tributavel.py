
from tributavel import Tributavel

class Manipulador_tributavel():

    def calcula_imposto(self,objeto):
        if isinstance(objeto, Tributavel):
            return objeto.get_valor_tributado()
        else:
            print('Objeto não é tributável!')
            return 0