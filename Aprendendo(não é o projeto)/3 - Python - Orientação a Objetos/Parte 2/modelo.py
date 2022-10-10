


# Classe de Filmes


class Filme: # Classe Filme
    def __init__(self, nome, ano, duracao): # Método construtor
        self.__nome = nome.title() # Atributo nome
        self.ano = ano # Atributo ano
        self.duracao = duracao # Atributo duração
        self.__likes = 0 # Atributo likes
        
    @property # Decorador
    def likes(self): # Método likes
        return self.__likes # Retorna o valor de likes
        
    @property # Decorador
    def nome(self): # Método nome
        return self.__nome # Retorna o valor de nome
    
    @nome.setter # Decorador
    def nome(self, novo_nome): # Método nome
        self.__nome = novo_nome.title() # Atribui o valor de novo_nome a nome

    def dar_like(self): # Método dar_like
        self.__likes += 1 # Atributo likes
      
      
        
# Classe de Séries


class Serie: # Classe Série
    def __init__(self, nome, ano, temporadas): # Método construtor
        self.__nome = nome.title() # Atributo nome
        self.ano = ano # Atributo ano
        self.temporadas = temporadas # Atributo temporadas
        self.__likes = 0 # Atributo likes
        
    @property # Decorador
    def likes(self): # Método likes
        return self.__likes # Retorna o valor de likes
        
    @property # Decorador
    def nome(self): # Método nome
        return self.__nome # Retorna o valor de nome
    
    @nome.setter # Decorador
    def nome(self, novo_nome): # Método nome
        self.__nome = novo_nome.title() # Atribui o valor de novo_nome a nome

    def dar_like(self): # Método dar_like
        self.__likes += 1 # Atributo likes



# Definições e prints de séries de filmes


vingadores = Filme('vingadores - guerra infinita', 2018, 160) # Instância da classe Filme
vingadores.dar_like() # Chama o método dar_like da instância vingadores
print(f'Nome: {vingadores.nome}, Ano: {vingadores.ano}, Duração: {vingadores.duracao}, Likes: {vingadores.likes}') # Imprime o nome, ano, temporadas e likes da série

atlanta = Serie('atlanta', 2018, 2) # Instância da classe Série
atlanta.dar_like() # Chama o método dar_like da instância atlanta
atlanta.dar_like() # Chama o método dar_like da instância atlanta
print(f'Nome: {atlanta.nome}, Ano: {atlanta.ano}, Temporadas: {atlanta.temporadas}, Likes: {atlanta.likes}') # Imprime o nome, ano, temporadas e likes da série




