'''Escriba una función de Python para encontrar el máximo de tres números. '''

def mayor(num1= 0, num2= 0, num3= 0):
    mayor = 0
    if num1 >= num2 and num1 >= num3:
        mayor = num1
    elif num2 >= num1 and num2 >= num3:
        mayor = num2
    else:
        mayor = num3
    return mayor


num1 = float(input('Digite el primer número: '))
num2 = float(input('Digite el segundo número: '))
num3 = float(input('Digite tercer número: '))
print()
mayor = mayor(num1, num2, num3)
print(mayor)
