
def receberQuantidadeValor():
    try:
        quantidadeNumeros = int(input('Digite a quantidade de números: '))
        return quantidadeNumeros

    except ValueError:
        print('O valor informado não é um número')
        return receberQuantidadeValor()
    
def armazenarValores(tamanhoCollection):
    lista = []
    for i in range(tamanhoCollection):
        valor = int(input(f'Digite o {i + 1}: '))
        lista.append(str(valor))
    
    tupla = tuple(lista)

    return lista, tupla

quantidade = receberQuantidadeValor()
lista, tupla = armazenarValores(quantidade)

print(lista)
print(tupla)