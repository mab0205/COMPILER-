def divideLexemas(lexema, contColumnas, tabelaSimbolos):
    for palavra in lexema:
        for letra in palavra:
            #contColumnas+=1

            if letra == "\"":# encontra abre aspas
                fecha_aspas = palavra[palavra.index(letra)+1]
                i = 1
                while fecha_aspas != "\"":# procura fecha aspas
                    if i < len(palavra):
                        fecha_aspas = palavra[palavra.index(letra)+i]
                        i += 1
                if i == len(palavra) and fecha_aspas == "\"": break

            try:
                if (palavra.index(letra) != len(palavra)):
                    prox = palavra[palavra.index(letra)+1]
            except:
                prox = None

            if prox in tabelaSimbolos:
                letra = letra + prox
                        
            if letra in tabelaSimbolos and len(palavra) > len(letra) and not letra.isdigit():
                lista = palavra.split(letra)
                lista.append(letra)
                      
                for s in lista:
                    if s != '':
                        lexema.append(s)
                                
                lista.clear()
                lexema.remove(palavra)
                break
    
    for palavra in lexema: # ajusta o ponto e virgula para o final da lista
        if palavra == ";":
            lexema.append(palavra)
            lexema.remove(palavra)
            break

    return lexema

# essa função elimina os espaços dentro de uma cadeia estre as aspas
def entreAspas(linha, contLinhas):
    indice_aspas = linha.index("\"")
    i = indice_aspas+1
    entre_aspas = "\""
    while linha[i] != "\"":# separa a cadeia que esta entre as aspas
      entre_aspas = entre_aspas + linha[i]
      i += 1
      if i >= len(linha):
        print("Erro na linha {}: Esperado caractere Fecha Aspas", contLinhas)
    entre_aspas = entre_aspas + "\""
    entre_aspas = entre_aspas.replace(" ", '')# elimina os espaços
    linha = linha[0:indice_aspas: ] + entre_aspas + linha[i+1: :]# devolve para a lista original
    return linha