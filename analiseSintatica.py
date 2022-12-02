def verifica_folhas(regra,x):
    for iter in regra:
        if x == iter: 
            return True

def som(x,cont):
    x = None
    cont+=1
    return x, cont

def hola(): 
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
                             
    if cont == tamLexema : print("Regra da lingaugem: True", cont) 
    else: print("Regra da lingaugem: False", cont)


if __name__ == "__main__":
    hola()    