# 1. Escribe un programa que permita al usuario ingresar una cadena de texto. Luego, implementa
# una función que tome esa cadena como entrada y la muestre en pantalla en su forma invertida.
# Asegúrate de utilizar una función para llevar a cabo la inversión de la cadena y realice las
# validaciones necesarias para evitar problemas de ejecución.

# def ingresar_cadena(cadena):
#     try:
#         for i in cadena:
#             if i.isdigit():
#                 assert False
#     except AssertionError:
#         print(f"La cadena {cadena} no es un string, igrese solo cadenas")
#
#     return cadena[::-1]
#
#
# cadena = input("Ingrese la cadena: ")
# print(f"La cadena {cadena} en su forma invertida es: {ingresar_cadena(cadena)}")


# 2. Realice un programa que solicite al usuario ingresar una lista de palabras. Implemente una
# función que tome esa lista como entrada y devuelva una nueva lista con solo las palabras que
# son palíndromos. Si el usuario no ingresa ninguna palabra, muestra un mensaje indicando que no
# se ingresaron datos.

# def es_palindromo(palabra):
#     return palabra == palabra[::-1]
#
#
# def obtener_palindromos(lista_palabras):
#     return [palabra for palabra in lista_palabras if es_palindromo(palabra)]
#
#
# lista_palabras = input("Ingrese una lista de palabras separadas por espacios: ").split()
#
# if not lista_palabras:
#     print("No se ingresaron datos.")
# else:
#     palindromos = obtener_palindromos(lista_palabras)
#
#     if palindromos:
#         print("Palíndromos encontrados:")
#         print(", ".join(palindromos))
#     else:
#         print("No se encontraron palíndromos.")

# 3. Desarrolle un programa que permita al usuario ingresar una cadena de texto. Luego, implementa una función que tome esa cadena como entrada y muestre en pantalla una versión de la misma cadena con los caracteres repetidos eliminados.

# def eliminar_caracteres_repetidos(cadena):
#     caracteres_sin_repetir = ""
#     for caracter in cadena:
#         if caracter not in caracteres_sin_repetir:
#             caracteres_sin_repetir += caracter
#     return caracteres_sin_repetir
#
#
# cadena_ingresada = input("Ingresa una cadena de texto: ")
# cadena_sin_repetir = eliminar_caracteres_repetidos(cadena_ingresada)
# print("Cadena sin caracteres repetidos:", cadena_sin_repetir)


# 4. Desarrolle un programa que solicite al usuario ingresar una cadena de texto. Luego, implemente una función que tome esa cadena como entrada y devuelva una versión de la misma cadena sin las vocales. Si el usuario ingresa un valor que no es una cadena, captura la excepción y muestra un mensaje de error.

def eliminar_vocales(cadena):
    vocales = "aeiouAEIOU"
    cadena_sin_vocales = ''.join(caracter for caracter in cadena if caracter not in vocales)
    return cadena_sin_vocales


try:
    cadena_ingresada = input("Ingresa una cadena de texto: ")
    cadena_sin_vocales = eliminar_vocales(cadena_ingresada)
    print("Cadena sin vocales:", cadena_sin_vocales)
except TypeError:
    print("Error: El valor ingresado no es una cadena de texto.")
