# -*- coding: utf-8 -*-
class NumeroFraccionario(object):
    def __init__(self, numerador, denominador=1):
        self.__numerador = numerador
        self.__denominador = denominador

    def get_numerador(self):
        return self.__numerador

    def set_numerador(self, numerador):
        self.__numerador = numerador

    def get_denominador(self):
        return self.__denominador

    def set_denominador(self, denominador):
        self.__denominador = denominador

    def __str__(self):
        return "%s / %s" % (str(self.get_numerador()), str(self.get_denominador()))

    def mcm(self, other_denominador):
        if self.get_denominador() > other_denominador:
            mayor = self.get_denominador()
        else:
            mayor = other_denominador

        while True:
            if (mayor % self.get_denominador() == 0) and (mayor % other_denominador == 0):
                mcm = mayor
                break
            mayor += 1

        return mcm

    def __add__(self, other):
        minimo_comun = self.mcm(other.get_denominador())

        numerador_uno = minimo_comun / self.get_denominador() * self.get_numerador()
        self.set_numerador(numerador_uno)
        self.set_denominador(minimo_comun)

        numerador_dos = minimo_comun / other.get_denominador() * other.get_numerador()

        numerador_final = self.get_numerador() + numerador_dos
        self.set_numerador(numerador_final)

        return self

    def __mul__(self, other):
        self.set_numerador(self.get_numerador() * other.get_numerador())
        self.set_denominador(self.get_denominador() * other.get_denominador())

        return self

num1 = NumeroFraccionario(1, 2)
num2 = NumeroFraccionario(1, 2)

print num1 * num2
print num1 + num2
















