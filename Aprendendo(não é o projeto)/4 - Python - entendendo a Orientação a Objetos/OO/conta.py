

class Conta: 
    
    def __init__(self, numero, titular, saldo, limite): #cria uma conta
        print("Construindo objeto ... {}".format(self)) #imprime a mensagem
        self.numero  = numero  #atribui o numero a conta
        self.titular = titular #atribui o titular a conta
        self.saldo   = saldo   #atribui o saldo a conta
        self.limite  = limite  #atribui o limite a conta
    
    