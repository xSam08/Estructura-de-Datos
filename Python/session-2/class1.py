'''
    1. creacion de la clase: class NombreClase
    2. creacion del método inicializador de la clase: def __init__()
'''

class Clase1:
    def __init__(self):
        self.user_name = ''
        self.age = 0
        self.marital_status = 0

    #Estoy afuera del método inicializador de la clase
    def register_form(self): #El método tiene como parámetro el self para poder utilizar las variables del método init

        print('Por favor, ingresa la siguiente información: ')

        # Permitir el ingreso de datos por teclado por parte del user
        self.user_name = input('Nombre: ')

        # Permitir varios intentos al usuario
        while(True):
            # Manejo de excepciones para cuando se espera un valor númerico pero el user ingresa texto
            try:
                self.age = int(input('Edad: '))
                break
            except ValueError:
                print('Error en la respuesta, se esperaba un número')
        
        while(True):   
            try:
                self.marital_status = int(input('Selecciona una opción:\n    1 -> Soltero\n    2 -> Casado\n    3 -> Es complicado\n >> '))
                if self.marital_status != 1 and self.marital_status != 2 and self.marital_status != 3:
                    print('Error en la respuesta.')
                else:
                    print('Usuario registrado.')
                    # El break finaliza el ciclo while
                    break
            except ValueError:
                print('Error en la respuesta, se esperaba un número')