'''Escriba una función de Python para calcular el factorial de un número (un entero no negativo).
La función acepta el número como argumento.'''

def factorial(num: int):
    factorial = 1
    while num:
        factorial = factorial * num
        num -= 1
    return factorial

while True:
    num = int(input('Digite un número entero mayor que cero: '))
    print(num)
    print()
    if num < 0:
        print('Número inválido. Intentelo nuevamente')
        continue
    elif num == 0:
        factorial = 0
        break
    else:
        factorial = factorial(num)
        break
print(factorial)