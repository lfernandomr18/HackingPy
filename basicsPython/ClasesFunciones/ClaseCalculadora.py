def resta(valor1,valor2):
    print("La resta es: {}".format(valor1-valor2))
 
 
def suma(valor1,valor2):
    print("La suma es: {}".format(valor1 + valor2))
 
def muiltiplicacion(valor1,valor2):
    print("La multiplicación es: {}".format(valor1 * valor2))
 
def division(valor1,valor2):
    print("La división es: {}".format(valor1 / valor2))
 
def main():
    while True:
        print("\nBienvenidos a la Calculadora\n")
        print("1. Suma dos numeros")
        print("2. Resta dos numeros")
        print("3. Multiplica dos numeros")
        print("4. Divide dos numeros")
        print("5. Salir")
 
        opcion = int(input("\nOpción: "))
 
        if opcion == 1:
            valor1 = int(input("Ingrese Valor 1: "))
            valor2 = int(input("Ingrese Valor 2: "))
            suma(valor1,valor2)
 
        elif opcion == 2:
            valor1 = int(input("Ingrese Valor 1: "))
            valor2 = int(input("Ingrese Valor 2: "))
            resta(valor1,valor2)
 
        elif opcion == 3:
            valor1 = int(input("Ingrese Valor 1: "))
            valor2 = int(input("Ingrese Valor 2: "))
            muiltiplicacion(valor1, valor2)
 
        elif opcion == 4:
            valor1 = int(input("Ingrese Valor 1: "))
            valor2 = int(input("Ingrese Valor 2: "))
            division(valor1, valor2)
 
        elif opcion == 5:
            exit()
 
        else:
            print("\n Opción invalida\n")
 
 
if __name__== '__main__':
    main()
