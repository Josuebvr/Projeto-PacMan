



#Apartir daqui são somente as variáveis



def cria_conta(numero, titular, saldo, limite): #cria uma conta
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite} #cria uma conta
    return conta #retorna a conta



def deposita(conta, valor): #função deposita
    conta["saldo"] += valor #adiciona o valor ao saldo



def saca(conta, valor): #função saca
    conta["saldo"] -= valor #subtrai o valor do saldo
    
    

def extrato(conta): #função extrato
    print("Saldo é {}".format(conta["saldo"])) #imprime o saldo da conta
