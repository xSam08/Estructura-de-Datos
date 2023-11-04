class singleLinkedList:

    class Node:
        def __init__(self, value):
            self.value = value
            self.puntero_next = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_node_end(self, value):
        # value = input("Ingresa un valor >> ")

        # No hay nodos en la lista
        new_node = self.Node(value)

        if self.head == None:
            # La cabeza de la lista es el nuevo nodo
            self.head = new_node
            self.tail = self.head
        else:
            # Si hay nodos en la lista
            # Recorremos la lista desde la cabeza
            current_node = self.head
            while(current_node.puntero_next):
                current_node = current_node.puntero_next
            current_node.puntero_next = new_node
            self.tail.puntero_next = new_node
            self.tail = new_node
        self.length += 1

    def add_initial_node(self, value):
        new_node = self.Node(value)

        if self.head == None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.puntero_next = self.head
            self.head = new_node
        self.length += 1

    def remove_last_node(self):
        if self.head == None:
            return None
        else:
            # Identificar el último nodo
            current_node = self.head

            '''
                current es el nodo actual
                current.puntero_next va hasta el ultimo nodo
                current.puntero_next.puntero_next va hasta el penultimo nodo
            '''
            while(current_node.puntero_next.puntero_next):
                # Saltamos al siguiente nodo
                current_node = current_node.puntero_next
            # Eliminamos el último nodo
            current_node.puntero_next = None
            self.length -= 1


        
    def show_list(self):
        # Creamos una lista vacía
        nodes_list = []
        print(f'La cantidad de nodos de la lista {self.length}')
        current_node = self.head
        while current_node:
            nodes_list.append(current_node.value)
            current_node = current_node.puntero_next
        print(nodes_list)
        