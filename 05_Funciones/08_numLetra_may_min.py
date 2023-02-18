'''Escriba una función de Python que acepte una cadena y calcule el número de letras mayúsculas y minúsculas.'''

def canLetrasM_m_o(cadena):
    mayusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    minusculas = 'abcdefghijklmnopqrstuvwxyz'
    i = 0
    tamaño = len(cadena)
    mayu = 0
    minu = 0
    otros = 0
    while i < tamaño:
        letra = cadena[i]
        if letra in mayusculas:
            mayu += 1
        elif letra in minusculas:
            minu += 1
        else:
            otros += 1
        i += 1        
    return mayu, minu, otros

cadena = 'ertTRESerdTR123%&4RTd#4' 
listaValores = canLetrasM_m_o(cadena)
mayu, minu, otros = listaValores
print(f'Número de caracteres en mayúsculas: {mayu}')
print(f'Número de caracteres en minúsculas: {minu}')
print(f'Número de otros caracteres: {otros}')
