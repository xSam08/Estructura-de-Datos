'''
    2. Solicitar al usuario un valor numérico y validar si es un número par negativo
       permitirle n cantidad de intentos hasta que cumpla con la condición
'''

class Clase4:

    def __init__(self):
        self.numero = 0

    def validar_numero_par_negativo(self):
        while(True):
            try:
                self.numero = int(input("Ingresa un número: "))
                if self.numero % 2 == 0 and self.numero < 0:
                    print(f"{self.numero} es un par negativo. Felicitaciones.")
                    break
                elif self.numero % 2 == 0 and self.numero >= 0:
                    print(f"{self.numero} es par, pero no es negativo, intenta de nuevo.")
                elif self.numero % 2 != 0 and self.numero < 0:
                    print(f"{self.numero} no es par, pero es negativo, intenta de nuevo.")
                else:
                    print(f"{self.numero} no es ni par, ni negativo, intenta de nuevo.")
            except ValueError:
                print("Error en la respuesta, se espera un valor numérico.")