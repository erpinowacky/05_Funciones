'''Escriba una función de Python para sumar todos los números de una lista. Lista de muestras:
(8, 2, 3, 0, 7)Resultado esperado: 20.'''

def sumaLista(numList):
    suma = 0
    for i in numList:
        suma += i
    return suma

numList = [8, 2, 3, 0, 7]
suma = sumaLista(numList)
print(suma)
