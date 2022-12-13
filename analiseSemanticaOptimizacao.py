import numpy as np
from Grafo import isfloat
from main2 import tabelaIdentificadores,listaSaida

def insereVariavel(nome,tipo,escopo,linha,valor):
    global tabelaIdentificadores
    global listaSaida
    if (valor != None and verificaVariavel(valor) == False and tipo != "String"):
         listaSaida.append("Erro Semantico: variavel nao declarada: {}".format(valor))
         return print("Erro Semantico: variavel nao declarada: ",valor) 
    elif nome in tabelaIdentificadores:
        listaSaida.append("Erro Semantico: Duas vezes declarada a variavel: {} na linha: {}".format(nome,linha))
        return print("Erro Semantico: Duas vezes declarada a variavel: "+nome+" na linha: ",linha)
    
    tabelaIdentificadores[nome] = [tipo,atribuicaoVariavel(nome,valor,tipo), escopo, linha]
    return True 

def verificaVariavel(x):
    global tabelaIdentificadores
    if((x.isdigit() or isfloat(x) or (x in tabelaIdentificadores)) == False):
        return False 
    else:
        return True

def conversaoString(num):
    ch = '"'
    num = num.rstrip(ch)
    num = num[1:]
    num = ''.join([r'%x'%ord(c) for c in num])
    num = int(num,16)
    return num

def atribuicaoVariavel(nome,x,tipo):
    if (x in tabelaIdentificadores and tabelaIdentificadores[x][0] == tipo):
        return tabelaIdentificadores[x][1]
    else:
        try:
            if(( x in tabelaIdentificadores) and (tabelaIdentificadores[x][0] != tipo)):
                if(tipo == "Inteiro" ):
                    num = tabelaIdentificadores[x][1]
                    if (num.isdigit() or isfloat(num)) : return num
                    listaSaida.append(" Warning: Tipos incompativeis foi assinado a Inteiro {}".format(x))
                    return conversaoString(num)
                elif(tipo == "Float"):
                    num = tabelaIdentificadores[x][1]
                    if (num.isdigit() or isfloat(num)) : return num 
                    listaSaida.append("Warning: Tipos incompativeis foi assinado a Float {}".format(x))
                    return conversaoString(num)
                elif(tipo == "String"):
                    num = tabelaIdentificadores[x][1]
                    listaSaida.append("Warning: Tipos incompativeis foi assinado a String {}".format(x))
                    return str(num) 
            else :
                return x 
        except: 
            return None


def operacaoMat(x,y,simbolo):
    print(simbolo)
    #soma
    if(simbolo == "+"):
        return( x + y)
    #subtracao
    elif(simbolo == "-"):
        return (x - y)
    #multiplicacao
    elif(simbolo == "*"):
        return (x * y)
    #divisao
    elif (simbolo == "/"):
        try:
            return (x / y)
        except:
            listaSaida.append("Erro Semantico: incopativel tipo de divisao: {} e {}".format(x , y))
            return None
    else : return None 

def verificaTipo(x,y):
    if(tabelaIdentificadores[x][0] == "Inteiro" and y.isdigit()):
        return True
    elif(tabelaIdentificadores[x][0] == "Float" and isfloat(y)):
        return True
    elif(tabelaIdentificadores[x][0] == "String" and str(y)):
        return True
    elif ((y in tabelaIdentificadores)):
        if(tabelaIdentificadores[x][0] == tabelaIdentificadores[y][0]):
            return True
    else : return False 

def verificaWhileIf(x,y):
    if(tabelaIdentificadores[x][0] == "Inteiro" and y.isdigit()):
        return True
    elif(tabelaIdentificadores[x][0] == "Float" and isfloat(y)):
        return True
    elif(tabelaIdentificadores[x][0] == "String" and str(y)):
        return False
    elif ((y in tabelaIdentificadores)):
        if(tabelaIdentificadores[x][0] == tabelaIdentificadores[y][0]):
            return True
    else : return False

def erroSemantico(linha):
    global listaSaida 
    listaSaida.append("Erro Semantico: variavel na linha: {}".format(linha))
    return print("Erro Semantico: variavel na linha: ",linha)
