'''Escriba un programa Python para invertir una cadena. Cadena de ejemplo:
"1234abcd" Resultado esperado: "dcba4321"'''

def invertirCadena(cadena):
    nCadena = ''
    for i in cadena[ ::-1]:
        nCadena += i 
    return nCadena 

cadena = "1234abcd"
nCadena = invertirCadena(cadena)
print(nCadena)
