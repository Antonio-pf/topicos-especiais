def receberIeJ():
    i = int(input('Digite i: '))
    j = int(input('Digite j: '))
    return i,j

## valores gerados pelos valores das colunas
def gerarArray2D(i,j):
    array2D = []

    for linha in range(i):
        nova_linha = []
        for coluna in range(j):
            nova_linha.append(linha * coluna)
            print(nova_linha)
        array2D.append(nova_linha)
            
    return array2D, nova_linha


i, j = receberIeJ()
resultado, nova_linha = gerarArray2D(i, j)

print(resultado)
