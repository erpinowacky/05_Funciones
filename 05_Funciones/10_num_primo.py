'''Escriba una función de Python que tome un número como parámetro y verifique que el número sea primo o no.
Un número primo (o primo) es un número natural mayor que 1 y que no tiene divisores positivos aparte de 1 y
sí mismo.'''

def primo(num):
    resultado = False
    if num == 1:
        resultado = True
    elif num > 1:
        divisor = 2
        while True:
            if num % divisor == 0:
                if num == divisor:
                    resultado = True
                    break
                else:
                    break
            else:
                divisor += 1
    else:
        return
    return resultado

    


num = int(input('Digite un número entero: '))
resultado = primo(num)
if resultado == True:
    print('El número es primo.')
elif resultado == None:
    print('El valor ingresado es menor o igual a cero.')
else:
    print('El número no es primo.')