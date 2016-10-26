# -*- coding: utf-8 -*-
import calendar

import datetime


class Fecha(object):
    def __init__(self, dia, mes, anio):
        self.__dia = dia
        self.__mes = mes
        self.__anio = anio
        self.valida()

    def leer(self):
        dia = input("Introduzca el día (entre 1 y 31):")
        self.set_dia(dia)

        mes = input("Introduzca el mes (entre 1 y 12):")
        self.set_mes(mes)

        anio = input("Introduzca el año (entre 1900 y 2050):")
        self.set_anio(anio)

        self.valida()

    def bisiesto(self):
        return (self.get_anio() % 4 == 0 and self.__anio % 100 != 0) or self.__anio % 400 == 0

    def dias_mes(self, mes):
        dias_mes = {1 : 31, 2 : 28, 3 : 31, 4 : 30, 5 : 31, 6 : 30, 7 : 31, 8 : 31, 9 : 30, 10 : 31, 11 : 30, 12 : 31}

        if mes == 2:
            if self.get_anio() % 4 == 0:
                return dias_mes[mes] + 1
            else:
                return dias_mes[mes]
        else:
            return dias_mes[mes]

    """Correccion de luismi. Esto devuelve una tupla con el dia de la semana (0 lunes, 1 martes...)
    y el total de días del mes."""
    def dias_mes(self, anio, mes):
        return calendar.monthrange(anio, mes)[1]

    def valida(self):
        if self.get_dia() < 1 or self.get_dia() > 31:
            self.set_dia(1)

        if self.get_mes() < 1 or self.get_mes() > 12:
            self.set_mes(1)

        if self.get_anio() < 1900 or self.get_anio() > 2050:
            self.set_anio(1900)

    def validate_date(self):
        try:
            str_fecha = str(self.get_dia()) + "/" + str(self.get_mes()) + "/" + str(self.get_anio())
            datetime.datetime.strptime(str_fecha, '%m/%d/%Y')
            return True
        except ValueError:
            return False

    def corta(self):
        return "%s-%s-%s" % (str(self.get_dia()), str(self.get_mes()), str(self.get_anio()))

    def larga(self):
        return "%s de %s de %s" % (str(self.get_dia()), str(self.get_mes()), str(self.get_anio()))

    def siguiente(self):
        if self.get_mes() != 2:
            if self.get_dia() != 31:
                self.set_dia(self.get_dia()+1)
            else:
                self.set_dia(1)
                if self.get_mes() == 12:
                    self.set_mes(1)
                    self.set_anio(self.get_anio()+1)
        else:
            if self.bisiesto():
                if self.get_dia() != 29:
                    self.set_dia(self.get_dia()+1)
                else:
                    self.set_dia(1)
                    self.set_mes(self.get_mes()+1)
            else:
                if self.get_dia() != 28:
                    self.set_dia(self.get_dia()+1)
                else:
                    self.set_dia(1)
                    self.set_mes(self.get_mes()+1)

    def anterior(self):
        if self.get_mes() == 5 or self.get_mes() == 7 or self.get_mes() == 10 or self.get_mes() == 12:
            self.set_dia(30)
            self.set_mes(self.get_mes()-1)
        elif self.get_mes() == 1:
            self.set_dia(31)
            self.set_mes(12)
            self.set_anio(self.get_anio()-1)
        elif self.get_mes() == 8:
            self.set_dia(31)
            self.set_mes(self.get_mes()-1)
        elif self.get_mes() == 3:
            if self.bisiesto():
                self.set_dia(29)
            else:
                self.set_dia(28)
            self.set_mes(self.get_mes()-1)

    def __le__(self, other):
        res = False
        if self.get_anio() < other.get_anio():
            res = True
        elif self.get_anio() == other.get_anio():
            if self.get_mes() < other.get_mes():
                res = True
            elif self.get_mes() == other.get_mes():
                if self.get_dia() <= other.get_dia():
                    res = True

        return res

    def __lt__(self, other):
        res = False

        if self.get_anio() < other.get_anio():
            res = True
        elif self.get_anio() == other.get_anio():
            if self.get_mes() < other.get_mes():
                res = True
            elif self.get_mes() == other.get_mes():
                if self.get_dia() < other.get_dia():
                    res = True

        return res

    def __ge__(self, other):
        res = False

        if self.get_anio() > other.get_anio():
            res = True
        elif self.get_anio() == other.get_anio():
            if self.get_mes() > other.get_mes():
                res = True
            elif self.get_mes() == other.get_mes():
                if self.get_dia() >= other.get_dia():
                    res = True

        return res

    def __gt__(self, other):
        res = False

        if self.get_anio() > other.get_anio():
            res = True
        elif self.get_anio() == other.get_anio():
            if self.get_mes() > other.get_mes():
                res = True
            elif self.get_mes() == other.get_mes():
                if self.get_dia() > other.get_dia():
                    res = True

        return res

    def __eq__(self, other):
        res = False

        if self.get_anio() == other.get_anio():
            if self.get_mes() == other.get_mes():
                if self.get_dia() == other.get_dia():
                    res = True
        return res

    def get_dia(self):
        return self.__dia

    def set_dia(self, dia):
        self.__dia = dia

    def get_mes(self):
        return self.__mes

    def set_mes(self, mes):
        self.__mes = mes

    def get_anio(self):
        return self.__anio

    def set_anio(self, anio):
        self.__anio = anio