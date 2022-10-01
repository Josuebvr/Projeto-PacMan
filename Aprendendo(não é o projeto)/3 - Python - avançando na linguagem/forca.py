def jogar():  # Função jogo_forca

    # Isso aqui é só pra deixar o output mais bonito
    print("--------------------------------")
    print("---Bem vindo ao jogo de Forca---")  # Imprime na tela
    print("--------------------------------")

    palavra_secreta = "banana"  # Palavra secreta
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]  # Lista de letras acertadas

    enforcou = False  # Variável que diz se o jogador foi enforcado
    acertou = False  # Variável que diz se o jogador acertou a palavra secreta
    
    print(letras_acertadas)  # Imprime na tela a prévia de quantas letras tem a palavra secreta

    # Enquanto o jogador não for enforcado e não acertar a palavra secreta
    while (not enforcou and not acertou):

        # Pede para o jogador digitar uma letra
        # Pede para o jogador digitar uma letra
        chute = input("Qual a letra? ")
        chute = chute.strip()  # Remove os espaços em branco

        index = 0  # Variável que vai guardar o índice da letra
        for letra in palavra_secreta:  # Para cada letra na palavra secreta
            # Se o chute for igual a letra (ignorando maiúsculas e minúsculas)
            if (chute.upper() == letra.upper()):
                # Imprime na tela caso o chute seja igual a letra
                letras_acertadas[index] = letra # Coloca a letra na lista de letras acertadas
            index = index + 1  # Incrementa o índice

        print(letras_acertadas)  # Imprime na tela a lista de letras acertadas

    # Isso aqui é indicar que acabou o jogo
    print("Fim do jogo")  # Imprime na tela


if (__name__ == "__main__"):  # Se o arquivo for executado diretamente
    jogar()  # Executa a função de jogar
