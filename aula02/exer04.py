def centuryFromYear(ano):
    if(len(ano) == 4):
        print(ano[:2])
    else:
        print(ano[0])

ano = input('Digite o ano: ')
centuryFromYear(ano)