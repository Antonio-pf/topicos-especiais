
valor = int(input("Resistência 0: "))
maior = valor
menor = valor

for i in range(1, 4):
    valor = int(input("Resistência {i}: ".format(i=i)))
    if valor > maior:
        maior = valor

    if valor < menor:
        menor = valor


print(f"A Maior resistência: {maior}")
print(f"A Menor resistência: {menor}")
