# -*- coding: utf-8 -*-
class Figura(object):
    def __init__(self):
        pass


class Triangulo(Figura):
    def __init__(self, base=5, altura=10):
        super(Triangulo, self).__init__()
        self.__base = base
        self.__altura = altura

    def get_base(self):
        return self.__base

    def set_base(self, base):
        self.__base = base

    def get_altura(self):
        return self.__altura

    def set_altura(self, altura):
        self.__altura = altura


class Cuadrado(Figura):
    def __init__(self, lado=10):
        super(Cuadrado, self).__init__()
        self.__lado = lado

    def get_lado(self):
        return self.__lado

    def set_lado(self, lado):
        self.__lado = lado


class Circulo(Figura):
    def __init__(self, radio=10):
        super(Circulo, self).__init__()
        self.__radio = radio

    def get_radio(self):
        return self.__radio

    def set_radio(self, radio):
        self.__radio = radio
