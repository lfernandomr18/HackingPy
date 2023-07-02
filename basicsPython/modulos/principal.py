from modulos import modulo_calculadora
from ClasesFunciones.primeraFuncion import saludo

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
            modulo_calculadora.suma(valor1,valor2)
            #aca esta usando el modulo desde otra carpeta
            saludo()
            
 
        elif opcion == 2:
            valor1 = int(input("Ingrese Valor 1: "))
            valor2 = int(input("Ingrese Valor 2: "))
            modulo_calculadora.resta(valor1,valor2)
 
        elif opcion == 3:
            valor1 = int(input("Ingrese Valor 1: "))
            valor2 = int(input("Ingrese Valor 2: "))
            modulo_calculadora.muiltiplicacion(valor1, valor2)
 
        elif opcion == 4:
            valor1 = int(input("Ingrese Valor 1: "))
            valor2 = int(input("Ingrese Valor 2: "))
            modulo_calculadora.division(valor1, valor2)
 
        elif opcion == 5:
            exit()
 
        else:
            print("\n Opción invalida\n")
 
 
if __name__== '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nSaliendo...")
        exit()
    