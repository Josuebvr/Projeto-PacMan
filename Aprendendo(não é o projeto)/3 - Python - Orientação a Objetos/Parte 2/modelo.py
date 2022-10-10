class Filme: # Classe Filme
    def __init__(self, nome, ano, duracao): # Método construtor
        self.nome = nome.title() # Atributo nome
        self.ano = ano # Atributo ano
        self.duracao = duracao # Atributo duração
        self.likes = 0 # Atributo likes

    def dar_like(self): # Método dar_like
        self.likes += 1 # Atributo likes

class Serie: # Classe Série
    def __init__(self, nome, ano, temporadas): # Método construtor
        self.nome = nome.title() # Atributo nome
        self.ano = ano # Atributo ano
        self.temporadas = temporadas # Atributo temporadas
        self.likes = 0 # Atributo likes

    def dar_like(self): # Método dar like
        self.likes += 1 # Atributo likes



vingadores = Filme('vingadores - guerra infinita', 2018, 160) # Instância da classe Filme

vingadores.dar_like() # Chama o método dar_like da instância vingadores

print(f'Nome: {vingadores.nome}, Ano: {vingadores.ano}, Duração: {vingadores.duracao}, Likes: {vingadores.likes}') # Imprime o nome, ano, temporadas e likes da série

atlanta = Serie('atlanta', 2018, 2) # Instância da classe Série

atlanta.dar_like() # Chama o método dar_like da instância atlanta

print(f'Nome: {atlanta.nome}, Ano: {atlanta.ano}, Temporadas: {atlanta.temporadas}, Likes: {atlanta.likes}') # Imprime o nome, ano, temporadas e likes da série

