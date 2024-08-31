
def mesagemAviso(texto):
    return print(f"\033[1;31m{texto}\033[0m", end='\n')

def qtdNumerosPares(lista):
    count = 0
    for i in lista:
        if i % 2 == 0:
            count += 1
    return count

def percorreLista(lista):
    for i in lista:
        return i
    
def numerosImpares(lista):
    numImpares = []
    for i in lista:
        if i % 2 != 0:
            numImpares.append(i)
    
    return numImpares

def menorNumero(lista):
    
    return min(lista)

def maiorNumero(lista):
    return max(lista)

def media(lista):

    try:
        soma = 0
        for i in lista:
            soma += i
        media = soma / len(lista)

        return round(media, 2)
    except ZeroDivisionError:
        print("Divisão por zero. Digite um novo valor")
    except Exception:
        print("Insira número válidos!")
    

def receber_valores():
    numeros = []
    while True:
        try:
            valor = int(input("Digite um número (ou '000' para sair): "))
            
            if valor == 000:
                break
            numeros.append(valor)
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")
    return numeros
def main():
    numeros = receber_valores()

    qtd_pares = qtdNumerosPares(numeros)
    impares = numerosImpares(numeros)
    menor = menorNumero(numeros)
    maior = maiorNumero(numeros)
    media_aritmetica = media(numeros)

    print(f"Quantidade de números pares: {qtd_pares}")
    print(f"Números ímpares: {impares}")
    print(f"Menor número: {menor}")
    print(f"Maior número: {maior}")
    print(f"Média dos números: {media_aritmetica}")

main()

