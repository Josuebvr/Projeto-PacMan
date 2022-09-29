def jogar():  # Função jogo_forca

    # Isso aqui é só pra deixar o output mais bonito
    print("--------------------------------")
    print("---Bem vindo ao jogo de Forca---")  # Imprime na tela
    print("--------------------------------")

    palavra_secreta = "banana"  # Palavra secreta

    enforcou = False  # Variável que diz se o jogador foi enforcado
    acertou = False  # Variável que diz se o jogador acertou a palavra secreta

    # Enquanto o jogador não for enforcado e não acertar a palavra secreta
    while (not enforcou and not acertou):

        # Pede para o jogador digitar uma letra
        chute = input("Qual a letra? ") # Pede para o jogador digitar uma letra

        index = 0  # Variável que vai guardar o índice da letra
        for letra in palavra_secreta:  # Para cada letra na palavra secreta
            if (chute == letra):  # Se o chute for igual a letra
                print("Encontrei a letra {} na posição {}".format(letra, index))  # Imprime na tela caso o chute seja igual a letra
            index = index + 1  # Incrementa o índice

        print("Jogando...")  # Imprime que ainda está jogando

    # Isso aqui é indicar que acabou o jogo
    print("Fim do jogo")  # Imprime na tela


if (__name__ == "__main__"):  # Se o arquivo for executado diretamente
    jogar()  # Executa a função de jogar
