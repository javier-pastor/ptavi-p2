#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys


class Calculadora():

    def plus(self):
        return self.operand1 + self.operand2

    def minus(self):
        return self.operand1 - self.operand2

    def __init__(self, operand1, operand2):
        self.operand1 = operand1
        self.operand2 = operand2
        """los atributos tienen vida dentro de toda la clase"""

if __name__ == "__main__":
    operand1 = int(sys.argv[1])
    operand2 = int(sys.argv[3])
    objetoCalculadora = Calculadora(operand1, operand2)
    # Creo un objeto de la clase Calculadora
    # y le paso atributo en la inicialización
    if sys.argv[2] == "suma":
        result = objetoCalculadora.plus()
    elif sys.argv[2] == "resta":
        result = objetoCalculadora.minus()
    else:
        sys.exit('Operación sólo puede ser sumar o restar.')

    print(result)
