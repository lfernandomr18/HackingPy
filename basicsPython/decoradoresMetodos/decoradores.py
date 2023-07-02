
#classmethod
#staticmethod
#property


class prueba1(object):
    def __init__(self,radio):
        self.radio=radio
    #permite usar funcion sin que antes la clase sea atribuida a un objeto
    @classmethod    
    def saludo(cls,nombre):
        print("Hola {}".format(nombre))

    #permite llamar a la funcion SIN ARGUMENTO pero debe ser instanciado
    @staticmethod
    def saludo_static():
        print("Bienvenido")
    #se define a una funcion que funciona como una propiedad de la clase instanciada
    @property
    def area_circulo(self):
        return 3.14*self.radio

        
def main():
    
    # prueba1.saludo("Fernando")
    # p=prueba1()
    # p.saludo_static()
    p=prueba1(10)
    print(p.area_circulo)


 
if __name__== '__main__':
    main()