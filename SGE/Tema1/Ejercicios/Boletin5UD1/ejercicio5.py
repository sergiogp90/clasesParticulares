# -*- coding: utf-8 -*-
class CuerpoCeleste(object):
    def __init__(self, masa, diametro):
        self.__masa = masa
        self.__diametro = diametro

    def get_masa(self):
        return self.__masa

    def set_masa(self, masa):
        self.__masa = masa

    def get_diametro(self):
        return self.__diametro

    def set_diametro(self, diametro):
        self.__diametro = diametro

    def __str__(self):
        return "Masa: %s \n Diametro: %s" % (str(self.get_masa()), str(self.get_diametro()))

    def __cmp__(self, other):
        if self.get_masa() == other.get_masa():
            if self.get_diametro() == other.get_diametro():
                return True
        else:
            return False


class Planeta(CuerpoCeleste):
    def __init__(self, masa, diametro, periodo_traslacion, tiempo_rotacion):
        super(Planeta, self).__init__(masa, diametro)
        self.__periodo_traslacion = periodo_traslacion
        self.__tiempo_rotacion = tiempo_rotacion

    def get_periodo_traslacion(self):
        return self.__periodo_traslacion

    def set_periodo_traslacion(self, periodo_traslacion):
        self.__periodo_traslacion = periodo_traslacion

    def get_tiempo_rotacion(self):
        return self.__tiempo_rotacion

    def set_tiempo_rotacion(self, tiempo_rotacion):
        self.__tiempo_rotacion = tiempo_rotacion

    def __str__(self):
        return super(Planeta, self).__str__() + \
               "\nPropiedades del planeta: \nPeriodo de traslación: %s\nTiempo de rotación: %s"\
               % (str(self.get_periodo_traslacion()), str(self.get_tiempo_rotacion()))


class Satelite(CuerpoCeleste):
    def __init__(self, masa, diametro, periodo_traslacion, tiempo_rotacion):
        super(Satelite, self).__init__(masa, diametro)
        self.__periodo_traslacion = periodo_traslacion
        self.__tiempo_rotacion = tiempo_rotacion

    def get_periodo_traslacion(self):
        return self.__periodo_traslacion

    def set_periodo_traslacion(self, periodo_traslacion):
        self.__periodo_traslacion = periodo_traslacion

    def get_tiempo_rotacion(self):
        return self.__tiempo_rotacion

    def set_tiempo_rotacion(self, tiempo_rotacion):
        self.__tiempo_rotacion = tiempo_rotacion

    def __str__(self):
        return super(Satelite, self).__str__() + \
               "\nPropiedades del planeta: \nPeriodo de traslación: %s\nTiempo de rotación: %s"\
               % (str(self.get_periodo_traslacion()), str(self.get_tiempo_rotacion()))

planeta1 = Planeta(12000, 2400.20, 365, 200)
satelite1 = Satelite(20000, 1200.50, 300, 100)

print (planeta1 == satelite1)
