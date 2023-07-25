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
# coordenadas y almacena los resultados en una nueva lista. Por ejemplo, si la lista es [(2, 3), (4, 5), (1, 6)], la lista resultante debería ser [6, 20, 6]. Asegúrate de manejar cualquier error que pueda
# surgir si alguna de las coordenadas no es una tupla de dos elementos.