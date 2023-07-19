
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

personas = []
informacion = {}
num_personas = int(input("Ingrese el numero de personas que desea agregar: "))

contador = 0

while contador <= num_personas:
    print(f"Ingresando el alumno N° {contador}")

    nombre = input("Ingrese el nombre de la persona: ")
    edad = int(input("Ingrese la edad de la persona: "))
    telefono = int(input("Ingrese el telefono de la persona: "))
    correo = input("Ingrese el correo de la persona: ")
    