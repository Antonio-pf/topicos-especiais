import os

def limpar_tela():
    os.system('clear')

def ler_numero():
    while True:
        try:
            numero = int(input('Informe um valor: '))
            return numero
        except Exception:
            print("Digite um número!")

def soma(n1, n2):
    return n1 + n2

def exibir_intervalo(ini = 0, fim = 10, passo = 1):
    for item in range(ini, fim, passo):
        print(item)

def main():
    # limpar_tela()
    # print("\033[1;32mTexto verde em negrito\033[0m")

    # n1 = ler_numero()
    # n2 = ler_numero()
    
    # print(soma(n1, n2))
    exibir_intervalo(1,6,2)
    exibir_intervalo(fim = 5, passo =2)

main()