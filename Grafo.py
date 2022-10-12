#self o nome do objeto ( construtor ) a ser invocado no método; ademais, é o padrão especificado pela PEP-8.
#cria o gafo e um dictornary que tem os vertices dentro
class Grafo(object):
    def __init__(self):
        self.relaciones = {} #dictionary ou matriz de adjacencia
    def __str__(self): #metodo padrao de pyhton que transforma os objetos da clase a strings 
        return str(self.relaciones)
    def __repr__(self): # print a matriz
        return f'Grafo(relaciones={self.relaciones})'

# Crea as arestas entre os vertices
class Aresta(object):
    def __init__(self, elemento, peso):
        self.elemento = elemento
        self.peso = peso       
    def __str__(self):
        return str(self.elemento) + str(self.peso)
    def __repr__(self): # print a matriz
        return f'->{self.elemento} peso={self.peso}'
 
#funcao para addicionar um novo vertice ao dictionario 
def agregar(grafo, elemento):
    grafo.relaciones.update({elemento:[]})

#funcao para juntar 2 vertices com a Aresta criada 
def relacionar(grafo, vertice1, vertice2, peso = 1):
    grafo.relaciones[vertice1].append(Aresta(vertice2, peso))
  
def imprimeGrafo(grafo):
       print (grafo.relaciones)