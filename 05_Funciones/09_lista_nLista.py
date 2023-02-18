'''Escriba una función de Python que tome una lista y devuelva una nueva lista con elementos 
únicos de la primera lista. '''

def itemsUnicos(lista):
    contador = 0
    newList = []
    for i in lista:
        contador = lista.count(i)
        if contador == 1:
            newList.append(i)
    return newList


cNum = 0
num = 0.0
lista = []

print('*****CREAR LISTA Y AGREGAR NÚMEROS A LA LISTA*****')
cNum = int(input('Digite cantidad de números en la lista: '))
for i in range(cNum):
    num = float(input('Digite los números que quiere guardar en la lista: '))
    lista.append(num)

print('*****LISTA*****')
print(lista)
print()

newList = itemsUnicos(lista)
print('*****NUEVA LISTA*****')
print(newList)

