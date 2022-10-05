

class Conta:  
    
    def __init__(self, numero, titular, saldo, limite): #cria uma conta
        print("Construindo objeto ... {}".format(self)) #imprime a mensagem
        self.__numero  = numero  #atribui o numero a conta
        self.__titular = titular #atribui o titular a conta
        self.__saldo   = saldo   #atribui o saldo a conta
        self.__limite  = limite  #atribui o limite a conta
        
    def extrato(self): #função extrato
        print("Saldo {} do titular {}".format(self.__saldo, self.__titular)) #imprime o saldo da conta    
        
    def deposita(self, valor): #função deposita
        self.__saldo += valor #adiciona o valor ao saldo
    
    def saca(self, valor): #função saca
        self.__saldo -= valor #subtrai o valor do saldo
        
    def transfere(self, valor, origem, destino): #função transfere
        origem.saca(valor) #saca o valor da conta origem
        destino.deposita(valor) #deposita o valor na conta destino
     