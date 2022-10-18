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

#verifica se a string é float sem retornar erro. Utilizado para diferenciar tk identificador e tk constante
def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

 # verifica se a linguagem aceita a palavra
def verificaPalavra(grafo, palavra, estadosFinais):
    estadosVisitados = [] # para armazenar os estados em que o caractere/letra nao foi aceito
    estado = 0 # estado atual
    indice = -1 # armazena a posição da lista (indexação) do caractere atual
    for letra in palavra:
        indice += 1
        estadosVisitados.clear()
        aux = grafo.relaciones[estado] # armazena a lista de arestas do estado atual
        for aresta in aux: # percorre cada aresta
            if(letra not in aresta.peso): # se a letra nao foi aceita
                estadosVisitados.append(aresta.elemento)
                continue
            else: # caso a letra é aceita
                estado = aresta.elemento # troca de estado
                if(estado in estadosFinais and indice == len(palavra)-1):
                    return True # se o estado for final e a letra é a última da palavra, palavra aceita
                break
        if(len(estadosVisitados) == len(aux)): return False # caso todas as arestas ja tenham sido visitadas





