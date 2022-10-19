# Definições de comentários
# Para mudanças entre classes: ##-----------------------------------------------------------------##-----------------------------------------------------------------##
# Para mudanças dentro de uma classe: #--------------------------------------------------------------------------------------------------------------------------------------#

# Pressione "P" para pausar o jogo

import pygame 
from abc import ABCMeta, abstractmethod 
import random 


pygame.init() # Inicializa o pygame

##-----------------------------------------------------------------##-----------------------------------------------------------------##

screen = pygame.display.set_mode((770, 560), 0) # Cria a tela (Alterar as dimensões da tela aqui)
font = pygame.font.SysFont("Trebuchet MS", 20, True, False) # Cria a fonte (Alterar a fonte aqui)


                                 # Definição de cores
AMARELO      =  (255, 255, 0)    # 
PRETO        =  (0, 0, 0)        # 
ROXO         =  (48, 25, 52)     # 
VERMELHO     =  (139, 0, 0)      #
BRANCO       =  (255, 255, 255)  #
AZUL_VIOLETA =  (138, 43, 226)   # 
VIOLETA      =  (148, 0, 211)    # 
INDIGO       =  (75,0,130)       # 
AZUL         =  (25,25,112)      #
ROXO_ROXO    =  (128,0,128)      #

VELOCIDADE = 1 # Velocidade do pacman

ACIMA = 1      # 
ABAIXO = 2     #
DIREITA = 3    #
ESQUERDA = 4   #

##-----------------------------------------------------------------##-----------------------------------------------------------------##

class ElementoJogo(metaclass=ABCMeta): # Classe abstrata
    @abstractmethod # Método abstrato
    def printar(self, tela): # Método pintar
        pass # Passa para o próximo método

    @abstractmethod # Método abstrato
    def calcular_regras(self): # Método calcular_regras
        pass # Passa para o próximo método

    @abstractmethod # Método abstrato
    def processar_eventos(self, eventos): # Método processar_eventos
        pass # Passa para o próximo método

##-----------------------------------------------------------------##-----------------------------------------------------------------##

class Movivel(metaclass=ABCMeta): # Classe abstrata
    @abstractmethod # Método abstrato
    def aceitar_movimento(self): # Método aceitar_movimento
        pass # Passa para o próximo método

    @abstractmethod # Método abstrato
    def recusar_movimento(self, direcoes): # Método recusar_movimento
        pass # Passa para o próximo método

    @abstractmethod # Método abstrato
    def esquina(self, direcoes): # Método esquina
        pass # Passa para o próximo método

##-----------------------------------------------------------------##-----------------------------------------------------------------##

class Cenario(ElementoJogo): # Classe Cenario
    def __init__(self, tamanho, pac): # Construtor
        self.pacman = pac  # Pacman
        self.moviveis = [] # Lista de moviveis
        self.pontos = -1   # Pontos (Quantidade de pontos iniciais)
        
        # Estados possiveis:
        # 0 - Jogando 
        # 1 - Pausado 
        # 2 - Fim de Jogo  
        # 3 - Vitoria
        
        self.estado = 0 # Estado
        self.tamanho = tamanho # Tamanho
        self.vidas = 3  # Vidas
        self.matriz = [ # Matriz que faz o mapa
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], # Linha 0
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2], # Linha 1
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2], # Linha 2
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2], # Linha 3  
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2], # Linha 4
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2], # Linha 5
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2], # Linha 6
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2], # Linha 7
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2], # Linha 8
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2], # Linha 9
            [2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2], # Linha 10
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 0, 0, 0, 0, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2], # Linha 11
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2], # Linha 12
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2], # Linha 13
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2], # Linha 14
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2], # Linha 15 
            [2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2], # Linha 16
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2], # Linha 17
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2], # Linha 18
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2], # Linha 19
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2], # Linha 20
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2], # Linha 21
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2], # Linha 22
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2], # Linha 23
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2], # Linha 24
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2], # Linha 25
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2], # Linha 26
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]  # Linha 27
        ] # Fim da matriz

