
def saludo(nombre,edad):
    print("Hola {} tienes {}".format(nombre,edad))


def main():
    nombre=input("Nombre: ")
    edad=int(input("Edad: "))
    saludo(nombre=nombre,edad=edad)


if __name__ == '__main__':
    main()