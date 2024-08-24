def validarSenha(senha):

    if len(senha) < 6 and len(senha) <= 12:
        return False    
    
    letraMaiuscula = any(letra.isupper() for letra in senha)
    letraMinuscula = any(letra.islower() for letra in senha)
    simbolos = any(letra.isalpha() for letra in senha)
    numeros = any(letra.isdigit() for letra in senha)

    
    if letraMaiuscula and letraMinuscula and simbolos and numeros:
        return True
    
    return False
    

valida = validarSenha('1232@44aaA6')

print(valida)