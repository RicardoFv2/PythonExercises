# 1. Desarrolle un programa que solicite al usuario ingresar dos números. Luego, declare una función
# para dividir el primer número entre el segundo número y muestra el resultado. Si el segundo
# número es cero, maneja el error de división por cero y muestra un mensaje adecuado.

# try:
#     numero1 = int(input("Ingrese el numero 1: "))
#     numero2 = int(input("Ingrese el numero 2: "))

#     def dividir_numeros(num1, num2):
#         return (numero1 / numero2)

#     print(f"El resultado de la división entre {numero1} y {numero2} es: {dividir_numeros(numero1,numero2)}")
# except ValueError:
#     print("Ingrese un numero valido, no se aceptan caracteres")
  
# except ZeroDivisionError:
#     print("No se puede dividir entre 0")

# 2. Escribir un programa que solicite al usuario ingresar una lista de números separados por espacios.
# Luego, calcula la suma de todos los elementos de la lista y muestra el resultado. Asegúrate de
# manejar cualquier posible error si el usuario ingresa elementos no numéricos.

# def obtener_lista_numeros():

#     entrada = input("Ingresa una lista de números separados por espacios: ")

#     numeros_como_cadenas = entrada.split()
    
#     numeros = []
#     for numero in numeros_como_cadenas:
#         try:
#             numero_entero = int(numero)
#             numeros.append(numero_entero)
#         except ValueError:
#             print(f"El valor '{numero}' no es un número válido y será ignorado.")

#     return numeros

# def calcular_suma(lista_numeros):
#     suma = 0
#     for numero in lista_numeros:
#         suma += numero
#     return suma

# lista_numeros = obtener_lista_numeros()

# try:
#     suma = calcular_suma(lista_numeros)
#     print("La suma de los números es:", suma)
# except TypeError:
#     print("Error: La lista contiene elementos no numéricos.")
    
#     3. Dada una lista de coordenadas (tuplas) en dos dimensiones, calcula el producto de las
# coordenadas y almacena los resultados en una nueva lista. Por ejemplo, si la lista es [(2, 3), (4, 5), (1, 6)], la lista resultante debería ser [6 20, 6]. Asegúrate de manejar cualquier error que pueda surgir si alguna de las coordenadas no es una tupla de dos elementos.

# def calcular_producto_coordenadas(coordenadas):
#     resultados = []
#     for coordenada in coordenadas:
#         if isinstance(coordenada, tuple) and len(coordenada) == 2:
#             resultado = coordenada[0] * coordenada[1]
#             resultados.append(resultado)
#         else:
#             print(f"La coordenada {coordenada} no es una tupla de dos elementos y será ignorada.")
#     return resultados

# datos_tupla = [(2, 3), (4, 5), (1, 6)]

# resultado_producto = calcular_producto_coordenadas(datos_tupla)

# print("El producto de las coordenadas es:", resultado_producto)

# 4. Tomando como base el ejercicio complementario n° 1, implemente excepciones para evitar el ingreso de valores negativos datos no válidos.

# 5. Desarrolle un programa que contendrá una función llamada calcular_area_circulo que tome el radio de un círculo como argumento y calcule el área del círculo. Asegúrese de manejar el error si el radio es negativo o si se ingresa un valor no numérico.

# import math

# def calcular_area_circulo(radio):
#     return math.pi * radio ** 2
# try:
#   radio = int(input("Ingrese el radio: "))
#   if radio <= 0:
#       raise ValueError("El radio no puede ser negativo.")
#   print(f"El calculo del area del circulo es: {calcular_area_circulo(radio)}")
# except ValueError as error:
#         raise ValueError("Error: " + str(error))
# except Exception as e:
#         raise ValueError("Error: El valor ingresado no es numérico.")

# 6. Realice un programa con una función que calcule el factorial de un número ingresado por el usuario. El factorial de un número n se define como el producto de todos los enteros positivos desde 1 hasta n. Asegúrese de manejar cualquier error que pueda surgir si el usuario ingresa un número negativo o no entero.

def calcular_factorial(numero):
    try:
        numero_entero = int(numero)
        if numero_entero < 0:
            raise ValueError("El número no puede ser negativo.")
        factorial = 1
        for i in range(1, numero_entero + 1):
            factorial *= i
        return factorial
    except ValueError as error:
        raise ValueError("Error: " + str(error))
    except Exception as e:
        raise ValueError("Error: El valor ingresado no es un número entero.")
    except ZeroDivisionError:
        print("No se puede con 0")

while True:
    numero_ingresado = input("Ingresa un número entero para calcular su factorial: ")
    try:
        resultado_factorial = calcular_factorial(numero_ingresado)
        print(f"El factorial de: {numero_ingresado} es: {resultado_factorial}")
        break
    except ValueError as error:
        print(error)

