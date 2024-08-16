
infoProduto = {}

def setValorProduto():
    valorDigitado = int(input("Valor do produto: "))
    if valorDigitado <= 0:
        print("Digite um valor maior que zero!")
        setValorProduto()
    else:
        infoProduto['valor'] = valorDigitado
        setDesconto(valorDigitado)

def setInfoProduto():
    infoProduto['nome'] = input("Nome do produto: ")
    setValorProduto()

def setDesconto(valorProduto):

    if valorProduto <= 50 and valorProduto < 200:
        infoProduto['desconto'] = 0.05 * infoProduto['valor'] + infoProduto['valor']
    elif valorProduto >= 200 and valorProduto < 500:
        infoProduto['desconto'] = 0.06 * infoProduto['valor'] + infoProduto['valor']
    elif valorProduto >= 500 and valorProduto < 1000:
        infoProduto['desconto'] = 0.07 * infoProduto['valor'] + infoProduto['valor']
    elif valorProduto >= 1000:
        infoProduto['desconto'] = 0.08 * infoProduto['valor'] + infoProduto['valor']


setInfoProduto()

print(infoProduto)
