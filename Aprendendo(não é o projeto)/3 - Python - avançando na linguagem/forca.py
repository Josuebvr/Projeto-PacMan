def jogar():  # Função jogo_forca

    # Isso aqui é só pra deixar o output mais bonito
    print("--------------------------------")
    print("---Bem vindo ao jogo de Forca---")  # Imprime na tela
    print("--------------------------------")

    palavra_secreta = "banana".upper()  # Palavra secreta
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]  # Lista de letras acertadas

    enforcou = False  # Variável que diz se o jogador foi enforcado
    acertou = False  # Variável que diz se o jogador acertou a palavra secreta
    erros = 0  # Variável que conta os erros
    
    print(letras_acertadas)  # Imprime na tela a prévia de quantas letras tem a palavra secreta

    # Enquanto o jogador não for enforcado e não acertar a palavra secreta
    while (not enforcou and not acertou):

        # Pede para o jogador digitar uma letra
        # Pede para o jogador digitar uma letra
        chute = input("Qual a letra? ")
        chute = chute.strip().upper()  # Remove os espaços em branco e deixa tudo em maiúsculo
        
        if(chute in palavra_secreta): # Se a letra digitada estiver na palavra secreta
            index = 0  # Variável que vai guardar o índice da letra
            for letra in palavra_secreta:  # Para cada letra na palavra secreta
                # Se o chute for igual a letra
                if (chute == letra): # Imprime na tela caso o chute seja igual a letra
                    letras_acertadas[index] = letra # Coloca a letra na lista de letras acertadas
                index += 1  # Incrementa o índice
        else:
            erros += 1  # Incrementa o número de erros
            
        enforcou = erros == 6  # Se o número de erros for igual a 6, o jogador é enforcado
        acertou = "_" not in letras_acertadas  # Se não tiver mais "_" na lista de letras acertadas, o jogador acertou a palavra secreta
        print(letras_acertadas)  # Imprime na tela a lista de letras acertadas

    # Isso aqui é indicar que acabou o jogo
    if(acertou):
        print("Você ganhou!") 
    else:
        print("Você perdeu!") 
    print("Fim do jogo")  

if (__name__ == "__main__"):  # Se o arquivo for executado diretamente
    jogar()  # Executa a função de jogar
