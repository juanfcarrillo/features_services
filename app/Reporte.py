from app import Ciudadano
from app import TipoReporte


class Reporte:

    def __init__(self, ciudadano: Ciudadano, tipo_reporte: TipoReporte, **kwargs):
        self.__ciudadano = ciudadano
        self.__tipo_reporte = tipo_reporte
        if kwargs.get("ubicacion"):
            self.__ubicacion = kwargs.get("ubicacion")
        self.__frecuencia = "Desconocida"
        self.__prioridad = None
        self.__estado_registro = "pendiente"

    def validar_reporte(self) -> bool:
        es_valido = bool(self.__ciudadano and self.__tipo_reporte and self.__ubicacion)
        return es_valido

    def get_tipo_reporte(self):
        return self.__tipo_reporte

    def get_ciudadano(self):
        return self.__ciudadano

    def set_frecuencia(self, frecuencia):
        self.__frecuencia = frecuencia

    def get_ubicacion(self):
        return self.__ubicacion

    def get_frecuencia(self):
        return self.__frecuencia

    def set_prioridad(self, prioridad):
        self.__prioridad = prioridad

    def get_prioridad(self):
        return self.__prioridad

    def get_estado_registro(self):
        return self.__estado_registro

    def set_estado_registro(self, estado):
        self.__estado_registro = estado