class Pessoa:
    def __init__(self, nome, d_nas, alt):
        self._nome = nome
        self._d_nas = d_nas
        self._alt = alt
    

    @property
    def gNome(self):
        return self._nome
    
    @gNome.setter
    def set_nome(self, novoNome):
        self._nome = novoNome
        
    @property
    def gData(self):
        return self._d_nas 
    
    @gData.setter
    def set_d_nas (self, novoData):
        self._d_nas  = novoData
        
    @property
    def gAlt(self):
        return self._alt
    
    @gAlt.setter
    def set_alt(self, novoAlt):
        self._alt = novoAlt
    
    def imprimir(self):
        print('Nome:', self.gNome)
        print('DATA de nascimento:', self.gData)
        print('ALTURA: ', self.gAlt)

    def cal_idade(self):
        idade = 2022 - self.gData
        print(idade,'Anos')   