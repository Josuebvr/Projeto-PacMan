# Classe Pai
class Programa: # Classe Pai
    def __init__(self, nome, ano): # Método construtor
        self._nome = nome.title() # Atributo nome
        self.ano = ano # Atributo ano
        self._likes = 0 # Atributo likes
        
    @property # Decorador
    def likes(self): # Método likes
        return self._likes # Retorna o valor de likes
    
    def dar_like(self): # Método dar_like
        self._likes += 1 # Atributo likes 
        
    @property # Decorador
    def nome(self): # Método nome
        return self._nome # Retorna o valor de nome
    
    @nome.setter # Decorador
    def nome(self, novo_nome): # Método nome
        self._nome = novo_nome.title() # Atribui o valor de novo_nome a nome 
        
    def __str__(self): # Método str
        return f'{self._nome} - {self.ano} - {self._likes} Likes' # Retorna o valor de nome, ano e likes 



# Classe de Filmes
class Filme(Programa): # Classe Filha
    def __init__(self, nome, ano, duracao): # Método construtor
        super().__init__(nome, ano) # Herança
        self.duracao = duracao # Atributo duração
        
    def __str__(self): # Método imprime
        return f'{self._nome} - {self.ano} - {self.duracao} min - {self._likes} Likes' # Imprime os valores de nome, ano, duração e likes
      
      
        
# Classe de Séries
class Serie(Programa): # Classe Filha
    def __init__(self, nome, ano, temporadas): # Método construtor
        super().__init__(nome, ano) # Herança
        self.temporadas = temporadas # Atributo temporadas
        
    def __str__(self): # Método imprime
        return f'{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} Likes' # Imprime os valores de nome, ano, duração e likes
  
  
  
# Classe de Playlists  
class Playlist: # Classe playlist
    def __init__ (self, nome, programas): # Método construtor
        self.nome = nome # Atributo nome
        self.programas = programas  # Atributo programas
        
    def tamanho(self): # Método tamanho
        return len(self.programas) # Retorna o tamanho da lista programas



# Definições e prints de séries de filmes
vingadores = Filme('vingadores - guerra infinita', 2018, 160) # Instância da classe Filme
atlanta = Serie('atlanta', 2018, 2) # Instância da classe Série
tmep = Filme('todo mundo em pânico', 1999, 100) # Instância da classe Filme
demolidor = Serie('demolidor', 2016, 2) # Instância da classe Série



vingadores.dar_like() # Chama o método dar_like da instância vingadores
tmep.dar_like()       # Chama o método dar_like da instância tmep
tmep.dar_like()       # Chama o método dar_like da instância tmep
tmep.dar_like()       # Chama o método dar_like da instância tmep
tmep.dar_like()       # Chama o método dar_like da instância tmep
demolidor.dar_like()  # Chama o método dar_like da instância demolidor
demolidor.dar_like()  # Chama o método dar_like da instância demolidor
atlanta.dar_like()    # Chama o método dar_like da instância atlanta
atlanta.dar_like()    # Chama o método dar_like da instância atlanta
atlanta.dar_like()    # Chama o método dar_like da instância atlanta

fimes_e_series = [vingadores, atlanta, demolidor, tmep] # Lista de filmes e séries
playlist_fim_de_semana = Playlist ('fim de semana', fimes_e_series) # Instância da classe playlist

for programa in playlist_fim_de_semana.programas: # Laço de repetição
    print(programa) # Imprime os valores de programa


