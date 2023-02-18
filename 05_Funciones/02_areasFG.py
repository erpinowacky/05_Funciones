'''Escriba un programa para calcular las áreas de las figuras geométricas utilizando 
una función para cada área.'''

def cuadrado(lado= 0):
    area = lado * lado
    return area

def rectangulo(base= 0, altura= 0):
    area = base * altura
    return area

def triangulo(base= 0, altura= 0):
    DIVISOR = 2
    area = (base * altura) / DIVISOR
    return area

def circulo(radio= 0):
    PI = 3.1416
    area = PI * radio**2
    return area

def rombo(diagMayor= 0, diagMenor= 0):
    DIVISOR = 2
    area = (diagMayor * diagMenor) / DIVISOR
    return area

def trapecio(baseMayor= 0, baseMenor= 0, altura= 0):
    DIVISOR = 2
    area = ((baseMayor * baseMenor) / DIVISOR) * altura
    return area


radio = 0.0
baseMayor = 0.0
baseMenor = 0.0
diagMayor = 0.0
diagMenor = 0.0
base = 0.0
altura = 0.0
lado = 0.0
area = 0.0
opcion = ''

print('***ÁREAS***')
print('****************************')
print()
MENU = '''***MENÚ ÁREAS***
1. Cuádrado
2. Rectángulo
3. Triángulo
4. Círculo
5. Rombo
6. Trapecio
7. Fin'''
while True:
    print(MENU)
    opcion = input('Elegir una opción: ')
    if (opcion not in '123456') and opcion != '7':
        print('Número no válido')
        continue
    elif opcion == '7':
        print('Adiós')
        exit()
    else:
        if opcion == '1':
            print('***CUÁDRADO***')
            lado = float(input('Digite la base del triángulo: '))
            area = cuadrado(lado)
            print(f'El área del cuádrado es: {area}')
        elif opcion == '2':
            print('***RECTÁNGULO***')
            base = float(input('Digite la base del rectángulo: '))
            altura = float(input('Digite la altura del rectángulo: '))
            area = rectangulo(base, altura)
            print(f'El área del rectángulo es: {area}')
        elif opcion == '3':
            print('***TRIÁNGULO***')
            base = float(input('Digite la base del triángulo: '))
            altura = float(input('Digite la altura del triángulo: '))
            area = triangulo(base, altura)
            print(f'El área del triángulo es: {area}')
        elif opcion == '4':
            print('***CÍRCULO***')
            radio = float(input('Digite el radio del círculo: '))
            area = circulo(radio)
            print(f'El área del círculo es: {area}')
        elif opcion == '5':
            print('***ROMBO***')
            diagMayor = float(input('Digite la medida del diagonal mayor: '))
            diagMenor = float(input('Digite la medida del diagonal menor: '))
            area = rombo(diagMayor, diagMenor)
            print(f'El área del rombo es: {area}')
        else:
            print('***TRAPECIO***')
            baseMayor = float(input('Digite la base mayor: '))
            baseMenor = float(input('Digite la base menor: '))
            altura = float(input('Digite la altura: '))
            area = trapecio(baseMayor, baseMenor, altura)
            print(f'El área del trapecio es: {area}')