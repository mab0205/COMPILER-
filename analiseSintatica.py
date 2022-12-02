def verifica_regra(regra,x,cont):
    for iter in regra:
        if x == iter: 
            x = None
            cont += 1
            return True,cont 
    


def hola(): 
    #exemplo de entrada para verificar  
    exe = ["TK_If","TK_Abre_Parenteses","TK_Identificador","TK_Menor","TK_Constante","TK_Fecha_Parenteses","TK_Abre_Chaves"]
    
    whileLexema = ["While_If","TK_Abre_Parenteses","OP","TK_Fecha_Parenteses","TK_Abre_Chaves"]
    OP = ["Operando","LOG","Operando"]
    Operando = ["TK_Constante", "TK_Identificador"]
    LOG = ["TK_Maior_Igual","TK_Verifica_Igual","TK_Verifica_Diferente","TK_Maior","TK_Menor","TK_Menor_Igual"]
    While_If = ["TK_While","TK_If"]
    lista = ["TK_While","TK_If"]
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
                    resp, cont = verifica_regra(While_If,x,cont)
                    print("while_if",resp)
                    print(cont)
                    i+= 1     
                if whileLexema[i] == "OP":        
                    for op in OP:
                        if op ==  "Operando": 
                            for perando in Operando:
                                if x == perando:
                                    print("True Operando")
                                    x = None
                                    cont += 1
                                    break
                        elif op ==  "LOG": 
                            for log in LOG:
                                if x == log:
                                    print("True LOG")
                                    x = None
                                    cont += 1
                                    break
                    
    if cont == tamLexema : print("Regra da lingaugem: True", cont) 
    else: print("Regra da lingaugem: False", cont)


if __name__ == "__main__":
    hola()    