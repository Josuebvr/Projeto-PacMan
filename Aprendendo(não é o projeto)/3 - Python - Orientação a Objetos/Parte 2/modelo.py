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
        self._nome = nome.title() # Atributo nome
        self.ano = ano # Atributo ano
        self.duracao = duracao # Atributo duração
        self._likes = 0 # Atributo likes
      
      
        
# Classe de Séries


class Serie(Programa): # Classe Filha
    def __init__(self, nome, ano, temporadas): # Método construtor
        self._nome = nome.title() # Atributo nome
        self.ano = ano # Atributo ano
        self.temporadas = temporadas # Atributo temporadas
        self._likes = 0 # Atributo likes



# Definições e prints de séries de filmes


vingadores = Filme('vingadores - guerra infinita', 2018, 160) # Instância da classe Filme
vingadores.dar_like() # Chama o método dar_like da instância vingadores
print(f'Nome: {vingadores.nome}, Ano: {vingadores.ano}, Duração: {vingadores.duracao}, Likes: {vingadores.likes}') # Imprime o nome, ano, temporadas e likes da série

atlanta = Serie('atlanta', 2018, 2) # Instância da classe Série
atlanta.dar_like() # Chama o método dar_like da instância atlanta
atlanta.dar_like() # Chama o método dar_like da instância atlanta
print(f'Nome: {atlanta.nome}, Ano: {atlanta.ano}, Temporadas: {atlanta.temporadas}, Likes: {atlanta.likes}') # Imprime o nome, ano, temporadas e likes da série




