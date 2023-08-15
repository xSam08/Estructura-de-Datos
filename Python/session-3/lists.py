class ListClass:

    def __init__(self):
        self.data = []

    # Añadir valores a la lista
    def add(self):
        #Preguntar al usuario cuántos valores quiere añadir
        n = int(input("¿Cuántos valores desea añadir? >> "))

        for i in range(1, n+1):
            # Preguntar al usuario por cada valor
            valor = input(f"Ingrese el valor {i}: ")
            # Añadir el valor a la lista
            self.data.append(valor)
        # Imprimir la lista con los valores ingresados
        print(f"Los valores ingresados son: {self.data}")

    # Obtener un valor específico de la lista
    def getitem(self, index):
        # Imprimir el valor en el índice especificado
        print(self.data[index-1])

    # Eliminar el ultimo valor de la lista
    def remove(self):
        # Eliminar el último valor en la lista
        self.data.pop()
        # Imprimir la lista con el valor eliminado
        print(self.data)

    # Eliminar un valor especifico de la lista
    def removeitem(self, index):
        # Validar que el índice exista en la lista
        if index < 0 or index > len(self.data):
            print("El índice no existe.")
        else: 
            # Eliminar el valor en el índice especificado
            self.data.pop(index-1)

        # Imprimir la lista con el valor eliminado
        print(self.data)

    def remove_value(self, value):
        # Validar que existe el valor en la lista
        if value not in self.data:
            print("El valor no existe.")
        else:
            # Eliminar el valor en el indice especificado
            self.data.remove(value)
            # Imprimir la lista con el valor eliminado
            print(self.data)