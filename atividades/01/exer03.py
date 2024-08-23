def inputPalavras():
    listaNomes = list()
    for i in range(5):
        palavra = input('Digite a palavra: ')
        listaNomes.append(palavra)
    
    listaNomes.sort()
    return ', '.join(listaNomes)

palavras = inputPalavras()

print(palavras)