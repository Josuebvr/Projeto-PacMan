

class Conta:  
    
    def __init__(self, numero, titular, saldo, limite): #cria uma conta
        print("Construindo objeto ... {}".format(self)) #imprime a mensagem
        self.__numero  = numero  #atribui o numero a conta
        self.__titular = titular #atribui o titular a conta
        self.__saldo   = saldo   #atribui o saldo a conta
        self.__limite  = limite  #atribui o limite a conta
        
    def extrato(self): #função extrato
        print("Saldo {} do titular {}".format(self.__saldo, self.__titular)) #imprime o saldo da conta    
        
    def deposita(self, valor): #função deposita o valor
        self.__saldo += valor  #adiciona o valor ao saldo
        
    def __pode_sacar(self, valor_a_sacar):                      #função que verifica se pode sacar
        valor_disponivel_a_sacar = self.__saldo + self.__limite #soma o saldo com o limite
        return valor_a_sacar <= valor_disponivel_a_sacar        #retorna se o valor é menor ou igual ao saldo + limite
    
    def saca(self, valor):            #função saca o valor
        if(self.__pode_sacar(valor)): #se o valor for menor ou igual ao saldo + limite
            self.__saldo -= valor     #subtrai o valor do saldo
        else: #se não
            print("O valor {} passou o limite".format(valor)) #imprime a mensagem caso não tenha limite suficiente
        
    def transfere(self, valor, origem, destino): #função que transfere entre as contas
        origem.saca(valor)                       #saca o valor da conta origem
        destino.deposita(valor)                  #deposita o valor na conta destino
    
    @property  
    def saldo(self):        #função que pega_saldo
        return self.__saldo #retorna o saldo
    
    @property
    def titular(self):        #função que devolve para o titular
        return self.__titular #retorna o titular
    
    @property
    def limite(self):        #função que pega limite
        return self.__limite #retorna o limite
    
    @limite.setter
    def limite(self, limite):  #função que seta o limite
        self.__limite = limite #atribui o limite a conta
     