#--------------------------------------------------------------------------------------------------------------------------------------#

    def adicionar_movivel(self, obj): # Adiciona um objeto movível
        self.moviveis.append(obj)     # Adiciona o objeto na lista de movíveis

    def printar_pontuacao(self, tela): # Printa o score na tela
        pontos_x = self.tamanho * 30   # Posição x do score
        pontos_img = font.render("Pontuação: {}".format(self.pontos), True, VERMELHO) # Imagem do score
        vidas_img = font.render("Vidas: {}".format(self.vidas), True, VERMELHO)       # Imagem das vidas
        tela.blit(pontos_img, (pontos_x, 50)) # Printa o score na tela
        tela.blit(vidas_img, (pontos_x, 100)) # Printa as vidas na tela

    def printar_linha(self, tela, numero_linha, linha): # Printa uma linha da matriz
        for numero_coluna, coluna in enumerate(linha):  # Para cada coluna da linha
            x = numero_coluna * self.tamanho # Posição x da coluna
            y = numero_linha * self.tamanho  # Posição y da linha
            half = self.tamanho // 2 # Metade do tamanho do bloco
            cor = PRETO # Cor do bloco
            if coluna == 2: # Se o bloco for um bloco destrutível
                cor = ROXO  # Cor do bloco
            pygame.draw.rect(tela, cor, (x, y, self.tamanho, self.tamanho), 0) # Printa o bloco na tela
            
            # Desenhas os blocos destrutiveis(Pastilhas)
            if coluna == 1: # Se o bloco for um bloco indestrutível
                pygame.draw.circle(tela, VERMELHO, (x + half, y + half), self.tamanho // 10, 0) # Pinta o círculo na tela / Tamanho do círculo

#--------------------------------------------------------------------------------------------------------------------------------------#

    def printar(self, tela):             # Printa a matriz na tela
        if self.estado == 0:             # Se o estado for 0
            self.printar_jogando(tela)   # Printa Jogando na tela
        elif self.estado == 1:           # Se o estado for 1
            self.printar_jogando(tela)   # Printa Jogando na tela
            self.printar_pausado(tela)   # Printa a mensagem de pausado na tela
        elif self.estado == 2:           # Se o estado for 2
            self.printar_jogando(tela)   # Printa Jogando na tela
            self.printar_fimdejogo(tela) # Printa a mensagem de final de jogo na tela
        elif self.estado == 3:           # Se o estado for 3
            self.printar_jogando(tela)   # Printa Jogando na tela
            self.printar_vitoria(tela)   # Printa a mensagem de vitória na tela

#--------------------------------------------------------------------------------------------------------------------------------------#

    def printar_texto_vitoria(self, tela, texto): # Printa o texto no centro da tela quando o jogador ganha
        texto_img = font.render(texto, True, VERMELHO) # Imagem do texto
        texto_x = (tela.get_width() - texto_img.get_width()) // 1.05 # Posição x do texto
        texto_y = (tela.get_height() - texto_img.get_height()) // 2  # Posição y do texto
        tela.blit(texto_img, (texto_x, texto_y)) # Printa o texto na tela
        
    def printar_texto_fimdejogo(self, tela, texto): # Printa o texto no centro da tela quando o jogador perde
        texto_img = font.render(texto, True, VERMELHO) # Imagem do texto
        texto_x = (tela.get_width() - texto_img.get_width()) // 1.07 # Posição x do texto
        texto_y = (tela.get_height() - texto_img.get_height()) // 2  # Posição y do texto
        tela.blit(texto_img, (texto_x, texto_y)) # Printa o texto na tela
        
    def printar_texto_pausado(self, tela, texto): # Printa o texto no centro da tela quando o jogador pausa
        texto_img = font.render(texto, True, VERMELHO) # Imagem do texto
        texto_x = (tela.get_width() - texto_img.get_width()) // 1.10 # Posição x do texto
        texto_y = (tela.get_height() - texto_img.get_height()) // 2  # Posição y do texto
        tela.blit(texto_img, (texto_x, texto_y)) # Printa o texto na tela
        
#--------------------------------------------------------------------------------------------------------------------------------------#

    def printar_vitoria(self, tela): # Função que printa a mensagem de vitória na tela
        self.printar_texto_vitoria(tela, "VOCÊ VENCEU !!!") # Printa a mensagem de vitória na tela

    def printar_fimdejogo(self, tela): # Função que printa a mensagem de fim de jogo na tela
        self.printar_texto_fimdejogo(tela, "FIM DE JOGO") # Printa a mensagem de fim de jogo na tela

    def printar_pausado(self, tela): # Função que printa a mensagem de pausado na tela
        self.printar_texto_pausado(tela, "PAUSADO") # Printa a mensagem de pausado na tela

    def printar_jogando(self, tela): # Função que printa a mensagem de jogando na tela
        for numero_linha, linha in enumerate(self.matriz): # Para cada linha da matriz
            self.printar_linha(tela, numero_linha, linha) # Printa a linha na tela
        self.printar_pontuacao(tela) # Printa o score na tela

#--------------------------------------------------------------------------------------------------------------------------------------#

    def get_direcoes(self, linha, coluna): # Função que retorna as direções possíveis
        direcoes = [] # Lista de direções
        if self.matriz[int(linha - 1)][int(coluna)] != 2: # Se a linha acima não for um bloco destrutível
            direcoes.append(ACIMA)                        # Adiciona a direção acima na lista de direções
        if self.matriz[int(linha + 1)][int(coluna)] != 2: # Se a linha abaixo não for um bloco destrutível
            direcoes.append(ABAIXO)                       # Adiciona a direção abaixo na lista de direções
        if self.matriz[int(linha)][int(coluna - 1)] != 2: # Se a coluna a esquerda não for um bloco destrutível
            direcoes.append(ESQUERDA)                     # Adiciona a direção esquerda na lista de direções
        if self.matriz[int(linha)][int(coluna + 1)] != 2: # Se a coluna a direita não for um bloco destrutível
            direcoes.append(DIREITA)                      # Adiciona a direção direita na lista de direções
        return direcoes # Retorna a lista de direções

#--------------------------------------------------------------------------------------------------------------------------------------#

    def calcular_regras(self): # Função que calcula as regras do jogo
        if self.estado == 0:                 # Se o estado for 0
            self.calcular_regras_jogando()   # Continua jogando
        elif self.estado == 1:               # Se o estado for 1
            self.calcular_regras_pausado()   # Jogo Pausado
        elif self.estado == 2:               # Se o estado for 2
            self.calcular_regras_fimdejogo() # Fim de Jogo

    def calcular_regras_fimdejogo(self): # Função que calcula as regras do jogo quando for fim de jogo
        pass # Não faz nada

    def calcular_regras_pausado(self): # Função que calcula as regras do jogo quando estiver pausado
        pass # Não faz nada


    def calcular_regras_jogando(self): # Função que calcula as regras do jogo quando estiver jogando
        for movivel in self.moviveis:  # Para cada movível
            lin = int(movivel.linha)   # Linha do movível
            col = int(movivel.coluna)  # Coluna do movível
            lin_intencao = int(movivel.linha_intencao)  # Linha de intenção do movível
            col_intencao = int(movivel.coluna_intencao) # Coluna de intenção do movível
            direcoes = self.get_direcoes(lin, col) # Direções possíveis
            if len(direcoes) >= 3:        # Se tiver 3 ou mais direções possíveis
                movivel.esquina(direcoes) # Movível é uma esquina
            if isinstance(movivel, Fantasma) and movivel.linha == self.pacman.linha and \
                    movivel.coluna == self.pacman.coluna: # ^^^Se o movível for um fantasma e estiver na mesma posição do pacman^^^
                self.vidas -= 1     # Perde uma vida
                if self.vidas <= 0: # Se não tiver mais vidas
                    self.estado = 2 # Estado é 2
                else:               # Se tiver mais vidas
                    self.pacman.linha = 1  # Posição do pacman na linha é 1
                    self.pacman.coluna = 1 # Posição do pacman na coluna é 1
            else:
                if 0 <= col_intencao < 28 and 0 <= lin_intencao < 29 and \
                        self.matriz[lin_intencao][col_intencao] != 2: # ^^^ Se a posição de intenção do movível estiver dentro da matriz e não for um bloco destrutível^^^
                    movivel.aceitar_movimento() # Movível aceita o movimento
                    if isinstance(movivel, Pacman) and self.matriz[lin][col] == 1: # Se o movível for um pacman e a posição atual dele for um bloco comum
                        self.pontos += 1 # Adiciona um ponto
                        self.matriz[lin][col] = 0 # Posição atual do pacman na matriz é 0
                        if self.pontos >= 281: # Se o score for maior ou igual a 281 (que é a pontuação máxima)
                            self.estado = 3 # Estado é 3
                else: # Se a posição de intenção do movível não estiver dentro da matriz ou for um bloco destrutível
                    movivel.recusar_movimento(direcoes) # Movível recusa o movimento

#--------------------------------------------------------------------------------------------------------------------------------------#

    def processar_eventos(self, evts): # Função que processa os eventos
        for e in evts: # Para cada evento
            if e.type == pygame.QUIT: # Se o evento for sair
                exit() # Sai do jogo
            if e.type == pygame.KEYDOWN: # Se o evento for uma tecla pressionada
                if e.key == pygame.K_p:  # Se a tecla for p
                    if self.estado == 0: # Se o estado for 0
                        self.estado = 1  # Estado é 1
                    else:                # Se o estado não for 0
                        self.estado = 0  # Estado é 0

##-----------------------------------------------------------------##-----------------------------------------------------------------##

class Pacman(ElementoJogo, Movivel): # Classe que representa o pacman
    def __init__(self, tamanho): # Função que inicializa o pacman
        self.coluna = 1 # Coluna do pacman
        self.linha = 1  # Linha do pacman
        self.centro_x = 400 # Centro do pacman na horizontal
        self.centro_y = 300 # Centro do pacman na vertical
        self.tamanho = tamanho # Tamanho do pacman
        self.vel_x = 0 # Velocidade do pacman na horizontal
        self.vel_y = 0 # Velocidade do pacman na vertical
        self.raio = self.tamanho // 2 # Raio do pacman
        self.coluna_intencao = self.coluna # Coluna de intenção do pacman
        self.linha_intencao = self.linha   # Linha de intenção do pacman
        self.abertura = 0            # Abertura da boca do pacman
        self.velocidade_abertura = 1 # Velocidade da abertura da boca do pacman

#--------------------------------------------------------------------------------------------------------------------------------------#

    def calcular_regras(self): # Função que calcula as regras do pacman
        self.coluna_intencao = self.coluna + self.vel_x # Coluna de intenção do pacman é a coluna atual + a velocidade na horizontal
        self.linha_intencao = self.linha + self.vel_y   # Linha de intenção do pacman é a linha atual + a velocidade na vertical
        self.centro_x = int(self.coluna * self.tamanho + self.raio) # Centro do pacman na horizontal é a coluna atual * o tamanho do pacman + o raio do pacman
        self.centro_y = int(self.linha * self.tamanho + self.raio)  # Centro do pacman na vertical é a linha atual * o tamanho do pacman + o raio do pacman

#--------------------------------------------------------------------------------------------------------------------------------------#

    def printar(self, tela): # Função que printa o pacman 
        # Desenhar o corpo do Pacman 
        pygame.draw.circle(tela, VERMELHO, (self.centro_x, 
                           self.centro_y), self.raio, 0) # ^^^Desenha o corpo do pacman^^^ 	

        self.abertura += self.velocidade_abertura # Abertura da boca do pacman é a abertura atual + a velocidade da abertura da boca do pacman 
        if self.abertura > self.raio: # Se a abertura for maior que o raio 
            self.velocidade_abertura = -1 # Velocidade da abertura é -1 (para fechar a boca)
        if self.abertura <= 0: # Se a abertura for menor ou igual a 0   
            self.velocidade_abertura = 1 # Velocidade da abertura é 1 (para abrir a boca)

        # Desenho da boca do Pacman 
        canto_boca = (self.centro_x, self.centro_y) # Canto da boca do pacman é o centro do pacman 
        labio_superior = (self.centro_x + self.raio, 
                          self.centro_y - self.abertura) # ^^^Labio superior do pacman é o centro do pacman + o raio do pacman^^^ 
        labio_inferior = (self.centro_x + self.raio,
                          self.centro_y + self.abertura) # ^^^Labio inferior do pacman é o centro do pacman + o raio do pacman^^^ 
        pontos = [canto_boca, labio_superior, labio_inferior] # Lista de pontos do pacman 
        pygame.draw.polygon(tela, PRETO, pontos, 0) # ^^^Desenha a boca do pacman^^^ 

        # Olho do Pacman 
        olho_x = int(self.centro_x + self.raio / 3) # Olho do pacman na horizontal é o centro do pacman + o raio do pacman / 3 
        olho_y = int(self.centro_y - self.raio * 0.70) # Olho do pacman na vertical é o centro do pacman - o raio do pacman * 0.70 
        olho_raio = int(self.raio / 10) # Raio do olho do pacman é o raio do pacman / 10 
        pygame.draw.circle(tela, PRETO, (olho_x, olho_y), olho_raio, 0) # ^^^Desenha o olho do pacman^^^ 

#--------------------------------------------------------------------------------------------------------------------------------------#

    def processar_eventos(self, eventos): # Função que processa os eventos do pacman 
        for e in eventos: # Para cada evento 
            if e.type == pygame.KEYDOWN:     # Se o evento for uma tecla pressionada 
                if e.key == pygame.K_RIGHT:  # Se a tecla for seta para a direita 
                    self.vel_x = VELOCIDADE  # Velocidade na horizontal é a velocidade definida no início do código 
                elif e.key == pygame.K_LEFT: # Se a tecla for seta para a esquerda 
                    self.vel_x = -VELOCIDADE # Velocidade na horizontal é a velocidade negativa definida no início do código
                elif e.key == pygame.K_UP:   # Se a tecla for seta para cima 
                    self.vel_y = -VELOCIDADE # Velocidade na vertical é a velocidade negativa definida no início do código
                elif e.key == pygame.K_DOWN: # Se a tecla for seta para baixo 
                    self.vel_y = VELOCIDADE  # Velocidade na vertical é a velocidade definida no início do código
            elif e.type == pygame.KEYUP:     # Se o evento for uma tecla solta  
                if e.key == pygame.K_RIGHT:  # Se a tecla for seta para a direita 
                    self.vel_x = 0           # Velocidade na horizontal é 0 
                elif e.key == pygame.K_LEFT: # Se a tecla for seta para a esquerda 
                    self.vel_x = 0           # Velocidade na horizontal é 0 
                elif e.key == pygame.K_UP:   # Se a tecla for seta para cima 
                    self.vel_y = 0           # Velocidade na vertical é 0 
                elif e.key == pygame.K_DOWN: # Se a tecla for seta para baixo 
                    self.vel_y = 0           # Velocidade na vertical é 0 

    def aceitar_movimento(self): # Função que aceita o movimento do pacman 
        self.linha = self.linha_intencao   # Linha atual é a linha de intenção 
        self.coluna = self.coluna_intencao # Coluna atual é a coluna de intenção 

    def recusar_movimento(self, direcoes): # Função que recusa o movimento do pacman 
        self.linha_intencao = self.linha   # Linha de intenção é a linha atual 
        self.coluna_intencao = self.coluna # Coluna de intenção é a coluna atual 

    def esquina(self, direcoes): # Função que verifica se o pacman está em uma esquina 
        pass # Não faz nada 

##-----------------------------------------------------------------##-----------------------------------------------------------------##

class Fantasma(ElementoJogo): # Classe fantasma que herda da classe ElementoJogo 
    def __init__(self, cor, tamanho): # Função que inicializa o fantasma 
        self.coluna = 13.0 # Coluna atual do fantasma (13.0)
        self.linha = 15.0  # Linha atual do fantasma (15.0) 
        self.linha_intencao = self.linha   # Linha de intenção do fantasma é a linha atual 
        self.coluna_intencao = self.coluna # Coluna de intenção do fantasma é a coluna atual 
        self.velocidade = 1 # Velocidade do fantasma é 1 
        self.direcao = ABAIXO  # Direção do fantasma é para baixo 
        self.tamanho = tamanho # Tamanho do fantasma é o tamanho passado como parâmetro 
        self.cor = cor # Cor do fantasma é a cor passada como parâmetro 

    def printar(self, tela): # Função que printa o fantasma 
        fatia = self.tamanho // 8 # Fatia do fantasma é o tamanho do fantasma / 8 
        px = int(self.coluna * self.tamanho) # Posição x do fantasma é a coluna atual * o tamanho do fantasma 
        py = int(self.linha * self.tamanho)  # Posição y do fantasma é a linha atual * o tamanho do fantasma 
        
        contorno = [(px, py + self.tamanho),                # Lista de pontos do contorno do fantasma 
                    (px + fatia, py + fatia * 2),           # 
                    (px + fatia * 2, py + fatia // 2),      # 
                    (px + fatia * 3, py),                   #
                    (px + fatia * 5, py),                   #
                    (px + fatia * 6, py + fatia // 2),      #
                    (px + fatia * 7, py + fatia * 2),       #
                    (px + self.tamanho, py + self.tamanho)] # 
        pygame.draw.polygon(tela, self.cor, contorno, 0)    # ^^^Desenha o contorno do fantasma^^^ 

        olho_raio_ext = fatia       # Raio externo do olho do fantasma é a fatia 
        olho_raio_int = fatia // 2  # Raio interno do olho do fantasma é a fatia / 2 

        olho_e_x = int(px + fatia * 2.5) # Posição x do olho esquerdo do fantasma é a posição x do fantasma + a fatia * 2.5 
        olho_e_y = int(py + fatia * 2.5) # Posição y do olho esquerdo do fantasma é a posição y do fantasma + a fatia * 2.5

        olho_d_x = int(px + fatia * 5.5) # Posição x do olho direito do fantasma é a posição x do fantasma + a fatia * 5.5 
        olho_d_y = int(py + fatia * 2.5) # Posição y do olho direito do fantasma é a posição y do fantasma + a fatia * 2.5

        pygame.draw.circle( # Desenha o olho esquerdo do fantasma 
            tela, BRANCO, (olho_e_x, olho_e_y), olho_raio_ext, 0) # Tela, cor, posição, raio externo, espessura 
        pygame.draw.circle(tela, PRETO, (olho_e_x, olho_e_y), olho_raio_int, 0) # Desenha o olho interno do olho esquerdo 
        pygame.draw.circle( # Desenha o olho direito do fantasma 
            tela, BRANCO, (olho_d_x, olho_d_y), olho_raio_ext, 0) # Tela, cor, posição, raio externo, espessura 
        pygame.draw.circle(tela, PRETO, (olho_d_x, olho_d_y), olho_raio_int, 0) # Desenha o olho interno do olho direito 

#--------------------------------------------------------------------------------------------------------------------------------------#

    def calcular_regras(self): # Função que calcula as regras do fantasma
        if self.direcao == ACIMA:                   # Se a direção for para cima 
            self.linha_intencao -= self.velocidade  # Linha de intenção é a linha de intenção - a velocidade 
        elif self.direcao == ABAIXO:                # Se a direção for para baixo 
            self.linha_intencao += self.velocidade  # Linha de intenção é a linha de intenção + a velocidade 
        elif self.direcao == ESQUERDA:              # Se a direção for para esquerda 
            self.coluna_intencao -= self.velocidade # Coluna de intenção é a coluna de intenção - a velocidade 
        elif self.direcao == DIREITA:               # Se a direção for para direita 
            self.coluna_intencao += self.velocidade # Coluna de intenção é a coluna de intenção + a velocidade 

#--------------------------------------------------------------------------------------------------------------------------------------#

    def mudar_direcao(self, direcoes):         # Função que muda a direção do fantasma 
        self.direcao = random.choice(direcoes) # Direção do fantasma é uma direção aleatória da lista de direções passada como parâmetro 

    def esquina(self, direcoes):     # Função que verifica se o fantasma está em uma esquina 
        self.mudar_direcao(direcoes) # Muda a direção do fantasma para uma direção aleatória da lista de direções passada como parâmetro 

    def aceitar_movimento(self):           # Função que verifica se o fantasma pode se mover 
        self.linha = self.linha_intencao   # Linha do fantasma é a linha de intenção 
        self.coluna = self.coluna_intencao # Coluna do fantasma é a coluna de intenção 

    def recusar_movimento(self, direcoes): # Função que verifica se o fantasma não pode se mover 
        self.linha_intencao = self.linha   # Linha de intenção do fantasma é a linha atual 
        self.coluna_intencao = self.coluna # Coluna de intenção do fantasma é a coluna atual 
        self.mudar_direcao(direcoes)       # Muda a direção do fantasma para uma direção aleatória da lista de direções passada como parâmetro 

    def processar_eventos(self, evts): # Função que processa os eventos do fantasma 
        pass                           # Não faz nada 

#--------------------------------------------------------------------------------------------------------------------------------------#

if __name__ == "__main__": # Se o arquivo for executado diretamente 
    size = 600 // 30       # Tamanho da tela é 600 / 30 
    pacman = Pacman(size)  # Cria o objeto Pacman 
    fantasma1 = Fantasma(ROXO_ROXO, size)    # Cria o objeto Fantasma 1 (roxo)
    fantasma2 = Fantasma(INDIGO, size)       # Cria o objeto Fantasma 2 (indigo)
    fantasma3 = Fantasma(AZUL_VIOLETA, size) # Cria o objeto Fantasma 3 (azul violeta)
    fantasma4 = Fantasma(VIOLETA, size)      # Cria o objeto Fantasma 4 (violeta)
    cenario = Cenario(size, pacman)   # Cria o objeto Cenario
    cenario.adicionar_movivel(pacman) # Adiciona o Pacman ao cenário
    cenario.adicionar_movivel(fantasma1)  # Adiciona o Fantasma 1 (roxo) ao cenário
    cenario.adicionar_movivel(fantasma2)  # Adiciona o Fantasma 2 (indigo) ao cenário
    cenario.adicionar_movivel(fantasma3)  # Adiciona o Fantasma 3 (azul violeta) ao cenário
    cenario.adicionar_movivel(fantasma4)  # Adiciona o Fantasma 4 (violeta) ao cenário

    while True: # Loop infinito
        # Calcula as regras 
        pacman.calcular_regras()      # Calcula as regras do Pacman
        fantasma1.calcular_regras()   # Calcula as regras do Fantasma 1 (roxo)
        fantasma2.calcular_regras()   # Calcula as regras do Fantasma 2 (indigo)
        fantasma3.calcular_regras()   # Calcula as regras do Fantasma 3 (azul violeta)
        fantasma4.calcular_regras()   # Calcula as regras do Fantasma 4 (violeta)
        cenario.calcular_regras()     # Calcula as regras do cenário

        # Printa os elementos do jogo na tela e define a velocidade
        screen.fill(PRETO)       # Pinta a tela de preto 
        cenario.printar(screen)  # Printa o cenário na tela 
        pacman.printar(screen)   # Printa o Pacman na tela 
        fantasma1.printar(screen)    # Printa o Fantasma 1 (roxo) na tela 
        fantasma2.printar(screen)    # Printa o Fantasma 2 (indigo) na tela 
        fantasma3.printar(screen)    # Printa o Fantasma 3 (azul violeta) na tela 
        fantasma4.printar(screen)    # Printa o Fantasma 4 (violeta) na tela 
        pygame.display.update() # Atualiza a tela 
        pygame.time.delay(90)   # velocidade do jogo (100) 

        # Captura os eventos 
        eventos = pygame.event.get()       # Captura os eventos 
        pacman.processar_eventos(eventos)  # Processa os eventos do Pacman 
        cenario.processar_eventos(eventos) # Processa os eventos do cenário 
        
        
        
        
   
   
   
   
        

