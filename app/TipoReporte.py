class TipoReporte:
    def __init__(self, asunto: str, descripcion: str):
        self.__asunto = asunto
        self.__descripcion = descripcion

    @property
    def asunto(self):
        return self.__asunto

    @property
    def descripcion(self):
        return self.__descripcion
