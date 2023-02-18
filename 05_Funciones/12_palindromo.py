'''Escriba una función de Python que compruebe si una cadena pasada es palíndromo o no.
Una palabra o frase que es palíndromo se lee igual de izquierda a derecha que de derecha a izquierda.
Por ejemplo: Ana, Anita lava la tina. '''

def palindromo(cadena):
    resultado = False
    nCadena = cadena[::-1]
    listaC = cadena.split()
    listaN = nCadena.split()
    if ''.join(listaC) == ''.join(listaN):
        resultado = True
    return resultado


cadena = input('Digite la palabra o frase: ')
resultado = palindromo(cadena)
if resultado == True:
    print('La frase o cadena es un palíndromo')
else:
    print('La frase o cadena no es un palíndromo')
