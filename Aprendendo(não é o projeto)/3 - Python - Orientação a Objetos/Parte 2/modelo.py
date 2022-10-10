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



# Classe de Filmes
class Filme(Programa): # Classe Filha
    def __init__(self, nome, ano, duracao): # Método construtor
        super().__init__(nome, ano) # Herança
        self.duracao = duracao # Atributo duração
      
      
        
# Classe de Séries
class Serie(Programa): # Classe Filha
    def __init__(self, nome, ano, temporadas): # Método construtor
        super().__init__(nome, ano) # Herança
        self.temporadas = temporadas # Atributo temporadas



# Definições e prints de séries de filmes
vingadores = Filme('vingadores - guerra infinita', 2018, 160) # Instância da classe Filme
vingadores.dar_like() # Chama o método dar_like da instância vingadores
print(f'{vingadores.nome} - {vingadores.duracao}: {vingadores.likes}') # Imprime o nome, duração e likes da série

atlanta = Serie('atlanta', 2018, 2) # Instância da classe Série
atlanta.dar_like() # Chama o método dar_like da instância atlanta
atlanta.dar_like() # Chama o método dar_like da instância atlanta
print(f'{atlanta.nome} - {atlanta.temporadas}: {atlanta.likes}') # Imprime o nome, temporadas e likes da série

fimes_e_series = [vingadores, atlanta] # Lista de filmes e séries

for programa in fimes_e_series: # Laço de repetição
    detalhes = programa.duracao if hasattr(programa, 'duracao') else programa.temporadas # Condição do detalhe(duração ou temporadas)
    print(f'{programa.nome} - {detalhes} - {programa.likes}') # Imprime o nome e likes de cada filme e série


