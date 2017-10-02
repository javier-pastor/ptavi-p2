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


class CalculadoraHija(Calculadora):

    def multiply(self):
        return self.operand1 * self.operand2

    def div(self):
        if self.operand2 == 0:
            return "Division by zero is not allowed"
        else:
            return self.operand1 / self.operand2

if __name__ == "__main__":
    operand1 = int(sys.argv[1])
    operand2 = int(sys.argv[3])
    objetoCalculadora = CalculadoraHija(operand1, operand2)
    if sys.argv[2] == "suma":
        result = objetoCalculadora.plus()
    elif sys.argv[2] == "resta":
        result = objetoCalculadora.minus()
    elif sys.argv[2] == "multiplicar":
        result = objetoCalculadora.multiply()
    elif sys.argv[2] == "dividir":
        result = objetoCalculadora.div()
    else:
        sys.exit('Operación sólo puede ser sumar o restar.')

    print(result)
