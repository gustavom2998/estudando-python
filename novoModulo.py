"""Este módulo é um módulo de exemplo.

Ele possui Uma Classe, Uma função e uma instância da classe."""
def printNumeroUm():
    print("1")
    
class Numero():
    def __init__(self,valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    @valor.setter
    def valor(self, novoValor):
        self._valor = novoValor
        
x = Numero(5)