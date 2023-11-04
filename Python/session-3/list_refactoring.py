class ListasV2:

    def __init__(self):
        self.lista_ciudades = []
        self.cantidad_ciudades = 0
        self.ciudad = ''
        self.indice_ciudad = 0
        self.opcion_menu = 0
        self.creacionLista()
        self.menu_operaciones_listas()

    def creacionLista(self):
        while True:
            try:
                self.cantidad_ciudades = int(input("\nCantidad de ciudades que conoces >> "))
                if self.cantidad_ciudades > 0:
                    print('Nombre de las ciudades:')
                    for i in range(self.cantidad_ciudades):
                        self.ciudad = input(f"Ciudad {i+1} >> ")
                        self.lista_ciudades.append(self.ciudad)
                    print(f"Las ciudades ingresadas son: {self.lista_ciudades}")
                    break
                else:
                    print(" *** Debes salir más de casa ***")
            except ValueError:
                print("El valor ingresado no es un número entero.")
                self.creacionLista()
                break

    def menu_operaciones_listas(self):
        while True:
            try:
                print("\nMENU: Operaciones con listas")
                print("1. Agregar una ciudad")
                print("2. Eliminar una ciudad")
                print("3. Ordenar la lista")
                print("4. Invertir la lista")
                print("5. Eliminar elementos duplicados")
                print("6. Tamaño de la lista")
                print("7. Contar las veces que aparece un elemento")
                print("8. Unir dos listas")
                print("9. Eliminar el último elemento de la lista")
                print("10. Eliminar un elemento de la lista en una posición específica")
                print("11. Listas de tuplas")
                print("12. Eliminar tupla por ciudad")
                print("13. Eliminar tuplas por departamento")
                print("14. Salir")
                self.opcion_menu = int(input("Opción >> "))
                if self.opcion_menu < 1 or self.opcion_menu > 14:
                    print("Opción incorrecta, intente nuevamente.")
                    self.opcion_menu = int(input(" >> "))
                elif self.opcion_menu == 1:
                    self.agregar_ciudad()
                    break
                elif self.opcion_menu == 2:
                    self.eliminar_ciudad()
                    break
                elif self.opcion_menu == 3:
                    self.ordenar_lista()
                    break
                elif self.opcion_menu == 4:
                    self.invertir_lista()
                    break
                elif self.opcion_menu == 5:
                    self.eliminar_duplicados()
                    break
                elif self.opcion_menu == 6:
                    self.tamanio_lista()
                    break
                elif self.opcion_menu == 7:
                    self.contar_veces_aparece_elemento()
                    break
                elif self.opcion_menu == 8:
                    self.union_listas()
                    break
                elif self.opcion_menu == 9:
                    self.eliminar_ultimo_elemento()
                    break
                elif self.opcion_menu == 10:
                    self.eliminar_elemento_posicion_especificada()
                    break
                elif self.opcion_menu == 11:
                    self.listas_tuplas()
                    break
                elif self.opcion_menu == 12:
                    self.eliminar_tupla_por_ciudad()
                    break
                elif self.opcion_menu == 13:
                    self.eliminar_tuplas_por_departamento()
                    break
                elif self.opcion_menu == 14:
                    print("Gracias por usar el programa")
                    break
                else:
                    print("Opción incorrecta")
            except ValueError:
                print("El valor ingresado no es un número entero.")
                self.menu_operaciones_listas()
                break

    def agregar_ciudad(self): 
        self.ciudad = input("Ciudad a agregar >> ")
        self.lista_ciudades.append(self.ciudad)
        print(f"La lista de ciudades es: {self.lista_ciudades}")
        self.menu_operaciones_listas()

    def eliminar_ciudad(self):
        self.ciudad = input("Ciudad a eliminar >> ")
        self.lista_ciudades.remove(self.ciudad)
        print(f"La lista de ciudades es: {self.lista_ciudades}")
        self.menu_operaciones_listas()

    def ordenar_lista(self):
        ''' Se utiliza lista.sort() para ordenar la lista '''
        self.lista_ciudades.sort()
        print(f"La lista de ciudades es: {self.lista_ciudades}")
        self.menu_operaciones_listas()

    def invertir_lista(self):
        ''' Se utiliza lista.reverse() para invertir la lista '''
        self.lista_ciudades.reverse()
        print(f"La lista de ciudades es: {self.lista_ciudades}")
        self.menu_operaciones_listas()

    def eliminar_duplicados(self):
        ''' Se utiliza set(lista) para eliminar los elementos duplicados de la lista '''
        self.lista_ciudades = list(set(self.lista_ciudades))
        print(f"La lista de ciudades es: {self.lista_ciudades}")
        self.menu_operaciones_listas()

    def tamanio_lista(self):
        ''' Se utiliza len(lista) para obtener el tamaño de la lista'''
        print(f"La lista de ciudades tiene {len(self.lista_ciudades)} elementos.")
        self.menu_operaciones_listas()
    
    def contar_veces_aparece_elemento(self):
        ''' Se utiliza lista.count(elemento) para contar las veces que aparece un elemento en la lista'''
        self.ciudad = input("Ciudad a buscar >> ")
        print(f"La ciudad {self.ciudad} aparece {self.lista_ciudades.count(self.ciudad)} veces en la lista.")
        self.menu_operaciones_listas()

    def union_listas(self):
        ''' Se utiliza lista.extend(lista2) para unir dos listas '''
        lista2 = [
            'Cucuta',
            'Popayan',
            'Bucaramanga',
            'Bogota'
        ]
        self.lista_ciudades.extend(lista2)
        print(f"La lista de ciudades es: {self.lista_ciudades}")
        self.menu_operaciones_listas()

    def eliminar_ultimo_elemento(self):
        ''' Se utiliza lista.pop() para eliminar el último elemento de la lista '''
        self.lista_ciudades.pop()
        print(f"La lista de ciudades es: {self.lista_ciudades}")
        self.menu_operaciones_listas()

    def eliminar_elemento_posicion_especificada(self):
        ''' Se utiliza lista.pop(posicion) para eliminar el elemento de la posición especificada de la lista '''
        self.indice_ciudad = int(input("Indice de la ciudad a eliminar >> "))
        self.lista_ciudades.pop(self.indice_ciudad)
        print(f"La lista de ciudades es: {self.lista_ciudades}")
        self.menu_operaciones_listas()

    def listas_tuplas(self):
        ''' Se utiliza tuple(lista) para convertir una lista en una tupla '''
        lista_caracteristicas_ciudades = []
        nombre_ciudad = 'Manizales'
        departamento = 'Caldas'
        poblacion_ciudad = 400000
        lista_caracteristicas_ciudades.append((nombre_ciudad, departamento, poblacion_ciudad))
        print(f"La tupla inicial de ciudades es: {lista_caracteristicas_ciudades}")
        ''' Menú para agregar ciudades a la lista de tuplas '''
        agregar_ciudad = input("¿Desea agregar una ciudad nueva? (S/N) >> ")
        ''' El usuario pudo ingresar: s, S, n, N '''
        while agregar_ciudad.upper() == 'S':
            nombre_ciudad = input("Nombre de la ciudad >> ")
            departamento = input("Departamento >> ")
            poblacion_ciudad = int(input("Población >> "))
            lista_caracteristicas_ciudades.append((nombre_ciudad, departamento, poblacion_ciudad))
            break
        print(f"La lista de ciudades es: {lista_caracteristicas_ciudades}")
        self.menu_operaciones_listas()

    def eliminar_tupla_por_ciudad(self):
        lista_caracteristicas_ciudades = [
            ('Manizales', 'Caldas', 400000),
            ('Cali', 'Valle', 1032324),
            ('Medellin', 'Antioquia', 1231234)
        ]
        print(f"La tupla es: {lista_caracteristicas_ciudades}")

        ''' Se busca la ciudad a eliminar dentro de la tupla y elimina la lista completa '''
        nombre_ciudad = input("Nombre de la ciudad a eliminar >> ")
        for ciudad in lista_caracteristicas_ciudades:
            if ciudad[0] == nombre_ciudad:
                lista_caracteristicas_ciudades.remove(ciudad)
        print(f"La tupla es: {lista_caracteristicas_ciudades}")
        self.menu_operaciones_listas()

    def eliminar_tuplas_por_departamento(self):
        lista_caracteristicas_ciudades = [
            ('Manizales', 'Caldas', 400000),
            ('Manzanares', 'Caldas', 1032324),
            ('Medellin', 'Antioquia', 1231234)
        ]
        
        print(f"La tupla es: {lista_caracteristicas_ciudades}")

        departamento_a_eliminar = input("Departamento a eliminar >> ")

        # Crear una copia de la lista para iterar mientras modificamos la original
        lista_copia = lista_caracteristicas_ciudades.copy()

        # Iterar sobre la copia y eliminar las tuplas con el departamento especificado
        for tupla in lista_copia:
            if tupla[1] == departamento_a_eliminar:
                lista_caracteristicas_ciudades.remove(tupla)

        print(f"La tupla después de eliminar:")
        for tupla in lista_caracteristicas_ciudades:
            print(tupla)

        self.menu_operaciones_listas()
        