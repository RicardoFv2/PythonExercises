
# 1. Cree un programa con una función que calcule el área de un círculo y otra función que calcule el volumen de un cilindro usando la primera función.
# import math

# def circle_area(radio):
#     formatted_result = f"{math.pi * radio**2}"
#     return formatted_result

# def cilinder_volume(height):
#     radio = int(input("Write the radio: "))
#     formatted_result = f"{circle_area(radio) * height}"
#     return formatted_result

# circle_radio = int(input("Write the radio of the circle: "))
# print(f"The area of the circle is: {circle_area(circle_radio)}")

# cilinder_height = int(input("Write the height of cilinder: "))
# print(f"The volumen of the cilinder is: {cilinder_volume(cilinder_height)}")


# 2. Escribir un programa con una función que calcule el total de una factura tras aplicarle el IVA. La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.

# def calcultor_IVA(amount, rate= 21):
#     return (rate / 100) * amount

# amount = float(input("Enter the value of the product: "))
# rate = int(input("Enter the IVA rate: "))

# print(f"The value of the product without IVA is: {amount} \nThe value of the product with the added IVA is: {calcultor_IVA(amount,rate) + amount} ")

# 3. Escribir una función que reciba una muestra de números en una lista y devuelva un diccionario con su media, varianza y desviación típica.
 
# def calcular_estadisticas(list):
    
#     media = sum(list) / len(list)
#     varianza = sum((x - media) ** 2 for x in list) / len(list)
#     desviacion_tipica = varianza ** 0.5

#     diccionario = {
#         "media": media,
#         "varianza": varianza,
#         "desviacion_tipica": desviacion_tipica
#     }
#     return diccionario

# cantidad_nums = int(input("Ingrese la cantidad de numeros a ingresas: "))
# contador = 0
# muestra = []

# while contador <= cantidad_nums:
#     numero_ingresado = int(input("Ingrese un numero a la lista: "))
#     muestra.append(numero_ingresado)
#     resultado = calcular_estadisticas(muestra)
#     contador += 1
# print(resultado)

# 4. Escribir una función que reciba un número entero positivo y devuelva su factorial.

# def number(num):
#     if num < 0:
#       print("El numero debe ser mayor a 0")
#     else: 
#         resultado = 1
#         for i in range(1, num + 1):
#             resultado *= i
#         return resultado

# numero = int(input("Ingrese el numero para devolver su factorial: "))
# print(f"El factoria de {numero} es : {number(numero)}")

# 5. Tomando como base el ejercicio 5 de la guía de “Estructuras de datos”, cree un programa con una función que contendrá el abecedario en una lista y deberá eliminar los elementos según las posiciones de un múltiplo de un numero ingresado por el usuario.

# 6. Desarrolle un programa que le solicite al usuario que ingrese un número entero e informar si es primo o no, utilizando una función booleana que lo decida.
# import math

# def es_primo(numero):
#     if numero <= 1:
#         return False
#     elif numero == 2:
#         return True
#     else:
#         for i in range(2, int(math.sqrt(numero)) + 1):
#             if numero % i == 0:
#                 return False
#         return True

# numero = int(input("Ingrese un numero para comprobar si es primo: "))
# if numero <= 0:
#   print("El numero tiene que ser mayor a 0")

# print(f"Usted ingreso el numero: {numero} \n (TRUE = PRIMO, FALSE = NO ES PRIMO) \n {es_primo(numero)}")

# 7. Diseñar un programa con una función que recibirá el radio de una circunferencia y calcule el área y el perímetro.
# import math

# def calcular_area(radio):

#     area = math.pi * radio ** 2
#     perimetro = 2 * math.pi * radio
    
#     return area, perimetro

# radio = float(input("Ingresa el radio de la circunferencia: "))
# area, perimetro = calcular_area(radio)
# print(f"El área de la circunferencia es: {area:.2f}")
# print(f"El perímetro de la circunferencia es: {perimetro:.2f}")