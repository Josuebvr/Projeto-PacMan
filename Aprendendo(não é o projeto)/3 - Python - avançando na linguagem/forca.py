def jogar(): # Função jogo_forca

    # Isso aqui é só pra deixar o output mais bonito
    print("--------------------------------") #
    print("---Bem vindo ao jogo de Forca---") # Imprime na tela
    print("--------------------------------") #
    
    palavra_secreta = "banana" # Palavra secreta
    
    enforcou = False # Variável que diz se o jogador foi enforcado
    acertou = False # Variável que diz se o jogador acertou a palavra secreta
    
    while(not enforcou and not acertou): # Enquanto o jogador não for enforcado e não acertar a palavra secreta
        print("Jogando...") # Imprime que ainda está jogando	

    # Isso aqui é indicar que acabou o jogo
    print("Fim do jogo") # Imprime na tela

if(__name__ == "__main__"): # Se o arquivo for executado diretamente
    jogar() # Executa a função de jogar
