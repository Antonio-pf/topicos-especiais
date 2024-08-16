#  Elabore uma aplicação que receba o nome de um produto
# e o seu valor. 
# O desconto deve ser calculado de acordo
# com o valor fornecido conforme a Tabela.


# <= 50 e < 200 = 5
# >= 200 e < 500 = 6
# >= 500 e < 1000 = 7
# >= 1000 = 8 

# – Apresente em tela o nome do produto, valor original do
# produto e o novo valor depois de ser realizado o desconto.
# Caso o valor digitado seja menor que zero, deve ser
# emitida uma mensagem de aviso.
infoProduto = {}

def setValorProduto():
    valorDigitado = int(input("Valor do produto: "))

    # if not valorDigitado.isdigit():
    #     print("Por favor, digite um número válido!")
    #     setValorProduto()
    # else:
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
