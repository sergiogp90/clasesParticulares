# -*- coding: utf-8 -*-
class Direccion(object):
    def __init__(self, calle, ciudad, cp, provincia):
        self.__calle = calle
        self.__ciudad = ciudad
        self.__cp = cp
        self.__provincia = provincia

    def get_calle(self):
        return self.__calle

    def set_calle(self, calle):
        self.__calle = calle

    def get_ciudad(self):
        return self.__ciudad

    def set_ciudad(self, ciudad):
        self.__ciudad = ciudad

    def get_cp(self):
        return self.__cp

    def set_cp(self, cp):
        self.__cp = cp

    def get_provincia(self):
        return self.__provincia

    def set_provincia(self, provincia):
        self.__provincia = provincia


class Persona(object):
    def __init__(self, nombre, apellidos, nif, direccion):
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__nif = nif
        self.__direccion = direccion

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_apellidos(self):
        return self.__apellidos

    def set_apellidos(self, apellidos):
        self.__apellidos = apellidos

    def get_nif(self):
        return self.__nif

    def set_nif(self, nif):
        self.__nif = nif

    def get_direccion(self):
        return self.__direccion

    def set_direccion(self, direccion):
        self.__direccion = direccion

    def __str__(self):
        return "Persona[nombre: %s, apellidos: %s, nif: %s, direccion: %s]" % (self.get_nombre(), self.get_apellidos(),
                                                                               str(self.get_nif()), self.get_direccion())

    
class Estudiante(Persona):
    def __init__(self, nombre, apellidos, nif, direccion, id_estudiante):
        super(Estudiante, self).__init__(nombre, apellidos, nif, direccion)
        self.__id_estudiante = id_estudiante

    def get_id_estudiante(self):
        return self.__id_estudiante

    def set_id_estudiante(self, id_estudiante):
        self.__id_estudiante = id_estudiante
        
    def __str__(self):
        return super(Estudiante, self).__str__() + " Estudiante[id del estudiante: %s]" % (str(self.get_id_estudiante()))


class Profesor(Persona):
    def __init__(self, nombre, apellidos, nif, direccion, num_despacho):
        super(Profesor, self).__init__(nombre, apellidos, nif, direccion)
        self.__num_despacho = num_despacho

    def get_num_despacho(self):
        return self.__num_despacho

    def set_num_despacho(self, num_despacho):
        self.__num_despacho = num_despacho

    def __str__(self):
        return super(Profesor, self).__str__() + " Profesor[número de despacho: %s]" % (str(self.get_num_despacho()))

profesor1 = Profesor("Paco", "Gutierrez", "30238173G", Direccion("c/ Ajimez 1 8ºB", "Sevilla", "41008", "Sevilla"), 202)
profesor2 = Profesor("Lola", "Guerrero", "19283721B", Direccion("c/ San Jacinto", "Sevilla", "41010", "Sevilla"), 101)

estudiante1 = Estudiante("Pepe", "Fernández", "12345678A", Direccion("c/ Condes de Bustillo 17", "Sevilla", "41010", "Sevilla"), 1)
estudiante2 = Estudiante("María", "Pérez", "87654321A", Direccion("c/ Real 2", "Dos Hermanas", "41020", "Sevilla"), 2)


lista_personas = [profesor1, profesor2, estudiante1, estudiante2]

print lista_personas[0].get_num_despacho()
print lista_personas[2].get_id_estudiante()
