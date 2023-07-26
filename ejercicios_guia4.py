# 1. Escribe un programa que permita al usuario ingresar una cadena de texto. Luego, implementa
# una función que tome esa cadena como entrada y la muestre en pantalla en su forma invertida.
# Asegúrate de utilizar una función para llevar a cabo la inversión de la cadena y realice las
# validaciones necesarias para evitar problemas de ejecución.

def ingresar_cadena(cadena):
    try:
        for i in cadena:
            if i.isdigit():
                assert False
    except AssertionError:
        print(f"La cadena {cadena} no es un string, igrese solo cadenas")

    return cadena[::-1]


cadena = input("Ingrese la cadena: ")
print(f"La cadena {cadena} en su forma invertida es: {ingresar_cadena(cadena)}")
