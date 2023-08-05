# 1. Definir la clase
class Clase2:
    # 2. Definir método inicializador de la clase
    def __init__(self):
        # 3. Definir las variables globales de la clase
        self.courses_list = [] # Lista que contiene todos los cursos
        self.name_course = '' # Variable que contiene el nombre del curso
        self.cant_course = 0 # Variable que contiene la cantidad de cursos

    # 3. Creamos función para solicitar la información al usuario
    def register_courses(self):
        # Solicitar cantidad de asignaturas al usuario, validar que sea un valor int
        # Permitirle varios intentos hasta que ingrese un valor númerico
        # Las asignaturas mínimo pueden ser 1 y máximo 5
        while(True):
            try:
                self.cant_course = int(input('Ingrese la cantidad de asignaturas: '))
                if self.cant_course >= 1 and self.cant_course <= 5:
                    # Ciclo que permite solicitar los nombres de las asignaturas
                    for item in range(0, self.cant_course):
                        self.name_course = input(f"Asignatura {item+1}: ")
                        # Función append de listas: Añade valor al final de la lista
                        self.courses_list.append(self.name_course)
                    print(f"\nSus asignaturas son: {self.courses_list}")
                    break
                else:
                    print('\nFuera del rango, inténtalo nuevamente.\n')
            except ValueError:
                print('\nError en la respuesta, se espera un valor numérico.\n')