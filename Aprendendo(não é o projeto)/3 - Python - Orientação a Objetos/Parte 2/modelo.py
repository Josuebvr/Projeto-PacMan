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
        
    def imprime(self): # Método imprime
        print(f'{self._nome} - {self.ano} - {self._likes} Likes') # Imprime os valores de nome, ano e likes



# Classe de Filmes
class Filme(Programa): # Classe Filha
    def __init__(self, nome, ano, duracao): # Método construtor
        super().__init__(nome, ano) # Herança
        self.duracao = duracao # Atributo duração
        
    def imprime(self): # Método imprime
        print(f'{self._nome} - {self.ano} - {self.duracao} min - {self._likes} Likes') # Imprime os valores de nome, ano, duração e likes
      
      
        
# Classe de Séries
class Serie(Programa): # Classe Filha
    def __init__(self, nome, ano, temporadas): # Método construtor
        super().__init__(nome, ano) # Herança
        self.temporadas = temporadas # Atributo temporadas
        
    def imprime(self): # Método imprime
        print(f'{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} Likes') # Imprime os valores de nome, ano, duração e likes



# Definições e prints de séries de filmes
vingadores = Filme('vingadores - guerra infinita', 2018, 160) # Instância da classe Filme
vingadores.dar_like() # Chama o método dar_like da instância vingadores

atlanta = Serie('atlanta', 2018, 2) # Instância da classe Série
atlanta.dar_like() # Chama o método dar_like da instância atlanta
atlanta.dar_like() # Chama o método dar_like da instância atlanta

fimes_e_series = [vingadores, atlanta] # Lista de filmes e séries

for programa in fimes_e_series: # Laço de repetição
    programa.imprime() # Chama o método imprime da instância programa


