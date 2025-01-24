class Ciudadano:
    def __init__(self, nombre, correo, identificacion):
        self.__nombre = nombre
        self.__correo = correo
        self.__identificacion = identificacion

    def get_nombre(self):
        return self.__nombre

    def get_correo(self):
        return self.__correo

    def get_identificacion(self):
        return self.__identificacion