

class Cliente:
    
    def __init__(self, nome): #cria um cliente
        self.__nome = nome #atribui o nome ao cliente
        
    @property 
    def nome(self): #função que pega o nome
        print("Chamando @property nome()") #imprime a mensagem
        return self.__nome.title() #retorna o nome
    
    @nome.setter    
    def nome(self, nome): #função que seta o nome
        print("Chamando setter nome()") #imprime a mensagem
        self.__nome = nome #atribui o nome ao cliente