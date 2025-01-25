class Ciudadano:
    def __init__(self, nombre: str, correo: str, identificacion: str):
        self.__nombre = nombre
        self.__correo = correo
        self.__identificacion = identificacion

    @property
    def nombre(self):
        return self.__nombre

    @property
    def correo(self):
        return self.__correo

    @property
    def identificacion(self):
        return self.__identificacion
