from Grafo import *
from analiseSintatica import *
import numpy as np
from operator import index
from traceback import print_tb
# import o alfabeto em codigo Ascii 
import string 
# manipular os dados de excel com xlrd
#import xlrd

#Analise Semantica 
contColchetes = 0
tabelaIdentificadores = {}

# VARAIBLES GLOBALES
tamanhoAlfabeto = len(string.printable)
alfabeto = []
listaSaida = []

# Ajuste do numero de estados para criar o automato
# VARAIBLES GLOBALES
tamanhoAlfabeto = len(string.printable)
alfabeto = []
# Ajuste do numero de estados para criar o automato
numEstados = 29 #son 28 estados en total pero como el rango de [0;28] tiene que se x<41
estadosList = [i for i in range(numEstados)]

def criaAlfabeto():
    alfabeto.extend(string.printable)  #cria uma nova lista contendo o alfabeto

estadosFinais=[1,3,4,6,7,8,9,10,11,12,13,14,15,16,17,18,19,21,22,23,24,25,28]

##################################LEITRUA E TABELA DE SIMBOLOS ############################################
################################## AUTOMATOO ###############################################################
def criaAutomato(grafo): 
    
    for x in range(numEstados): agregar(grafo, estadosList[x]) # Cria o grafo de 40 estados
    letras=[]
    algarismos=[]

    for cont in range(0,52): #armazena so as letras do alfabeto
        letras.append(alfabeto[cont+10])
    for cont in range(0,10): # armazena so os numeros do alfabeto 
        algarismos.append(alfabeto[cont])
    
    relacionar(grafo, estadosList[0], estadosList[1], algarismos)
    relacionar(grafo, estadosList[1], estadosList[1], algarismos)
    relacionar(grafo, estadosList[2], estadosList[3], algarismos)
    relacionar(grafo, estadosList[3], estadosList[3], algarismos)
    relacionar(grafo, estadosList[0], estadosList[4], letras)
    relacionar(grafo, estadosList[4], estadosList[4], alfabeto)
    relacionar(grafo, estadosList[1], estadosList[2], '.')
    relacionar(grafo, estadosList[0], estadosList[5], '\\')
    relacionar(grafo, estadosList[5], estadosList[6], '\\')
    relacionar(grafo, estadosList[0], estadosList[7], '(')
    relacionar(grafo, estadosList[0], estadosList[8], ')')
    relacionar(grafo, estadosList[0], estadosList[9], '{')
    relacionar(grafo, estadosList[0], estadosList[10], '}')
    relacionar(grafo, estadosList[0], estadosList[11], '=')
    relacionar(grafo, estadosList[11], estadosList[12], '=')
    relacionar(grafo, estadosList[0], estadosList[13], '+')
    relacionar(grafo, estadosList[13], estadosList[14], '+')
    relacionar(grafo, estadosList[0], estadosList[15], '-')
    relacionar(grafo, estadosList[15], estadosList[16], '-')
    relacionar(grafo, estadosList[0], estadosList[17], '*')
    relacionar(grafo, estadosList[0], estadosList[18], '/')
    relacionar(grafo, estadosList[0], estadosList[19], '%')
    relacionar(grafo, estadosList[0], estadosList[20], '!')
    relacionar(grafo, estadosList[20], estadosList[21], '=')
    relacionar(grafo, estadosList[0], estadosList[22], '>')
    relacionar(grafo, estadosList[22], estadosList[23], '=')
    relacionar(grafo, estadosList[0], estadosList[24], '<')
    relacionar(grafo, estadosList[24], estadosList[25], '=')
    relacionar(grafo, estadosList[0], estadosList[26], '"')
    relacionar(grafo, estadosList[26], estadosList[27], algarismos)
    relacionar(grafo, estadosList[26], estadosList[27], letras)
    relacionar(grafo, estadosList[27], estadosList[28], '"')


