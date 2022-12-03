def verifica_folhas(regra,x):
    for iter in regra:
        if x == iter: 
            return True


def verificaSimples(exe,lexema, tamLexema):
    cont = 0
    i = 0
    try:
        for x in exe:
            if x == lexema[i]:
                print("True")
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
     if cont == tamanho : print("Regra da lingaugem: True", cont) 
     else: print("Regra da lingaugem: False", cont)

def whileIf(): 
    #exemplo de entrada para verificar  
    exe = ["TK_If","TK_Abre_Parenteses","TK_Identificador","TK_Menor","TK_Constante","TK_Fecha_Parenteses","TK_Abre_Chaves"]
    
    whileLexema = ["While_If","TK_Abre_Parenteses","OP","TK_Fecha_Parenteses","TK_Abre_Chaves"]
    OP = ["Operando","LOG","Operando"]
    Operando = ["TK_Constante", "TK_Identificador"]
    LOG = ["TK_Maior_Igual","TK_Verifica_Igual","TK_Verifica_Diferente","TK_Maior","TK_Menor","TK_Menor_Igual"]
    While_If = ["TK_While","TK_If"]

    tamLexema = 7
    i = 0
    
    print("-----------------------------------------------------")
    cont = 0
    for x in exe: 
            if x == whileLexema[i+1] or x == whileLexema[i]:
                cont +=1
                print("True condition")
                i+=1 
            elif x != whileLexema[i]: 
                #print(x)
                #print(whileLexema[i])
                if whileLexema[i] == "While_If":
                    resp = verifica_folhas(While_If,x)
                    print("while_if",resp)
                    x , cont = som(x,cont)                  
                    i+= 1     
                if whileLexema[i] == "OP":        
                    for op in OP:
                        if op ==  "Operando": 
                           if (verifica_folhas(Operando,x) == True):
                                print("Operando",True)
                                x , cont = som(x,cont)
                                break
                        elif op ==  "LOG": 
                             if (verifica_folhas(LOG,x) == True):
                                print("LOG",True)
                                x , cont = som(x,cont)
                                break
    lexemaCheck(cont,tamLexema)




def read():
    #exemplo de entrada para verificar  
    exe = ["TK_Read","TK_Abre_Parenteses","TK_Identificador","TK_Fecha_Parenteses"]
   
    readLexema = ["TK_Read","TK_Abre_Parenteses","TK_Identificador","TK_Fecha_Parenteses"]   
    verificaSimples(exe,readLexema, len(readLexema))


def comentario():
    exe = ["TK_Comentario"]
   
    comentarioLexema = ["TK_Comentario"]   
    verificaSimples(exe,comentarioLexema, len(comentarioLexema))


def fecharChaves():    
    exe = ["TK_Fecha_Chaves"]
   
    fechaChaveLexema = ["TK_Fecha_Chaves"]   
    verificaSimples(exe,fechaChaveLexema, len(fechaChaveLexema))


#####################################################################
def definicaoVariavel():
    exe = ["TK_String","TK_Identificador","TK_Identificador","TK_Atribui_Valor","TK_Aspa","TK_Constante","TK_Aspa"]
    
    lexemaVariavel = ["TV","VA"]
    TV = ["TK_Inteiro", "TK_Flutuante" , "TK_Char"]
    VA = ["Variavel", "OP" ]
    OP = ["Variavel","TK_Virgula","Variáveis_Apresentadas"]
    Variavel = ["TK_Identificador", "J"]
    J = ["TK_Identificador","TK_Atribui_Valor","VV"]
    VV = ["TK_Constante" , "X"] 
    X = ["TK_AspaTK_Constante","TK_Aspa"]

    #for x in exe:


def write():
    #exemplo de entrada para verificar  
    exe = ["TK_If","TK_Abre_Parenteses","TK_Identificador","TK_Menor","TK_Constante","TK_Fecha_Parenteses","TK_Abre_Chaves"]



def atribucaoIdentificador():
   #exemplo de entrada para verificar  
    exe = ["TK_If","TK_Abre_Parenteses","TK_Identificador","TK_Menor","TK_Constante","TK_Fecha_Parenteses","TK_Abre_Chaves"]
    
    whileLexema = ["While_If","TK_Abre_Parenteses","OP","TK_Fecha_Parenteses","TK_Abre_Chaves"]
    OP = ["Operando","LOG","Operando"]
    Operando = ["TK_Constante", "TK_Identificador"]
    LOG = ["TK_Maior_Igual","TK_Verifica_Igual","TK_Verifica_Diferente","TK_Maior","TK_Menor","TK_Menor_Igual"]
    While_If = ["TK_While","TK_If"] 


if __name__ == "__main__":
    read() 
    whileIf() 
    comentario()
    fecharChaves()