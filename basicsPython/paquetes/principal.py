from paquete1 import calculadora_paquete

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
            calculadora_paquete.suma(valor1,valor2)
            
            
 
        elif opcion == 2:
            valor1 = int(input("Ingrese Valor 1: "))
            valor2 = int(input("Ingrese Valor 2: "))
            calculadora_paquete.resta(valor1,valor2)
 
        elif opcion == 3:
            valor1 = int(input("Ingrese Valor 1: "))
            valor2 = int(input("Ingrese Valor 2: "))
            calculadora_paquete.muiltiplicacion(valor1, valor2)
 
        elif opcion == 4:
            valor1 = int(input("Ingrese Valor 1: "))
            valor2 = int(input("Ingrese Valor 2: "))
            calculadora_paquete.division(valor1, valor2)
 
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
    