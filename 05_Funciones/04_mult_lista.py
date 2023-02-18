'''Escriba una función de Python para multiplicar todos los números de una lista. Lista de muestra:
(8, 2, 3, -1, 7)Resultado esperado: -336'''

def multLista(numList):
    multiplicacion = 1
    for i in numList:
        multiplicacion *= i
    return multiplicacion


numList = [8, 2, 3, -1, 7]
multiplicacion = multLista(numList)
print(multiplicacion)
