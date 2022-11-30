class Elevador:
    def __init__(self,atual,total,cap,pessoa):
        self._atual = int(atual)
        self._total = int(total)
        self._cap = int(cap)
        self._pessoa = int(pessoa)


    @property
    def nAtual(self):
        return self._atual
        
    @property
    def nTotal(self):
        return self._total
    
    @property
    def nCap(self):
        return self._cap
    
    @property
    def nPessoa(self):
        return self._pessoa
           
    def inicializa(self, novo1,novo2):
        self._total = novo1
        self._cap = novo2

    def entra(self):
        if self.nPessoa < self.nCap:
            self._pessoa+=1
            print(self.nPessoa,'pessoa(s)')
        else:
            print('Capacidade insuficiente (Elevador cheio)')

    def sai(self):
        if self.nPessoa> 0:
            self._pessoa-=1
            print(self.nPessoa,'pessoa(s)')
        else:
            print('Elevador Vazio !!!')

    def sobe(self):
        if self.nAtual < self.nTotal:
            self._atua+=1
            print('Andar',self.nAtual)

    def desce(self):
        if self.nAtual > 0:
            self._atua-=1
            print('Andar',self.nAtual)