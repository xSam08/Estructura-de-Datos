'''
    3. Solicitar al usuario un número positivo, el cual debe coincidir con un número
       generado de forma aleatoria entre 50 y 60, permitirle hasta 3 intentos y
       validar que no ingrese un valor duplicado
'''

import random

class Clase5:

    def __init__(self):
        self.numero_generado = random.randint(50, 60)
        self.intentos = 3
        self.numeros_ingresados = set()
        self.numero = 0

    def validar_numero_aleatorio(self):
        while self.intentos > 0:
            try:
                self.numero = int(input("Ingresa un número entre 50 y 60: "))
                if self.numero < 50 or self.numero > 60:
                    print(f"{self.numero} no está entre 50 y 60, intenta de nuevo.\n")
                elif self.numero in self.numeros_ingresados:
                    print(f"Ya ingresaste {self.numero}, no se pueden ingresar números repetidos, intenta nuevamente.\n")
                elif self.numero == self.numero_generado:
                    print(f"¡Felicitaciones! Has acertado.\n")
                    break
                else:
                    self.intentos = self.intentos - 1
                    print(f"Fallaste. Intentos restantes: {self.intentos}\n")
                    self.numeros_ingresados.add(self.numero)
            except ValueError:
                print("Error en la respuesta, se espera un número positivo, intenta nuevamente.\n")
        else:
            print("¡Has perdido!\n")