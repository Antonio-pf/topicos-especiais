import os

def limpar_tela():
    os.system('clear')

def mesagemAviso(texto):
    return print(f"\033[1;31m{texto}\033[0m", end='\n')

def ler_numeros():
    while True:
        try:
            altura = float(input('Informe um sua altura em metros: '))
            peso = float(input('Digite sua massa em KG: '))
            
            imc = calculaIMC(peso, altura)
            if imc is None:
                break
            classificaIMC(imc)
            break  
        except ValueError:
            mesagemAviso("Digite um número válido!")

def calculaIMC(peso, altura):
    try:
        return peso / (altura ** 2)

    except ZeroDivisionError:
        mesagemAviso("Insira valores diferentes de 0 para divisão!")

def classificaIMC(calculoIMC):
    match calculoIMC:
        case calculoIMC if calculoIMC < 18.5:
            print("\033[1;33mAbaixo do peso\033[0m")
            print_imc(calculoIMC)
        case calculoIMC if 18.5 <= calculoIMC < 25:
            print("\033[1;32mPeso normal\033[0m")
            print_imc(calculoIMC)
        case calculoIMC if 25 <= calculoIMC < 30:
            print("\033[1;33mSobrepeso\033[0m")
            print_imc(calculoIMC)
        case calculoIMC if calculoIMC >= 30:
            print("\033[1;35mObesidade\033[0m")
            print_imc(calculoIMC)

def print_imc(imc):
    print(f"\033[1;33mIMC: {imc:.2f} kg/m²\033[0m") 
def main():
    limpar_tela()
    print("\033[1;32mCálculo de IMC\033[0m")
    ler_numeros()


main()