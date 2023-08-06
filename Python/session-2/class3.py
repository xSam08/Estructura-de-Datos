'''
    1. Generar un array de 10 números aleatorios entre -20 y 20
'''

import random

class Clase3:

   def __init__(self):
      self.arreglo = []

   def generar_array_aleatorio(self):
      self.arreglo = [random.randint(-20, 20) for _ in range(10)]
      
      print(f"Array generado: {self.arreglo}")