#####################################################ANALISE LEXICA ############################
# importa as funcoes 
from analiseLexicaScanner import *

####################################################RECUPERACAO DE ERROS##################################
def Erro(tipo, X, Y, erro):
    if tipo == "Lexico":
        print("[Erro: Análise {}]: símbolo incorreto na linha {}, coluna {}. O símbolo {} não pertence ao alfabeto da linguagem.".format(tipo, X, Y, erro))
        global listaSaida 
        listaSaida.append("[Erro: Análise {}]: símbolo incorreto na linha {}, coluna {}. O símbolo {} não pertence ao alfabeto da linguagem.".format(tipo, X, Y, erro))

########################################################SEMANTICA ####################################################
from analiseSemanticaOptimizacao import *

########################################## ANALISE SINTATICA ####################################

def Sintatica(tokens_lexema,contLinhas,listaLexema):
        global tabelaIdentificadores 
        global contColchetes
        global listaSaida 

        if(tokens_lexema[0] == 'TK_Fecha_Chaves'):
            if fecharChaves(tokens_lexema,contLinhas):
                contColchetes -= 1
                print(contColchetes)
            else:
                return erroSemantico(contLinhas)
        elif(((tokens_lexema[0] == 'TK_While') or (tokens_lexema[0] =='TK_If')) and whileIf(tokens_lexema,contLinhas)  ):
            #print(whileIf(tokens_lexema,contLinhas))
            contColchetes += 1
            print(contColchetes)
            if(listaLexema[2] in tabelaIdentificadores and (verificaWhileIf(listaLexema[2],listaLexema[4]))):
                #print("condicion aceptada")
                jump = 0
            else: 
                return erroSemantico(contLinhas)
                
        elif((tokens_lexema[0] == 'TK_Int') and atribuiInt(tokens_lexema,contLinhas) ):
            #print(atribuiInt(tokens_lexema,contLinhas))
            if len(tokens_lexema) == 4:
                insereVariavel(listaLexema[1],"Inteiro",contColchetes,contLinhas,listaLexema[3])
            else:
                insereVariavel(listaLexema[1],"Inteiro",contColchetes,contLinhas,None)
            
        elif((tokens_lexema[0] == 'TK_Float') and atribuiFloat(tokens_lexema,contLinhas)):
            #print(atribuiFloat(tokens_lexema,contLinhas))
            if len(tokens_lexema) == 4:
                insereVariavel(listaLexema[1],"Float",contColchetes,contLinhas,listaLexema[3])
            else:
                insereVariavel(listaLexema[1],"Float",contColchetes,contLinhas,None)     
           
        elif((tokens_lexema[0] == 'TK_String') and atribuiString(tokens_lexema,contLinhas)):
            #print(atribuiString(tokens_lexema,contLinhas))
            if len(tokens_lexema) == 4:
                insereVariavel(listaLexema[1],"String",contColchetes,contLinhas,listaLexema[3])
            else:
                insereVariavel(listaLexema[1],"String",contColchetes,contLinhas,None)  
             
        elif((tokens_lexema[0] == 'TK_Write') and write(tokens_lexema,contLinhas)):
            if( verificaVariavel(listaLexema[2]) or (tokens_lexema[2] == "TK_Entre_Aspas")): 
                listaSaida.append(tabelaIdentificadores[listaLexema[2]][1] )
                # abrir um arquivo executavel 
            else :
                return erroSemantico(contLinhas) 
            
        elif((tokens_lexema[0] == 'TK_Read') and read(tokens_lexema,contLinhas) ):
            if( verificaVariavel(listaLexema[2]) ): 
                listaSaida.append("Variavel lida corretamente: {}".format(listaLexema[2]))
                # ler um arquivo executavel  
            else :
                return erroSemantico(contLinhas)
            
        elif(tokens_lexema[0] == 'TK_Identificador'):
            #print(operacaoIdentificador2(tokens_lexema,contLinhas))
            if((len(tokens_lexema) == 2) and operacaoIdentificador2(tokens_lexema,contLinhas)):
                if(verificaVariavel(listaLexema[0]) and tabelaIdentificadores[listaLexema[0]][0] == "Inteiro"):
                    b = tabelaIdentificadores[listaLexema[0]][1] 
                    if b == None: b = 0
                    b = int(b) + 1
                    tabelaIdentificadores[listaLexema[0]][1] = b
                else:
                    return erroSemantico(contLinhas) 
                 
            elif((len(tokens_lexema) == 3) and operacaoIdentificador3(tokens_lexema,contLinhas)):
                if(listaLexema[0] in tabelaIdentificadores and (verificaTipo(listaLexema[0],listaLexema[2]))):
                    try :
                        tabelaIdentificadores[listaLexema[0]][1] = tabelaIdentificadores[listaLexema[2]][1]
                    except:
                        tabelaIdentificadores[listaLexema[0]][1] = listaLexema[2]
                else:
                    try:
                       tabelaIdentificadores[listaLexema[0]][1] = atribuicaoVariavel(listaLexema[0],listaLexema[2],tabelaIdentificadores[listaLexema[0]][0]) 
                    except : return erroSemantico(contLinhas)
                
            elif((len(tokens_lexema) == 5) and operacaoIdentificador5(tokens_lexema,contLinhas)):
                #print(operacaoIdentificador5(tokens_lexema,contLinhas))
                #///////////////////////////////////////////////////////////////////////////////////////////////////
                if listaLexema[0] in tabelaIdentificadores:
                    if( verificaTipo(listaLexema[0],listaLexema[2]) and (verificaTipo(listaLexema[0],listaLexema[4]))):
                        #programar atribucion y optimizacion del codigo 
                        if((listaLexema[2] in tabelaIdentificadores) and (listaLexema[4] in tabelaIdentificadores)): 
                            tabelaIdentificadores[listaLexema[0]][1] =  operacaoMat(int(tabelaIdentificadores[listaLexema[2]][1]),int(tabelaIdentificadores[listaLexema[4]][1]),listaLexema[3])
                        elif (listaLexema[2] in tabelaIdentificadores):
                            tabelaIdentificadores[listaLexema[0]][1] = operacaoMat(int(tabelaIdentificadores[listaLexema[2]][1]),int(listaLexema[4]),listaLexema[3])  
                        elif (listaLexema[4] in tabelaIdentificadores):
                            tabelaIdentificadores[listaLexema[0]][1] = operacaoMat(int(tabelaIdentificadores[listaLexema[4]][1]),int(listaLexema[2]),listaLexema[3])    
                        else: 
                            tabelaIdentificadores[listaLexema[0]][1] = operacaoMat(int(listaLexema[2]),int(listaLexema[4]),listaLexema[3])
                        
                        listaSaida.append(tabelaIdentificadores[listaLexema[0]][1] )
                    else: 
                        return erroSemantico(contLinhas)
                else: 
                        return erroSemantico(contLinhas)
            else: 
                listaSaida.append("Erro Regra Sintatica: Na atribuicao de variavel")
                print("Erro Regra Sintatica: Na atribuicao de variavel ")
        else:
            listaSaida.append("Erro Regra Sintaticadddd– Linha: {}".format(contLinhas))
            print("Erro Regra Sintaticadddd– Linha:",contLinhas)


