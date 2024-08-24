def qtdMaiusculasEMinusculas(sequencia):
    qtdMinuscula, qtdMaiusculas = 0, 0
    for letra in sequencia:

        if not letra.isalpha(): continue

        if letra.islower():
            qtdMinuscula += 1
            continue
        
        qtdMaiusculas += 1
        
    return qtdMaiusculas, qtdMinuscula


resultado = qtdMaiusculasEMinusculas('Hello world!')
print('Maiúsculas ', resultado[0])
print('Minúsculas ',resultado[1])