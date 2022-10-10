class Filme: # Classe Filme
    def __init__(self, nome, ano, duracao): # Método construtor
        self.nome = nome.title() # Atributo nome
        self.ano = ano # Atributo ano
        self.duracao = duracao # Atributo duração


class Serie: # Classe Série
    def __init__(self, nome, ano, temporadas): # Método construtor
        self.nome = nome.title() # Atributo nome
        self.ano = ano # Atributo ano
        self.temporadas = temporadas # Atributo temporadas

vingadores = Filme('vingadores - guerra infinita', 2018, 160) # Instância da classe Filme
print(f'Nome: {vingadores.nome}, Ano: {vingadores.ano}, Duração: {vingadores.duracao}') # Imprime o nome do filme

atlanta = Serie('atlanta', 2018, 2) # Instância da classe Série
print(f'Nome: {atlanta.nome}, Ano: {atlanta.ano}, Temporadas: {atlanta.temporadas}') # Imprime o nome, ano e temporadas da série
