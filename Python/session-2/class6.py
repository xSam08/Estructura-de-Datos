'''
    4. Se tiene una lista [] que va almacenar 4 nombres de personas ingresados por el
       usuario, los nombres deben de almacenarse de forma ordenada ascendente [A-Z] y
       descendente [Z-A]. El usuario mediante un menú de dos opciones elige como ver la
       lista.
       Ejemplo:
            1. Ver la lista ordenada de forma ascendente [A-Z]
            2. Ver la lista ordenada de forma descendente [Z-A]
'''

class Clase6:

    def __init__(self):
        self.lista_ordenada = []
        self.lista_nombres = []
        self.nombre = ''
        self.opcion = 0

    def menu_nombres_listados(self):
        for i in range (1,5):
            self.nombre = input(f"Ingresa el nombre #{i}: ")
            self.lista_nombres.append(self.nombre)

        while(True):
            print("\nMenú:")
            print("1. Ver la lista ordenada de forma ascendente [A-Z]")
            print("2. Ver la lista ordenada de forma descendente [Z-A]")
            print("3. Salir")

            try:
                self.opcion = int(input("\nElige una opción: "))
                if self.opcion == 1:
                    self.lista_ordenada = sorted(self.lista_nombres)
                    print(f"Lista ordenada de manera ascendente [A-Z]: {self.lista_ordenada}")
                elif self.opcion == 2:
                    self.lista_ordenada = sorted(self.lista_nombres, reverse=True)
                    print(f"Lista ordenada de manera descendente [Z-A]: {self.lista_ordenada}")
                elif self.opcion == 3:
                    print("Hasta pronto.\n")
                    break
                else:
                    print("Esa opción no existe en el menú intente nuevamente.")
            except ValueError:
                print("Error en la respuesta, se espera un valor númerico. Intente nuevamente.")