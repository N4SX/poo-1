lista_pessoas = []
class Agenda:
    def armazenaPessoa(self, nome, idade, altura):
        pessoa = Pessoa(nome, idade, altura)
        try:
            lista_pessoas.append(pessoa)
            return True
        except:
            return False
        
    def buscaPessoa(self, nome):
        aux = 0
        for i in lista_pessoas:
            if i.gNome == nome:
                flag = 1
                break
            else:
                aux+=1
        
        if flag == 1:
            return aux
        else:
            return -1
        
    def removePessoa(self, nome):
        aux = self.buscaPessoa(nome)
        lista_pessoas.pop(int(aux))
        
    def imprimeAgenda(self):
        print("IMPRIMINDO AGENDA ...")
        for i in lista_pessoas:
            print("\nNome: ",i.gNome)
            print("Idade: ",i.gIdade)
            print("Altura: ",i.gAltura)
            
        print("\n... FIM DA AGENDA")
        
    def imprimePessoa(self, nome):
        aux = self.buscaPessoa(nome)
        
        print("\nINDEX: ",aux)
        print("Nome: ",lista_pessoas[aux].gNome)
        print("Idade: ",lista_pessoas[aux].gIdade)
        print("Altura: ",lista_pessoas[aux].gAltura)
            
        
class Pessoa:
    def __init__(self,nome,idade,altura):
        self._nome = nome
        self._idade = idade
        self._altura = altura
        
    @property
    def gNome(self):
        return self._nome

    @property
    def gIdade(self):
        return self._idade
    
    @property
    def gAltura(self):
        return self._altura