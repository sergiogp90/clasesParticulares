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

    def __add__(self, other):
        if self.get_denominador() == other.get_denominador():
            self.set_numerador(self.get_numerador() + other.get_numerador())
            return self
        else:
            mcm = self.mcm(other.get_denominador())

            num_suma1 = (mcm / self.get_denominador()) * self.get_numerador()
            num_suma2 = (mcm / other.get_denominador()) * other.get_numerador()

            self.__denominador = mcm
            self.__numerador = num_suma1 + num_suma2
            return self

    def __sub__(self, other):
        if self.get_denominador() == other.get_denominador():
            self.set_numerador(self.get_numerador() - other.get_numerador())
            return self
        else:
            mcm = self.mcm(other.get_denominador())

            num_resta1 = (mcm / self.get_denominador()) * self.get_numerador()
            num_resta2 = (mcm / other.get_denominador()) * other.get_numerador()

            self.__denominador = mcm
            self.__numerador = num_resta1 - num_resta2
            return self

    def __mul__(self, other):
        self.__numerador *= other.get_numerador()
        self.__denominador *= other.get_denominador()

        return self

    def __div__(self, other):
        self.__numerador *= other.get_denominador()
        self.__denominador *= other.get_numerador()

        return self

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

    def __str__(self):
        return "%s / %s" % (str(self.get_numerador()), str(self.get_denominador()))

    def __eq__(self, other):
        if self.get_denominador() != self.get_denominador():
            mcm = self.mcm(self.get_denominador())

            numerador_1 = self.get_numerador() * mcm
            numerador_2 = other.get_numerador() * mcm

            if numerador_1 == numerador_2:
                return True
            else:
                return False
        else:
            if self.get_numerador() == other.get_numerador():
                return True
            else:
                return False

    def __gt__(self, other):
        resultado = False

        if self.get_denominador() != self.get_denominador():
            mcm = self.mcm(self.get_denominador())

            numerador_self = self.get_numerador() * mcm
            numerador_other = other.get_numerador() * mcm

            if numerador_self > numerador_other:
                resultado = True
        else:
            if self.get_numerador() > other.get_numerador():
                resultado = True

        return resultado

    def __lt__(self, other):
        resultado = False

        if self.get_denominador() != self.get_denominador():
            mcm = self.mcm(self.get_denominador())

            numerador_self = self.get_numerador() * mcm
            numerador_other = other.get_numerador() * mcm

            if numerador_self < numerador_other:
                resultado = True
        else:
            if self.get_numerador() < other.get_numerador():
                resultado = True

        return resultado

num1 = NumeroFraccionario(2, 8)
num2 = NumeroFraccionario(4, 4)

print num1 == num2
print num2 > num1
print num1 < num2
print num1
print num2
