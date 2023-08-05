'''
    1. Importamos las otras clases
    2. Se crea una instancia por cada clase
    3. Mediante la instancia accedemos a methods y atributos de la clase importada
'''

# from nombre_fichero import nombre_clase
from class1 import Clase1
from class2 import Clase2

# nombre_instancia = nombre_clase()
inst_clase1 = Clase1()
inst_clase2 = Clase2()

# instancia.nombre_funcion()
# inst_clase1.register_form()
inst_clase2.register_courses()