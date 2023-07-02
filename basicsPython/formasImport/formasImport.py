# Cuando necesitas importar módulos desde otras carpetas en diferentes niveles, hay varias formas de hacerlo en Python. A continuación, te mostraré algunos escenarios comunes y cómo realizar las importaciones correspondientes.

# Escenario 1: Importar un módulo desde una carpeta superior:

# Supongamos que tienes la siguiente estructura de directorios:

# proyecto/
# ├── carpeta1/
# │   └── modulo1.py
# └── carpeta2/
#     └── modulo2.py

# Si estás en el archivo modulo1.py y quieres importar el módulo modulo2.py que está en la carpeta carpeta2, puedes utilizar una importación relativa. El código para importar sería el siguiente:

# from ..carpeta2 import modulo2

# En este caso, el prefijo .. indica que quieres retroceder un nivel en la estructura de directorios para acceder a la carpeta carpeta2, y luego importas el módulo modulo2.



# *****************************************************************
# Escenario 2: Importar un módulo desde una carpeta inferior:

# Supongamos que tienes la siguiente estructura de directorios:

# proyecto/
# ├── carpeta1/
# │   └── modulo1.py
# └── carpeta2/
#     └── subcarpeta/
#         └── modulo2.py

# Si estás en el archivo modulo1.py y quieres importar el módulo modulo2.py que está en la subcarpeta subcarpeta dentro de carpeta2, puedes utilizar una importación relativa. El código para importar sería el siguiente:

# from ..carpeta2.subcarpeta import modulo2

# En este caso, el prefijo .. indica que quieres retroceder un nivel en la estructura de directorios hasta llegar a la carpeta carpeta2, luego especificas la subcarpeta subcarpeta y finalmente importas el módulo modulo2.


# *****************************************************************



# Escenario 3: Importar un módulo desde una carpeta en un nivel superior:

# Supongamos que tienes la siguiente estructura de directorios:

# proyecto/
# ├── carpeta1/
# │   └── modulo1.py
# └── carpeta2/
#     └── modulo2.py


# Si estás en el archivo modulo2.py y quieres importar el módulo modulo1.py que está en la carpeta carpeta1 que se encuentra en el nivel superior, puedes utilizar una importación absoluta. El código para importar sería el siguiente:

# from carpeta1 import modulo1

# En este caso, no se utiliza una importación relativa, sino una importación absoluta. Simplemente especificas el nombre de la carpeta (carpeta1) y luego importas el módulo modulo1.

# Estos son solo algunos escenarios comunes, pero la forma de importar módulos puede variar según la estructura específica de tu proyecto. Si tienes una estructura diferente o necesitas más ayuda, por favor proporciona más detalles para que pueda brindarte una respuesta más específica.


# ***********************************************


# La forma en la que pude ejecutar es en consola es :

# C:\Users\Usuario\Desktop\Hacking\basicsPython>python -m modulos.principal



# *******************************

# basicsPython/
# ├── paquetes/
#     └── paquete1/
# │     └── __init__.py
# │     └── calculadora_paquete.py
#     └── principal.py

# En este caso desde principal.py se puede utilizar a los metodos de calculadora_paquete.py utilizando el import de la siguiente forma:


# from paquete1 import calculadora_paquete