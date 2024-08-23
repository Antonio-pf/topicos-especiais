import string

def calcularLetrasEDigitos(sequencia):
    countNums  = len([num for num in sequencia if num.isdigit()])
    countLetras = len([letra for letra in sequencia if letra.isalpha()])
    
    return countNums, countLetras
    
resultado = (calcularLetrasEDigitos('hello world! 123'))

print("Letras ", resultado[0])
print("Digitos ", resultado[1])

