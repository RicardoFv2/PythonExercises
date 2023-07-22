
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
 