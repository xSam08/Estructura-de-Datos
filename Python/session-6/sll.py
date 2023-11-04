class sll:
    class Node:
        def __init__(self, data):
            self.next = None
            self.value = data

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def create_nodo(self, value):
        new_node = self.Node(value)
        print(f"El valor del nodo es de: {new_node.value}")

    def punto_uno(self, value):
        if value % 2 == 0 and value >= -50 and value <= 50:

            new_node = self.Node(value)

            if self.length == 0:
                self.head = new_node
                self.tail = self.head
            else:
                self.tail.next = new_node
                self.tail = new_node
                self.tail.next = None
            self.length += 1
        else:
            print("El valor no es par entre 2 y 50.")

    def validar(self, value):
        if value % 2 != 0 and value < 0:
            return True
        else:
            return False

    def punto_dos(self, value):
        if self.validar(value) == True:
            new_node = self.Node(value)

            if self.length == 0:
                self.head = new_node
                self.tail = self.head
            else:
                new_node.next = self.head
                self.head = new_node
            self.length += 1
        else:
            print("El valor no es impar negativo")

    def es_par(self, value):
        if value % 2 == 0:
            return True
        else:
            return False

    def es_impar(self, value):
        if value % 2 != 0 and value > 0:
            return True
        else:
            return False

    def punto_tres(self):

        if self.length > 0:
            current_node = self.head
            while(current_node.next):
                current_node = current_node.next
            if self.es_par(current_node.value):
                current_node2 = self.head
                while(current_node2.next != None):
                    current_node2 = current_node2.next
                current_node2.next = None
                self.tail = current_node2
            else:
                print("El valor no cumple con la condición de ser par negativo")
        else:
            print("La lista está vacía")

    def punto_cuatro(self):

        if self.length > 0:
            if self.es_impar(self.head.value) == True:
                current_node = self.head
                current_node = current_node.next
                self.head = None
                current_node = self.head
            else:
                print("El valor no cumple con la condición de ser impar positivo")
        else:
            print("Lista vacía")

    def imprimir_lista(self):
        current_node = self.head
        while current_node:
            print(current_node.value)
            current_node = current_node.next
            
    def eliminar_nodos_repetidos(self):
        if self.length <= 1:
            # No hay nodos repetidos si la lista tiene 0 o 1 elemento.
            print("La lista por lo menos debe tener dos o más nodos.")
        else:
            valores_unicos = set()
            valores_repetidos = set()
            nodo_actual = self.head
            nodo_anterior = None

            while nodo_actual:
                if nodo_actual.value in valores_unicos:
                    valores_repetidos.add(nodo_actual.value)
                    # Elimina el nodo actual ajustando los punteros del nodo anterior.
                    nodo_anterior.next = nodo_actual.next
                    nodo_actual = nodo_actual.next
                    if nodo_actual == self.tail:
                        self.tail = nodo_anterior  # Actualiza la cola si es necesario.
                    self.length -= 1
                else:
                    # Agrega el valor del nodo actual al conjunto de valores únicos.
                    valores_unicos.add(nodo_actual.value)
                    nodo_anterior = nodo_actual
                    nodo_actual = nodo_actual.next

            nodo_actual = self.head
            nodo_anterior = None

            while nodo_actual:
                if nodo_actual.value in valores_repetidos:
                    nodo_anterior.next = nodo_actual.next
                    nodo_actual = nodo_actual.next
                    if nodo_actual == self.tail:
                        self.tail = nodo_anterior
                    self.length -= 1
                else:
                    nodo_anterior = nodo_actual
                    nodo_actual = nodo_actual.next


    def eliminar_nodos_pares(self):
        if self.length == 0:
            print("La lista está vacía, no hay nada que eliminar.")
        else:
            current_node = self.head
            previous_node = None

            while current_node:
                if self.es_par(current_node.value):
                    # Si el nodo actual es par, lo eliminamos
                    if previous_node:
                        previous_node.next = current_node.next
                    else:
                        # Si el nodo par es el primer nodo, actualizamos la cabeza
                        self.head = current_node.next

                    # Actualizamos la longitud y avanzamos al siguiente nodo
                    self.length -= 1
                    current_node = current_node.next
                else:
                    # Si el nodo no es par, simplemente avanzamos
                    previous_node = current_node
                    current_node = current_node.next

            # Después de recorrer toda la lista, actualizamos la cola si es necesario
            if previous_node:
                self.tail = previous_node