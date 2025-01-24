class TipoReporte:
    def __init__(self, asunto, descripcion):
        self.__asunto = asunto
        self.__descripcion = descripcion

    def _str_(self):
        return f"Asunto: {self.__asunto}, Descripción: {self.__descripcion}"

    def get_asunto(self):
        return self.__asunto

    def get_descripcion(self):
        return self.__descripcion