def tem_numero(s):
    return any(char.isdigit() for char in s)

############################################## MAIN ############################################
def main(arquivo):
    global listaSaida 
    criaAlfabeto()
    tabelaSimbolos = {'WHILE': 'TK_While', 'IF': 'TK_If', 'INT': 'TK_Int',
    'FLOAT': 'TK_Float', 'STRING': 'TK_String', 'WRITE': 'TK_Write', 'READ': 'TK_Read',
    '(': 'TK_Abre_Parenteses', ')': 'TK_Fecha_Parenteses', '{': 'TK_Abre_Chaves', '}': 'TK_Fecha_Chaves',
    '=': 'TK_Atribui_Valor', '+': 'TK_Soma', '-': 'TK_Subtracao', '*': 'TK_Multiplicacao', '/': 'TK_Divisao', 
    '%': 'TK_Mod', '++': 'TK_Incrementa_Um', '--': 'TK_Decrementa_Um', '==': 'TK_Verifica_Igual', '!=': 'TK_Verifica_Diferente',
    '>': 'TK_Maior', '<': 'TK_Menor', '>=': 'TK_Maior_Igual', '<=': 'TK_Menor_Igual', '\\\\': 'TK_Comentario'} #dictionary
    #criaTabelaSimbolos(tabelaSimbolos)
    tokens_lexema = []

    grafo = Grafo()
    criaAutomato(grafo)
    # variaveis para armazenar os tokens dependo do tipo 
    contFloat = 0 
    contInt = 0
    contString = 0 
    contEntreAspas = 0
    
    # Analise Lexica
    contLinhas = 0
    contColumnas = 0
    lista = []

    # Leitura do arquivo 
    #with open('teste3.maf') as arquivo:
    for linha in arquivo:
            if linha == '\n': continue # desconsidera linhas vazias
            contLinhas += 1

            if "\\" in linha:
                if linha.startswith("\\"): continue
                linha = linha[0:linha.index("\\")]
            try:
                if "\"" in linha:# a função elimina os espaços dentro da cadeia que esta estre aspas antes do
                    linha = entreAspas(linha, contLinhas)# split abaixo para que a cadeia nao fique fragmentada
            except:
                continue
            lexema = linha.split()
            lista = divideLexemas(lexema, contColumnas, tabelaSimbolos)
            
            for w in lista:
                contColumnas+=1
                if(verificaPalavra(grafo, w, estadosFinais)):
                    chave = w.upper()
                    if(chave in tabelaSimbolos and tem_numero(tabelaSimbolos[chave]) == False):
                        tokens_lexema.append(tabelaSimbolos[chave])
                    elif chave in tabelaSimbolos and tem_numero(tabelaSimbolos[chave]):
                        s = ''.join([i for i in tabelaSimbolos[chave] if not i.isdigit()])
                        s = s[:-1]
                        tokens_lexema.append(s)
                    else: 
                        if(w.isdigit()):
                            tabelaSimbolos[w] = "TK_Inteiro_"+str(contInt)
                            tokens_lexema.append("TK_Inteiro")
                            contInt+=1
                        elif(isfloat(w)): 
                            tabelaSimbolos[w] = "TK_Flutuante_"+str(contFloat)
                            tokens_lexema.append("TK_Flutuante") 
                            contFloat+=1
                        elif w[0] == "\"":
                            tabelaSimbolos[w] = "TK_Entre_Aspas_"+str(contEntreAspas)
                            tokens_lexema.append("TK_Entre_Aspas")
                            contEntreAspas += 1
                        else:
                            tabelaSimbolos[chave] = "TK_Identificador_"+str(contString)
                            tokens_lexema.append("TK_Identificador") 
                            contString+=1
                else :
                    print("Erro Automato:") 
                    #tokens_lexema.clear()
                    Erro("Lexico", contLinhas, contColumnas, w)
                    break
                
            #print(tokens_lexema)
            #print(lista)
            Sintatica(tokens_lexema, contLinhas,lista)
            
            print(".....................................................")
            tokens_lexema.clear()
    print(tabelaIdentificadores)
    if contColchetes != 0:
            listaSaida.append("Erro Semantico: Nao foi fechado: {}".format(contColchetes))
            print("Erro Semantico: Nao foi fechado: ",contColchetes, "colchetes")
    #print(tabelaSimbolos)
    print("Numero de linhas do Codigo: {}".format(contLinhas))
    return listaSaida
