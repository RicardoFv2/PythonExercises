
# Desarrolle un programa que solicite al usuario un número entero positivo y en una lista proceda a almacenarlo todos los números impares desde 1 hasta el número ingresado, posteriormente muestre el resultado de la lista en pantalla.


# numero = int(input("Ingrese un numero entero: "))
# impares = []

# contador = 0

# while contador <= numero:
#     if contador % 2 != 0:
#         impares.append(contador)
#     contador += 1

# for impar in impares:
#     print(f"Los numeros impares son: {impar}")


# Cree un programa que almacene en una lista las asignaturas que esté cursando un estudiante (por ejemplo, Matemáticas, Física, Química, Historia, Lenguaje, etc.) las cuales serán ingresadas por el mismo dependiendo la cantidad que desee almacenar (por ejemplo, una materia, dos
# materias, etc.); posteriormente haciendo uso de un bucle proceda a mostrar en pantalla el mensaje "Yo estudio <asignatura>", donde <asignatura> es cada una de las asignaturas de la lista.

# num_materias = int(input("Ingrese el numero de materias que esta cursando: "))
# materias = []
# if num_materias <= 0 or num_materias >= 6:
#     print("Numero de materias no valido, ingrese entre 1 a 5 materias")
#     quit()

# contador = 0
# while contador < num_materias:
#     materia = input(
#         "Ingrese la materia (Matemáticas, Física, Química, Historia o Lenguaje: ")
#     materias.append(materia)
#     contador += 1

# for subjects in materias:
#     print(f"Yo estudio la materia de {subjects}")

# Escribir un programa que cree un diccionario vacío y lo vaya completando con información sobre una persona (por ejemplo, nombre, edad, teléfono, correo electrónico, etc.) que se le solicite al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.

# personas = []

# num_personas = int(input("Ingrese el numero de personas que desea agregar: "))

# contador = 1

# while contador <= num_personas:
#     print(f"Ingresando la persona N° {contador}")

#     nombre = input("Ingrese el nombre de la persona: ")
#     edad = int(input("Ingrese la edad de la persona: "))
#     telefono = int(input("Ingrese el telefono de la persona: "))
#     correo = input("Ingrese el correo de la persona: ")

#     informacion = {}

#     informacion ['nombre'] = nombre
#     informacion ['edad'] = edad
#     informacion ['telefono'] = telefono
#     informacion ['correo'] = correo

#     personas.append(informacion)
#     contador +=1

#     for pers in personas:
#         print(f"Agregaste a la persona N° {contador} detalle: {pers}")

# Desarrolle un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for nums in reversed(numeros):
#     print(nums)

# Cree un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.
# 6. Investigue sobre el uso de la función list(), una vez comprendido su funcionamiento escriba un programa que solicite al usuario una palabra y muestre por pantalla si es un palíndromo.
# EJERCICIOS COMPLEMENTARIOS
# 1. Realice un programa que almacene en una lista los números de la serie Fibonacci (0, 1, 1, 2, 3, 5, 8, etc.) generados hasta un numero introducido por el usuario. Por ejemplo, si un usuario ingresa 10, la serie solo mostrara los valores 0, 1, 1, 2, 3, 5 y 8.
# 2. Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista y muestre por pantalla su media y desviación típica.
