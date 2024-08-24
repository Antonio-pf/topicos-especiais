from datetime import datetime

dataAtual = datetime.now()

meses = [
    "janeiro", "fevereiro", "março", "abril", "maio", "junho",
    "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
]

dataFormatada = dataAtual.strftime("%d/%m/%Y")

data_extenso = f"{dataAtual.day} de {meses[dataAtual.month - 1]} de {dataAtual.year}"

print("Data atual:", dataAtual)
print("Ano atual:", dataAtual.year)
print("Mês atual:", dataAtual.month)
print("Dia atual:", dataAtual.day)
print("Data atual formatada (dia/mês/ano):", dataFormatada)
print("Por extenso:", data_extenso)
