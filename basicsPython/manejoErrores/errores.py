

try:
    while True:
        print("Hola")
except NameError:
    print("Error: ", NameError)
except KeyboardInterrupt:
    print("Salida Forzosa")
finally:
    print("Termino la ejecución")

try:
    raise IOError
except IOError:
    print("Ocurrio un error")