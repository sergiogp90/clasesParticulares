# -*- coding: utf-8 -*-
class Punto(object):
    def __init__(self, eje_x, eje_y):
        self.__eje_x = eje_x
        self.__eje_y = eje_y

    def get_eje_x(self):
        return self.__eje_x

    def set_eje_x(self, eje_x):
        self.__eje_x = eje_x

    def get_eje_y(self):
        return self.__eje_y

    def set_eje_y(self, eje_y):
        self.__eje_y = eje_y


class Rectangulo(object):
    def __init__(self, punto_a, punto_b, punto_c, punto_d):
        self.__punto_a = punto_a
        self.__punto_b = punto_b
        self.__punto_c = punto_c
        self.__punto_d = punto_d

    def get_punto_a(self):
        return self.__punto_a

    def set_punto_a(self, punto_a):
        self.__punto_a = punto_a

    def get_punto_b(self):
        return self.__punto_b

    def set_punto_b(self, punto_b):
        self.__punto_b = punto_b

    def get_punto_c(self):
        return self.__punto_c

    def set_punto_c(self, punto_c):
        self.__punto_c = punto_c

    def get_punto_d(self):
        return self.__punto_d

    def set_punto_d(self, punto_d):
        self.__punto_d = punto_d

    def calcular_superficie(self):
        punto_a = self.get_punto_a()
        eje_x = punto_a.get_eje_x()


pun1 = Punto(2, 4)
pun2 = Punto(4, 8)
pun3 = Punto(2, 8)
pun4 = Punto(4, 18)

rect1 = Rectangulo(pun1, pun2, pun3, pun4)

rect1.calcular_superfici





