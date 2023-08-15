'''
    1. Importamos las otras clases
    2. Se crea una instancia por cada clase
    3. Mediante la instancia accedemos a methods y atributos de la clase importada
'''

from lists import ListClass

inst_listclass = ListClass()

inst_listclass.add()

index = int(input("Ingrese el índice del valor que desea obtener >> "))
inst_listclass.getitem(index)

# inst_listclass.remove()

index = int(input("Ingrese el índice del valor que desea eliminar >> "))
inst_listclass.removeitem(index)

value = input("Ingrese el valor que desea eliminar >> ")
inst_listclass.remove_value(value)