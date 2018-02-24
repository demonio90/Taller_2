#Menu
def menu():
    print("\nMenu:\n"
        "1. Binarios.\n"
        "2: Octales.\n"
        "3. Salir.\n")

    opcion = int(input('Ingrese la opcion deseada...\n'))

    if opcion == 1:
        binarios()
    if opcion == 2:
        octal()
    if opcion == 3:
        print('\nHasta pronto.')
        exit()

#Funcion principal de binarios
def binarios():
    binarioUno = input('\nIngrese el primer número binario:\n')
    binarioDos = input('\nIngrese el segundo número binario:\n')
    if binarioUno == '' or binarioDos == '':
        print('Lo sentimos, estos campos son obligatorios.')
        main()

    num1 = conversionBinaria(binarioUno)
    num2 = conversionBinaria(binarioDos)
    sumar = suma(num1, num2)
    restar = resta(num1, num2)
    multiplicar = multiplicacion(num1, num2)
    dividir = division(num1, num2)

    print("\nLa suma de " + binarioUno + " mas " + binarioDos + " es " + conversionEntero(sumar))
    print("La resta de " + binarioUno + " menos " + binarioDos + " es " + conversionEntero(restar))
    print("La multiplicación de " + binarioUno + " por " + binarioDos + " es " + conversionEntero(multiplicar))
    print("La división de " + binarioUno + " entre " + binarioDos + " es " + conversionEntero(dividir))
    menu()

#Funcion que convierte un valor dado a numero entero
def conversionBinaria(numBinario):
        longitud = len(numBinario) - 1
        numEntero = 0
        for c in numBinario:
            potencia = 2 ** longitud
            numEntero = numEntero + (int(c) * potencia)
            longitud = longitud - 1
        return numEntero

#Funcion que convierte un numero entero a numero binario
def conversionEntero(numEntero):
        numBinario = ""
        while (True):
                auxiliar = str(numEntero % 2)
                numEntero = int(numEntero / 2)
                numBinario = auxiliar + numBinario
                
                if (numEntero <= 1):
                        numBinario = (str(numEntero) if numEntero > 0 else "") + numBinario
                        break
        
        return numBinario

#Funcion que suma los numeros binarios
def suma(num1, num2):
	resultado = num1 + num2
	return resultado

#Funcion que resta los numeros binarios
def resta(num1, num2):
	resultado = num1 - num2
	return resultado

#Funcion que multiplica los numeros binarios
def multiplicacion(num1, num2):
	resultado = num1 * num2
	return resultado

#Funcion que divide los numeros binarios
def division(num1, num2):
	resultado = num1 / num2
	return resultado

#Funcion principal octal
def octal():
    octalUno = input('\nIngrese el primer número.\n')
    octalDos = input('\nIngrese el segundo número.\n')

    if octalUno == '' or octalDos == '':
        print('Lo sentimos, estos campos son obligatorios.')
        main()

    num1 = validarNumeros(octalUno)
    num2 = validarNumeros(octalDos)

    sumar(num1, num2)

def sumar(num1, num2):
    val1 = num1
    val2 = num2
    d = [''] * len(val1)
    h = [''] * len(val1)

    diferencia = 0
    carrete = 0

    for c in reversed(range(len(val1))):
        a = int(val1[c]) + int(val2[c]) + carrete

        if a >= 8:
            diferencia = a - 8
            carrete = 1
            a = diferencia
        else:
            diferencia = 0
            carrete = 0

        d[(len(val1) - 1) - c] = a

        #INVIERTE EL RESULTADO
        a = d[(len(val1) - 1) - c]
        h[c] = a

    print(h)

#Validacion de numeros
def validarNumeros(octal):
    cifra = octal

    for i in octal:
        if int(i) >= 8:
            print('\nLo sentimos, solo se permiten numeros menores a 8')
            main()

    return cifra

#Funcion principal main
def main():
    menu()

#Llamada a la funcion principal main
main()