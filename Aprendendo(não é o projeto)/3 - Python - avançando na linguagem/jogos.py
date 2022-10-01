import forca # Importa o arquivo Forca.py
import adivinhação # Importa o arquivo Adivinhação.py

def escolhe_jogo(): # Função escolhe_jogo
    # Isso aqui é só pra deixar o output mais bonito
    print("--------------------------------") #
    print("-------Escolha o seu jogo-------") # Imprime na tela
    print("--------------------------------") #

    # Isso aqui é pra definir o jogo
    print("(1) Forca (2) Adivinhação") # Imprime na tela

    jogo = int(input("Qual jogo? ")) # Pede pra definir o jogo


    if (jogo == 1): # Se o jogo for 1
        print("Jogando Forca") 
        forca.jogar() # Executa a função jogo_forca
    elif (jogo == 2): # Se o jogo for 2
        adivinhação.jogar() # Executa a função jogo_adivinhacao
        print("Jogando Adivinhação") 





if(__name__ == "__main__"): # Se o arquivo for executado diretamente
    escolhe_jogo() # Executa a função de escolher o jogo