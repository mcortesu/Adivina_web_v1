

'''
Esta función recibe una cadena y devuelve True si es un entero y False si no lo es
'''
def isEntero(texto):
    try:
        int(texto)
        return True
    except:
        return False

'''
Esta función recibe el límite inferior y superior y comprueba que son números y si el límite inferior es 
menor que el límite superior
'''
def datosCorrectosEntrada(menor,mayor):
    if isEntero(menor) and isEntero(mayor):
        if int(menor) < int(mayor):
            return True
    return False

'''
Esta función recibe la apuesta y comprueba que es un número y si está entre límite inferior y límite superior
'''
def datosCorrectosJuego(valor, minimo, maximo):
    if isEntero(valor) and int(minimo) <= int(valor) <= int(maximo):
        return True
    return False
