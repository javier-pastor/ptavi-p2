#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import csv


class Calculadora():

    def plus(self):

        self.result = int(self.lista[1])
        for i in self.lista[2:]:
            self.result = self.result + int(i)
        return self.result

    def minus(self):

        self.result = int(self.lista[1])
        for i in self.lista[2:]:
            self.result = self.result - int(i)
        return self.result

    def __init__(self, lista, result):
        self.lista = lista
        self.result = result


class CalculadoraHija(Calculadora):

    def multiply(self):
        self.result = int(self.lista[1])
        for i in self.lista[2:]:
            self.result = self.result * int(i)
        return self.result

    def div(self):
        self.result = int(self.lista[1])
        for i in self.lista[2:]:
            if (self.result != -1):
                if int(i) == 0:
                    self.result = -1
                else:
                    self.result = self.result / int(i)
        return self.result


if __name__ == "__main__":

    with open(sys.argv[1]+'.csv', 'r') as csvfile:
        read = csv.reader(csvfile)
        for row in read:
            objetoCalculadora = CalculadoraHija(row, 0)
            if row[0] == "suma":
                result = objetoCalculadora.plus()
                print(result)
            elif row[0] == "resta":
                result = objetoCalculadora.minus()
                print(result)
            elif row[0] == "multiplica":
                result = objetoCalculadora.multiply()
                print(result)
            elif row[0] == "divide":
                result = objetoCalculadora.div()
                if (result == -1):
                    print("Division by zero is not allowed")
                else:
                    print(result)
            else:
                sys.exit('Operación sólo puede ser sumar o restar.')
