'''Escriba un programa Python para imprimir los números pares de una lista determinada.'''

def pares(lista):
    listaP = []
    for i in lista:
        if i % 2 == 0:
            print(i)
            listaP.append(i)
    return listaP


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

print('Lista con los números pares:\n', pares(lista))