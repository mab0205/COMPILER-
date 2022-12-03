#*********************************FUNCOES AUXILIARES*****************************************************
def casoAtribucao(exe, Lexema, Lexema2, OP):
    i = 0
    cont = 0
    if (len(exe) == 2):
        verificaSimples(exe, Lexema, len(Lexema)) 
    elif(len(exe) == 4):
        for x in exe:
            if x != Lexema2[i]:
                if( verifica_folhas(OP,x)):
                    cont+=1
                    i+=1
                else: break
            elif x == Lexema2[i]:
                cont+=1
                i+=1
            else:
                print("False")
        lexemaCheck(cont,len(Lexema2))
    else :
        print("error sintatica")

def verifica_folhas(regra,x):
    for iter in regra:
        if x == iter: 
            return True

def verificaSimples(exe, lexema, tamLexema):
    cont = 0
    i = 0
    try:
        for x in exe:
            if x == lexema[i]:
                cont+= 1
                i+=1
            else: 
                print("Error False")
                break
    except:
        print("Error Sintatico")
        cont = None
    lexemaCheck(cont,tamLexema)

def som(x,cont):
    x = None
    cont+=1
    return x, cont

def lexemaCheck(cont,tamanho):
     if cont == tamanho : print("Regra: True", cont) 
     else: print("Regra: False", cont)

#*********************************REGRAS*****************************************************

def read(exe):
    readLexema = ["TK_Read","TK_Abre_Parenteses","TK_Identificador","TK_Fecha_Parenteses"]   
    verificaSimples(exe,readLexema, len(readLexema))

def write(exe): 
    writeLexema = ["TK_Write","TK_Abre_Parenteses","P","TK_Fecha_Parenteses"] 
    
    P = ["TK_Identificador","TK_Entre_Aspas"] 
    i = 0
    cont = 0
    if(len(exe)==len(writeLexema)):
        for x in exe:
            if x != writeLexema[i]:
                if( verifica_folhas(P,x) ):
                    cont+=1
                    i+=1
                else: break
            elif x == writeLexema[i]:
                cont+=1
                i+=1
            else:
                print("False")
    lexemaCheck(cont,len(writeLexema))

def comentario(exe):
    comentarioLexema = ["TK_Comentario"]   
    verificaSimples(exe,comentarioLexema, len(comentarioLexema))

def fecharChaves(exe):    
    fechaChaveLexema = ["TK_Fecha_Chaves"]   
    verificaSimples(exe,fechaChaveLexema, len(fechaChaveLexema))

def whileIf(exe): 
    whileLexema = ["While_If","TK_Abre_Parenteses","OP","TK_Fecha_Parenteses","TK_Abre_Chaves"]
    
    OP = ["Operando","LOG","Operando"]
    Operando = ["TK_Inteiro", "TK_Identificador", "TK_Flutuante"]
    LOG = ["TK_Maior_Igual","TK_Verifica_Igual","TK_Verifica_Diferente","TK_Maior","TK_Menor","TK_Menor_Igual"]
    While_If = ["TK_While","TK_If"]

    tamLexema = 7
    i = 0
    
    cont = 0
    if(len(exe) == tamLexema):
        for x in exe: 
                if x == whileLexema[i+1] or x == whileLexema[i]:
                    cont +=1
                    
                    i+=1 
                elif x != whileLexema[i]: 
                    #print(x)
                    #print(whileLexema[i])
                    if whileLexema[i] == "While_If":
                        resp = verifica_folhas(While_If,x)
                        
                        x , cont = som(x,cont)                  
                        i+= 1     
                    if whileLexema[i] == "OP":        
                        for op in OP:
                            if op ==  "Operando": 
                                if (verifica_folhas(Operando,x)):
                                    
                                    x , cont = som(x,cont)
                                    break
                            elif op ==  "LOG": 
                                if (verifica_folhas(LOG,x)):
                                    
                                    x , cont = som(x,cont)
                                    break
    lexemaCheck(cont,tamLexema)

def operacaoIdentificador2(exe): 
    identificadorLexema2 = ["TK_Identificador","M"]
    
    M = ["TK_Incrementa_Um","TK_Decrementa_Um"]
    i = 0
    cont = 0
    if(len(exe)==len(identificadorLexema2)):
        for x in exe:
            if x != identificadorLexema2[i]:
                if( verifica_folhas(M,x)):
                    cont+=1
                    i+=1
                else: break
            elif x == identificadorLexema2[i]:
                cont+=1
                i+=1
            else:
                print("False")
    lexemaCheck(cont,len(identificadorLexema2))

def operacaoIdentificador3(exe): 
    identificadorLexema3 = ["TK_Identificador","TK_Atribui_Valor","M"]
    
    M = ["TK_Flutuante","TK_Inteiro","TK_Identificador"]
    i = 0
    cont = 0
    if(len(exe)==len(identificadorLexema3)):
        for x in exe:
            if x != identificadorLexema3[i]:
                if( verifica_folhas(M,x)):
                    cont+=1
                    i+=1
                else: break
            elif x == identificadorLexema3[i]:
                cont+=1
                i+=1
            else:
                print("False")
    lexemaCheck(cont,len(identificadorLexema3))

def operacaoIdentificador5(exe): 
    identLexema5 = ["TK_Identificador","TK_Atribui_Valor","OP"]
    
    OP = ["Operando","SIMMAT","Operando2"]
    Operando = ["TK_Flutuante", "TK_Inteiro","TK_Identificador"]
    Operando2 = ["TK_Flutuante", "TK_Inteiro","TK_Identificador"]
    SIMMAT = ["TK_Soma","TK_Subtracao","TK_Multiplicacao","TK_Mod","TK_Divisao"]

    tamLexema = 5
    i = 0
    
    cont = 0
    if(len(exe) == tamLexema):
        for x in exe: 
                if x == identLexema5[i]:
                    cont +=1
                    i+=1 
                elif x != identLexema5[i]: 
                    #print(x)
                    #print(whileLexema[i])
                    if identLexema5[i] == "OP":        
                        for op in OP:
                            if op ==  "Operando": 
                                if (verifica_folhas(Operando,x)):
                                    
                                    x , cont = som(x,cont)
                                    break
                            if op ==  "Operando2": 
                                if (verifica_folhas(Operando2,x)):
                                    
                                    x , cont = som(x,cont)
                                    break    
                            elif op ==  "SIMMAT": 
                                if (verifica_folhas(SIMMAT,x)):
                                    
                                    x , cont = som(x,cont)
                                    break
    lexemaCheck(cont,tamLexema)

def atribuiInt(exe):
    intLexema = ["TK_Int","TK_Identificador"]
    intLexema2 = ["TK_Int","TK_Identificador","TK_Atribui_Valor","OP"]
    
    OP =  ["TK_Inteiro","TK_Identificador"]

    casoAtribucao(exe, intLexema, intLexema2, OP)

def atribuiFloat(exe):
    floatLexema = ["TK_Float","TK_Identificador"]
    floatLexema2 = ["TK_Float","TK_Identificador","TK_Atribui_Valor","OP"]
    
    OP =  ["TK_Flutuante","TK_Identificador"]

    casoAtribucao(exe, floatLexema, floatLexema2, OP)

def atribuiString(exe):
    stringLexema = ["TK_String","TK_Identificador"]
    stringLexema2 = ["TK_String","TK_Identificador","TK_Atribui_Valor","OP"]
    
    OP =  ["TK_Entre_Aspas","TK_Identificador"]

    casoAtribucao(exe, stringLexema, stringLexema2, OP)

