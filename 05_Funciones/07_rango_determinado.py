'''Escriba una función de Python para comprobar si un número cae en un rango determinado.'''
def rango(num):
    rango1 = range(10)
    rango2 = range(10, 100)
    rango3 = range(100, 1000)
    if num in rango1:
        print('El número está entre 0 y 9')
    elif num in rango2:
        print('el número está entre 10 y 99')
    elif num in rango3:
        print('El número está entre 100 y 999')
    else:
        print('El número es mayor o igual a 1000')

num = int(input('Digite un número entero: '))
if num < 0:
    print('El número es menor que cero (0)')
else:
    rango(num)
