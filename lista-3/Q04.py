class Televisao:
    def __init__(self,volume,canal):
        self._volume = volume
        self._canal = canal
    

    @property
    def nVolume(self):
        return self._volume
    
    @property
    def nCanal(self):
        return self._canal

class ControleRemoto:
    def __init__(self,v,c):
        self._v = 0
        self._c = 0
        
    @property
    def nV(self):
        return self._v

    @property
    def nC(self):
        return self._c

    def aumentaVol(self):
        if(self.nV<100):
            self._v +=1
        else:
            print('volume no maximo')
        c = Televisao(self.nV, self.nC)
        print('Volume: ', c.nVolume)

    def diminuiVol(self):
        if(self.nV>0):
            self._v-=1
        else:
            print('Volume no minimo')
        c = Televisao(self.nV, self.nC)
        print('Volume: ', c.nVolume )

    def trocaCanal(self):
        self._c = int(input('Digite o numero do canal'))
        c = Televisao(self.nV, self.nC)
        print('Canal: ',c.nCanal)

    def aumentaCal(self):
        self._c +=1
        c = Televisao(self.nV, self.nC)
        print('Canal: ', c.nCanal)

    def diminuiCal(self):
        if(self.nC > 0):
            self._c-=1
        else:
            print('canal inesistente')
        c = Televisao(self.nV, self.nC)
        print('Canal: ', c.nCanal)