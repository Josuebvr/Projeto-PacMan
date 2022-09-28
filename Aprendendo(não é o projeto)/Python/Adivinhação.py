import random # Importa a biblioteca random

def jogar(): # Função jogo_adivinhacao

    # Isso aqui é só pra deixar o output mais bonito
    print("--------------------------------") #
    print("Bem vindo ao jogo de adivinhação") # Imprime na tela
    print("--------------------------------") #

    # Isso aqui é pra definir o número secreto
    numero_secreto = random.randrange(1, 101) # Gera um número aleatório entre 1 e 100
    total_de_tentativas = 0 # Define o número de tentativas
    pontos = 1000 # Define os pontos

    # Isso aqui é pra definir o nível de dificuldade
    print("Qual nível de dificuldade?") # Imprime na tela
    print("(1) Fácil (2) Médio (3) Difícil") # Imprime na tela
    nivel = int(input("Defina o nível: ")) # Pede pra definir o nível
    if(nivel == 1): # Se o nível for 1
        total_de_tentativas = 20 # Define o número de tentativas como 20
    elif(nivel == 2): # Se o nível for 2
        total_de_tentativas = 10 # Define o número de tentativas como 10
    else: # Se o nível for 3
        total_de_tentativas = 5 # Define o número de tentativas como 5

    # Ínicio do loop
    for rodada in range(1, total_de_tentativas + 1): # range(1, 4) = 1, 2, 3
        print("Tentativa {} de {}".format(rodada, total_de_tentativas)) # Imprime na tela
        chute = input("Digite um número entre 1 e 100: ") # Imprime na tela e recebe um valor
        print("Você digitou ", chute) # Imprime na tela
        chute = int(chute) # Converte o valor recebido para inteiro
        
        # Isso aqui é pra verificar se o chute está correto
        if(chute < 1 or chute > 100): # Verifica se o valor está entre 1 e 100
            print("Você deve digitar um número entre 1 e 100!") # Imprime na tela
            continue # Volta para o início do loop
        # Condições pra verificar se o chute está correto
        acertou = chute == numero_secreto # Verifica se o valor é igual ao número secreto
        maior = chute > numero_secreto # Verifica se o valor é maior que o número secreto
        menor = chute < numero_secreto # Verifica se o valor é menor que o número secreto

    # Isso aqui é pra imprimir o resultado
        if (acertou): # Verifica se o valor é igual ao número secreto
            print("Você acertou e fez {} pontos!".format(pontos)) # Imprime na tela
            break # Sai do loop
        else: # Se o valor não for igual ao número secreto
            if (maior): # Verifica se o valor é maior que o número secreto
                print("Você errou! O seu chute foi maior que o número secreto.") # Imprime na tela
            elif (menor): # Verifica se o valor é menor que o número secreto
                print("Você errou! O seu chute foi menor que o número secreto.") # Imprime na tela
            # Isso aqui é pra definir os pontos perdidos
            pontos_perdidos = abs(numero_secreto - chute) # Calcula os pontos perdidos
            pontos = pontos - pontos_perdidos # Calcula os pontos restantes
        
    # Isso aqui é indicar que acabou o jogo
    print("Fim do jogo") # Imprime na tela