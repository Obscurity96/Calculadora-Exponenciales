# Actividad Calculadora de exponenciales 

import math

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: división por cero"

def potencia(base, exponente):
    return base ** exponente

def raiz_cuadrada(numero):
    if numero >= 0:
        return math.sqrt(numero)
    else:
        return "Error: raíz cuadrada de un número negativo"

def calculadora():
    print("Bienvenido a la calculadora con funciones exponenciales")
    print("Seleccione la operación que desea realizar:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    print("6. Raíz cuadrada")

    opcion = input("Ingrese el número de la operación deseada (1/2/3/4/5/6): ")

    if opcion in ['1', '2', '3', '4']:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
    elif opcion == '5':
        num1 = float(input("Ingrese la base: "))
        num2 = float(input("Ingrese el exponente: "))
    elif opcion == '6':
        num1 = float(input("Ingrese el número para calcular la raíz cuadrada: "))

    if opcion == '1':
        print("El resultado de la suma es:", suma(num1, num2))
    elif opcion == '2':
        print("El resultado de la resta es:", resta(num1, num2))
    elif opcion == '3':
        print("El resultado de la multiplicación es:", multiplicacion(num1, num2))
    elif opcion == '4':
        print("El resultado de la división es:", division(num1, num2))
    elif opcion == '5':
        print("El resultado de la potencia es:", potencia(num1, num2))
    elif opcion == '6':
        print("La raíz cuadrada es:", raiz_cuadrada(num1))
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")

# Ejecutar la calculadora
calculadora()
