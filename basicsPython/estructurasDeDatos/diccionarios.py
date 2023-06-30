# Programa que itera sobre un diccionario de estudiantes
estudiantes = {
    "Juan": 18,
    "María": 20,
    "Pedro": 19,
    "Ana": 21
}
# imprimiendo usando el key
print("Juan: ",estudiantes["Juan"])
print("María: ",estudiantes["María"])
print("Pedro: ",estudiantes["Pedro"])
print("##################")
for nombre, edad in estudiantes.items():
    print("Nombre:", nombre)
    print("Edad:", edad)
    print("---")

print("¡Bucle for completado!")
