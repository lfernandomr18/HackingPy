class Calculadora:
    def __init__(self):
        pass
    
    def suma(self, a, b):
        return a + b
    
    def resta(self, a, b):
        return a - b
    
    def multiplicacion(self, a, b):
        return a * b
    
    def division(self, a, b):
        if b != 0:
            return a / b
        else:
            print("Error: No se puede dividir entre cero.")
            return None


mi_calculadora = Calculadora()

resultado_suma = mi_calculadora.suma(5, 3)
print("Suma:", resultado_suma)

resultado_resta = mi_calculadora.resta(10, 4)
print("Resta:", resultado_resta)

resultado_multiplicacion = mi_calculadora.multiplicacion(6, 2)
print("Multiplicación:", resultado_multiplicacion)

resultado_division = mi_calculadora.division(10, 2)
if resultado_division is not None:
    print("División:", resultado_division)
